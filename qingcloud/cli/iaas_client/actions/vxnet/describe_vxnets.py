# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class DescribeVxnetsAction(BaseAction):

    action = 'DescribeVxnets'
    command = 'describe-vxnets'
    usage = '%(prog)s [-v "vxnet_id, ..."] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-v', '--vxnets', dest='vxnets',
                action='store', type=str, default='',
                help='the comma separated IDs of vxnets you want to list.')

        parser.add_argument('-V', '--verbose', dest='verbose',
                action='store', type=int, default=0,
                help='the number to specify the verbose level, larger the number, the more detailed information will be returned.')

        parser.add_argument('-W', '--search_word', dest='search_word',
                action='store', type=str, default='',
                help='the combined search column')

    @classmethod
    def build_directive(cls, options):
        return {
                'vxnets': explode_array(options.vxnets),
                'search_word': options.search_word,
                'verbose': options.verbose,
                'offset':options.offset,
                'limit': options.limit,
                }
