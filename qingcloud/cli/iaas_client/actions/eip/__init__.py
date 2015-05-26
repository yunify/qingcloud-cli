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

from .allocate_eips import AllocateEipsAction
from .release_eips import ReleaseEipsAction
from .associate_eip import AssociateEipAction
from .change_eips_bandwidth import ChangeEipsBandwidthAction
from .change_eips_billing_mode import ChangeEipsBillingModeAction
from .describe_eips import DescribeEipsAction
from .dissociate_eips import DissociateEipsAction
from .modify_eip_attributes import ModifyEipAttributesAction

__all__ = [AllocateEipsAction, ReleaseEipsAction, AssociateEipAction,
        ChangeEipsBandwidthAction, ChangeEipsBillingModeAction,
        DescribeEipsAction, DissociateEipsAction, ModifyEipAttributesAction]
