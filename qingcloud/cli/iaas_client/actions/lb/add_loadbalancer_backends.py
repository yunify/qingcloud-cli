# coding: utf-8

import json

from qingcloud.cli.iaas_client.actions.base import BaseAction

class AddLoadBalancerBackendsAction(BaseAction):

    action = 'AddLoadBalancerBackends'
    command = 'add-loadbalancer-backends'
    usage = '%(prog)s -s <lb_listener> -b <backends> [-f <conf_file>]'
    description = 'Add one or more backends to load balancer listener'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-s', '--lb_listener', dest='lb_listener',
                action='store', type=str, default='',
                help='ID of load balancer listener which you add backends to.')

        parser.add_argument('-b', '--backends', dest='backends',
                action='store', type=str, default='',
                help='JSON string of backend list. e.g. \
                      \'[{"loadbalancer_backend_name": "demo","resource_id":"i-1234abcd","port":"80","weight":"5"}]\'')

    @classmethod
    def build_directive(cls, options):
        required_params = {
                'loadbalancer_listener': options.lb_listener,
                'backends': options.backends,
                }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print 'error: [%s] should be specified' % param
                return None

        return {
                'loadbalancer_listener': options.lb_listener,
                'backends': json.loads(options.backends),
                }
