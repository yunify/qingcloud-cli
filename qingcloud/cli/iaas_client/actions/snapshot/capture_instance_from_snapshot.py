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

class CaptureInstanceFromSnapshotAction(BaseAction):

    action = 'CaptureInstanceFromSnapshot'
    command = 'capture-instance-from-snapshot'
    usage = '%(prog)s -s <snapshot> -n <image-name> [-f <conf_file>]'
    description = 'capture instance image from snapshot.'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-s', '--snapshot', dest='snapshot',
                action='store', type=str, default='',
                help='the ID of snapshot you want to capture as image.')

        parser.add_argument('-N', '--image-name', dest='image_name',
                action='store', type=str, default='',
                help='the name of image.')

    @classmethod
    def build_directive(cls, options):
        required_params = {
                'snapshot': options.snapshot,
                }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('error: [%s] should be specified' % param)
                return None

        return {
                'snapshot': options.snapshot,
                'image_name': options.image_name,
                }
