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


class CreateUserGroupsAction(BaseAction):
    action = 'CreateUserGroups'
    command = 'create-user-groups'
    usage = '%(prog)s [-n <user_group_name> ...] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-n", "--user-group-name", dest="user_group_name",
                            action="store", type=str, default=None,
                            help="the name of user groups.")

        parser.add_argument("-d", "--description", dest="description",
                            action="store", type=str, default=None,
                            help="the description of user groups.")

        parser.add_argument("-c", "--count", dest="count",
                            action="store", type=int, default=1,
                            help="the number of user groups created at one time,defaults 1.")

    @classmethod
    def build_directive(cls, options):
        directive = {
            "user_group_name": options.user_group_name,
            "description": options.description,
            "count": options.count,
        }

        return directive
