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

class ReleaseEipsAction(BaseAction):

    action = 'ReleaseEips'
    command = 'release-eip'
    usage = '%(prog)s -e "eip_id, ..." [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-e', '--eips', dest='eips',
                action='store', type=str, default='',
                help='the comma separated IDs of eips you want to release.')

        parser.add_argument('-F', '--force', dest='force',
                action='store', type=int, default=0,
                help='0 for normal release and 1 for forcibly release.')

    @classmethod
    def build_directive(cls, options):
        eips = explode_array(options.eips)
        if not eips:
            print('error: [eips] should be specified')
            return None

        return {
                'eips': eips,
                'force': options.force,
                }
