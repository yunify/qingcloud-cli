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
    except Exception as e:
        print(e)
        output = None
    return output

def yaml_load(stream):
    '''
    Load from yaml stream and create a new python object

    @return object or `None` if failed
    '''
    try:
        obj = load(stream, Loader=Loader)
    except Exception as e:
        print(e)
        obj = None
    return obj

__all__ = [yaml_dump, yaml_load]
