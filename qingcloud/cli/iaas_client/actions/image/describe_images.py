# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class DescribeImagesAction(BaseAction):

    action = 'DescribeImages'
    command = 'describe-images'
    usage = '%(prog)s [-i "image_id, ..."] [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-i', '--images', dest='images',
                action='store', type=str, default='',
                help='The comma separated IDs of images you want to describe. ')

        parser.add_argument('-s', '--status', dest='status',
                action='store', type=str, default='',
                help='Status: pending, available, deleted')

        parser.add_argument('-p', '--processor_type', dest='processor_type',
                action='store', type=str, default='',
                help='Filter by processor type, supported processor types are `64bit` and `32bit`')

        parser.add_argument('-F', '--os_family', dest='os_family',
                action='store', type=str, default='',
                help='Filter by OS family, supported values are windows/debian/centos/ubuntu.')

        parser.add_argument('-v', '--visibility', dest='visibility',
                action='store', type=str, default='',
                help='Filter by visibility, supported values are `public`, `private`')

        parser.add_argument('-W', '--search_word', dest='search_word',
                action='store', type=str, default='',
                help='The combined search column')

        parser.add_argument('-P', '--provider', dest='provider',
                action='store', type=str, default='',
                help='Filter by the image provider, supported values are `self`, `system`')

    @classmethod
    def build_directive(cls, options):
        return {
                'images': explode_array(options.images),
                'processor_type': explode_array(options.processor_type),
                'os_family':explode_array(options.os_family),
                'visibility': explode_array(options.visibility),
                'status': explode_array(options.status),
                'provider': options.provider,
                'search_word': options.search_word,
                'offset':options.offset,
                'limit': options.limit,
                }
