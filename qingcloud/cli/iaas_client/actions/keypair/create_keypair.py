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

class CreateKeyPairAction(BaseAction):

    action = 'CreateKeyPair'
    command = 'create-keypair'
    usage = '%(prog)s --keypair_name <keypair_name> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-N', '--keypair_name', dest='keypair_name',
                action='store', type=str, default=None,
                help='name of the keypair.')

        parser.add_argument('-m', '--mode', dest='mode',
                action='store', type=str, default='system',
                help='the keypair creation mode, `system` or `user`. Default is `system`')

        parser.add_argument('-e', '--encrypt_method', dest='encrypt_method',
                action='store', type=str, default='ssh-rsa',
                help='if creation mode is `system`, you can specify the encrypt method. Supported encrypt method: `ssh-rsa`, `ssh-dss`, default is `ssh-rsa`.')

        parser.add_argument('-p', '--public_key', dest='public_key',
                action='store', type=str, default='',
                help='if creation mode is `user`, you can specify your owned public key content here.')

        parser.add_argument('-u', '--target-user', dest='target_user',
                            action='store', type=str, default=None,
                            help='the ID of user who will own this resource.')

    @classmethod
    def build_directive(cls, options):
        required_params = {'keypair_name': options.keypair_name}
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('param [%s] should be specified' % param)
                return None

        return {
                'keypair_name': options.keypair_name,
                'mode': options.mode,
                'encrypt_method': options.encrypt_method,
                'public_key': options.public_key,
                'target_user': options.target_user,
                }
