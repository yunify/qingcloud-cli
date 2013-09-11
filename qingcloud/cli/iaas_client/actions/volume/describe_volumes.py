# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class DescribeVolumesAction(BaseAction):

    action = 'DescribeVolumes'
    command = 'describe-volumes'
    usage = '%(prog)s -v "volume_id,..." [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-v', '--volumes', dest='volumes',
                action='store', type=str, default='',
                help='the comma separated IDs of volumes you want to describe.')

        parser.add_argument('-i', '--instance_id', dest='instance_id',
                action='store', type=str, default='',
                help='ID of the instance that volume is currently attached to.')

        parser.add_argument('-s', '--status', dest='status',
                action='store', type=str, default='',
                help='volume status: pending, available, in-use, deleted, ceased.')

        parser.add_argument('-W', '--search_word', dest='search_word',
                action='store', type=str, default='',
                help='the combined search column')

    @classmethod
    def build_directive(cls, options):
        return {
                'volumes': explode_array(options.volumes),
                'instance_id': explode_array(options.instance_id),
                'status': explode_array(options.status),
                'search_word': options.search_word,
                'offset':options.offset,
                'limit': options.limit,
                }
