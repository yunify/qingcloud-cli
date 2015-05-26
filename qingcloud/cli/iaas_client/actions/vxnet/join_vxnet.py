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

class JoinVxnetAction(BaseAction):

    action = 'JoinVxnet'
    command = 'join-vxnet'
    usage = '%(prog)s --instances "instance_id, ..." --vxnet <vxnet_id> [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-i', '--instances', dest='instances',
                action='store', type=str, default='',
                help='IDs of instances that will join a vxnet.')

        parser.add_argument('-v', '--vxnet', dest='vxnet',
                action='store', type=str, default='',
                help='the id of vxnet the instances will join.')

    @classmethod
    def build_directive(cls, options):
        instances = explode_array(options.instances)
        if not options.vxnet or not instances:
            print('error: [instances] and [vxnet] should be specified')
            return None

        return {
                'vxnet': options.vxnet,
                'instances': instances,
                }
