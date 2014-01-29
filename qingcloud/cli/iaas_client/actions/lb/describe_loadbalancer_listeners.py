# coding: utf-8

from qingcloud.cli.iaas_client.actions.base import BaseAction
from qingcloud.cli.misc.utils import explode_array

class DescribeLoadBalancerListenersAction(BaseAction):

    action = 'DescribeLoadBalancerListeners'
    command = 'describe-loadbalancer-listeners'
    usage = '%(prog)s [-s <lb_listeners> -l <loadbalancer> -f <conf_file>]'
    description = 'Describe load balancer listeners.'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-s', '--lb_listeners', dest='lb_listeners',
                action='store', type=str, default='',
                help='the comma separated IDs of load balancer listeners.')

        parser.add_argument('-l', '--loadbalancer', dest='loadbalancer',
                action='store', type=str, default='',
                help='the ID of load balancer.')

        parser.add_argument('-V', '--verbose', dest='verbose',
                action='store', type=int, default=0,
                help='the number to specify the verbose level, larger the number, the more detailed information will be returned.')

    @classmethod
    def build_directive(cls, options):
        return {
                'loadbalancer_listeners': explode_array(options.lb_listeners),
                'loadbalancer': options.loadbalancer,
                'verbose': options.verbose,
                'offset':options.offset,
                'limit': options.limit,
                }
