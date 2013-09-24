# coding: utf-8

from qingcloud.cli.iaas_client.actions.base import BaseAction

class CreateVolumesAction(BaseAction):

    action = 'CreateVolumes'
    command = 'create-volumes'
    usage = '%(prog)s --size <volume_size> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-s', '--size', dest='size',
                action='store', type=int, default=None,
                help='the size of each volume. Unit is GB.')

        parser.add_argument('-c', '--count', dest='count',
                action='store', type=int, default=1,
                help='the number of volumes to create.')

        parser.add_argument('-N', '--volume_name', dest='volume_name',
                action='store', type=str, default='',
                help='short name of volume')

    @classmethod
    def build_directive(cls, options):
        required_params = {'size': options.size}
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print 'error: [%s] should be specified' % param
                return None

        return {
                'size': options.size,
                'count' : options.count,
                'volume_name' : options.volume_name
                }
