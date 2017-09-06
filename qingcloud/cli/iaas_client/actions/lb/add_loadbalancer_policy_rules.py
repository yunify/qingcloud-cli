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

class AddLoadBalancerPolicyRulesAction(BaseAction):

    action = 'AddLoadBalancerPolicyRules'
    command = 'add-loadbalancer-policy-rules'
    usage = '%(prog)s -p <loadbalancer_policy> -r <rules> [-f <conf_file>]'
    description = 'Add policy rules to loadbalancer'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument("-p", "--loadbalancer_policy", dest="loadbalancer_policy",
                action="store", type=str, default="",
                help='''the ID of loadbalancer_policy whose rules you want to add. ''')

        parser.add_argument("-r", "--rules", dest="rules",
                action="store", type=str, default="",
                help='''a json string of rules list. 
                    e.g. '[{"rule_type":"domain","val":"www.qingcloud.com"},{"rule_type":"url","val":"/scripts"}]' ''',
                          )

    @classmethod
    def build_directive(cls, options):
        required_params = {
                'loadbalancer_policy': options.loadbalancer_policy,
                'rules': options.rules,
                }

        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('error: [%s] should be specified' % param)
                return None

        loadbalancer_policy = options.loadbalancer_policy
        rules = json.loads(options.rules)
        if rules is None or len(rules) == 0 or len(loadbalancer_policy) == 0:
            return None

        return {"loadbalancer_policy": loadbalancer_policy,
                "rules": rules,
                }
