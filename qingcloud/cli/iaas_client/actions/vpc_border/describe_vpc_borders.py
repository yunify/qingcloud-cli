# =========================================================================
# Copyright 2012-present Yunify, Inc.
# -------------------------------------------------------------------------
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this work except in compliance with the License.
# You may obtain a copy of the License in the LICENSE file, or at:
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========================================================================

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction


class DescribeVpcBordersAction(BaseAction):

    action = 'DescribeVpcBorders'
    command = 'describe_vpc_borders'
    usage = '%(prog)s -b <vpc border ids> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-b", "--vpc_borders", dest="vpc_borders",
                            action="store", type=str, default=None,
                            help='the comma separated IDs of vpc_borders you want to describe border.')

        parser.add_argument("-s", "--status", dest="status",
                            action="store", type=str, default=None,
                            help='the comma separated status of vpc border. eg: pending, available, ceased, deleted.')

        parser.add_argument("-n", "--border_name", dest="border_name",
                            action="store", type=str, default=None,
                            help='''the short name of borders''')

        parser.add_argument("-t", "--border_type", dest="border_type",
                            action="store", type=int, default=None,
                            help="the type of border, "
                                  "0: vpc border, 1: intranet router")

        parser.add_argument("-r", "--router", dest="router_id",
                            action="store", type=str, default=None,
                            help="the id of the router whose vpc_border you want to describe.")

        parser.add_argument("-l", "--l3vni", dest="l3vni",
                            action="store", type=int, default=None,
                            help="the l3vni of the router whose vpc_border you want to describe.")

        parser.add_argument("-V", "--verbose", dest="verbose",
                            action="store", type=int, default=None,
                            help="the number to specify the verbose level, larger the number, "
                                 "the more detailed information will be returned.")

        parser.add_argument("-W", "--search_word", dest="search_word",
                            action="store", type=str, default=None,
                            help='the search word.')

        parser.add_argument("-o", "--owner", dest="owner",
                            action="store", type=str, default=None,
                            help='the owner id.')

    @classmethod
    def build_directive(cls, options):

        return {'vpc_borders': explode_array(options.vpc_borders),
                'status': explode_array(options.status),
                'router_id': options.router_id,
                'l3vni': options.l3vni,
                'border_type': options.border_type,
                'border_name': options.border_name,
                'owner': options.owner,
                'search_word': options.search_word,
                'offset': options.offset,
                'limit': options.limit,
                'verbose': options.verbose}
