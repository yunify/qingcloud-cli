# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class DeleteVxnetsAction(BaseAction):

    action = 'DeleteVxnets'
    command = 'delete-vxnet'
    usage = '%(prog)s --vxnets "vxnet_id, ..." [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-v', '--vxnets', dest='vxnets',
                action='store', type=str, default='',
                help='IDs of vxnets you want to delete.')
        
    @classmethod
    def build_directive(cls, options):
        vxnets = explode_array(options.vxnets)
        if not vxnets:
            print '[vxnets] should be specified.'
            return None
        
        return {'vxnets': vxnets}
