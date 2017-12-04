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


class DeleteGroupRolesAction(BaseAction):
    action = 'DeleteGroupRoles'
    command = 'delete-group-roles'
    usage = '%(prog)s [-r <group_roles>] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-r", "--group-roles", dest="group_roles",
                            action="store", type=str, default='',
                            help="an array including the IDs of group roles.")

    @classmethod
    def build_directive(cls, options):
        group_roles = explode_array(options.group_roles)
        if not group_roles:
            print('error: group_roles should be specified')
            return None

        directive = {
            "group_roles": group_roles,
        }

        return directive
