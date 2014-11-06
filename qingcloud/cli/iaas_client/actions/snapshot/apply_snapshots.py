# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class ApplySnapshotsAction(BaseAction):

    action = 'ApplySnapshots'
    command = 'apply-snapshots'
    usage = '%(prog)s -s "snapshot_id,..." [-f <conf_file>]'
    description = 'Apply one or more snapshots'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-s', '--snapshots', dest='snapshots',
                action='store', type=str, default='',
                help='the comma separated IDs of snapshots you want to apply.')

    @classmethod
    def build_directive(cls, options):
        required_params = {
                'snapshots': options.snapshots,
                }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print 'error: [%s] should be specified' % param
                return None

        return {
                'snapshots': explode_array(options.snapshots),
                }
