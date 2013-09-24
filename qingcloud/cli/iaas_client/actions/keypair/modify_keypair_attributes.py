# coding: utf-8

from qingcloud.cli.iaas_client.actions.base import BaseAction

class ModifyKeyPairAttributesAction(BaseAction):

    action = 'ModifyKeyPairAttributes'
    command = 'modify-keypair-attributes'
    usage = '%(prog)s -k <keypair> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-k', '--keypair', dest='keypair',
                action='store', type=str, default='',
                help='the id of the keypair whose attributes you want to modify.')

        parser.add_argument('-N', '--keypair_name', dest='keypair_name',
                action='store', type=str, default=None,
                help='specify the new keypair name.')

        parser.add_argument('-D', '--description', dest='description',
                action='store', type=str, default=None,
                help='the detailed description of the resource')

    @classmethod
    def build_directive(cls, options):
        if not options.keypair:
            return None

        return {
                'keypair': options.keypair,
                'keypair_name': options.keypair_name,
                'description': options.description,
                }
