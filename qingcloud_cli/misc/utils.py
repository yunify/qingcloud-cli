# coding: utf-8

import time
import os
import errno
import stat

from .yaml_tool import yaml_load
from .json_tool import json_load, json_dump

def explode_array(list_str, separator = ","):
    """
    Explode list string into array
    """
    result = []
    disk_list = list_str.split(separator)
    for disk in disk_list:
        disk = disk.strip()
        if disk != "":
            result.append(disk)
    return result

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
        print "config file should be specified"
        return None

    if conf_file.startswith('~'):
        conf_file = os.path.expanduser(conf_file)

    if not os.path.isfile(conf_file):
        print "config file [%s] not exists" % conf_file
        return None

    with open(conf_file, "r") as fd:
        conf = yaml_load(fd)
        if conf is None:
            print "config file [%s] format error" % conf_file
            return None
        for param in require_params:
            if param not in conf:
                print "[%s] should be specified in conf_file" % param
                return None
    return conf

def prints(req, rep):
    """ print request and reply """

    if isinstance(req, str):
        req = json_load(req)
    if isinstance(rep, str):
        rep = json_load(rep)

    #print '======================================='
    #print "sending:", json_dump(req, indent=2)
    #print '======================================='
    #print "recv:", json_dump(rep, indent=2)
    print json_dump(rep, indent=2)

def save_private_key(file_name, private_key):
    """ save ssh private key """
    if not save_file(file_name, private_key):
        return False
    os.chmod(file_name, stat.S_IREAD + stat.S_IWRITE)
    return True

def save_file(file_name, content):
    try:
        with open("%s" % file_name, "w") as f:
            f.write("%s" % content)
    except Exception, e:
        print "save private key [%s] to [%s] failed, [%s]" % (content, file_name, e)
        return False
    return True

def mkdir(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

def get_utf8_value(value):
    if not isinstance(value, str) and not isinstance(value, unicode):
        value = str(value)
    if isinstance(value, unicode):
        return value.encode('utf-8')
    else:
        return value

ISO8601 = '%Y-%m-%dT%H:%M:%SZ'
ISO8601_MS = '%Y-%m-%dT%H:%M:%S.%fZ'

def get_ts(ts=None):
    """
    Get formatted time
    """
    if not ts:
        ts = time.gmtime()
    return time.strftime(ISO8601, ts)

def parse_ts(ts):
    """
    Return as timestamp
    """
    ts = ts.strip()
    try:
        ts_s = time.strptime(ts, ISO8601)
        return time.mktime(ts_s)
    except ValueError:
        ts_s = time.strptime(ts, ISO8601_MS)
        return time.mktime(ts_s)

def get_expired_ts(ts, time_out):
    ts_expired_s = parse_ts(ts) + time_out
    ts_expired = time.localtime(ts_expired_s)
    return get_ts(ts_expired)
