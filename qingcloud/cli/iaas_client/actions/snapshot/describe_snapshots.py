# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class DescribeSnapshotsAction(BaseAction):

    action = 'DescribeSnapshots'
    command = 'describe-snapshots'
    usage = '%(prog)s -s "snapshot_id,..." [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-n', '--snapshots', dest='snapshots',
                action='store', type=str, default='',
                help='the comma separated IDs of snapshots you want to describe.')

        parser.add_argument('-r', '--resource', dest='resource_id',
                action='store', type=str, default='',
                help='ID of the resource that snapshot is created from.')

        parser.add_argument('-t', '--snapshot-type', dest='snapshot_type',
                action='store', type=int, default=None,
                help='snapshot type: 0 for incremental snapshot, 1 for full snapshot.')

        parser.add_argument('-s', '--status', dest='status',
                action='store', type=str, default='',
                help='snapshot status: pending, available, suspended, deleted, ceased')

        parser.add_argument('-V', '--verbose', dest='verbose',
                action='store', type=int, default=0,
                help='the number to specify the verbose level, larger the number, the more detailed information will be returned.')

        parser.add_argument('-W', '--search-word', dest='search_word',
                action='store', type=str, default='',
                help='the combined search column')

    @classmethod
    def build_directive(cls, options):
        return {
                'snapshots': explode_array(options.snapshots),
                'snapshot_type': options.snapshot_type,
                'resource_id': options.resource_id,
                'status': explode_array(options.status),
                'search_word': options.search_word,
                'verbose': options.verbose,
                'offset':options.offset,
                'limit': options.limit,
                }
