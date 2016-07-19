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

class ModifyRouterStaticEntryAttributesAction(BaseAction):

    action = 'ModifyRouterStaticEntryAttributes'
    command = 'modify-router-static-entry-attributes'
    usage = '%(prog)s -s <router_static_entry_id> [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-e', '--router-static-entry', dest='router_static_entry',
                action='store', type=str, default=None,
                help='the ID of router static entry you want to modify.')

        parser.add_argument('-N', '--name', dest='router_static_entry_name',
                action='store', type=str, default=None,
                help='the name of router static entry.')

        parser.add_argument('--val1', dest='val1',
                action='store', type=str, default=None,
                help='the val1')

        parser.add_argument('--val2', dest='val2',
                action='store', type=str, default=None,
                help='the val2')

    @classmethod
    def build_directive(cls, options):
        if not options.router_static_entry:
            print('error: [router-static-entry] should be specified.')
            return None

        directive = {
            'router_static_entry': options.router_static_entry,
            'router_static_entry_name': options.router_static_entry_name,
            'val1': options.val1,
            'val2': options.val2,
        }
        return directive
