# coding: utf-8

from qingcloud.cli.iaas_client.actions.base import BaseAction

class ModifyVxnetAttributesAction(BaseAction):

    action = 'ModifyVxnetAttributes'
    command = 'modify-vxnet-attributes'
    usage = '%(prog)s [-v <vxnet_id>] [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-v', '--vxnet_id', dest='vxnet_id',
                action='store', type=str, default='',
                help='the ID of the vxnet whose attributes you want to modify.')

        parser.add_argument('-N', '--vxnet_name', dest='vxnet_name',
                action='store', type=str, default=None,
                help='specify the new vxnet name.')

        parser.add_argument('-D', '--description', dest='description',
                action='store', type=str, default=None,
                help='the detailed description of the resource')

    @classmethod
    def build_directive(cls, options):
        if not options.vxnet_id:
            return None

        return {
                'vxnet': options.vxnet_id,
                'vxnet_name': options.vxnet_name,
                'description': options.description,
                }
