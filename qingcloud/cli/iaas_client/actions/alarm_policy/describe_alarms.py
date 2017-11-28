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


class DescribeAlarmsAction(BaseAction):
    action = 'DescribeAlarms'
    command = 'describe-alarms'
    usage = '%(prog)s [-a <alarms> ...] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-a", "--alarms", dest="alarms",
                            action="store", type=str, default=None,
                            help="an array including IDs of the alarms you want to list.")

        parser.add_argument("-p", "--policy", dest="policy",
                            action="store", type=str, default=None,
                            help=" the ID of alarm policy.")

        parser.add_argument("-r", "--resource", dest="resource",
                            action="store", type=str, default=None,
                            help="the ID of resource associated to this policy.")

        parser.add_argument("-s", "--status", dest="status",
                            action="store", type=str, default=None,
                            help="ok stand for normal,alarm stand for alarming,insufficient stand for monitoring data cannot be collected.")

    @classmethod
    def build_directive(cls, options):
        directive = {
            "alarms": explode_array(options.alarms),
            "policy": options.policy,
            "resource": options.resource,
            "status": options.status
        }

        return directive
