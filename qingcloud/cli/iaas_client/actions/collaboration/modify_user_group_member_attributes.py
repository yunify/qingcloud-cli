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


class ModifyUserGroupMemberAttributesAction(BaseAction):
    action = 'ModifyUserGroupMemberAttributes'
    command = 'modify-user-group-member-attributes'
    usage = '%(prog)s [-g <user_group>...] [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-g", "--user-group", dest="user_group",
                            action="store", type=str, default='',
                            help="The ID of user group which attributes you want to modify.")

        parser.add_argument("-u", "--user", dest="user",
                            action="store", type=str, default='',
                            help="The ID of user which will be modified.")

        parser.add_argument("-r", "--remarks", dest="remarks",
                            action="store", type=str, default=None,
                            help="The description of the user group.")

        parser.add_argument("-s", "--status", dest="status",
                            action="store", type=str, default=None,
                            help="the status of user group.")

    @classmethod
    def build_directive(cls, options):
        if options.user_group == '':
            print('error: user_group should be specified')
            return None
        if options.user == '':
            print('error: user should be specified')
            return None

        directive = {
            "user_group": options.user_group,
            "user": options.user,
            "remarks": options.remarks,
            "status": options.status,
        }

        return directive
