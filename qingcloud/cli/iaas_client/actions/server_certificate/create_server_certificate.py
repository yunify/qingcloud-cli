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
import os

from qingcloud.cli.iaas_client.actions.base import BaseAction


class CreateServerCertificateAction(BaseAction):

    action = 'CreateServerCertificate'
    command = 'create-server_certificate'
    usage = '%(prog)s -N <name> -C <content> -K <private-key> [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-N', '--certificate-name', dest='server_certificate_name',
                            action='store', type=str, default=None,
                            help='the name of the server certificate.')

        parser.add_argument('-C', '--certificate-content', dest='certificate_content',
                            action='store', type=str, default=None,
                            help='the file name of certificate content.')

        parser.add_argument('-K', '--private-key', dest='private_key',
                            action='store', type=str, default=None,
                            help='the file name of matched private key.')

    @classmethod
    def build_directive(cls, options):
        required_params = {
            'server_certificate_name': options.server_certificate_name,
            'certificate_content': options.certificate_content,
            'private_key': options.private_key,
        }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('param [%s] should be specified' % param)
                return None

        if not os.path.isfile(options.certificate_content):
                print('File of certifiate content not found')
                return None

        if not os.path.isfile(options.private_key):
                print('File of private key not found')
                return None

        return {
            'server_certificate_name': options.server_certificate_name,
            'certificate_content': file(options.certificate_content).read(),
            'private_key': file(options.private_key).read(),
        }
