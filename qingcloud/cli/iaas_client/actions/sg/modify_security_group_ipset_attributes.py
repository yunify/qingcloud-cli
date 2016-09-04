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

class ModifySecurityGroupIPSetAttributesAction(BaseAction):

    action = 'ModifySecurityGroupIPSetAttributes'
    command = 'modify-security-group-ipset-attributes'
    usage = '%(prog)s -s <security_group_ipset_id> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-s', '--security_group_ipset_id', dest='security_group_ipset_id',
                action='store', type=str, default='',
                help='the ID of the security group ipset you want to update its content.')

        parser.add_argument('-N', '--security_group_ipset_name', dest='security_group_ipset_name',
                action='store', type=str, default=None,
                help='the new name for the security group ipset you want to update.')

        parser.add_argument('-D', '--description', dest='description',
                action='store', type=str, default=None,
                help='the detailed description of the resource')

        parser.add_argument('-V', '--val', dest='val',
                action='store', type=str, default=None,
                help='the val of the resource, such as 192.168.1.0/24 or 10000-15000')


    @classmethod
    def build_directive(cls, options):
        required_params = {
                'security_group_ipset_id': options.security_group_ipset_id,
                }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('param [%s] should be specified' % param)
                return None

        return {
                'security_group_ipset': options.security_group_ipset_id,
                'security_group_ipset_name': options.security_group_ipset_name,
                'val': options.val,
                'description': options.description,
                }
