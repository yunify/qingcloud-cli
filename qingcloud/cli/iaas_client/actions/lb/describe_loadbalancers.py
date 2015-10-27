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

class DescribeLoadBalancersAction(BaseAction):

    action = 'DescribeLoadBalancers'
    command = 'describe-loadbalancers'
    usage = '%(prog)s [-l <loadbalancers> -f <conf_file>]'
    description = 'Describe load balancers.'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-l', '--loadbalancers', dest='loadbalancers',
                action='store', type=str, default='',
                help='the comma separated IDs of load balancers.')

        parser.add_argument('-s', '--status', dest='status',
                action='store', type=str, default='',
                help='load balancer status: pending, active, stopped, suspended, deleted, ceased')

        parser.add_argument('-W', '--search_word', dest='search_word',
                action='store', type=str, default='',
                help='the combined search column')

        parser.add_argument('-V', '--verbose', dest='verbose',
                action='store', type=int, default=0,
                help='the number to specify the verbose level, larger the number, the more detailed information will be returned.')

    @classmethod
    def build_directive(cls, options):
        return {
                'loadbalancers': explode_array(options.loadbalancers),
                'status': explode_array(options.status),
                'verbose': options.verbose,
                'search_word': options.search_word,
                'offset':options.offset,
                'limit': options.limit,
                'tags': explode_array(options.tags),
                }
