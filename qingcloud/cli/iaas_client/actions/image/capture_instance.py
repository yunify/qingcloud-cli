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

class CaptureInstanceAction(BaseAction):

    action = 'CaptureInstance'
    command = 'capture-instance'
    usage = '%(prog)s --instance <instance_id> --image_name <image_name> [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-i', '--instance', dest='instance',
                action='store', type=str, default=None,
                help='ID of the instance you want to capture.')

        parser.add_argument('-N', '--image_name', dest='image_name',
                action='store', type=str, default='',
                help='short name of the image.')

    @classmethod
    def build_directive(cls, options):
        if not options.instance:
            return None

        return {
                'instance': options.instance,
                'image_name': options.image_name
                }
