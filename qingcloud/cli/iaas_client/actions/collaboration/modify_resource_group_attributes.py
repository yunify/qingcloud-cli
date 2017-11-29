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


class ModifyResourceGroupAttributesAction(BaseAction):
    action = 'ModifyResourceGroupAttributes'
    command = 'modify-resource-group-attributes'
    usage = '%(prog)s [-r <resource_group>] [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-r", "--resource-group", dest="resource_group",
                            action="store", type=str, default='',
                            help="The ID of resource group which attributes you want to modify.")

        parser.add_argument("-n", "--resource-group-name", dest="resource_group_name",
                            action="store", type=str, default=None,
                            help="The new name of the resource group which will be modified.")

        parser.add_argument("-d", "--description", dest="description",
                            action="store", type=str, default=None,
                            help="The description of the resource group.")

    @classmethod
    def build_directive(cls, options):
        if options.resource_group == '':
            print('error: resource_group should be specified')
            return None

        directive = {
            "resource_group": options.resource_group,
            "description": options.description,
            "resource_group_name": options.resource_group_name,
        }

        return directive
