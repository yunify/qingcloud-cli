# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class DissociateEipsAction(BaseAction):

    action = 'DissociateEips'
    command = 'dissociate-eips'
    usage = '%(prog)s -e "eip_id, ..." [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-e', '--eips', dest='eips',
                action='store', type=str, default='',
                help='the comma separated IDs of eips you want to dissociate from instances.')

    @classmethod
    def build_directive(cls, options):
        eips = explode_array(options.eips)
        if not eips:
            return None

        return {'eips': eips}
