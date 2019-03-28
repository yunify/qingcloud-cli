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

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction


class JoinInstanceGroupAction(BaseAction):

    action = 'JoinInstanceGroup'
    command = 'join-instance-group'
    usage = '%(prog)s -i "instance_id,..." -g <group_id> [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-i', '--instances', dest='instances',
                            action='store', type=str, default=None,
                            help='the comma separated IDs of instances you want to join into group.')

        parser.add_argument('-g', '--instance_group', dest='instance_group',
                            action='store', type=str,
                            help='the group id of destination group.')

        return parser

    @classmethod
    def build_directive(cls, options):

        instances = explode_array(options.instances)
        instance_group = options.instance_group

        required_params = {
            'instances': instances,
            'instance_group': instance_group
        }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('error: [%s] should be specified' % param)
                return None

        return {
            'instances': instances,
            'instance_group': instance_group
        }
