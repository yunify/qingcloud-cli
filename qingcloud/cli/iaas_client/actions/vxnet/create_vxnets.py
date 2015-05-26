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

class CreateVxnetsAction(BaseAction):

    action = 'CreateVxnets'
    command = 'create-vxnets'
    usage = '%(prog)s --count <count> --vxnet_name <vxnet_name> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-c', '--count', dest='count',
                action='store', type=int, default=1,
                help='the number of vxnets to create.')
        
        parser.add_argument('-N', '--vxnet_name', dest='vxnet_name',
                action='store', type=str, default='',
                help='the short name of vxnet you want to create.')

        parser.add_argument('-t', '--vxnet_type', dest='vxnet_type',
                action='store', type=int, default=1,
                help='the vxnet type. 0: unmanaged vxnet, 1: managed vxnet. Default 1.')
        
    @classmethod
    def build_directive(cls, options):
        if not options.vxnet_name:
            print('[vxnet_name] should be specified.')
            return None
        
        return {
                'vxnet_name': options.vxnet_name,
                'vxnet_type': options.vxnet_type,
                'count': options.count}
