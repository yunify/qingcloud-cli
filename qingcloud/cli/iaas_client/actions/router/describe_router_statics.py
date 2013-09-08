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
                help='The comma separated IDs of router_statics you want to list. ')
        
        parser.add_argument('-r', '--router', dest='router',
                action='store', type=str, default='',
                help='Filter by router. ')
        
        parser.add_argument('-v', '--vxnet', dest='vxnet',
                action='store', type=str, default='',
                help='Filter by vxnet. ')
        
        parser.add_argument('-t', '--static_type', dest='static_type',
                action='store', type=str, default=None,
                help='The static type. 0: fixed ips; 1: port forwarding.')
            
        parser.add_argument('-V', '--verbose', dest='verbose',
                action='store', type=int, default=0,
                help='The number to specify the verbose level, larger the number, the more detailed information will be returned.')

    @classmethod
    def build_directive(cls, options):
        directive = {
                'router_statics': explode_array(options.router_statics),
                'router': options.router,
                'vxnet': options.vxnet,
                'verbose': options.verbose,
                'offset':options.offset,
                'limit': options.limit,
                }
        if options.static_type is not None:
            directive.update({'static_type': options.static_type})

        return directive
