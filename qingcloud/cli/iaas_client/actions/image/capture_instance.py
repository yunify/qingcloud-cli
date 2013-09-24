# coding: utf-8

from qingcloud.cli.iaas_client.actions.base import BaseAction

class CaptureInstanceAction(BaseAction):

    action = 'CaptureInstance'
    command = 'capture-instance'
    usage = '%(prog)s --instance <instance_id> --image_name <image_name> [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-i', '--instance', dest='instance',
                action='store', type=str, default=None,
                help='ID of the instance you want to capture.')

        parser.add_argument('-N', '--image_name', dest='image_name',
                action='store', type=str, default='',
                help='short name of the image.')

    @classmethod
    def build_directive(cls, options):
        if not options.instance:
            return None

        return {
                'instance': options.instance,
                'image_name': options.image_name
                }
