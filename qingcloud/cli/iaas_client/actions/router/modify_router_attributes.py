# coding: utf-8

from qingcloud.cli.iaas_client.actions.base import BaseAction

class ModifyRouterAttributesAction(BaseAction):

    action = 'ModifyRouterAttributes'
    command = 'modify-router-attributes'
    usage = '%(prog)s -r <router_id>] [-f <features> -v <vxnet_id> -e <eip>] [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-r', '--router', dest='router',
                action='store', type=str, default='',
                help='The id of the router whose attributes you want to modify.')
     
        parser.add_argument('-v', '--vxnet', dest='vxnet',
                action='store', type=str, default='',
                help='The id of the vxnet whose feature you want to modify.')
                
        parser.add_argument('-F', '--features', dest='features',
                action='store', type=int, default=None,
                help='''The integer value of the bit mask that represent the selected features. 
                        Masking Bit:
                        1 - dhcp server
                        ''')

        parser.add_argument('-e', '--eip', dest='eip',
                action='store', type=str, default='',
                help='ID of eip that will apply to the vxnet.')
     
        parser.add_argument('-s', '--security_group', dest='security_group',
                action='store', type=str, default='',
                help='The id of the security_group you want to apply to router.')

        parser.add_argument('-N', '--router_name', dest='router_name',
                action='store', type=str, default='',
                help='New router_name.')

        parser.add_argument('-D', '--description', dest='description',
                action='store', type=str, default='',
                help='New description.')
              
    @classmethod
    def build_directive(cls, options):
        router = options.router
        if not router:
            print '[router] should be specified.'
            return None

        return {
                'router': router,
                'vxnet': options.vxnet,
                'features': options.features,
                'router_name': options.router_name,
                'description': options.description,
                'eip': options.eip,
                'security_group': options.security_group,
                }
