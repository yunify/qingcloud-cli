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


class GetWanInfoAction(BaseAction):

    action = 'GetWanInfo'
    command = 'get-wan-info'
    usage = '%(prog)s -r "wan_access_id, ..." -t <info_type> [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-r', '--resources', dest='resources',
                            action='store', type=str, default=None,
                            help='the comma separated IDs of wan resource.')

        parser.add_argument('-t', '--info_type', dest='info_type',
                            action="store", type=str,  default=None,
                            help='the info type. eg: cpe_mobile_info.')

    @classmethod
    def build_directive(cls, options):
        if options.resources is None:
            print('error: resources should be specified.')
            return None

        if options.info_type is None:
            print('error: info_type should be specified.')
            return None

        return {
            "resources": explode_array(options.resources),
            "info_type": options.info_type,
        }
