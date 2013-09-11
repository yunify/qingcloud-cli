# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class DescribeVxnetInstancesAction(BaseAction):

    action = 'DescribeVxnetInstances'
    command = 'describe-vxnet-instances'
    usage = '%(prog)s -v <vxnet_id> [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-v', '--vxnet', dest='vxnet',
                action='store', type=str, default='',
                help='ID of vxnet whose instances you want to list.')

        parser.add_argument('-m', '--image', dest='image',
                action='store', type=str, default='',
                help='filter by ID of image that instance based')

        parser.add_argument('-i', '--instances', dest='instances',
                action='store', type=str, default='',
                help='filter by comma separated IDs of instances')

        parser.add_argument('-t', '--instance_type', dest='instance_type',
                action='store', type=str, default='',
                help='filter by instance type')

        parser.add_argument('-s', '--status', dest='status',
                action='store', type=str, default='',
                help='filter by instance status: pending, running, stopped, suspended, terminated, ceased')

    @classmethod
    def build_directive(cls, options):
        if not options.vxnet:
            print '[vxnet] should be provided'
            return None

        return {
                'vxnet': options.vxnet,
                'image': explode_array(options.image),
                'instances': explode_array(options.instances),
                'instance_type': explode_array(options.instance_type),
                'status': explode_array(options.status),
                'offset':options.offset,
                'limit': options.limit,
                }
