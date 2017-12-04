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


class DeleteUserGroupMembersAction(BaseAction):
    action = 'DeleteUserGroupMembers'
    command = 'delete-user-group-members'
    usage = '%(prog)s [-g <user_group> ...] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-g", "--user-group", dest="user_group",
                            action="store", type=str, default='',
                            help="the ID of the user group.")

        parser.add_argument("-u", "--users", dest="users",
                            action="store", type=str, default='',
                            help="An array including IDs of users which you want to delete.")

    @classmethod
    def build_directive(cls, options):
        if options.user_group == '':
            print('error: user_group should be specified')
            return None
        users = explode_array(options.users)
        if not users:
            print('error: users should be specified')
            return None

        directive = {
            "user_group": options.user_group,
            "users": users
        }

        return directive
