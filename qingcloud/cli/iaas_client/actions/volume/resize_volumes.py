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
                help='the comma separated IDs of volumes you want to resize.')
        
        parser.add_argument('-s', '--size', dest='size',
                action='store', type=int, default=0,
                help='new volume size you want to resize to.')

    @classmethod
    def build_directive(cls, options):
        if not options.volumes:
            print 'error: [volumes] should be specified'
            return None

        if options.size <= 0:
            print 'error: [size] should be larger than 0'
            return None

        return {
                'volumes': explode_array(options.volumes),
                'size': options.size
                }
