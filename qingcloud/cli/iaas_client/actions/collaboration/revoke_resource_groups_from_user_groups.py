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

import json


class RevokeResourceGroupsFromUserGroupsAction(BaseAction):
    action = 'RevokeResourceGroupsFromUserGroups'
    command = 'revoke-resource-groups-from-user-groups'
    usage = '%(prog)s [-r <ru_set>] [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-r", "--ru-set", dest="ru_set",
                            action="store", type=str, default='',
                            help="a list of JSON Object which contains ID of resource group and ID of user group. \
                                 'For Example:' \
                                 '[{'resource_group': 'rg-xxxxx', 'user_group': 'ug-xxxxx', 'priority': '2', 'protocol': 'tcp'}]'.")

        parser.add_argument("-R", "--resource-groups", dest="resource_groups",
                            action="store", type=str, default=None,
                            help="an array including IDs of resource groups. \
                                  if it is not empty, will revoke all authorization relationships of specified resource groups.")

        parser.add_argument("-u", "--user-groups", dest="user_groups",
                            action="store", type=str, default=None,
                            help="an array including IDs of resource groups. \
                                  if it is not empty, will revoke all authorization relationships of specified user groups.")

        parser.add_argument("-g", "--group-roles", dest="group_roles",
                            action="store", type=str, default=None,
                            help="an array including IDs of resource groups. \
                                  if it is not empty, will revoke all authorization relationships of specified group roles.")

    @classmethod
    def build_directive(cls, options):
        if options.ru_set == '':
            print('error: ru_set should be specified')
            return None

        directive = {
            "ru_set": json.loads(options.ru_set),
            "resource_groups": explode_array(options.resource_groups),
            "user_groups": explode_array(options.user_groups),
            "group_roles": explode_array(options.group_roles),
        }

        return directive
