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

class CreateSnapshotsAction(BaseAction):

    action = 'CreateSnapshots'
    command = 'create-snapshots'
    usage = '%(prog)s -r <resources> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-r', '--resources', dest='resources',
                action='store', type=str, default=None,
                help='the IDs of resources you want to create snapshot from')

        parser.add_argument('-F', '--is-full', dest='is_full',
                action='store', type=int, default=0,
                help='1 means create full snapshot, 0 means determined by the system.')

        parser.add_argument('-N', '--name', dest='snapshot_name',
                action='store', type=str, default='',
                help='short name of snapshot')

    @classmethod
    def build_directive(cls, options):
        required_params = {'resources': options.resources}
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('error: [%s] should be specified' % param)
                return None

        return {
                'resources': explode_array(options.resources),
                'is_full' : options.is_full,
                'snapshot_name' : options.snapshot_name
                }
