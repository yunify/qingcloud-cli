# coding: utf-8

from qingcloud_cli.misc.utils import explode_array
from qingcloud_cli.iaas_client.actions.base import BaseAction

class DescribeImagesAction(BaseAction):

    action = 'DescribeImages'
    command = 'describe-images'
    usage = '%(prog)s [-i image_id, ...] [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-i', '--images', dest='images',
                action='store', type=str, default='',
                help='The comma separated IDs of images you want to describe. ')

        parser.add_argument('-s', '--status', dest='status',
                action='store', type=str, default='',
                help='Status: pending, available, deleted')

        parser.add_argument('-p', '--platform', dest='platform',
                action='store', type=str, default='',
                help='What kind of bundled OS of the images you want to list. \
                        linux, windows, openSolaris. \
                        No platform specified means list all.')

        parser.add_argument('-F', '--os_family', dest='os_family',
                action='store', type=str, default='',
                help='OS family, windows/debian/centos/ubuntu.')

        parser.add_argument('-a', '--architecture', dest='architecture',
                action='store', type=str, default='',
                help='x86_64, i386')

        parser.add_argument('-N', '--image_name', dest='image_name',
                action='store', type=str, default='',
                help='The name of the image. Support partial match. ')

        parser.add_argument('-P', '--provider', dest='provider',
                action='store', type=str, default='',
                help='The id of the image provider, `self`, `system`')

    @classmethod
    def build_directive(cls, options):
        return {
                'images': explode_array(options.images),
                'platform': explode_array(options.platform),
                'architecture': explode_array(options.architecture),
                'os_family':explode_array(options.os_family),
                'status': explode_array(options.status),
                'provider': options.provider,
                'image_name': options.image_name,
                'offset':options.offset,
                'limit': options.limit,
                }
