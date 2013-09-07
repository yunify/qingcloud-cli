# coding: utf-8

from qingcloud_cli.misc.utils import explode_array
from qingcloud_cli.iaas_client.actions.base import BaseAction

class DescribeVxnetsAction(BaseAction):

    action = 'DescribeVxnets'
    command = 'describe-vxnets'
    usage = '%(prog)s [-v vxnet_id, ...] [-o <owner>] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-v', '--vxnets', dest='vxnets',
                action='store', type=str, default='',
                help='The comma separated IDs of vxnets you want to list.')

        parser.add_argument('-V', '--verbose', dest='verbose',
                action='store', type=int, default=0,
                help='The number to specify the verbose level, larger the number, the more detailed information will be returned.')

        parser.add_argument('-N', '--vxnet_name', dest='vxnet_name',
                action='store', type=str, default='',
                help='Name of the vnxet. Support partial match. ')

    @classmethod
    def build_directive(cls, options):
        return {
                'vxnets': explode_array(options.vxnets),
                'vxnet_name': options.vxnet_name,
                'verbose': options.verbose,
                'offset':options.offset,
                'limit': options.limit,
                }
