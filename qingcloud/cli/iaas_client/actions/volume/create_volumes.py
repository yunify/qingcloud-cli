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

from qingcloud.cli.iaas_client.actions.base import BaseAction

class CreateVolumesAction(BaseAction):

    action = 'CreateVolumes'
    command = 'create-volumes'
    usage = '%(prog)s --size <volume_size> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-s', '--size', dest='size',
                action='store', type=int, default=None,
                help='the size of each volume. Unit is GB.')

        parser.add_argument('-t', '--type', dest='volume_type',
                action='store', type=int, default=0,
                help='''the type of volumes:
                "0" means high performance volume.
                "1" means high capacity volume in pek1, gd1, ap1.
                "2" means high capacity volume in pek2.
                ''')

        parser.add_argument('-c', '--count', dest='count',
                action='store', type=int, default=1,
                help='the number of volumes to create.')

        parser.add_argument('-N', '--volume_name', dest='volume_name',
                action='store', type=str, default='',
                help='short name of volume')

    @classmethod
    def build_directive(cls, options):
        required_params = {'size': options.size}
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('error: [%s] should be specified' % param)
                return None

        return {
                'size': options.size,
                'count' : options.count,
                'volume_name' : options.volume_name,
                'volume_type' : options.volume_type,
                }
