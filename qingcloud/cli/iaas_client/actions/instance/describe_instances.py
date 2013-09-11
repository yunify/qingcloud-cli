# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class DescribeInstancesAction(BaseAction):

    action = 'DescribeInstances'
    command = 'describe-instances'
    usage = '%(prog)s [-i "instance_id, ..."] [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-i', '--instances', dest='instances',
                action='store', type=str, default='',
                help='the comma separated IDs of instances you want to describe.')

        parser.add_argument('-s', '--status', dest='status',
                action='store', type=str, default='',
                help='instance status: pending, running, stopped, terminated, ceased')

        parser.add_argument('-m', '--image_id', dest='image_id',
                action='store', type=str, default='',
                help='the image id of instances.')

        parser.add_argument('-t', '--instance_type',
                action='store', type=str,
                dest='instance_type', default='',
                help='instance type: small_b, small_c, medium_a, medium_b, medium_c, \
                large_a, large_b, large_c')

        parser.add_argument('-W', '--search_word', dest='search_word',
                action='store', type=str, default='',
                help='the combined search column')

        parser.add_argument('-V', '--verbose', dest='verbose',
                action='store', type=int, default=0,
                help='the number to specify the verbose level, larger the number, the more detailed information will be returned.')

        return parser

    @classmethod
    def build_directive(cls, options):
        return {
                'instances': explode_array(options.instances),
                'status': explode_array(options.status),
                'image_id': explode_array(options.image_id),
                'instance_type': explode_array(options.instance_type),
                'search_word': options.search_word,
                'verbose': options.verbose,
                'offset':options.offset,
                'limit': options.limit,
                }
