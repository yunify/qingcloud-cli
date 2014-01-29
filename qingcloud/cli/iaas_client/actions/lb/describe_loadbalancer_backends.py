# coding: utf-8

from qingcloud.cli.iaas_client.actions.base import BaseAction
from qingcloud.cli.misc.utils import explode_array

class DescribeLoadBalancerBackendsAction(BaseAction):

    action = 'DescribeLoadBalancerBackends'
    command = 'describe-loadbalancer-backends'
    usage = '%(prog)s [-b <lb_backends> -s <lb_listener> -l <loadbalancer> -f <conf_file>]'
    description = 'Describe load balancer backends.'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-b', '--lb_backends', dest='lb_backends',
                action='store', type=str, default='',
                help='the comma separated IDs of load balancer backends.')

        parser.add_argument('-s', '--lb_listener', dest='lb_listener',
                action='store', type=str, default='',
                help='the ID of load balancer listener.')

        parser.add_argument('-l', '--loadbalancer', dest='loadbalancer',
                action='store', type=str, default='',
                help='the ID of load balancer.')

        parser.add_argument('-V', '--verbose', dest='verbose',
                action='store', type=int, default=0,
                help='the number to specify the verbose level, larger the number, the more detailed information will be returned.')

    @classmethod
    def build_directive(cls, options):
        return {
                'loadbalancer_backends': explode_array(options.lb_backends),
                'loadbalancer_listener': options.lb_listener,
                'loadbalancer': options.loadbalancer,
                'verbose': options.verbose,
                'offset':options.offset,
                'limit': options.limit,
                }
