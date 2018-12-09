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


class ModifyServerCertificateAttributesAction(BaseAction):

    action = 'ModifyServerCertificateAttributes'
    command = 'modify-server_certificate-attributes'
    usage = '%(prog)s -t <server_certificate> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-s', '--server-certificate', dest='server_certificate',
                            action='store', type=str, default='',
                            help='the id of the server_certificate whose attributes you want to modify.')

        parser.add_argument('-N', '--certificate-name', dest='server_certificate_name',
                            action='store', type=str, default=None,
                            help='specify the new server_certificate name.')

        parser.add_argument('-D', '--description', dest='description',
                            action='store', type=str, default=None,
                            help='the detailed description of the resource')

    @classmethod
    def build_directive(cls, options):
        if not options.server_certificate:
            return None

        return {
            'server_certificate': options.server_certificate,
            'server_certificate_name': options.server_certificate_name,
            'description': options.description,
        }
