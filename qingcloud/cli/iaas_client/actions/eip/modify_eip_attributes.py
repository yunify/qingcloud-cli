# coding: utf-8

from qingcloud.cli.iaas_client.actions.base import BaseAction

class ModifyEipAttributesAction(BaseAction):

    action = 'ModifyEipAttributes'
    command = 'modify-eip-attributes'
    usage = '%(prog)s -e <eip_id> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-e', '--eip_id', dest = 'eip_id',
                action='store', type=str, default='',
                help='the id of the eip whose attributes you want to modify.')

        parser.add_argument('-n', '--eip_name', dest='eip_name',
                action='store', type=str, default=None,
                help='specify the new eip name.')

        parser.add_argument('-d', '--description', dest='description',
                action='store', type=str, default=None,
                help='the detailed description of the resource')

    @classmethod
    def build_directive(cls, options):
        if not options.eip_id:
            return None

        return {
                'eip': options.eip_id,
                'eip_name': options.eip_name,
                'description': options.description,
                }
