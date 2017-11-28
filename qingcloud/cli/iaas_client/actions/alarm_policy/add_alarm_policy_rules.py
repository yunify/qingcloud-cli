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


class AddAlarmPolicyRulesAction(BaseAction):
    action = 'AddAlarmPolicyRules'
    command = 'add-alarm-policy-rules'
    usage = '%(prog)s [-a <alarm_policy>...] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument("-a", "--alarm-policy", dest="alarm_policy",
                            action="store", type=str, default='',
                            help="the ID of the alarm policy whose rules you want to add.")

        parser.add_argument("-r", "--rules", dest="rules",
                            action="store", type=str, default='',
                            help="it's a JSON string list of rules you want to add.")

    @classmethod
    def build_directive(cls, options):

        if options.alarm_policy == '':
            print('error: alarm_policy should be specified.')
            return None
        if options.rules == '':
            print('error: rules should be specified.')
            return None

        directive = {
            "alarm_policy": options.alarm_policy,
            "rules": json.loads(options.rules)
        }

        return directive
