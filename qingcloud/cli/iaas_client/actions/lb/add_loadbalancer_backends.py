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

import json

from qingcloud.cli.iaas_client.actions.base import BaseAction

class AddLoadBalancerBackendsAction(BaseAction):

    action = 'AddLoadBalancerBackends'
    command = 'add-loadbalancer-backends'
    usage = '%(prog)s -s <lb_listener> -b <backends> [-f <conf_file>]'
    description = 'Add one or more backends to load balancer listener'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-s', '--lb_listener', dest='lb_listener',
                action='store', type=str, default='',
                help='ID of load balancer listener which you add backends to.')

        parser.add_argument('-b', '--backends', dest='backends',
                action='store', type=str, default='',
                help='JSON string of backend list. e.g. \
                      \'[{"loadbalancer_backend_name": "demo","resource_id":"i-1234abcd","port":"80","weight":"5"}]\'')

    @classmethod
    def build_directive(cls, options):
        required_params = {
                'loadbalancer_listener': options.lb_listener,
                'backends': options.backends,
                }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('error: [%s] should be specified' % param)
                return None

        return {
                'loadbalancer_listener': options.lb_listener,
                'backends': json.loads(options.backends),
                }
