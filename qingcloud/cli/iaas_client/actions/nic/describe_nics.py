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

class DescribeNicsAction(BaseAction):

    action = 'DescribeNics'
    command = 'describe-nics'
    usage = '%(prog)s -n "nic_id,..." [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-n', '--nics', dest='nics',
                            action='store', type=str, default='',
                            help='the comma separated IDs of nics you want to describe.')

        parser.add_argument('-x', '--vxnets', dest='vxnets',
                            action='store', type=str, default='',
                            help='the comma separated IDs of vxnet which nic attached.')

        parser.add_argument('-t', '--vxnet-type', dest='vxnet_type',
                            action='store', type=str, default=None,
                            help='the type of vxnet, 0: unmanaged, 1: managed.')

        parser.add_argument('-s', '--status', dest='status',
                            action='store', type=str, default='',
                            help='nic status: available, in-use.')

        parser.add_argument('-N', '--nic-name', dest='nic_name',
                            action='store', type=str, default='',
                            help='the name of nic')

    @classmethod
    def build_directive(cls, options):
        return {
            'nics': explode_array(options.nics),
            'status': explode_array(options.status),
            'nic_name': options.nic_name,
            'vxnets': explode_array(options.vxnets),
            'vxnet_type': explode_array(options.vxnet_type),
            'offset': options.offset,
            'limit': options.limit,
        }
