# coding: utf-8

from qingcloud_cli.misc.utils import explode_array
from qingcloud_cli.iaas_client.actions.base import BaseAction

class DescribeSecurityGroupsAction(BaseAction):

    action = 'DescribeSecurityGroups'
    command = 'describe-security-groups'
    usage = '%(prog)s [-s security_group_id, ...] [-o <owner>] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-s', '--security_groups', dest='security_groups',
                action='store', type=str, default='',
                help='The comma separated IDs of security_groups you want to list. ')
        
        parser.add_argument('-N', '--security_group_name', dest='security_group_name',
                action='store', type=str, default='',
                help='Name of the security group. Support partial match. ')

        parser.add_argument('-V', '--verbose', dest='verbose',
                action='store', type =int, default=0,
                help='The number to specify the verbose level, larger the number, the more detailed information will be returned.')

    @classmethod
    def build_directive(cls, options):
        return {
                'security_groups': explode_array(options.security_groups),
                'security_group_name': options.security_group_name,
                'verbose': options.verbose,
                'offset':options.offset,
                'limit': options.limit,
                }
