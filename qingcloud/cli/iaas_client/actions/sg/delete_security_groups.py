# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class DeleteSecurityGroupsAction(BaseAction):

    action = 'DeleteSecurityGroups'
    command = 'delete-security-groups'
    usage = '%(prog)s -s "security_group_id, ..." [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-s', '--security_groups', dest='security_groups',
                action='store', type=str, default='',
                help='the IDs of the security groups you want to delete.')
        
    @classmethod
    def build_directive(cls, options):
        security_groups = explode_array(options.security_groups)
        if not security_groups:
            print '[security_groups] should be specified.'
            return None
        
        return {
                'security_groups': security_groups
                }
