# coding: utf-8

from qingcloud.cli.iaas_client.actions.base import BaseAction

class ModifyLoadBalancerAttributesAction(BaseAction):

    action = 'ModifyLoadBalancerAttributes'
    command = 'modify-loadbalancer-attributes'
    usage = '%(prog)s -l <loadbalancer> [-g <security_group> -N <name> -f <conf_file>]'
    description = 'Modify load balancer attributes.'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-l', '--loadbalancer', dest='loadbalancer',
                action='store', type=str, default='',
                help='the comma separated IDs of load balancers.')

        parser.add_argument('-g', '--security_group', dest='security_group',
                action='store', type=str, default=None,
                help='the id of the security group you want to apply to load balancer.')

        parser.add_argument('-N', '--lb_name', dest='lb_name',
                action='store', type=str, default=None,
                help='new load balancer name')

        parser.add_argument('-D', '--description', dest='description',
                action='store', type=str, default=None,
                help='new load balancer description')

    @classmethod
    def build_directive(cls, options):
        if not options.loadbalancer:
            print 'error: load balancer should be specified'
            return None

        return {
                'loadbalancer': options.loadbalancer,
                'security_group': options.security_group,
                'loadbalancer_name': options.lb_name,
                'description': options.description,
                }
