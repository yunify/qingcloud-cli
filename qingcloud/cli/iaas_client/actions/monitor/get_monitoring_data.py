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
from qingcloud.cli.misc.utils import explode_array, convert_to_utctime

class GetMonitorAction(BaseAction):

    action = 'GetMonitor'
    command = 'get-monitoring-data'
    usage = '%(prog)s -r <resource> -m <meters> -s <step> -b <start_time> -e <end_time> [-f <conf_file>]'
    description = 'Get resource monitoring data.'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-r', '--resource', dest='resource',
                action='store', type=str, default=None,
                help='the ID of resource, can be instance_id, volume_id, eip_id or router_id.')

        parser.add_argument('-m', '--meters', dest='meters',
                action='store', type=str, default=None,
                help='''list of metering types you want to get.
                If resource is instance, meter can be "cpu", "disk-os", "memory",
                "disk-"+attached_volume_id, "if-"+vxnet_mac_address.
                If resource is volume, meter should be "disk-"+volume_id.
                If resource is eip, meter should be "traffic".
                If resource is router, meter should be "vxnet-0".
                ''')

        parser.add_argument('-s', '--step', dest='step',
                action='store', type=str, default=None,
                help='the metering time step, valid steps: "5m", "15m", "30m", "1h", "2h", "1d".')

        parser.add_argument('-b', '--start_time', dest='start_time',
                action='store', type=str, default=None,
                help='the start time in the format YYYY-MM-DD hh:mm:ss.')

        parser.add_argument('-e', '--end_time', dest='end_time',
                action='store', type=str, default=None,
                help='the end time in the format YYYY-MM-DD hh:mm:ss.')

        parser.add_argument('--decompress', dest='decompress',
                action='store_true',
                help='decompress mointoring data from api.')

    @classmethod
    def build_directive(cls, options):
        start_time = convert_to_utctime(options.start_time)
        end_time = convert_to_utctime(options.end_time)
        required_params = {
                'resource': options.resource,
                'meters': options.meters,
                'step': options.step,
                'start_time': start_time,
                'end_time': end_time,
                }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('error: [%s] should be specified' % param)
                return None

        return {
                'resource': options.resource,
                'meters': explode_array(options.meters),
                'step': options.step,
                'start_time': start_time,
                'end_time': end_time,
                'decompress': options.decompress,
                }
