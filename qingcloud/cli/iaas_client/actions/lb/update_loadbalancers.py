# coding: utf-8

from qingcloud.cli.iaas_client.actions.base import BaseAction
from qingcloud.cli.misc.utils import explode_array

class UpdateLoadBalancersAction(BaseAction):

    action = 'UpdateLoadBalancers'
    command = 'update-loadbalancers'
    usage = '%(prog)s -l <loadbalancers> [-f <conf_file>]'
    description = 'Update one or more load balancers'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-l', '--loadbalancers', dest='loadbalancers',
                action='store', type=str, default='',
                help='the comma separated IDs of load balancers you want to update.')

    @classmethod
    def build_directive(cls, options):
        required_params = {
                'loadbalancers': options.loadbalancers,
                }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('error: [%s] should be specified' % param)
                return None

        return {
                'loadbalancers': explode_array(options.loadbalancers),
                }
