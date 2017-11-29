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
from qingcloud.cli.iaas_client.actions.collaboration.describe_shared_resource_groups import DescribeSharedResourceGroupsAction
from qingcloud.cli.iaas_client.actions.collaboration.describe_resource_groups import DescribeResourceGroupsAction
from qingcloud.cli.iaas_client.actions.collaboration.create_resource_groups import CreateResourceGroupsAction
from qingcloud.cli.iaas_client.actions.collaboration.modify_resource_group_attributes import ModifyResourceGroupAttributesAction
from qingcloud.cli.iaas_client.actions.collaboration.delete_resource_groups import DeleteResourceGroupsAction
from qingcloud.cli.iaas_client.actions.collaboration.describe_resource_group_items import DescribeResourceGroupItemsAction
from qingcloud.cli.iaas_client.actions.collaboration.add_resource_group_items import AddResourceGroupItemsAction
from qingcloud.cli.iaas_client.actions.collaboration.delete_resource_group_items import DeleteResourceGroupItemsAction
from qingcloud.cli.iaas_client.actions.collaboration.describe_user_groups import DescribeUserGroupsAction
from qingcloud.cli.iaas_client.actions.collaboration.create_user_groups import CreateUserGroupsAction
from qingcloud.cli.iaas_client.actions.collaboration.modify_user_group_attributes import ModifyUserGroupAttributesAction
from qingcloud.cli.iaas_client.actions.collaboration.delete_user_groups import DeleteUserGroupsAction
from qingcloud.cli.iaas_client.actions.collaboration.describe_user_group_members import DescribeUserGroupMembersAction
from qingcloud.cli.iaas_client.actions.collaboration.add_user_group_members import AddUserGroupMembersAction
from qingcloud.cli.iaas_client.actions.collaboration.modify_user_group_member_attributes import ModifyUserGroupMemberAttributesAction
from qingcloud.cli.iaas_client.actions.collaboration.delete_user_group_members import DeleteUserGroupMembersAction
from qingcloud.cli.iaas_client.actions.collaboration.describe_group_roles import DescribeGroupRolesAction
from qingcloud.cli.iaas_client.actions.collaboration.create_group_roles import CreateGroupRolesAction
from qingcloud.cli.iaas_client.actions.collaboration.modify_group_role_attributes import ModifyGroupRoleAttributesAction
from qingcloud.cli.iaas_client.actions.collaboration.delete_group_roles import DeleteGroupRolesAction
from qingcloud.cli.iaas_client.actions.collaboration.describe_group_role_rules import DescribeGroupRoleRulesAction
from qingcloud.cli.iaas_client.actions.collaboration.add_group_role_rules import AddGroupRoleRulesAction
from qingcloud.cli.iaas_client.actions.collaboration.modify_group_role_rule_attributes import ModifyGroupRoleRuleAttributesAction
from qingcloud.cli.iaas_client.actions.collaboration.delete_group_role_rules import DeleteGroupRoleRulesAction
from qingcloud.cli.iaas_client.actions.collaboration.grant_resource_groups_to_user_groups import GrantResourceGroupsToUserGroupsAction
from qingcloud.cli.iaas_client.actions.collaboration.revoke_resource_groups_from_user_groups import RevokeResourceGroupsFromUserGroupsAction
from qingcloud.cli.iaas_client.actions.collaboration.describe_resource_user_groups import DescribeResourceUserGroupsAction


__all__ = [
    DescribeSharedResourceGroupsAction, DescribeResourceGroupsAction,
    CreateResourceGroupsAction, ModifyResourceGroupAttributesAction,
    DeleteResourceGroupsAction, DescribeResourceGroupItemsAction,
    AddResourceGroupItemsAction, DeleteResourceGroupItemsAction,
    DescribeUserGroupsAction, CreateUserGroupsAction,
    ModifyUserGroupAttributesAction, DeleteUserGroupsAction,
    DescribeUserGroupMembersAction, AddUserGroupMembersAction,
    ModifyUserGroupMemberAttributesAction, DeleteUserGroupMembersAction,
    DescribeGroupRolesAction, CreateGroupRolesAction,
    ModifyGroupRoleAttributesAction, DeleteGroupRolesAction,
    DescribeGroupRoleRulesAction, AddGroupRoleRulesAction,
    ModifyGroupRoleRuleAttributesAction, DeleteGroupRoleRulesAction,
    GrantResourceGroupsToUserGroupsAction, RevokeResourceGroupsFromUserGroupsAction,
    DescribeResourceUserGroupsAction
]
