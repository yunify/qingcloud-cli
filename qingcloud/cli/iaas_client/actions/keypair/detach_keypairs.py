# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class DetachKeyPairsAction(BaseAction):

    action = 'DetachKeyPairs'
    command = 'detach-keypairs'
    usage = '%(prog)s --instances "instance_id, ..." --keypairs "kp_id, ..." [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        
        parser.add_argument('-k', '--keypairs', dest='keypairs',
                action='store', type=str, default='',
                help='the comma separated IDs of keypairs you want to detach from instances. ')

        parser.add_argument('-i', '--instances', dest='instances',
                action='store', type=str, default='',
                help='the IDs of instances the keypairs will be detached from.')

    @classmethod
    def build_directive(cls, options):
        keypairs = explode_array(options.keypairs)
        instances = explode_array(options.instances)
        if not keypairs or not instances:
            return None

        return {
                'keypairs': keypairs,
                'instances': instances,
                }
