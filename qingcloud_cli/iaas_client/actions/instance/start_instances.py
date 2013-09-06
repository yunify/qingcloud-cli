# coding: utf-8

from qingcloud_cli.misc.utils import explode_array
from qingcloud_cli.iaas_client.actions.base import BaseAction

class StartInstancesAction(BaseAction):

    action = 'StartInstances'
    command = 'start-instances'
    usage = '%(prog)s -i instance_id,... [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-i', '--instances', dest='instances',
                action='store', type=str, default='',
                help='要启动的主机ID列表，以逗号分隔')

        return parser

    @classmethod
    def build_directive(cls, options):
        instances = explode_array(options.instances)
        if not instances:
            print 'error:instance_id should be specified'
            return None

        return {'instances': instances}
