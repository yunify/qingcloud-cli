# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class DescribeRoutersAction(BaseAction):

    action = 'DescribeRouters'
    command = 'describe-routers'
    usage = '%(prog)s [-r "router_id, ..."] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-r', '--routers', dest='routers',
                action='store', type=str, default='',
                help='the comma separated IDs of routers you want to list.')

        parser.add_argument('-s', '--status', dest='status',
                action='store', type=str, default='',
                help='router status: pending, active, poweroffed, suspended, deleted, ceased')

        parser.add_argument('-W', '--search_word', dest='search_word',
                action='store', type=str, default='',
                help='the combined search column')

        parser.add_argument('-V', '--verbose', dest='verbose',
                action='store', type=int, default=0,
                help='the number to specify the verbose level, larger the number, the more detailed information will be returned.')


    @classmethod
    def build_directive(cls, options):
        return {
                'routers': explode_array(options.routers),
                'status': explode_array(options.status),
                'verbose': options.verbose,
                'search_word': options.search_word,
                'offset':options.offset,
                'limit': options.limit,
                }
