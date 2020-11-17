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


class CreateVpcBordersAction(BaseAction):

    action = 'CreateVpcBorders'
    command = 'create_vpc_borders'
    usage = '%(prog)s -t <border_type> [-n <border_name>] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-r', '--routers', dest='routers',
                            action='store', type=str, default='',
                            help='the comma separated IDs of routers you want to create vpc border.')

        parser.add_argument('-t', '--border_type', dest='border_type',
                            action='store', type=int, default=0,
                            help='the type of border, 1: intranet router, recommend ; 0: vpc border.')

        parser.add_argument('-n', '--border_name', dest='border_name', 
                            action='store', type=str, default='',
                            help='the short name of borders.')

        parser.add_argument('-d', '--description', dest='description',
                            action='store', type=str, default='', 
                            help='the description of borders.')

    @classmethod
    def build_directive(cls, options):
        routers = explode_array(options.routers)
        border_type = options.border_type

        if border_type == 0:
            if len(routers) == 0:
                print('error: routers should be specified when create vpc borders')
                return None
        elif border_type == 1:
            routers = None
        else:
            print('error: border type [%s] is not support' % border_type)
            return None

        return {'border_type': border_type,
                'border_name': options.border_name,
                'description': options.description,
                'routers': routers}
