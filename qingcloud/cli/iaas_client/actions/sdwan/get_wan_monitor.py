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


class GetWanMonitorAction(BaseAction):

    action = 'GetWanMonitor'
    command = 'get-wan-monitor'
    usage = '%(prog)s [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-r', '--resource', dest='resource',
                            action='store', type=str, default='',
                            help='the id of the resource whose monitoring data you want to get.')

        parser.add_argument('-t', '--access_type', dest='access_type',
                            action="store", type=str,  default='',
                            help='the wan access type. eg: line, vpc, cpe.')

        parser.add_argument('--interface_name', dest='interface_name',
                            action="store", type=str, default='',
                            help='interface name of cpe. eg: eth0, eth1.')

        parser.add_argument('--ha_member_index', dest='ha_member_index',
                            action="store", type=str, default='',
                            help='the ha member index . eg: 0/1')

        parser.add_argument('--monitor_type', dest='monitor_type',
                            action="store", type=str, default='',
                            help='monitor type. eg: internet, pop.')

        parser.add_argument('-m', '--meters', dest='meters',
                            action="store", type=str, default='',
                            help='the comma separated metering types you want to get. '
                                 'eg: traffic, flow, pps.')

        parser.add_argument('-s', '--step', dest='step',
                            action="store", type=str, default='',
                            help='the metering time step.'
                                 'eg: 1m, 5m, 15m, 30m, 1h, 2h, 1d')

        parser.add_argument('--start_time', dest='start_time',
                            action="store", type=str, default='',
                            help='the starting time stamp.')

        parser.add_argument('--end_time', dest='end_time',
                            action="store", type=str, default='',
                            help='the ending time stamp.')

    @classmethod
    def build_directive(cls, options):
        required_params = {
            'resource': options.resource,
            'access_type': options.access_type,
            'meters': explode_array(options.meters),
            'step': options.step,
            'start_time': options.start_time,
            'end_time': options.end_time,
        }

        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print "param [%s] should be specified" % param
                return None

        directive = {"resource": options.resource,
                     "access_type": options.access_type,
                     "meters": explode_array(options.meters),
                     "step": options.step,
                     "start_time": options.start_time,
                     "end_time": options.end_time,
                     }

        if options.interface_name:
            directive['interface_name'] = options.interface_name
        if options.monitor_type:
            directive['monitor_type'] = options.monitor_type
        if options.ha_member_index:
            directive['ha_member_index'] = options.ha_member_index

        return directive
