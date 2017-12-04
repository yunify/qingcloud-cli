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
from qingcloud.cli.iaas_client.actions.base import BaseAction


class CreateResourceGroupsAction(BaseAction):
    action = 'CreateResourceGroups'
    command = 'create-resource-groups'
    usage = '%(prog)s [-n <resource_group_name> ...] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-n", "--resource-group-name", dest="resource_group_name",
                            action="store", type=str, default=None,
                            help="the name of resource groups.")

        parser.add_argument("-d", "--description", dest="description",
                            action="store", type=str, default=None,
                            help="the description of resource groups.")

        parser.add_argument("-c", "--count", dest="count",
                            action="store", type=int, default=1,
                            help="the number of resource groups created at one time.")

    @classmethod
    def build_directive(cls, options):
        directive = {
            "resource_group_name": options.resource_group_name,
            "description": options.description,
            "count": options.count,
        }

        return directive
