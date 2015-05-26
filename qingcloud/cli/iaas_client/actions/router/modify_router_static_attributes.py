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

class ModifyRouterStaticAttributesAction(BaseAction):

    action = 'ModifyRouterStaticAttributes'
    command = 'modify-router-static-attributes'
    usage = '%(prog)s -s <router_static_id> -p <priority> [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-s', '--router-static', dest='router_static',
                action='store', type=str, default=None,
                help='the ID of router static you want to modify.')

        parser.add_argument('-N', '--static-name', dest='router_static_name',
                action='store', type=str, default=None,
                help='the name of router static.')

        parser.add_argument('--val1', dest='val1',
                action='store', type=str, default=None,
                help='the val1')

        parser.add_argument('--val2', dest='val2',
                action='store', type=str, default=None,
                help='the val2')

        parser.add_argument('--val3', dest='val3',
                action='store', type=str, default=None,
                help='the val3')

        parser.add_argument('--val4', dest='val4',
                action='store', type=str, default=None,
                help='the val4')

        parser.add_argument('--val5', dest='val5',
                action='store', type=str, default=None,
                help='the val5')

        parser.add_argument('--val6', dest='val6',
                action='store', type=str, default=None,
                help='the val6')

        parser.add_argument('-D', '--disable', dest='disabled',
                action='store_true', default=None,
                help='disable a router static.')

        parser.add_argument('-E', '--enable', dest='enabled',
                action='store_true', default=None,
                help='enable a router static')

    @classmethod
    def build_directive(cls, options):
        if not options.router_static:
            print('error: [router-static] should be specified.')
            return None

        directive = {
                'router_static': options.router_static,
                'router_static_name': options.router_static_name,
                'val1': options.val1,
                'val2': options.val2,
                'val3': options.val3,
                'val4': options.val4,
                'val5': options.val5,
                'val6': options.val6,
                }
        if options.enabled or options.disabled:
            directive.update({"disabled": 1 if options.disabled else 0})

        return directive
