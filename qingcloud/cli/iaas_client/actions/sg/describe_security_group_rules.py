# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class DescribeSecurityGroupRulesAction(BaseAction):

    action = 'DescribeSecurityGroupRules'
    command = 'describe-security-group-rules'
    usage = '%(prog)s -s <security_group_id> -r <security_group_rules> [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-s', '--security_group', dest='security_group',
                action='store', type=str, default='',
                help='ID of security_group whose rules you want to list. ')

        parser.add_argument('-r', '--security_group_rules', dest='security_group_rules',
                action='store', type=str, default='',
                help='ID of security group rule you want to list. ')

        parser.add_argument('-d', '--direction', dest='direction',
                action='store', type=int, default=None,
                help='0 for inbound; 1 for outbound.')

    @classmethod
    def build_directive(cls, options):
        return {
                'security_group': options.security_group,
                'security_group_rules': explode_array(options.security_group_rules),
                'direction': options.direction,
                'offset':options.offset,
                'limit': options.limit,
                }
