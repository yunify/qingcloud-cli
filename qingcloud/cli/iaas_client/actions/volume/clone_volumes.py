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


class CloneVolumesAction(BaseAction):

    action = 'CloneVolumes'
    command = 'clone-volumes'
    usage = '%(prog)s -z <zone_id> -v <volume_id> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-v', '--volume', dest='volume',
                            action='store', type=str, default=None,
                            help='the ID of volume you want to clone.')

        parser.add_argument('-t', '--volume-type', dest='volume_type',
                            action='store', type=int, default=None,
                            help='''the type of volumes.
                            @ref https://docs.qingcloud.com/product/api/action/volume/create_volumes.html
                            ''')

        parser.add_argument('-c', '--count', dest='count',
                            action='store', type=int, default=1,
                            help='the number of volumes to create.')

        parser.add_argument('-N', '--name', dest='volume_name',
                            action='store', type=str, default='',
                            help='short name of volume')

    @classmethod
    def build_directive(cls, options):
        required_params = {
            'zone': options.zone,
            'volume': options.volume,
            'volume_type': options.volume_type,
        }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('error: [%s] should be specified' % param)
                return None

        return {
            'zone': options.zone,
            'volume': options.volume,
            'volume_name': options.volume_name,
            'volume_type': options.volume_type,
            'count': options.count,
        }
