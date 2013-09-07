# coding: utf-8

from qingcloud.cli.iaas_client.actions.base import BaseAction

class ModifySecurityGroupRuleAttributesAction(BaseAction):

    action = 'ModifySecurityGroupRuleAttributes'
    command = 'modify-security-group-rule-attributes'
    usage = '%(prog)s -r <security_group_rule_id> -p <priority> [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-r', '--security_group_rule', dest='security_group_rule',
                action='store', type=str, default='',
                help='ID of security group rule whose attributes you want to update.')

        parser.add_argument('-p', '--priority', dest='priority',
                action='store', type=int, default=None,
                help='The priority of the rule. ')

    @classmethod
    def build_directive(cls, options):
        required_params = {
                'security_group_rule': options.security_group_rule,
                'priority': options.priority,
                } 
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print 'param [%s] should be specified' % param
                return None
    
        return {
                'security_group_rule': options.security_group_rule,
                'priority': options.priority,
                }
