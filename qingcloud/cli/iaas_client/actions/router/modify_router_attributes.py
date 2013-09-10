# coding: utf-8

from qingcloud.cli.iaas_client.actions.base import BaseAction

class ModifyRouterAttributesAction(BaseAction):

    action = 'ModifyRouterAttributes'
    command = 'modify-router-attributes'
    usage = '%(prog)s -r <router_id>] [-s <security_group> -e <eip>] [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-r', '--router', dest='router',
                action='store', type=str, default='',
                help='the id of the router whose attributes you want to modify.')
     
        parser.add_argument('-e', '--eip', dest='eip',
                action='store', type=str, default='',
                help='ID of eip that will apply to the router.')
     
        parser.add_argument('-s', '--security_group', dest='security_group',
                action='store', type=str, default='',
                help='the id of the security_group you want to apply to router.')

        parser.add_argument('-N', '--router_name', dest='router_name',
                action='store', type=str, default='',
                help='new router_name.')

        parser.add_argument('-D', '--description', dest='description',
                action='store', type=str, default='',
                help='new description.')
              
    @classmethod
    def build_directive(cls, options):
        router = options.router
        if not router:
            print '[router] should be specified.'
            return None

        return {
                'router': router,
                'router_name': options.router_name,
                'description': options.description,
                'eip': options.eip,
                'security_group': options.security_group,
                }
