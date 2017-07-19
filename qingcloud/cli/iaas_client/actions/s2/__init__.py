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
from qingcloud.cli.iaas_client.actions.s2.create_s2_server import CreateS2ServerAction
from qingcloud.cli.iaas_client.actions.s2.describe_s2_servers import DescribeS2ServersAction
from qingcloud.cli.iaas_client.actions.s2.modify_s2_server import ModifyS2ServerAttributesAction
from qingcloud.cli.iaas_client.actions.s2.resize_s2_servers import ResizeS2ServersAction
from qingcloud.cli.iaas_client.actions.s2.delete_s2_servers import DeleteS2ServersAction
from qingcloud.cli.iaas_client.actions.s2.poweron_s2_servers import PowerOnS2ServersAction
from qingcloud.cli.iaas_client.actions.s2.poweroff_s2_servers import PowerOffS2ServersAction
from qingcloud.cli.iaas_client.actions.s2.update_s2_servers import UpdateS2ServersAction
from qingcloud.cli.iaas_client.actions.s2.change_s2_server_vxnet import ChangeS2ServerVxnetAction
from qingcloud.cli.iaas_client.actions.s2.create_s2_shared_target import CreateS2SharedTargetAction
from qingcloud.cli.iaas_client.actions.s2.describe_s2_shared_targets import DescribeS2SharedTargetsAction
from qingcloud.cli.iaas_client.actions.s2.delete_s2_shared_targets import DeleteS2SharedTargetsAction
from qingcloud.cli.iaas_client.actions.s2.enable_s2_shared_targets import EnableS2SharedTargetsAction
from qingcloud.cli.iaas_client.actions.s2.disable_s2_shared_targets import DisableS2SharedTargetsAction
from qingcloud.cli.iaas_client.actions.s2.modify_s2_shared_target_attributes import ModifyS2SharedTargetAttributesAction
from qingcloud.cli.iaas_client.actions.s2.attach_to_s2_shared_target import AttachToS2SharedTargetAction
from qingcloud.cli.iaas_client.actions.s2.detach_from_s2_shared_target import DetachFromS2SharedTargetAction
from qingcloud.cli.iaas_client.actions.s2.describe_s2_default_parameters import DescribeS2DefaultParametersAction
from qingcloud.cli.iaas_client.actions.s2.create_s2_group import CreateS2GroupAction
from qingcloud.cli.iaas_client.actions.s2.describe_s2_groups import DescribeS2GroupsAction
from qingcloud.cli.iaas_client.actions.s2.modify_s2_group import ModifyS2GroupAction
from qingcloud.cli.iaas_client.actions.s2.delete_s2_group import DeleteS2GroupsAction
from qingcloud.cli.iaas_client.actions.s2.create_s2_account import CreateS2AccountAction
from qingcloud.cli.iaas_client.actions.s2.describe_s2_accounts import DescribeS2AccountsAction
from qingcloud.cli.iaas_client.actions.s2.modify_s2_account import ModifyS2AccountAction
from qingcloud.cli.iaas_client.actions.s2.delete_s2_accounts import DeleteS2AccountsAction
from qingcloud.cli.iaas_client.actions.s2.associate_s2_account_group import AssociateS2AccountGroupAction
from qingcloud.cli.iaas_client.actions.s2.dissociate_s2_account_group import DissociateS2AccountGroupAction


__all__ = [
    CreateS2ServerAction,
    DescribeS2ServersAction,
    ModifyS2ServerAttributesAction,
    ResizeS2ServersAction,
    DeleteS2ServersAction,
    PowerOnS2ServersAction,
    PowerOffS2ServersAction,
    UpdateS2ServersAction,
    ChangeS2ServerVxnetAction,
    CreateS2SharedTargetAction,
    DescribeS2SharedTargetsAction,
    DeleteS2SharedTargetsAction,
    EnableS2SharedTargetsAction,
    DisableS2SharedTargetsAction,
    ModifyS2SharedTargetAttributesAction,
    AttachToS2SharedTargetAction,
    DetachFromS2SharedTargetAction,
    DescribeS2DefaultParametersAction,
    CreateS2GroupAction,
    DescribeS2GroupsAction,
    ModifyS2GroupAction,
    DeleteS2GroupsAction,
    CreateS2AccountAction,
    DescribeS2AccountsAction,
    ModifyS2AccountAction,
    DeleteS2AccountsAction,
    AssociateS2AccountGroupAction,
    DissociateS2AccountGroupAction,
]
