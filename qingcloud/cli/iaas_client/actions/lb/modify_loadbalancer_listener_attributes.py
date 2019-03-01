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

class ModifyLoadBalancerListenerAttributessAction(BaseAction):

    action = 'ModifyLoadBalancerListenerAttributes'
    command = 'modify-loadbalancer-listener-attributes'
    usage = '%(prog)s -s <lb_listener> [options] [-f <conf_file>]'
    description = 'Modify load balancer listener attributes.'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-s', '--lb_listener', dest='lb_listener',
                action='store', type=str, default='',
                help='the ID of load balancer listener.')

        parser.add_argument('-M', '--balance_mode', dest='balance_mode',
                action='store', type=str, default=None,
                help='the balance mode: roundrobin, leastconn.')

        parser.add_argument('-F', '--forwardfor', dest='forwardfor',
                action='store', type=str, default=None,
                help='comma separated headers the listener will pass, \
                      including: "X_FORWARD_FOR", "QC_LB_ID", "QC_LB_IP".')

        parser.add_argument('-m', '--healthy_check_method', dest='healthy_check_method',
                action='store', type=str, default=None,
                help='heathy check method: "tcp","http|/url","http|/url|host", empty string means disable check.')

        parser.add_argument('-o', '--healthy_check_option', dest='healthy_check_option',
                action='store', type=str, default=None,
                help='healthy check option, formatted as \
                      "inter|timeout|fall|rise"')

        parser.add_argument('-k', '--session_sticky', dest='session_sticky',
                action='store', type=str, default=None,
                help='session sticky: "insert|cookie_timeout","prefix|cookie_name",\
                      empty string means disable sticky.')

        parser.add_argument('-N', '--lb_listener_name', dest='lb_listener_name',
                action='store', type=str, default=None,
                help='new listener name.')

        parser.add_argument('-S', '--server-certificate', dest='server_certificate_id',
                action='store', type=str, default=None,
                help='the comma separated IDs of server certificates.')

    @classmethod
    def build_directive(cls, options):
        if not options.lb_listener:
            print('error: listener should be specified')
            return None

        forwardfor = options.forwardfor
        if forwardfor:
            mapper = {
                    'X_FORWARD_FOR': 1,
                    'QC_LB_ID': 2,
                    'QC_LB_IP': 4,
                    }
            headers = [h for h in explode_array(forwardfor) if h in mapper]
            forwardfor = 0
            for header in headers:
                forwardfor |= mapper[header]

        return {
                'loadbalancer_listener': options.lb_listener,
                'loadbalancer_listener_name': options.lb_listener_name,
                'balance_mode': options.balance_mode,
                'forwardfor': forwardfor,
                'healthy_check_method': options.healthy_check_method,
                'healthy_check_option': options.healthy_check_option,
                'session_sticky': options.session_sticky,
                'server_certificate_id': explode_array(options.server_certificate_id),
                }
