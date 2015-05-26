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

class ResizeVolumesAction(BaseAction):

    action = 'ResizeVolumes'
    command = 'resize-volumes'
    usage = '%(prog)s -v "volume_id,..." -s <size> [-f <conf_file>]'
    description = 'Extend one or more volumes'

    @classmethod
    def add_ext_arguments(cls, parser):
        
        parser.add_argument('-v', '--volumes', dest='volumes',
                action='store', type=str, default='',
                help='the comma separated IDs of volumes you want to resize.')
        
        parser.add_argument('-s', '--size', dest='size',
                action='store', type=int, default=0,
                help='new volume size you want to resize to.')

    @classmethod
    def build_directive(cls, options):
        if not options.volumes:
            print('error: [volumes] should be specified')
            return None

        if options.size <= 0:
            print('error: [size] should be larger than 0')
            return None

        return {
                'volumes': explode_array(options.volumes),
                'size': options.size
                }
