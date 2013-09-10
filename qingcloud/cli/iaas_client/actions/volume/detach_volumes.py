# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class DetachVolumesAction(BaseAction):

    action = 'DetachVolumes'
    command = 'detach-volumes'
    usage = '%(prog)s -i <instance_id> -v "volume_id,..." [-f <conf_file>]'
    description = 'Detach one or more volumes from instance.'

    @classmethod
    def add_ext_arguments(cls, parser):
    
        parser.add_argument('-i', '--instance', dest='instance',
                action='store', type=str, default='',
                help='the comma separated IDs of volumes you want to describe.')

        parser.add_argument('-v', '--volumes', dest='volumes',
                action='store', type=str, default='',
                help='the ID of instance the volumes will be detached from.')

    @classmethod
    def build_directive(cls, options):
        volumes = explode_array(options.volumes)
        if not volumes or not options.instance:
            return None

        return {
                'volumes': volumes,
                'instance': options.instance,
                }
