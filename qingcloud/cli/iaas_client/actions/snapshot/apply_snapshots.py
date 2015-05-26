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

class ApplySnapshotsAction(BaseAction):

    action = 'ApplySnapshots'
    command = 'apply-snapshots'
    usage = '%(prog)s -s "snapshot_id,..." [-f <conf_file>]'
    description = 'Apply one or more snapshots'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-s', '--snapshots', dest='snapshots',
                action='store', type=str, default='',
                help='the comma separated IDs of snapshots you want to apply.')

    @classmethod
    def build_directive(cls, options):
        required_params = {
                'snapshots': options.snapshots,
                }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('error: [%s] should be specified' % param)
                return None

        return {
                'snapshots': explode_array(options.snapshots),
                }
