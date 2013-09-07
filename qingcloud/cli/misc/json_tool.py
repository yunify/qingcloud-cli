# coding:utf8

import json as jsmod

def json_dump(obj, indent = None):
    """ dump an object to json string, only basic python types are supported

    @return json string or `None` if failed
    """
    try:
        jstr = jsmod.dumps(obj, separators=(',',':'), indent = indent)
    except Exception, e:
        jstr = None
    return jstr

def json_load(json):
    """
    Load from json string and create a new python object

    @return object or `None` if failed
    """
    try:
        obj = jsmod.loads(json)
    except Exception, e:
        obj = None
    return obj

__all__ = [json_dump, json_load]
