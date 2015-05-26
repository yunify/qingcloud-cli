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

class CreateVolumeFromSnapshotAction(BaseAction):

    action = 'CreateVolumeFromSnapshot'
    command = 'create-volume-from-snapshot'
    usage = '%(prog)s -s "snapshot_id" -n <name> [-f <conf_file>]'
    description = 'Create volume from snapshot.'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-s', '--snapshot', dest='snapshot',
                action='store', type=str, default='',
                help='the ID of snapshot you want to create volume from it.')

        parser.add_argument('-N', '--volume-name', dest='volume_name',
                action='store', type=str, default='',
                help='the name of new volume.')

    @classmethod
    def build_directive(cls, options):
        if not options.snapshot:
            print('error: [snapshots] should be specified')
            return None

        return {
                'snapshot': options.snapshot,
                'volume_name': options.volume_name
                }
