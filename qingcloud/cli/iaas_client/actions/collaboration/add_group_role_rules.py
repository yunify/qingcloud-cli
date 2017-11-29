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


class AddGroupRoleRulesAction(BaseAction):
    action = 'AddGroupRoleRules'
    command = 'add-group-role-rules'
    usage = '%(prog)s [-r <group_role> ...] [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-r", "--group-role", dest="group_role",
                            action="store", type=str, default='',
                            help="the ID of the group role.")

        parser.add_argument("-p", "--policy", dest="policy",
                            action="store", type=str, default='',
                            help="the policy whose format is 'resource_typeor.operation_type', \
                                 See: https://docs.qingcloud.com/api/resource_acl/AddGroupRoleRules.html.")

        parser.add_argument("-d", "--description", dest="description",
                            action="store", type=str, default=None,
                            help="the description of rule.")

    @classmethod
    def build_directive(cls, options):
        if options.group_role == '':
            print('error: group_role should be specified')
            return None
        if options.policy == '':
            print('error: policy should be specified')
            return None

        directive = {
            "group_role": options.group_role,
            "policy": options.policy,
            "description": options.description,
        }

        return directive
