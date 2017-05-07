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

class CreateLoadBalancerAction(BaseAction):

    action = 'CreateLoadBalancer'
    command = 'create-loadbalancer'
    usage = '%(prog)s -e <eips> [-n <name> -s <sg> -f <conf_file>]'
    description = 'Associate one or more eips with load balancer'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-t', '--loadbalancer_type', dest='loadbalancer_type',
                action='store', type=int, default='0',
                help='the type of load balancer.')

        parser.add_argument('-e', '--eips', dest='eips',
                action='store', type=str, default='',
                help='the comma separated IDs of eips you want to associate.')

        parser.add_argument('-N', '--name', dest='name',
                action='store', type=str, default='',
                help='load balancer name.')

        parser.add_argument('-s', '--sg', dest='sg',
                action='store', type=str, default=None,
                help='the ID of security group which will be applied to load balancer.')

        parser.add_argument('-c', '--node_count', dest='node_count',
                action='store', type=int, default=None,
                help='the number of nodes in load balancer cluster.')

        parser.add_argument('--target-user', dest='target_user',
                action='store', type=str, default=None,
                help='ID of user who will own this resource, should be one of your sub-account.')

    @classmethod
    def build_directive(cls, options):
        required_params = {
                'eips': options.eips,
                }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('error: [%s] should be specified' % param)
                return None

        return {
                'eips': explode_array(options.eips),
                'loadbalancer_name': options.name,
                'loadbalancer_type': options.loadbalancer_type,
                'security_group': options.sg,
                'node_count': options.node_count,
                'target_user': options.target_user,
                }
