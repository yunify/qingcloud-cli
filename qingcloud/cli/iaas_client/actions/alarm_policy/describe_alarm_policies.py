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

class DescribeAlarmPoliciesAction(BaseAction):
    action = 'DescribeAlarmPolicies'
    command = 'describe-alarm-policies'
    usage = '%(prog)s [-a <alarm_policies> ...] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-a", "--alarm-policies", dest="alarm_policies",
                            action="store", type=str, default=None,
                            help="id IDs of alarm policies you want to describe.")

        parser.add_argument("-n", "--alarm-policy-name", dest="alarm_policy_name",
                            action="store", type=str, default=None,
                            help="the name of alarm policy.")

        parser.add_argument("-t", "--alarm-policy-type", dest="alarm_policy_type",
                            action="store", type=str, default=None,
                            help="valid values includes instance, eip, router, loadbalancer_listener_http, loadbalancer_listener_tcp, loadbalancer_backend_http, loadbalancer_backend_tcp.")

        parser.add_argument("-s", "--search-word", dest="search_word",
                            action="store", type=str, default=None,
                            help="you can use this field to search from id or name.")

        parser.add_argument("-r", "--resource", dest="resource",
                            action="store", type=str, default=None,
                            help="the ID of resource associated to this policy.")

        parser.add_argument("-S", "--status", dest="status",
                            action="store", type=str, default=None,
                            help="valid values includes active, suspended.")

        parser.add_argument("-v", "--verbose", dest="verbose",
                            action="store", type=int, default=None,
                            help="the number to specify the verbose level,")


    @classmethod
    def build_directive(cls, options):
        directive = {
            "alarm_policies": explode_array(options.alarm_policies),
            "alarm_policy_name": options.alarm_policy_name,
            "alarm_policy_type": options.alarm_policy_type,
            "search_word": options.search_word,
            "resource": options.resource,
            "status": explode_array(options.status),
            "verbose": options.verbose,
        }
        
        return directive
