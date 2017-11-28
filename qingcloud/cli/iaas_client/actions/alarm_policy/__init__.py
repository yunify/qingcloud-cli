# =========================================================================
# Copyright 2012-present Yunify, Inc.
# -------------------------------------------------------------------------
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this work except in compliance with the License.
# You may obtain a copy of the License in the LICENSE file, or at:
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========================================================================
from qingcloud.cli.iaas_client.actions.alarm_policy.describe_alarm_policies import DescribeAlarmPoliciesAction
from qingcloud.cli.iaas_client.actions.alarm_policy.add_alarm_policy_actions import AddAlarmPolicyActionsAction
from qingcloud.cli.iaas_client.actions.alarm_policy.add_alarm_policy_rules import AddAlarmPolicyRulesAction
from qingcloud.cli.iaas_client.actions.alarm_policy.apply_alarm_policy import ApplyAlarmPolicyAction
from qingcloud.cli.iaas_client.actions.alarm_policy.associate_alarm_policy import AssociateAlarmPolicyAction
from qingcloud.cli.iaas_client.actions.alarm_policy.create_alarm_policy import CreateAlarmPolicyAction
from qingcloud.cli.iaas_client.actions.alarm_policy.delete_alarm_policies import DeleteAlarmPoliciesAction
from qingcloud.cli.iaas_client.actions.alarm_policy.delete_alarm_policy_actions import DeleteAlarmPolicyActionsAction
from qingcloud.cli.iaas_client.actions.alarm_policy.delete_alarm_policy_rules import DeleteAlarmPolicyRulesAction
from qingcloud.cli.iaas_client.actions.alarm_policy.describe_alarm_history import DescribeAlarmHistoryAction
from qingcloud.cli.iaas_client.actions.alarm_policy.describe_alarm_policy_actions import DescribeAlarmPolicyActionsAction
from qingcloud.cli.iaas_client.actions.alarm_policy.describe_alarm_policy_rules import DescribeAlarmPolicyRulesAction
from qingcloud.cli.iaas_client.actions.alarm_policy.describe_alarms import DescribeAlarmsAction
from qingcloud.cli.iaas_client.actions.alarm_policy.dissociate_alarm_policy import DissociateAlarmPolicyAction
from qingcloud.cli.iaas_client.actions.alarm_policy.modify_alarm_policy_action_attributes import ModifyAlarmPolicyActionAttributesAction
from qingcloud.cli.iaas_client.actions.alarm_policy.modify_alarm_policy_attributes import ModifyAlarmPolicyAttributesAction
from qingcloud.cli.iaas_client.actions.alarm_policy.modify_alarm_policy_rule_attributes import ModifyAlarmPolicyRuleAttributesAction


__all__ = [
    DescribeAlarmPoliciesAction, AddAlarmPolicyActionsAction,
    AddAlarmPolicyRulesAction, ApplyAlarmPolicyAction,
    AssociateAlarmPolicyAction, CreateAlarmPolicyAction,
    DeleteAlarmPoliciesAction, DeleteAlarmPolicyActionsAction,
    DeleteAlarmPolicyRulesAction, DescribeAlarmHistoryAction,
    DescribeAlarmPolicyActionsAction, DescribeAlarmPolicyRulesAction,
    DescribeAlarmsAction, DissociateAlarmPolicyAction,
    ModifyAlarmPolicyActionAttributesAction, ModifyAlarmPolicyAttributesAction,
    ModifyAlarmPolicyRuleAttributesAction
]
