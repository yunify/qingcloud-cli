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

class DescribeRouterStaticEntriesAction(BaseAction):

    action = 'DescribeRouterStaticEntries'
    command = 'describe-router-static-entries'
    usage = '%(prog)s [-s "router_static_entry_id, ..."] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-e', '--router_static_entries', dest='router_static_entries',
                action='store', type=str, default='',
                help='the comma separated IDs of router_static_entries you want to list. ')

        parser.add_argument('-s', '--router_static', dest='router_static',
                action='store', type=str, default='',
                help='filter by router static. ')

    @classmethod
    def build_directive(cls, options):
        directive = {
            'router_static_entries': explode_array(options.router_static_entries),
            'router_static': options.router_static,
            'offset':options.offset,
            'limit': options.limit,
        }
        return directive
