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

from qingcloud.cli.iaas_client.actions.base import BaseAction

class ChangeS2ServerVxnetAction(BaseAction):
    action = 'ChangeS2ServerVxnet'
    command = 'change-s2-server-vxnet'
    usage = '%(prog)s -s <s2_server> -v <vxnet> [-p <private_ip> ...] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-s", "--s2-server", dest="s2_server",
                            action="store", type=str, default=None,
                            help="the ID of s2 server.")

        parser.add_argument("-v", "--vxnet", dest="vxnet",
                            action="store", type=str, default=None,
                            help="the ID of vxnet.")

        parser.add_argument("-p", "--private-ip", dest="private_ip",
                            action="store", type=str, default=None,
                            help="you may specify the ip address of this server.")


    @classmethod
    def build_directive(cls, options):
        for key in ['s2_server', 'vxnet']:
            if not hasattr(options, key):
                print("error: [%s] should be specified." % key)
                return None
        
        directive = {
            "s2_server": options.s2_server,
            "vxnet": options.vxnet,
            "private_ip": options.private_ip,
        }
        
        return directive
