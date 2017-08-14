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

class ApplySecurityGroupAction(BaseAction):

    action = 'ApplySecurityGroup'
    command = 'apply-security-group'
    usage = '%(prog)s -s <security_group_id> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        
        parser.add_argument('-s', '--security_group_id', dest='security_group_id',
                action='store', type=str, default='',
                help='ID of the security group you want to apply to instances.')

        parser.add_argument('-i', '--instances', dest='instances',
                action='store', type=str, default='',
                help='the comma-separated IDs of instances you want to apply the security group to.')

        parser.add_argument('-u', '--target-user', dest='target_user',
                            action='store', type=str, default=None,
                            help='the ID of user who will own this resource.')
      
    @classmethod
    def build_directive(cls, options):
        required_params = {'security_group_id': options.security_group_id} 
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('error: [%s] should be specified' % param)
                return None
        
        return {
                'security_group': options.security_group_id,
                'instances': explode_array(options.instances),
                'target_user': options.target_user,
                }
