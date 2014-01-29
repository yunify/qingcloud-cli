# coding: utf-8

from qingcloud.cli.iaas_client.actions.base import BaseAction
from qingcloud.cli.misc.utils import explode_array

class CreateLoadBalancerAction(BaseAction):

    action = 'CreateLoadBalancer'
    command = 'create-loadbalancer'
    usage = '%(prog)s -e <eips> [-n <name> -s <sg> -f <conf_file>]'
    description = 'Associate one or more eips with load balancer'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-e', '--eips', dest='eips',
                action='store', type=str, default='',
                help='the comma separated IDs of eips you want to associate.')

        parser.add_argument('-N', '--name', dest='name',
                action='store', type=str, default='',
                help='load balancer name.')

        parser.add_argument('-s', '--sg', dest='sg',
                action='store', type=str, default=None,
                help='the ID of security group which will be applied to load balancer.')

    @classmethod
    def build_directive(cls, options):
        required_params = {
                'eips': options.eips,
                }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print 'error: [%s] should be specified' % param
                return None

        return {
                'eips': explode_array(options.eips),
                'loadbalancer_name': options.name,
                'security_group': options.sg,
                }
