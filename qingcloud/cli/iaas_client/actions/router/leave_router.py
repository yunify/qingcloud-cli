# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class LeaveRouterAction(BaseAction):

    action = 'LeaveRouter'
    command = 'leave-router'
    usage = '%(prog)s -r <router_id>] -v "vxnet_id, ..." [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-r', '--router', dest='router',
                action='store', type=str, default='',
                help='the id of the router the vxnet will leave.')
     
        parser.add_argument('-v', '--vxnets', dest='vxnets',
                action='store', type=str, default='',
                help='the comm separated IDs of the vxnets that will leave the router.')

    @classmethod
    def build_directive(cls, options):
        router = options.router
        vxnets = explode_array(options.vxnets)
        if not router or not vxnets:
            print 'error: [router] and [vxnets] should be specified.'
            return None

        return {
                'router': router,
                'vxnets': vxnets,
                }
