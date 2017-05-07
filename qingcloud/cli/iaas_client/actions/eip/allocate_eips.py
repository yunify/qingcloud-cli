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

class AllocateEipsAction(BaseAction):

    action = 'AllocateEips'
    command = 'allocate-eips'
    usage = '%(prog)s --bandwidth <bandwidth> --count <count> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-c', '--count', dest='count',
                action='store', type=int, default=1,
                help='the number of the eips you want to allocate. Default 1')

        parser.add_argument('-b', '--bandwidth', dest='bandwidth',
                action='store', type=int, default=None,
                help='the bandwidth of the eip. Unit is MB.')

        parser.add_argument('-B', '--billing-mode', dest='billing_mode',
                action='store', type=str, default="bandwidth",
                help='the billing mode of the eip: "bandwidth" or "traffic".')

        parser.add_argument('-i', '--need_icp', dest='need_icp',
                action='store', type=int, default=0,
                help='whether need ICP code.')

        parser.add_argument('-n', '--eip_name', dest='eip_name',
                action='store', type=str, default='',
                help='the short name of eip')

        parser.add_argument('--target-user', dest='target_user',
                action='store', type=str, default=None,
                help='ID of user who will own this resource, should be one of your sub-account.')

    @classmethod
    def build_directive(cls, options):
        required_params = {'bandwidth': options.bandwidth}
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('error: [%s] should be specified' % param)
                return None

        return {
                'count': options.count,
                'bandwidth': options.bandwidth,
                'billing_mode': options.billing_mode,
                'eip_name' : options.eip_name,
                'need_icp': options.need_icp,
                'target_user': options.target_user,
                }
