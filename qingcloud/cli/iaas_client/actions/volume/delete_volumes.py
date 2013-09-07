# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class DeleteVolumesAction(BaseAction):

    action = 'DeleteVolumes'
    command = 'delete-volumes'
    usage = '%(prog)s -v "volume_id,..." [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
    
        parser.add_argument('-v', '--volumes', dest='volumes',
                action='store', type=str, default='',
                help='The comma separated IDs of volumes you want to delete.')
        
    @classmethod
    def build_directive(cls, options):
        volumes = explode_array(options.volumes)
        if not volumes:
            return None

        return {'volumes': volumes}
