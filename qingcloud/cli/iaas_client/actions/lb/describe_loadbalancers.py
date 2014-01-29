# coding: utf-8

from qingcloud.cli.iaas_client.actions.base import BaseAction
from qingcloud.cli.misc.utils import explode_array

class DescribeLoadBalancersAction(BaseAction):

    action = 'DescribeLoadBalancers'
    command = 'describe-loadbalancers'
    usage = '%(prog)s [-l <loadbalancers> -f <conf_file>]'
    description = 'Describe load balancers.'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-l', '--loadbalancers', dest='loadbalancers',
                action='store', type=str, default='',
                help='the comma separated IDs of load balancers.')

        parser.add_argument('-s', '--status', dest='status',
                action='store', type=str, default='',
                help='load balancer status: pending, active, stopped, suspended, deleted, ceased')

        parser.add_argument('-W', '--search_word', dest='search_word',
                action='store', type=str, default='',
                help='the combined search column')

        parser.add_argument('-V', '--verbose', dest='verbose',
                action='store', type=int, default=0,
                help='the number to specify the verbose level, larger the number, the more detailed information will be returned.')

    @classmethod
    def build_directive(cls, options):
        return {
                'loadbalancers': explode_array(options.loadbalancers),
                'status': explode_array(options.status),
                'verbose': options.verbose,
                'search_word': options.search_word,
                'offset':options.offset,
                'limit': options.limit,
                }
