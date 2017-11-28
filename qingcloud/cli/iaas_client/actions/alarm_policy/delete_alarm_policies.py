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


class DeleteAlarmPoliciesAction(BaseAction):

    action = 'DeleteAlarmPolicies'
    command = 'delete-alarm-policies'
    usage = '%(prog)s [-a alarm-policies] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-a', '--alarm-policies', dest='alarm_policies',
                            action='store', type=str, default='',
                            help='an array including IDs of alarm policies.')

    @classmethod
    def build_directive(cls, options):

        alarm_policies = explode_array(options.alarm_policies)
        if not alarm_policies:
            print('error: [alarm_policies] should be specified')
            return None

        directive = {
            "alarm_policies": alarm_policies,
        }

        return directive
