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
from qingcloud.cli.misc.utils import explode_array

from qingcloud.cli.iaas_client.actions.base import BaseAction


class DeleteResourceGroupsAction(BaseAction):
    action = 'DeleteResourceGroups'
    command = 'delete-resource-groups'
    usage = '%(prog)s [-r <resource_groups>] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-r", "--resource-groups", dest="resource_groups",
                            action="store", type=str, default='',
                            help=" An array including IDs of the resource groups which you want to delete.")

    @classmethod
    def build_directive(cls, options):
        resource_groups = explode_array(options.resource_groups)
        if not resource_groups:
            print('error: resource_groups should be specified')
            return None

        directive = {
            "resource_groups": resource_groups,
        }

        return directive
