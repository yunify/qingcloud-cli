# =========================================================================
# Copyright 2012-present Yunify, Inc.
# -------------------------------------------------------------------------
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this work except in compliance with the License.
# You may obtain a copy of the License in the LICENSE file, or at:
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========================================================================

import os
import json
import time
from datetime import datetime

from .yaml_tool import yaml_load

def explode_array(list_str, separator = ","):
    """
    Explode list string into array
    """
    if not list_str:
        return []
    return [item.strip() for item in list_str.split(separator) if item.strip() != '']

def send_request(action, directive, mgmt_handler):
    request = directive
    request["action"] = action
    response = mgmt_handler.handle(action, directive)
    prints(request, response)

    return response

def load_conf(conf_file):
    require_params = [
            "qy_access_key_id",
            "qy_secret_access_key",
            "zone",
            ]

    if conf_file == "":
        print("config file should be specified")
        return None

    if conf_file.startswith('~'):
        conf_file = os.path.expanduser(conf_file)

    if not os.path.isfile(conf_file):
        print("config file [%s] not exists" % conf_file)
        return None

    with open(conf_file, "r") as fd:
        conf = yaml_load(fd)
        if conf is None:
            print("config file [%s] format error" % conf_file)
            return None
        for param in require_params:
            if param not in conf:
                print("[%s] should be specified in conf_file" % param)
                return None
    return conf

def json_dumps(data, indent=0, ensure_ascii=False):
    return json.dumps(data, indent=indent, ensure_ascii=ensure_ascii)

def prints(req, rep):
    """ print request and reply """

    if isinstance(req, str):
        req = json.loads(req)
    if isinstance(rep, str):
        rep = json.loads(rep)

    #print('=======================================')
    #print("sending:%s" % json.dumps(req, indent=2))
    #print('=======================================')
    #print("recv:%s" % json.dumps(rep, indent=2))
    content = json_dumps(rep, indent=2, ensure_ascii=False)
    # python2/3 compatibility
    if str(type(content)) == "<type 'unicode'>":
        print(content.encode('utf-8'))
    else:
        print(content)

def prints_body(resp):
    if resp.getheader("content-type").startswith("application/json"):
        body = json.loads(resp.read())
        print json_dumps(body, indent=2)
    else:
        print resp.read()

ISO8601 = '%Y-%m-%dT%H:%M:%SZ'
def get_expire_time():
    curr_ts = time.time()
    adjust = 20 * 60
    expire_ts = curr_ts + adjust
    return time.strftime(ISO8601, time.gmtime(expire_ts))

def convert_to_utctime(time_str):
    try:
        _format = '%Y-%m-%d %H:%M:%S'
        dt = datetime.strptime(time_str, _format)
        gmt = time.gmtime(time.mktime(dt.timetuple()))
        return time.strftime(ISO8601, gmt)
    except:
        return None
