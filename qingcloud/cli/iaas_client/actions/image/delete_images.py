# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class DeleteImagesAction(BaseAction):

    action = 'DeleteImages'
    command = 'delete-images'
    usage = '%(prog)s -i "image_id, ..." [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-i', '--images', dest='images',
                action='store', type=str, default='',
                help='the comma separated IDs of images you want to delete. ')

    @classmethod
    def build_directive(cls, options):
        images = explode_array(options.images)
        if not images:
            return None

        return {'images': images}
