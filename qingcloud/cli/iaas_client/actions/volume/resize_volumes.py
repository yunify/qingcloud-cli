# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class ResizeVolumesAction(BaseAction):

    action = 'ResizeVolumes'
    command = 'resize-volumes'
    usage = '%(prog)s -v "volume_id,..." -s <size> [-f <conf_file>]'
    description = 'Extend one or more volumes'

    @classmethod
    def add_ext_arguments(cls, parser):
        
        parser.add_argument('-v', '--volumes', dest='volumes',
                action='store', type=str, default='',
                help='The comma separated IDs of volumes you want to resize.')
        
        parser.add_argument('-s', '--size', dest='size',
                action='store', type=int, default=0,
                help='New volume size you want to resize to.')

    @classmethod
    def build_directive(cls, options):
        volumes = explode_array(options.volumes)
        size = options.size
        if not volumes or size == 0:
            return None

        return {
                'volumes': volumes,
                'size': size
                }
