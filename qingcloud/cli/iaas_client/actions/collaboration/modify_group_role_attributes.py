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


class ModifyGroupRoleAttributesAction(BaseAction):
    action = 'ModifyGroupRoleAttributes'
    command = 'modify-group-role-attributes'
    usage = '%(prog)s [-r <group_role>] [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-r", "--group-role", dest="group_role",
                            action="store", type=str, default='',
                            help="The ID of group role which attributes you want to modify.")

        parser.add_argument("-t", "--role-type", dest="role_type",
                            action="store", type=str, default=None,
                            help="The type of role, Currently only support 'rule'.")

        parser.add_argument("-n", "--group-role-name", dest="group_role_name",
                            action="store", type=str, default=None,
                            help="The name of group role.")

        parser.add_argument("-d", "--description", dest="description",
                            action="store", type=str, default=None,
                            help="The description of group role.")

        parser.add_argument("-s", "--status", dest="status",
                            action="store", type=str, default=None,
                            help="The status of group role which could be 'disabled' or 'enabled'.")

    @classmethod
    def build_directive(cls, options):
        if options.group_role == '':
            print('error: group_role should be specified')
            return None

        directive = {
            "group_role": options.group_role,
            "role_type": options.role_type,
            "group_role_name": options.group_role_name,
            "description": options.description,
            "status": options.status,
        }

        return directive
