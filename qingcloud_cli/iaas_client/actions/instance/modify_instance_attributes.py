# coding: utf-8

from qingcloud_cli.iaas_client.actions.base import BaseAction

class ModifyInstanceAttributesAction(BaseAction):

    action = 'ModifyInstanceAttributes'
    command = 'modify-instance-attributes'
    usage = '%(prog)s -i <instance_id> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-i', '--instance_id', dest='instance_id',
                action='store', type=str, default='',
                help='要修改属性的主机ID')

        parser.add_argument('-n', '--instance_name', dest='instance_name',
                action='store', type=str, default='',
                help='主机名称')

        parser.add_argument('-d', '--description', dest='description',
                action='store', type=str, default='',
                help='主机描述')

        return parser

    @classmethod
    def build_directive(cls, options):
        if options.instance_id == '':
            print 'error:instance_id should be specified'
            return None

        return {
                'instance': options.instance_id,
                'instance_name': options.instance_name,
                'description': options.description,
                }
