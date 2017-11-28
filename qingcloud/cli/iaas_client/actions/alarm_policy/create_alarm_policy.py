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


class CreateAlarmPolicyAction(BaseAction):
    action = 'CreateAlarmPolicy'
    command = 'create-alarm-policy'
    usage = '%(prog)s [-t <alarm_policy_type> ...] [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument("-t", "--alarm-policy-type", dest="alarm_policy_type",
                            action="store", type=str, default='',
                            help="valid values includes instance,eip,router,loadbalancer_listener_http,loadbalancer_listener_tcp,loadbalancer_backend_http,loadbalancer_backend_tcp.")

        parser.add_argument("-p", "--period", dest="period",
                            action="store", type=str, default='',
                            help="the period of alarm_policy. For example: One minute : 1m.")

        parser.add_argument("-n", "--alarm-policy-name", dest="alarm_policy_name",
                            action="store", type=str, default=None,
                            help="the name of alarm policy.")

    @classmethod
    def build_directive(cls, options):

        if options.alarm_policy_type == '':
            print('error: alarm_policy_type should be specified.')
            return None
        if options.period == '':
            print('error: period should be specified.')
            return None

        directive = {
            "alarm_policy_type": options.alarm_policy_type,
            "period": options.period,
            "alarm_policy_name": options.alarm_policy_name,
        }

        return directive
