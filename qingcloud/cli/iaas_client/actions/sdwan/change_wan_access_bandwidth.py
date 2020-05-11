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


class ChangeWanAccessBandwidthAction(BaseAction):

    action = 'ChangeWanAccessBandwidth'
    command = 'change-wan-access-bandwidth'
    usage = '%(prog)s -a <wan_access_id> -b <bandwidth> [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-a', '--wan_access', dest='wan_access',
                            action='store', type=str, default=None,
                            help='the ID of wan_access you want to change bandwidth.')

        parser.add_argument('-t', '--bandwidth_type', dest='bandwidth_type',
                            action="store", type=str,  default='elastic',
                            help='bandwidth type, such as elastic.')

        parser.add_argument('-b', '--bandwidth', dest='bandwidth',
                            action="store", type=int, default=None,
                            help='the new bandwidth for wan_access, unit in Mbps.')

    @classmethod
    def build_directive(cls, options):
        if options.wan_access is None:
            print('error: wan_access should be specified.')
            return None

        directive = {
            "wan_access": options.wan_access,
            "bandwidth_type": options.bandwidth_type,
            "bandwidth": options.bandwidth}

        return directive
