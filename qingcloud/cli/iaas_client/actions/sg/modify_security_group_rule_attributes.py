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

class ModifySecurityGroupRuleAttributesAction(BaseAction):

    action = 'ModifySecurityGroupRuleAttributes'
    command = 'modify-security-group-rule-attributes'
    usage = '%(prog)s -r <security_group_rule_id> -p <priority> [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-r', '--security_group_rule', dest='security_group_rule',
                action='store', type=str, default='',
                help='ID of security group rule whose attributes you want to update.')

        parser.add_argument('-N', '--name', dest='name',
                action='store', type=str, default=None,
                help='name of the rule.')

        parser.add_argument('-p', '--priority', dest='priority',
                action='store', type=int, default=None,
                help='priority of the rule, from 0 to 100.')

        parser.add_argument('-P', '--protocol', dest='protocol',
                action='store', type=str, default=None,
                help='protocol of the rule.')

        parser.add_argument('-a', '--rule_action', dest='rule_action',
                action='store', type=str, default=None,
                help='action of the rule: "accept" or "drop".')

        parser.add_argument('-d', '--direction', dest='direction',
                action='store', type=int, default=None,
                help='direction of the rule: 0 for inbound, 1 for outbound.')

        parser.add_argument('--val1', dest='val1',
                action='store', type=str, default=None,
                help='''for "icmp", this field is icmp type;
                        for "tcp/udp", it is start port(empty means all).''')

        parser.add_argument('--val2', dest='val2',
                action='store', type=str, default=None,
                help='''for "icmp", this field is icmp code;
                        for "tcp/udp", it is end port(empty means all).''')

        parser.add_argument('--val3', dest='val3',
                action='store', type=str, default=None,
                help='ip network, e.g "1.2.3.0/24"')

    @classmethod
    def build_directive(cls, options):
        if not options.security_group_rule:
            print('error: [security_group_rule] should be specified')
            return None

        if options.rule_action or options.direction or options.protocol:
            if not options.priority:
                print('error: [priority] should be specified')
                return None

            if not options.protocol:
                print('error: [protocol] should be specified')
                return None

        return {
                'security_group_rule': options.security_group_rule,
                'priority': options.priority,
                'security_group_rule_name': options.name,
                'protocol': options.protocol,
                'direction': options.direction,
                'rule_action': options.rule_action,
                'val1': options.val1,
                'val2': options.val2,
                'val3': options.val3,
                }
