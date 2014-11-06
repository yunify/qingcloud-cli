# coding: utf-8

from qingcloud.cli.iaas_client.actions.base import BaseAction

class CaptureInstanceFromSnapshotAction(BaseAction):

    action = 'CaptureInstanceFromSnapshot'
    command = 'capture-instance-from-snapshot'
    usage = '%(prog)s -s <snapshot> -n <image-name> [-f <conf_file>]'
    description = 'capture instance image from snapshot.'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-s', '--snapshot', dest='snapshot',
                action='store', type=str, default='',
                help='the ID of snapshot you want to capture as image.')

        parser.add_argument('-N', '--image-name', dest='image_name',
                action='store', type=str, default='',
                help='the name of image.')

    @classmethod
    def build_directive(cls, options):
        required_params = {
                'snapshot': options.snapshot,
                }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print 'error: [%s] should be specified' % param
                return None

        return {
                'snapshot': options.snapshot,
                'image_name': options.image_name,
                }
