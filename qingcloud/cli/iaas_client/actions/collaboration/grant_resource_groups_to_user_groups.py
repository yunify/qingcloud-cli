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
import json


class GrantResourceGroupsToUserGroupsAction(BaseAction):
    action = 'GrantResourceGroupsToUserGroups'
    command = 'grant-resource-groups-to-user-groups'
    usage = '%(prog)s [-r <rur_set>] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-r", "--rur-set", dest="rur_set",
                            action="store", type=str, default='',
                            help="a list of JSON Object which contains 'ID of resource group', \
                                 'ID of user group' and 'ID of group role'. \
                                 'For Example:' \
                                 '[{'resource_group': 'rg-xxxxx', 'user_group': 'ug-xxxxx', 'group_role': 'gr-xxxxx','priority': '2', 'protocol': 'tcp'}]'.")

    @classmethod
    def build_directive(cls, options):
        if options.rur_set == '':
            print('error: rur_set should be specified')
            return None

        directive = {
            "rur_set": json.loads(options.rur_set),
        }

        return directive
