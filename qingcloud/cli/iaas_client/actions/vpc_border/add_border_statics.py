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

import json
from qingcloud.cli.iaas_client.actions.base import BaseAction


class AddBorderStaticsAction(BaseAction):

    action = 'AddBorderStatics'
    command = 'add_border_statics'
    usage = '%(prog)s -b <border_id> -s <statics> [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-b', '--border', dest='border',
                            action='store', type=str, default=None,
                            help='the ID of intranet router whose statics you want to add.'
                            )

        parser.add_argument('-s', '--statics', dest='statics',
                            action='store', type=str, default=None,
                            help='''a json string of rules list. e.g. 
                            '[{"static_type":0, "val1":"1.2.3.4/32","val2":"rtr-88qnzvvy"}]' '''
                            )

    @classmethod
    def build_directive(cls, options):
        required_params = {"border": options.border}
        for param in required_params:
            if required_params[param] is None or required_params[param] == "":
                print('error: [%s] should be specified' % param)
                return None

        return {"border": options.border,
                "statics": json.loads(options.statics)}
