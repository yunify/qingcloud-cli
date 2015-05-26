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

class LeaveRouterAction(BaseAction):

    action = 'LeaveRouter'
    command = 'leave-router'
    usage = '%(prog)s -r <router_id>] -v "vxnet_id, ..." [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-r', '--router', dest='router',
                action='store', type=str, default='',
                help='the id of the router the vxnet will leave.')
     
        parser.add_argument('-v', '--vxnets', dest='vxnets',
                action='store', type=str, default='',
                help='the comm separated IDs of the vxnets that will leave the router.')

    @classmethod
    def build_directive(cls, options):
        router = options.router
        vxnets = explode_array(options.vxnets)
        if not router or not vxnets:
            print('error: [router] and [vxnets] should be specified.')
            return None

        return {
                'router': router,
                'vxnets': vxnets,
                }
