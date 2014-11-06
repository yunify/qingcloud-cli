# coding: utf-8

from qingcloud.cli.iaas_client.actions.base import BaseAction

class CreateVolumeFromSnapshotAction(BaseAction):

    action = 'CreateVolumeFromSnapshot'
    command = 'create-volume-from-snapshot'
    usage = '%(prog)s -s "snapshot_id" -n <name> [-f <conf_file>]'
    description = 'Create volume from snapshot.'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-s', '--snapshot', dest='snapshot',
                action='store', type=str, default='',
                help='the ID of snapshot you want to create volume from it.')

        parser.add_argument('-N', '--volume-name', dest='volume_name',
                action='store', type=str, default='',
                help='the name of new volume.')

    @classmethod
    def build_directive(cls, options):
        if not options.snapshot:
            print 'error: [snapshots] should be specified'
            return None

        return {
                'snapshot': options.snapshot,
                'volume_name': options.volume_name
                }
