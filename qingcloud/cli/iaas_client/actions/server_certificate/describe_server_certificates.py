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


class DescribeServerCertificatesAction(BaseAction):

    action = 'DescribeServerCertificates'
    command = 'describe-server_certificates'
    usage = '%(prog)s [-s "server_certificate_id, ..."] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-s', '--server_certificates', dest='server_certificates',
                            action='store', type=str, default='',
                            help='the ids of server certificate you want to list.')

        parser.add_argument('-W', '--search_word', dest='search_word',
                            action='store', type=str, default='',
                            help='the combined search column')

        parser.add_argument('-V', '--verbose', dest='verbose',
                            action='store', type=int, default=0,
                            help='the number to specify the verbose level, larger the number, the more detailed information will be returned.')

    @classmethod
    def build_directive(cls, options):
        return {
            'server_certificates': explode_array(options.server_certificates),
            'search_word': options.search_word,
            'verbose': options.verbose,
            'offset': options.offset,
            'limit': options.limit,
        }
