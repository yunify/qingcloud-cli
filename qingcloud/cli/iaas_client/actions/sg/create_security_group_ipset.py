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

class CreateSecurityGroupIPSetAction(BaseAction):

    action = 'CreateSecurityGroupIPSet'
    command = 'create-security-group-ipset'
    usage = '%(prog)s --security_group_ipset_name <security_group_ipset_name> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-N', '--security_group_ipset_name', dest='security_group_ipset_name',
                action='store', type=str, default='',
                help='short name for the security group ipset you want to create.')

        parser.add_argument('-T', '--ipset_type', dest='ipset_type',
                action='store', type=int, default=0,
                help='type of the security group ipset you want to create, 0 is IP, 1 is port.')

        parser.add_argument('-V', '--val', dest='val',
                action='store', type=str, default='',
                help='value of this ipset, such as: 192.168.1.0/24 or 10000-15000.')

        parser.add_argument('-u', '--target-user', dest='target_user',
                            action='store', type=str, default=None,
                            help='the ID of user who will own this resource.')

    @classmethod
    def build_directive(cls, options):
        required_params = {
                'security_group_ipset_name': options.security_group_ipset_name,
                'ipset_type': options.ipset_type,
                'val': options.val,
                }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('param [%s] should be specified' % param)
                return None

        if options.target_user:
            required_params['target_user'] = options.target_user

        return required_params
