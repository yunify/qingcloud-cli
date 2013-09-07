# coding: utf-8

from qingcloud.cli.iaas_client.actions.base import BaseAction

class CreateKeyPairAction(BaseAction):

    action = 'CreateKeyPair'
    command = 'create-keypair'
    usage = '%(prog)s --keypair_name <keypair_name> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-n', '--keypair_name', dest='keypair_name',
                action='store', type=str, default=None,
                help='Name of the keypair.')
        
        parser.add_argument('-m', '--mode', dest='mode',
                action='store', type=str, default=None,
                help='The keypair creation mode, `system` or `user`.')
        
        parser.add_argument('-e', '--encrypt_method', dest='encrypt_method',
                action='store', type=str, default='ssh-rsa',
                help='The encrypt method: `ssh-rsa`, `ssh-dss`, default `ssh-rsa`')
        
        parser.add_argument('-p', '--public_key', dest='public_key',
                action='store', type=str, default='',
                help='You can provide your own public key here')

    @classmethod
    def build_directive(cls, options):
        required_params = {'keypair_name': options.keypair_name} 
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print 'param [%s] should be specified' % param
                return None
        
        return {
                'keypair_name': options.keypair_name,
                'mode': options.mode,
                'encrypt_method': options.encrypt_method,
                'public_key': options.public_key,
                }
