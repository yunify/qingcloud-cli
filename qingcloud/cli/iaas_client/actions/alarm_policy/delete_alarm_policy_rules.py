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

from qingcloud.cli.misc.utils import explode_array


class DeleteAlarmPolicyRulesAction(BaseAction):
    action = 'DeleteAlarmPolicyRules'
    command = 'delete-alarm-policy-rules'
    usage = '%(prog)s [-r <alarm_policy_rules> ] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-r", "--alarm-policy-rules", dest="alarm_policy_rules",
                            action="store", type=str, default='',
                            help="an array including IDs of alarm policy rules.")

    @classmethod
    def build_directive(cls, options):
        alarm_policy_rules = explode_array(options.alarm_policy_rules)
        if not alarm_policy_rules:
            print('error: alarm_policy_rules should be specified.')
            return None

        directive = {
            "alarm_policy_rules": alarm_policy_rules,
        }

        return directive
