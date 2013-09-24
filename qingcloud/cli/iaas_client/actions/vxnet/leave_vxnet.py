# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class LeaveVxnetAction(BaseAction):

    action = 'LeaveVxnet'
    command = 'leave-vxnet'
    usage = '%(prog)s --instances "instance_id, ..." --vxnet <vxnet_id> [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-i', '--instances', dest='instances',
                action='store', type=str, default='',
                help='the IDs of instances that will leave a vxnet.')

        parser.add_argument('-v', '--vxnet', dest='vxnet',
                action='store', type=str, default='',
                help='the ID of the vxnet the instances will leave. ')

    @classmethod
    def build_directive(cls, options):
        instances = explode_array(options.instances)
        if not options.vxnet or not instances:
            print 'error: [instances] and [vxnet] should be specified'
            return None

        return {
                'vxnet': options.vxnet,
                'instances': instances,
                }
