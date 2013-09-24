# coding: utf-8

import os
import json

from .yaml_tool import yaml_load

def explode_array(list_str, separator = ","):
    """
    Explode list string into array
    """
    if not list_str:
        return []
    return [item for item in list_str.split(separator) if item.strip() != '']

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
        req = json.loads(req)
    if isinstance(rep, str):
        rep = json.loads(rep)

    #print '======================================='
    #print "sending:", json.dumps(req, indent=2)
    #print '======================================='
    #print "recv:", json.dumps(rep, indent=2)
    print json.dumps(rep, indent=2, ensure_ascii=False)
