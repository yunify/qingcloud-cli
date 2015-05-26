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

class DeleteSecurityGroupsAction(BaseAction):

    action = 'DeleteSecurityGroups'
    command = 'delete-security-groups'
    usage = '%(prog)s -s "security_group_id, ..." [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-s', '--security_groups', dest='security_groups',
                action='store', type=str, default='',
                help='the IDs of the security groups you want to delete.')
        
    @classmethod
    def build_directive(cls, options):
        security_groups = explode_array(options.security_groups)
        if not security_groups:
            print('[security_groups] should be specified.')
            return None
        
        return {
                'security_groups': security_groups
                }
