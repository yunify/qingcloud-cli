# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class DescribeRouterStaticsAction(BaseAction):

    action = 'DescribeRouterStatics'
    command = 'describe-router-statics'
    usage = '%(prog)s [-s "router_static_id, ..."] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-s', '--router_statics', dest='router_statics',
                action='store', type=str, default='',
                help='the comma separated IDs of router_statics you want to list. ')

        parser.add_argument('-r', '--router', dest='router',
                action='store', type=str, default='',
                help='filter by router. ')

        parser.add_argument('-v', '--vxnet', dest='vxnet',
                action='store', type=str, default='',
                help='filter by vxnet. ')

        parser.add_argument('-t', '--static_type', dest='static_type',
                action='store', type=str, default=None,
                help='the static type. 1: port forwarding; 2: VPN; 3: DHCP options; 4: tunnels')

    @classmethod
    def build_directive(cls, options):
        directive = {
                'router_statics': explode_array(options.router_statics),
                'router': options.router,
                'vxnet': options.vxnet,
                'offset':options.offset,
                'limit': options.limit,
                }
        if options.static_type is not None:
            directive.update({'static_type': options.static_type})

        return directive
