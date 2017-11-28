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


class DescribeAlarmHistoryAction(BaseAction):
    action = 'DescribeAlarmHistory'
    command = 'describe-alarm-history'
    usage = '%(prog)s [-a <alarm> ...] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-a", "--alarm", dest="alarm",
                            action="store", type=str, default='',
                            help=" the ID of the resource alarm entity.")

        parser.add_argument("-t", "--history-type", dest="history_type",
                            action="store", type=str, default=None,
                            help="the types including trigger_action, status_change and config_update.")

    @classmethod
    def build_directive(cls, options):
        directive = {
            "alarm": options.alarm,
            "history_type": options.history_type,
        }

        return directive
