# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class DescribeEipsAction(BaseAction):

    action = 'DescribeEips'
    command = 'describe-eips'
    usage = '%(prog)s [-e "eip, ..."] [-g <eip_group>] [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-e', '--eips', dest='eips',
                action='store', type=str, default='',
                help='the comma separated IDs of eips you want to describe. ')

        parser.add_argument('-s', '--status', dest='status',
                action='store', type=str, default='',
                help='eip status: pending, available, associated, released.')

        parser.add_argument('-g', '--eip_group', dest='eip_group',
                action='store', type=str, default='',
                help='filter by eip group.')

        parser.add_argument('-W', '--search_word', dest='search_word',
                action='store', type=str, default='',
                help='the combined search column')

        parser.add_argument('-i', '--instance_id', dest='instance_id',
                action='store', type=str, default='',
                help='filter eips by instance id')

    @classmethod
    def build_directive(cls, options):
        return {
                'eips': explode_array(options.eips),
                'status': explode_array(options.status),
                'eip_group': explode_array(options.eip_group),
                'instance_id': options.instance_id,
                'search_word': options.search_word,
                'offset':options.offset,
                'limit': options.limit,
                }
