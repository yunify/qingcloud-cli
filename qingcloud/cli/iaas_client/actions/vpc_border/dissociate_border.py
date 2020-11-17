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


class DissociateBorderAction(BaseAction):

    action = 'DissociateBorder'
    command = 'dissociate_border'
    usage = '%(prog)s -b <border_id> -r <router_id> [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-b', '--border', dest='border',
                            action='store', type=str, default=None,
                            help='the intranet router you want to dissociate.')

        parser.add_argument('-r', '--router', dest='router',
                            action='store', type=str, default=None,
                            help='the id of the vpc router.')

    @classmethod
    def build_directive(cls, options):
        required_params = {"border": options.border,
                           "router": options.router}
        for param in required_params:
            if required_params[param] is None or required_params[param] == "":
                print('error: [%s] should be specified' % param)
                return None

        return {"border": options.border,
                "router": options.router}
