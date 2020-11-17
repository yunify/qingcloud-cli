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

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction


class DeleteVpcBordersAction(BaseAction):

    action = 'DeleteVpcBorders'
    command = 'delete_vpc_borders'
    usage = '%(prog)s -b <vpc border ids> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-b", "--vpc_borders", dest="vpc_borders",
                            action="store", type=str, default=None,
                            help='the comma separated IDs of vpc_borders you want to delete border.')

    @classmethod
    def build_directive(cls, options):
        required_params = {"vpc_borders": explode_array(options.vpc_borders)}
        for param in required_params:
            if required_params[param] is None or required_params[param] == "" \
                    or required_params[param] == []:
                print('error: [%s] should be specified' % param)
                return None

        return {"vpc_borders": explode_array(options.vpc_borders)}
