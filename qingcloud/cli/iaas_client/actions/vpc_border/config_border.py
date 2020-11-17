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


class ConfigBorderAction(BaseAction):

    action = 'ConfigBorder'
    command = 'config_border'
    usage = '%(prog)s -b <vpc border> -o operation [-d data] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-b', '--border', dest='border',
                            action='store', type=str, default=None,
                            help='the ID of intranet router.')

        parser.add_argument('-o', '--operation', dest='operation',
                            action='store', type=str, default=None,
                            help='operation : ConfigRoute')

        parser.add_argument('-d', '--data', dest='data',
                            action='store', type=str, default=None,
                            help='configuration data in json format.')

    @classmethod
    def build_directive(cls, options):
        required_params = {"border": options.border,
                           "operation": options.operation}
        for param in required_params:
            if required_params[param] is None or required_params[param] == "":
                print('error: [%s] should be specified' % param)
                return None

        res = {"border": options.border,
               "operation": options.operation}

        if options.data:
            res["data"] = json.loads(options.data)
        return res
