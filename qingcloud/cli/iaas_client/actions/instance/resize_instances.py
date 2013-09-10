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

        return parser

    @classmethod
    def build_directive(cls, options):
        instances = explode_array(options.instances)
        instance_type = options.instance_type
        if not instances or not instance_type:
            print 'error: [instances] and [instance_type] should be specified'
            return None

        return {
                'instances': instances,
                'instance_type': instance_type,
                }
