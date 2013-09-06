# coding: utf-8

from qingcloud_cli.misc.utils import explode_array
from qingcloud_cli.iaas_client.actions.base import BaseAction

class StopInstancesAction(BaseAction):

    action = 'StopInstances'
    command = 'stop-instances'
    usage = '%(prog)s -i instance_id,... [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        
        parser.add_argument('-i', '--instances', dest='instances',
                action='store', type=str, default='',
                help='要关闭的主机ID列表，以逗号分隔')

        parser.add_argument('-F', '--force',
                action='store_const', const=1,
                dest='force',
                help='是否强制关机，`1`为强制关机，`0`为正常关机')

        return parser

    @classmethod
    def build_directive(cls, options):
        instances = explode_array(options.instances)
        if not instances:
            print 'error:instance_id should be specified'
            return None

        directive = {
                'instances': instances,
                }
        if options.force:
            directive.update({'force': options.force})

        return directive
