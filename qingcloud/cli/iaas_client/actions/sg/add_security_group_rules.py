# coding: utf-8

from qingcloud.cli.misc.json_tool import json_load
from qingcloud.cli.iaas_client.actions.base import BaseAction

class AddSecurityGroupRulesAction(BaseAction):

    action = 'AddSecurityGroupRules'
    command = 'add-security-group-rules'
    usage = '%(prog)s -s <security_group_id> -r <rules> [-f <conf_file>]'
    description = 'Add one or more rules to security group'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-s', '--security_group', dest='security_group',
                action='store', type=str, default='',
                help='ID of security_group whose rules you want to list. ')

        parser.add_argument('-r', '--rules', dest='rules',
                action='store', type=str, default='',
                help='JSON string of rules list. e.g. "[{"protocol":"icmp","priority":"0","action":"accept","val2":"0","val1":"11"}]"')

    @classmethod
    def build_directive(cls, options):
        security_group = options.security_group
        rules = json_load(options.rules)
        if not rules or not security_group:
            print 'error: [rules] and [security_group] should be specified'
            return None

        return {
                'security_group': security_group,
                     'rules': rules,
                    }
