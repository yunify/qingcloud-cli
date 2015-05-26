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

class AddRouterStaticsAction(BaseAction):

    action = 'AddRouterStatics'
    command = 'add-router-statics'
    usage = '%(prog)s -r <router_id> -s <statics> [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-r', '--router', dest='router',
                action='store', type=str, default='',
                help='the ID of router you want to add statics to.')

        parser.add_argument('-s', '--statics', dest='statics',
                action='store', type=str, default='',
                help='''
                JSON string of static list. e.g.
                '[{"static_type":"3","val1":"i-b7zjztrf","val2":"domain-name-servers=8.8.8.8"},{"val4":"tcp","val1":"12","val2":"192.168.1.2","val3":"12","static_type":"1"}]'
                ''')

    @classmethod
    def build_directive(cls, options):
        required_params = {
                'router': options.router,
                'statics': options.statics,
                }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('param [%s] should be specified' % param)
                return None

        return {
                'router': options.router,
                'statics': json.loads(options.statics),
                }
