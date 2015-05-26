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

class DeleteSecurityGroupRulesAction(BaseAction):

    action = 'DeleteSecurityGroupRules'
    command = 'delete-security-group-rules'
    usage = '%(prog)s -r "security_group_rule_id, ..." [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-r', '--security_group_rules', dest='security_group_rules',
                action='store', type=str, default='',
                help='the comma separated IDs of security group rules you want to delete. ')

    @classmethod
    def build_directive(cls, options):
        security_group_rules = explode_array(options.security_group_rules)
        if not security_group_rules:
            print("[security_groups_rules] should be specified.")
            return None
        
        return {
                'security_group_rules': security_group_rules,
                }
