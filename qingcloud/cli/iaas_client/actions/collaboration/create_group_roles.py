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


class CreateGroupRolesAction(BaseAction):
    action = 'CreateGroupRoles'
    command = 'create-group-roles'
    usage = '%(prog)s [-t <role_type>] [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-t", "--role-type", dest="role_type",
                            action="store", type=str, default='',
                            help="the type of role, Currently only support 'rule'.")

        parser.add_argument("-n", "--group-role-name", dest="group_role_name",
                            action="store", type=str, default=None,
                            help="the name of group role.")

        parser.add_argument("-d", "--description", dest="description",
                            action="store", type=str, default=None,
                            help="the description of group role.")

        parser.add_argument("-c", "--count", dest="count",
                            action="store", type=int, default=1,
                            help="the number of user roles created at one time,defaults 1.")

    @classmethod
    def build_directive(cls, options):
        if options.role_type == '':
            print('error: role_type should be specified')
            return None

        directive = {
            "role_type": options.role_type,
            "group_role_name": options.group_role_name,
            "description": options.description,
            "count": options.count,
        }

        return directive
