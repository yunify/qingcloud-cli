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


class DeleteGroupRoleRulesAction(BaseAction):
    action = 'DeleteGroupRoleRules'
    command = 'delete-group-role-rules'
    usage = '%(prog)s [-r <group_role_rules> ...] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-r", "--group-role-rules", dest="group_role_rules",
                            action="store", type=str, default=None,
                            help="an array including the IDs of group role rules.")

        parser.add_argument("-R", "--group-roles", dest="group_roles",
                            action="store", type=str, default=None,
                            help="an array including the IDs of group roles.")

    @classmethod
    def build_directive(cls, options):
        directive = {
            "group_role_rules": explode_array(options.group_role_rules),
            "group_roles": explode_array(options.group_roles),
        }

        return directive
