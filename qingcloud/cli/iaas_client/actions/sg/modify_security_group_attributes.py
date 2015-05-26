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

class ModifySecurityGroupAttributesAction(BaseAction):

    action = 'ModifySecurityGroupAttributes'
    command = 'modify-security-group-attributes'
    usage = '%(prog)s -s <security_group_id> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-s', '--security_group_id', dest='security_group_id',
                action='store', type=str, default='',
                help='the ID of the security group you want to update its content.')

        parser.add_argument('-N', '--security_group_name', dest='security_group_name',
                action='store', type=str, default=None,
                help='the new name for the security group you want to update.')

        parser.add_argument('-D', '--description', dest='description',
                action='store', type=str, default=None,
                help='the detailed description of the resource')

    @classmethod
    def build_directive(cls, options):
        required_params = {
                'security_group_id': options.security_group_id,
                }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('param [%s] should be specified' % param)
                return None

        return {
                'security_group': options.security_group_id,
                'security_group_name': options.security_group_name,
                'description': options.description,
                }
