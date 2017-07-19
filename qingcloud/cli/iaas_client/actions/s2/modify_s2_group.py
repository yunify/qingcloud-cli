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

class ModifyS2GroupAction(BaseAction):
    action = 'ModifyS2Group'
    command = 'modify-s2-group'
    usage = '%(prog)s -s <s2_group> [-n <group_name> ...] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-s", "--s2-group", dest="s2_group",
                            action="store", type=str, default=None,
                            help="the ID of group.")

        parser.add_argument("-n", "--group-name", dest="group_name",
                            action="store", type=str, default=None,
                            help="the name of group.")

        parser.add_argument("-S", "--s2-accounts", dest="s2_accounts",
                            action="store", type=str, default=None,
                            help="the IDs of accounts.")

        parser.add_argument("-d", "--description", dest="description",
                            action="store", type=str, default=None,
                            help="the new value of description.")


    @classmethod
    def build_directive(cls, options):
        for key in ['s2_group']:
            if not hasattr(options, key):
                print("error: [%s] should be specified." % key)
                return None
        
        directive = {
            "s2_group": options.s2_group,
            "group_name": options.group_name,
            "s2_accounts": explode_array(options.s2_accounts),
            "description": options.description,
        }
        
        return directive
