# coding: utf-8

from qingcloud_cli.misc.utils import explode_array
from qingcloud_cli.iaas_client.actions.base import BaseAction

class TerminateInstancesAction(BaseAction):

    action = 'TerminateInstances'
    command = 'terminate-instances'
    usage = '%(prog)s -i instance_id,... [-f <conf_file>]'
    description = '销毁一台或多台主机'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-i', '--instances', dest='instances',
                action='store', type=str, default='',
                help='要销毁的主机ID列表，以逗号分隔')

        return parser

    @classmethod
    def build_directive(cls, options):
        instances = explode_array(options.instances)
        if not instances:
            print 'error:instance_id should be specified'
            return None

        return {'instances': instances}
