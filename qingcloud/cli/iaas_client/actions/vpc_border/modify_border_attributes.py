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

from qingcloud.cli.iaas_client.actions.base import BaseAction


class ModifyBorderAttributesAction(BaseAction):

    action = 'ModifyBorderAttributes'
    command = 'modify_border_attributes'
    usage = '%(prog)s -b <border> [-n <border_name>] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-n', '--border_name', dest='border_name', 
                            action='store', type=str, default=None,
                            help='the short name of borders.')

        parser.add_argument('-d', '--description', dest='description',
                            action='store', type=str, default=None,
                            help='the description of borders.')

        parser.add_argument('-b', '--border', dest='border',
                            action='store', type=str, default=None,
                            help='border id')

    @classmethod
    def build_directive(cls, options):
        required_params = {"border": options.border}
        for param in required_params:
            if required_params[param] is None or required_params[param] == "":
                print('error: [%s] should be specified' % param)
                return None

        return {"border": options.border,
                "border_name": options.border_name,
                "description": options.description}
