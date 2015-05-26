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

class DescribeVxnetInstancesAction(BaseAction):

    action = 'DescribeVxnetInstances'
    command = 'describe-vxnet-instances'
    usage = '%(prog)s -v <vxnet_id> [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-v', '--vxnet', dest='vxnet',
                action='store', type=str, default='',
                help='ID of vxnet whose instances you want to list.')

        parser.add_argument('-m', '--image', dest='image',
                action='store', type=str, default='',
                help='filter by ID of image that instance based')

        parser.add_argument('-i', '--instances', dest='instances',
                action='store', type=str, default='',
                help='filter by comma separated IDs of instances')

        parser.add_argument('-t', '--instance_type', dest='instance_type',
                action='store', type=str, default='',
                help='filter by instance type')

        parser.add_argument('-s', '--status', dest='status',
                action='store', type=str, default='',
                help='filter by instance status: pending, running, stopped, suspended, terminated, ceased')

    @classmethod
    def build_directive(cls, options):
        if not options.vxnet:
            print('[vxnet] should be provided')
            return None

        return {
                'vxnet': options.vxnet,
                'image': explode_array(options.image),
                'instances': explode_array(options.instances),
                'instance_type': explode_array(options.instance_type),
                'status': explode_array(options.status),
                'offset':options.offset,
                'limit': options.limit,
                }
