# coding: utf-8

from qingcloud.cli.misc.json_tool import json_load
from qingcloud.cli.iaas_client.actions.base import BaseAction

class AddRouterStaticsAction(BaseAction):

    action = 'AddRouterStatics'
    command = 'add-router-statics'
    usage = '%(prog) -r <router_id> -v <vxnet_id> -s <statics> [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-r', '--router', dest='router',
                action='store', type=str, default='',
                help='The ID of router whose statics you want to add. ')

        parser.add_argument('-s', '--statics', dest='statics',
                action='store', type=str, default='',
                help='''
                JSON string of rules list. e.g.
                '[{"static_type":0,"val1":"i-12345678","val2":"192.168.99.2","val3":"52:54:29:5c:de:a5","vxnet":"vxnet-1234567"},
                {"static_type":1,"val1":"80","val2":"192.168.99.2","val3":"8000"}]'
                ''')

    @classmethod
    def build_directive(cls, options):
        required_params = {
                'router': options.router,
                'statics': options.statics,
                }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print 'param [%s] should be specified' % param
                return None

        return {
                'router': options.router,
                'statics': json_load(options.statics),
                }
