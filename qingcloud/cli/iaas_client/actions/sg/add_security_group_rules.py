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

import json

from qingcloud.cli.iaas_client.actions.base import BaseAction

class AddSecurityGroupRulesAction(BaseAction):

    action = 'AddSecurityGroupRules'
    command = 'add-security-group-rules'
    usage = '%(prog)s -s <security_group_id> -r <rules> [-f <conf_file>]'
    description = 'Add one or more rules to security group'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-s', '--security_group', dest='security_group',
                action='store', type=str, default='',
                help='ID of security_group whose rules you want to list. ')

        parser.add_argument('-r', '--rules', dest='rules',
                action='store', type=str, default='',
                help='JSON string of rules list. e.g. \'[{"security_group_rule_name":"ping","protocol":"icmp","priority":"0","action":"accept","val2":"0","val1":"8"}]\'')

        parser.add_argument('-u', '--target-user', dest='target_user',
                            action='store', type=str, default=None,
                            help='the ID of user who will own this resource.')

    @classmethod
    def build_directive(cls, options):
        required_params = {
                'security_group': options.security_group,
                'rules': options.rules,
                }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('error: [%s] should be specified' % param)
                return None

        return {
                'security_group': options.security_group,
                'rules': json.loads(options.rules),
                'target_user': options.target_user,
                }
