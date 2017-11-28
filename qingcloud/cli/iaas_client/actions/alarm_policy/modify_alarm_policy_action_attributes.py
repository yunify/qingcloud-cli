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


class ModifyAlarmPolicyActionAttributesAction(BaseAction):
    action = 'ModifyAlarmPolicyActionAttributes'
    command = 'modify-alarm-policy-action-attributes'
    usage = '%(prog)s [-a <alarm_policy_action>...] [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument("-a", "--alarm-policy-action", dest="alarm_policy_action",
                            action="store", type=str, default='',
                            help="the ID of the alarm policy action whose content you want to update.")

        parser.add_argument("-A", "--trigger-action", dest="trigger_action",
                            action="store", type=str, default=None,
                            help="the ID of the trigger action.")

        parser.add_argument("-s", "--trigger-status", dest="trigger_status",
                            action="store", type=str, default=None,
                            help="when the monitor alarm state becomes 'ok' or 'alarm', "
                                 "the message will be sent to this trigger list.")

    @classmethod
    def build_directive(cls, options):

        if options.alarm_policy_action == '':
            print('error: alarm_policy_action should be specified.')
            return None

        directive = {
            "alarm_policy_action": options.alarm_policy_action,
            "trigger_action": options.trigger_action,
            "trigger_status": options.trigger_status,
        }

        return directive
