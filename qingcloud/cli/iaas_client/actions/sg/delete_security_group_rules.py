# coding: utf-8

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction

class DeleteSecurityGroupRulesAction(BaseAction):

    action = 'DeleteSecurityGroupRules'
    command = 'delete-security-group-rules'
    usage = '%(prog)s -r "security_group_rule_id, ..." [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-r', '--security_group_rules', dest='security_group_rules',
                action='store', type=str, default='',
                help='the comma separated IDs of security group rules you want to delete. ')

    @classmethod
    def build_directive(cls, options):
        security_group_rules = explode_array(options.security_group_rules)
        if not security_group_rules:
            print "[security_groups_rules] should be specified."
            return None
        
        return {
                'security_group_rules': security_group_rules,
                }
