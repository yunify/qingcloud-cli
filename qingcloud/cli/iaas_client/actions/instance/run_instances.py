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

class RunInstancesAction(BaseAction):

    action = 'RunInstances'
    command = 'run-instances'
    usage = '%(prog)s --image_id <image_id> --instance_type <instance_type> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-m', '--image_id', dest='image_id',
                action='store', type=str, default='',
                help='image ID')

        parser.add_argument('-t', '--instance_type', dest='instance_type',
                action='store', type=str, default=None,
                help='instance type: small_b, small_c, medium_a, medium_b, medium_c, \
                large_a, large_b, large_c')

        parser.add_argument('-c', '--count', dest = 'count',
                action='store', type=int, default=1,
                help='the number of instances to launch, default 1.')

        parser.add_argument('-C', '--cpu', dest='cpu',
                action='store', type=int, default=None,
                help='cpu core: 1, 2, 4, 8, 16')

        parser.add_argument('-M', '--memory', dest='memory',
                action='store', type=int, default=None,
                help='memory size in MB: 512, 1024, 2048, 4096, 8192, 16384')

        parser.add_argument('-N', '--instance_name', dest='instance_name',
                action='store', type=str, default='',
                help='instance name')

        parser.add_argument('-n', '--vxnets', dest='vxnets',
                action='store', type=str, default=None,
                help='specifies the IDs of vxnets the instance will join.')

        parser.add_argument('-s', '--security_group', dest='security_group',
                action='store', type=str, default=None,
                help='the ID of security group that will be applied to instance')

        parser.add_argument('-l', '--login_mode', dest='login_mode',
                action='store', type=str, default=None,
                help='SSH login mode: keypair or passwd')

        parser.add_argument('-p', '--login_passwd', dest='login_passwd',
                action='store', type=str, default='',
                help='login_passwd, should specified when SSH login mode is "passwd".')

        parser.add_argument('-k', '--login_keypair', dest='login_keypair',
                action='store', type=str, default='',
                help='login_keypair, should specified when SSH login mode is "keypair".')

        parser.add_argument('--hostname', dest='hostname',
                action='store', type=str, default='',
                help='the hostname you want to specify for the new instance.')

        return parser

    @classmethod
    def build_directive(cls, options):

        required_params = {
                'image_id': options.image_id,
                }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('error: [%s] should be specified' % param)
                return None
        if not options.instance_type:
            if not options.cpu or not options.memory:
                print('error: [instance_type] should be specified or specify both [cpu] and [memory]')
                return None

        return {
                'image_id': options.image_id,
                'instance_type' : options.instance_type,
                'cpu': options.cpu,
                'memory': options.memory,
                'instance_name' : options.instance_name,
                'count' : options.count,
                'vxnets': explode_array(options.vxnets),
                'security_group': options.security_group,
                'login_mode': options.login_mode,
                'login_passwd': options.login_passwd,
                'login_keypair': options.login_keypair,
                'hostname': options.hostname,
                }
