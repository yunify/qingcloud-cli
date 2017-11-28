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


class ModifyAlarmPolicyRuleAttributesAction(BaseAction):
    action = 'ModifyAlarmPolicyRuleAttributes'
    command = 'modify-alarm-policy-rule-attributes'
    usage = '%(prog)s [-r <alarm_policy_rule>...] [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument("-r", "--alarm-policy-rule", dest="alarm_policy_rule",
                            action="store", type=str, default='',
                            help="the ID of the alarm policy rule whose content you want to update.")

        parser.add_argument("-c", "--condition-type", dest="condition_type",
                            action="store", type=str, default='',
                            help="'gt' for greater than, 'lt' for less than.")

        parser.add_argument("-n", "--alarm-policy-rule-name", dest="alarm_policy_rule_name",
                            action="store", type=str, default=None,
                            help="the name of alarm policy rule.")

        parser.add_argument("-t", "--thresholds", dest="thresholds",
                            action="store", type=str, default=None,
                            help="the thresholds of alarm.")

        parser.add_argument("-d", "--data-processor", dest="data_processor",
                            action="store", type=str, default=None,
                            help="raw for use the monitoring data raw value, percent only for IP bandwidth monitoring.")

        parser.add_argument("-p", "--consecutive_periods", dest="consecutive_periods",
                            action="store", type=str, default=None,
                            help="uring several consecutive inspection periods, the monitoring data reaches the alarm threshold,then will trigger the alarm behavior.")

    @classmethod
    def build_directive(cls, options):

        if options.alarm_policy_rule == '':
            print('error: alarm_policy_rule should be specified.')
            return None
        if options.condition_type == '':
            print('error: condition_type should be specified.')
            return None

        directive = {
            "alarm_policy_rule": options.alarm_policy_rule,
            "condition_type": options.condition_type,
            "alarm_policy_rule_name": options.alarm_policy_rule_name,
            "thresholds": options.thresholds,
            "data_processor": options.data_processor,
            "consecutive_periods": options.consecutive_periods,
        }

        return directive
