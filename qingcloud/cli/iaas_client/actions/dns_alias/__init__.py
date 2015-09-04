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

from .describe_dns_aliases import DescribeDNSAliasesAction
from .associate_dns_alias import AssociateDNSAliasAction
from .dissociate_dns_aliases import DissociateDNSAliasesAction
from .get_dns_label import GetDNSLabelAction

__all__ = [GetDNSLabelAction, DescribeDNSAliasesAction,
        AssociateDNSAliasAction, DissociateDNSAliasesAction]
