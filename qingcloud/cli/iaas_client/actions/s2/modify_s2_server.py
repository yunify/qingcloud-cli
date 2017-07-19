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

class ModifyS2ServerAttributesAction(BaseAction):
    action = 'ModifyS2ServerAttributes'
    command = 'modify-s2-server'
    usage = '%(prog)s -s <s2_server> [-n <s2_server_name> ...] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-s", "--s2-server", dest="s2_server",
                            action="store", type=str, default=None,
                            help="the ID of s2 server.")

        parser.add_argument("-n", "--s2-server-name", dest="s2_server_name",
                            action="store", type=str, default=None,
                            help="the new name you want to use.")

        parser.add_argument("-d", "--description", dest="description",
                            action="store", type=str, default=None,
                            help="the new value of description.")


    @classmethod
    def build_directive(cls, options):
        for key in ['s2_server']:
            if not hasattr(options, key):
                print("error: [%s] should be specified." % key)
                return None
        
        directive = {
            "s2_server": options.s2_server,
            "s2_server_name": options.s2_server_name,
            "description": options.description,
        }
        
        return directive
