# coding: utf-8

from qingcloud_cli.misc.utils import explode_array
from qingcloud_cli.iaas_client.actions.base import BaseAction

class DescribeKeyPairsAction(BaseAction):

    action = 'DescribeKeyPairs'
    command = 'describe-keypairs'
    usage = '%(prog)s [-k keypair_id, ...] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        
        parser.add_argument('-k', '--keypairs', dest='keypairs',
                action='store', type=str, default='',
                help='The ids of keypairs you want to list.')

        parser.add_argument('-e', '--encrypt_method', dest='encrypt_method',
                action='store', type=str, default='',
                help='Encrypt method. supported method: `ssh-rsa` and `ssh-dss`')
        
        parser.add_argument('-N', '--keypair_name', dest='keypair_name',
                action='store', type=str, default='',
                help='Name of the key pair. Support partial match.')

        parser.add_argument('-V', '--verbose', dest='verbose',
                action='store', type=int, default=0,
                help='The number to specify the verbose level, larger the number, the more detailed information will be returned.')
         
    @classmethod
    def build_directive(cls, options):
        return {
                'keypairs': explode_array(options.keypairs),
                     'encrypt_method': explode_array(options.encrypt_method), 
                     'keypair_name': options.keypair_name,
                     'verbose': options.verbose,
                     'offset':options.offset,
                     'limit': options.limit,
                    }
