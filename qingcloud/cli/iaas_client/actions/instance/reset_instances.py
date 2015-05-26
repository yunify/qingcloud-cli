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


class ResetInstancesAction(BaseAction):

    action = 'ResetInstances'
    command = 'reset-instances'
    usage = '%(prog)s -i "instance_id, ..." [-f <conf_file> -m <login_mode> -p <login_passwd> -k <login_keypair>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-i', '--instances', dest='instances',
                action='store', type=str, default='',
                help='the comma separated IDs of instances you want to reset.')

        parser.add_argument('-l', '--login_mode', dest='login_mode',
                action='store', type=str, default=None,
                help='SSH login mode: keypair or passwd')

        parser.add_argument('-p', '--login_passwd', dest='login_passwd',
                action='store', type=str, default=None,
                help='login_passwd, should specified when SSH login mode is "passwd".')

        parser.add_argument('-k', '--login_keypair', dest='login_keypair',
                action='store', type=str, default=None,
                help='login_keypair, should specified when SSH login mode is "keypair".')

        return parser

    @classmethod
    def build_directive(cls, options):
        instances = explode_array(options.instances)
        if len(instances) == 0:
            print('error: [instances] should be specified')
            return None

        return {
                'instances': instances,
                'login_mode': options.login_mode,
                'login_passwd': options.login_passwd,
                'login_keypair': options.login_keypair,
                }
