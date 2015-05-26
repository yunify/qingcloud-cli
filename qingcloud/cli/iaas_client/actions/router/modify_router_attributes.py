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

class ModifyRouterAttributesAction(BaseAction):

    action = 'ModifyRouterAttributes'
    command = 'modify-router-attributes'
    usage = '%(prog)s -r <router_id> [-s <security_group> -e <eip> -v <vxnet> -F <features> -S <dyn_start_ip> -E <dyn_end_ip>] [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-r', '--router', dest='router',
                action='store', type=str, default='',
                help='the id of the router whose attributes you want to modify.')

        parser.add_argument('-e', '--eip', dest='eip',
                action='store', type=str, default='',
                help='ID of eip that will apply to the router.')

        parser.add_argument('-s', '--security_group', dest='security_group',
                action='store', type=str, default='',
                help='the id of the security_group you want to apply to router.')

        parser.add_argument('-N', '--router_name', dest='router_name',
                action='store', type=str, default=None,
                help='new router_name.')

        parser.add_argument('-D', '--description', dest='description',
                action='store', type=str, default=None,
                help='new description.')

        parser.add_argument('-v', '--vxnet', dest='vxnet',
                action='store', type=str, default=None,
                help='the id of the vxnet whose feature you want to modify.')

        parser.add_argument('-F', '--features', dest='features',
                action='store', type=int, default=None,
                help='''
                the integer value of the bit mask that represent the selected features.
                Masking Bit:
                1 - dhcp server
                ''')

        parser.add_argument('-S', '--dyn_ip_start', dest='dyn_ip_start',
                action='store', type=str, default=None,
                help='starting ip allocated from DHCP server, e.g. "192.168.x.2".')

        parser.add_argument('-E', '--dyn_ip_end', dest='dyn_ip_end',
                action='store', type=str, default=None,
                help='ending ip allocated from DHCP server, e.g. "192.168.x.254".')

    @classmethod
    def build_directive(cls, options):
        if not options.router:
            print('error: [router] should be specified.')
            return None

        if options.features is not None and not options.vxnet:
            print('error: [vxnet] should be specified if modify features.')
            return None

        if (options.dyn_ip_start or options.dyn_ip_end) and options.features is None:
            print('error: [features] should be specified if modify ip range.')
            return None

        return {
                'router': options.router,
                'router_name': options.router_name,
                'description': options.description,
                'eip': options.eip,
                'security_group': options.security_group,
                'vxnet': options.vxnet,
                'features': options.features,
                'dyn_ip_start': options.dyn_ip_start,
                'dyn_ip_end': options.dyn_ip_end,
                }
