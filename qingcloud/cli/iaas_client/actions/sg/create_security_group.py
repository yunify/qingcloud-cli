# coding: utf-8

from qingcloud.cli.iaas_client.actions.base import BaseAction

class CreateSecurityGroupAction(BaseAction):

    action = 'CreateSecurityGroup'
    command = 'create-security-group'
    usage = '%(prog)s --group_name <group_name> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-N', '--security_group_name', dest='security_group_name',
                action='store', type=str, default='',
                help='short name for the security group you want to create.')

    @classmethod
    def build_directive(cls, options):
        required_params = {
                'security_group_name': options.security_group_name,
                }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print 'param [%s] should be specified' % param
                return None

        return {'security_group_name': options.security_group_name}
