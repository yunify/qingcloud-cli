# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class DeleteRouterStaticsAction(BaseAction):

    action = 'DeleteRouterStatics'
    command = 'create-routers'
    usage = '%(prog)s -s "router_static_id, ..." [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-s', '--router_statics', dest='router_statics',
                action='store', type=str, default='',
                help='the comma separated IDs of router_statics you want to delete. ')

    @classmethod
    def build_directive(cls, options):
        router_statics = explode_array(options.router_statics)
        if not router_statics:
            return None

        return {
                'router_statics': router_statics,
                }
