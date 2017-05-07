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

class CreateNicsAction(BaseAction):

    action = 'CreateNics'
    command = 'create-nics'
    usage = '%(prog)s --vxnet <vxnet> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-x', '--vxnet', dest='vxnet',
                            action='store', type=str, default=None,
                            help='the ID of vxnet.')

        parser.add_argument('-N', '--nic-name', dest='nic_name',
                            action='store', type=str, default=None,
                            help='the name of nic.')

        parser.add_argument('-p', '--private-ips', dest='private_ips',
                            action='store', type=str, default=None,
                            help='''the private ip of nics. ''')

        parser.add_argument('-c', '--count', dest='count',
                            action='store', type=int, default=1,
                            help='the number of nics to create.')

    @classmethod
    def build_directive(cls, options):
        required_params = {'vxnet': options.vxnet}
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('error: [%s] should be specified' % param)
                return None

        return {
            'vxnet': options.vxnet,
            'count' : options.count,
            'nic_name' : options.nic_name,
            'private_ips': explode_array(options.private_ips),
        }
