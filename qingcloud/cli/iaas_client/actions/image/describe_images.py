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

class DescribeImagesAction(BaseAction):

    action = 'DescribeImages'
    command = 'describe-images'
    usage = '%(prog)s [-i "image_id, ..."] [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-i', '--images', dest='images',
                action='store', type=str, default=None,
                help='the comma separated IDs of images you want to describe. ')

        parser.add_argument('-s', '--status', dest='status',
                action='store', type=str, default=None,
                help='status: pending, available, deleted, ceased')

        parser.add_argument('-p', '--processor_type', dest='processor_type',
                action='store', type=str, default=None,
                help='filter by processor type, supported processor types are `64bit` and `32bit`')

        parser.add_argument('-F', '--os_family', dest='os_family',
                action='store', type=str, default=None,
                help='filter by OS family, supported values are windows/debian/centos/ubuntu.')

        parser.add_argument('-v', '--visibility', dest='visibility',
                action='store', type=str, default=None,
                help='filter by visibility, supported values are `public`, `private`')

        parser.add_argument('-W', '--search_word', dest='search_word',
                action='store', type=str, default=None,
                help='the combined search column')

        parser.add_argument('-P', '--provider', dest='provider',
                action='store', type=str, default=None,
                help='filter by the image provider, supported values are `self`, `system`')

        parser.add_argument("-V", "--verbose", dest="verbose",
                action="store", type=int, default=0,
                help='the number to specify the verbose level, larger the number, the more detailed information will be returned.')

    @classmethod
    def build_directive(cls, options):
        return {
                'images': explode_array(options.images),
                'processor_type': explode_array(options.processor_type),
                'os_family':explode_array(options.os_family),
                'visibility': explode_array(options.visibility),
                'status': explode_array(options.status),
                'provider': options.provider,
                'verbose': options.verbose,
                'search_word': options.search_word,
                'offset':options.offset,
                'limit': options.limit,
                }
