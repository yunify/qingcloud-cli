# coding: utf-8

from qingcloud.cli.iaas_client.actions.base import BaseAction

class ModifyLoadBalancerBackendAttributesAction(BaseAction):

    action = 'ModifyLoadBalancerBackendAttributes'
    command = 'modify-loadbalancer-backend-attributes'
    usage = '%(prog)s -b <lb_backend> [-p <port> -w <weight> -f <conf_file>]'
    description = 'Modify load balancer backend attributes.'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-b', '--lb_backend', dest='lb_backend',
                action='store', type=str, default='',
                help='the ID of load balancer backend.')

        parser.add_argument('-p', '--port', dest='port',
                action='store', type=int, default=None,
                help='the backend port.')

        parser.add_argument('-w', '--weight', dest='weight',
                action='store', type=int, default=None,
                help='the backend weight, valid value is from 1 to 100.')

        parser.add_argument('-N', '--name', dest='name',
                action='store', type=str, default=None,
                help='new backend name')

    @classmethod
    def build_directive(cls, options):
        if not options.lb_backend:
            print 'error: backend should be specified'
            return None

        return {
                'loadbalancer_backend': options.lb_backend,
                'loadbalancer_backend_name': options.name,
                'port': options.port,
                'weight': options.weight,
                }
