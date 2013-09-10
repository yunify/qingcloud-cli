# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class DescribeKeyPairsAction(BaseAction):

    action = 'DescribeKeyPairs'
    command = 'describe-keypairs'
    usage = '%(prog)s [-k "keypair_id, ..."] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-k', '--keypairs', dest='keypairs',
                action='store', type=str, default='',
                help='the ids of keypairs you want to list.')

        parser.add_argument('-e', '--encrypt_method', dest='encrypt_method',
                action='store', type=str, default='',
                help='encrypt method. supported method: `ssh-rsa` and `ssh-dss`')

        parser.add_argument('-W', '--search_word', dest='search_word',
                action='store', type=str, default='',
                help='the combined search column')

        parser.add_argument('-V', '--verbose', dest='verbose',
                action='store', type=int, default=0,
                help='the number to specify the verbose level, larger the number, the more detailed information will be returned.')

    @classmethod
    def build_directive(cls, options):
        return {
                'keypairs': explode_array(options.keypairs),
                'encrypt_method': explode_array(options.encrypt_method),
                'search_word': options.search_word,
                'verbose': options.verbose,
                'offset':options.offset,
                'limit': options.limit,
                }
