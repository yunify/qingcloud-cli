# coding: utf-8

from qingcloud.cli.iaas_client.actions.base import BaseAction
from qingcloud.cli.misc.utils import explode_array

class DeleteLoadBalancerBackendsAction(BaseAction):

    action = 'DeleteLoadBalancerBackends'
    command = 'delete-loadbalancer-backends'
    usage = '%(prog)s -b <lb_backends> [-f <conf_file>]'
    description = 'Delete one or more load balancer backends'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-b', '--lb_backends', dest='lb_backends',
                action='store', type=str, default='',
                help='the comma separated IDs of backends you want to delete.')

    @classmethod
    def build_directive(cls, options):
        required_params = {
                'lb_backends': options.lb_backends,
                }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print 'error: [%s] should be specified' % param
                return None

        return {
                'loadbalancer_backends': explode_array(options.lb_backends),
                }
