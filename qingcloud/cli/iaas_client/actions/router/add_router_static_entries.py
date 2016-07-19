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

import json
from qingcloud.cli.iaas_client.actions.base import BaseAction

class AddRouterStaticEntriesAction(BaseAction):

    action = 'AddRouterStaticEntries'
    command = 'add-router-static-entries'
    usage = '%(prog)s -r <router_static_id> -e <entries> [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-s', '--static', dest='static',
                action='store', type=str, default='',
                help='the ID of router static you want to add entries to.')

        parser.add_argument('-e', '--entries', dest='entries',
                action='store', type=str, default='',
                help='''
                JSON string of static entry list. e.g.
                '[{"val1":"vpn username","val2":"vpn passwd"}]'
                ''')

    @classmethod
    def build_directive(cls, options):
        required_params = {
            'static': options.static,
            'entries': options.entries,
        }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('param [%s] should be specified' % param)
                return None

        return {
            'router_static': options.static,
            'entries': json.loads(options.entries),
        }
