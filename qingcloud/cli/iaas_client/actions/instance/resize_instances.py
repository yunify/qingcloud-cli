# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class ResizeInstancesAction(BaseAction):

    action = 'ResizeInstances'
    command = 'resize-instances'
    usage = '%(prog)s -i "instance_id, ..." -t <instance_type> [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-i', '--instances', dest='instances',
                action='store', type=str, default='',
                help='the comma separated IDs of instances you want to resize.')

        parser.add_argument('-t', '--instance_type', dest='instance_type',
                action='store', type=str, default='',
                help='new instance type you want to resize to.')

        parser.add_argument('-C', '--cpu', dest='cpu',
                action='store', type=int, default=None,
                help='cpu core: 1, 2, 4, 8, 16')

        parser.add_argument('-M', '--memory', dest='memory',
                action='store', type=int, default=None,
                help='memory size in MB: 512, 1024, 2048, 4096, 8192, 16384')

        return parser

    @classmethod
    def build_directive(cls, options):
        instances = explode_array(options.instances)
        if not instances:
            print 'error: [instances] should be specified'
            return None

        instance_type = options.instance_type
        if not instance_type:
            if not options.cpu or not options.memory:
                print 'error: [instance_type] should be specified or specify both [cpu] and [memory]'
                return None

        return {
                'instances': instances,
                'instance_type': instance_type,
                'cpu': options.cpu,
                'memory': options.memory,
                }
