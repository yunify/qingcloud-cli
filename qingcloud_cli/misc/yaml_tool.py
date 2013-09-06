# coding:utf-8

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

def yaml_dump(obj):
    '''
    Dump an object to yaml string, only basic python types are supported

    @return yaml string or `None` if failed
    '''
    try:
        output = dump(obj, Dumper=Dumper)
    except Exception, e:
        output = None
    return output

def yaml_load(stream):
    '''
    Load from yaml stream and create a new python object

    @return object or `None` if failed
    '''
    try:
        obj = load(stream, Loader=Loader)
    except Exception, e:
        obj = None
    return obj

__all__ = [yaml_dump, yaml_load]
