# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class ApplySecurityGroupAction(BaseAction):

    action = 'ApplySecurityGroup'
    command = 'apply-security-group'
    usage = '%(prog)s -s <security_group_id> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        
        parser.add_argument('-s', '--security_group_id', dest='security_group_id',
                action='store', type=str, default='',
                help='ID of the security group you want to apply to instances.')

        parser.add_argument('-i', '--instances', dest='instances',
                action='store', type=str, default='',
                help='the comma-separated IDs of instances you want to apply the security group to.')
      
    @classmethod
    def build_directive(cls, options):
        required_params = {'security_group_id': options.security_group_id} 
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print 'error: [%s] should be specified' % param
                return None
        
        return {
                'security_group': options.security_group_id,
                'instances': explode_array(options.instances)
                }
