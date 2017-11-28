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


class DeleteAlarmPolicyActionsAction(BaseAction):
    action = 'DeleteAlarmPolicyActions'
    command = 'delete-alarm-policy-actions'
    usage = '%(prog)s [-a <alarm_policy_actions> ] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument("-a", "--alarm-policy-actions", dest="alarm_policy_actions",
                            action="store", type=str, default='',
                            help="an array including IDs of alarm policy actions.")

    @classmethod
    def build_directive(cls, options):

        alarm_policy_actions = explode_array(options.alarm_policy_actions)
        if not alarm_policy_actions:
            print('error: alarm_policy_actions should be specified.')
            return None

        directive = {
            "alarm_policy_actions": alarm_policy_actions,
        }

        return directive
