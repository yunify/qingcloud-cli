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
from qingcloud.cli.misc.utils import explode_array

from qingcloud.cli.iaas_client.actions.base import BaseAction

class ResizeS2ServersAction(BaseAction):
    action = 'ResizeS2Servers'
    command = 'resize-s2-servers'
    usage = '%(prog)s -s <s2_servers> -T <s2_server_type>  [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-s", "--s2-servers", dest="s2_servers",
                            action="store", type=str, default=None,
                            help="the IDs of s2 servers you want to resize.")

        parser.add_argument("-T", "--s2-server-type", dest="s2_server_type",
                            action="store", type=int, default=None,
                            help="valid values includes 0, 1, 2, 3.")


    @classmethod
    def build_directive(cls, options):
        for key in ['s2_servers', 's2_server_type']:
            if not hasattr(options, key):
                print("error: [%s] should be specified." % key)
                return None
        
        directive = {
            "s2_servers": explode_array(options.s2_servers),
            "s2_server_type": options.s2_server_type,
        }
        
        return directive
