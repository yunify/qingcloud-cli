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

class DescribeVxnetsAction(BaseAction):

    action = 'DescribeVxnets'
    command = 'describe-vxnets'
    usage = '%(prog)s [-v "vxnet_id, ..."] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-v', '--vxnets', dest='vxnets',
                action='store', type=str, default='',
                help='the comma separated IDs of vxnets you want to list.')

        parser.add_argument('-t', '--vxnet_type', dest='vxnet_type',
                action='store', type=int, default=None,
                help='filter by vxnet type: 0 - unmanaged vxnet, 1 - managed vxnet')

        parser.add_argument('-V', '--verbose', dest='verbose',
                action='store', type=int, default=0,
                help='the number to specify the verbose level, larger the number, the more detailed information will be returned.')

        parser.add_argument('-W', '--search_word', dest='search_word',
                action='store', type=str, default='',
                help='the combined search column')

    @classmethod
    def build_directive(cls, options):
        return {
                'vxnets': explode_array(options.vxnets),
                'vxnet_type': options.vxnet_type,
                'search_word': options.search_word,
                'verbose': options.verbose,
                'offset': options.offset,
                'limit': options.limit,
                'tags': explode_array(options.tags),
                }
