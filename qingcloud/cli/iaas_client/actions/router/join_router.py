# coding: utf-8

from qingcloud.cli.iaas_client.actions.base import BaseAction

class JoinRouterAction(BaseAction):

    action = 'JoinRouter'
    command = 'join-router'
    usage = '%(prog)s -r <router_id>] -v <vxnet_id> -n <ip_network> [-f <features>] [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-r', '--router', dest='router',
                action='store', type=str, default='',
                help='ID of the router which vxnet will join.')

        parser.add_argument('-v', '--vxnet', dest='vxnet',
                action='store', type=str, default='',
                help='The id of the vxnet that will join the router.')

        parser.add_argument('-F', '--features', dest='features',
                action='store', type=int, default=1,
                help='''
                The integer value of the bit mask that represent the selected features.
                Masking Bit:
                1 - dhcp server
                ''')

        parser.add_argument('-n', '--ip_network', dest='ip_network',
                action='store', type=str, default='',
                help='The ip_network, e.g. `192.168.x.0/24` ')

    @classmethod
    def build_directive(cls, options):
        router = options.router
        vxnet = options.vxnet
        ip_addr = options.ip_network
        if not router or not vxnet or not ip_addr:
            print 'error: router, vxnet and ip_network should be specified.'
            return None

        return {
                'router': router,
                'vxnet': vxnet,
                'features': options.features,
                'ip_network': options.ip_network,
                }
