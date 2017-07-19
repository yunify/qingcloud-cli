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

class CreateRoutersAction(BaseAction):

    action = 'CreateRouters'
    command = 'create-routers'
    usage = '%(prog)s [-c <count>] [-N <router_name>] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-c', '--count', dest='count',
                action='store', type=int, default=1,
                help='the number of routers to create.')

        parser.add_argument('-N', '--router_name', dest='router_name',
                action='store', type=str, default='',
                help='the short name of routers')

        parser.add_argument('-s', '--security_group', dest='security_group',
                action='store', type=str, default='',
                help='ID of the security group you want to apply to router, use default security group if not specified')

        parser.add_argument('-n', '--vpc_network', dest='vpc_network',
                action='store', type=str, default=None,
                help='VPC IP addresses range, currently support "192.168.0.0/16" or "172.16.0.0/16", required in zone pek3a')

        parser.add_argument('-t', '--router_type', dest='router_type',
                action='store', type=int, default=1,
                help='0 - Medium, 1 - Small, 2 - large, 3 - extra-large')

    @classmethod
    def build_directive(cls, options):
        required_params = {
                'router_name': options.router_name,
                }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('error: [%s] should be specified' % param)
                return None

        return {
            'count' : options.count,
            'router_name' : options.router_name,
            'security_group': options.security_group,
            'vpc_network': options.vpc_network,
            'router_type': options.router_type,
        }
