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

class DeleteRouterStaticEntriesAction(BaseAction):

    action = 'DeleteRouterStaticEntries'
    command = 'delete-router-static-entries'
    usage = '%(prog)s -e "router_static_entry_id, ..." [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-e', '--router_static_entries', dest='router_static_entries',
                action='store', type=str, default='',
                help='the comma separated IDs of router static entries you want to delete. ')

    @classmethod
    def build_directive(cls, options):
        router_static_entries = explode_array(options.router_static_entries)
        if not router_static_entries:
            return None

        return {
            'router_static_entries': router_static_entries,
        }
