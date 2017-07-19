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

class CreateS2GroupAction(BaseAction):
    action = 'CreateS2Group'
    command = 'create-s2-group'
    usage = '%(prog)s -T <group_type> [-n <group_name> ...] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-T", "--group-type", dest="group_type",
                            action="store", type=str, default=None,
                            help="valid values is NFS_GROUP or SMB_GROUP.")

        parser.add_argument("-n", "--group-name", dest="group_name",
                            action="store", type=str, default=None,
                            help="the name of group.")

        parser.add_argument("-s", "--s2-accounts", dest="s2_accounts",
                            action="store", type=str, default=None,
                            help="the IDs of s2 accounts.")

        parser.add_argument("-d", "--description", dest="description",
                            action="store", type=str, default=None,
                            help="the detailed description of the resource.")


    @classmethod
    def build_directive(cls, options):
        for key in ['group_type']:
            if not hasattr(options, key):
                print("error: [%s] should be specified." % key)
                return None
        
        directive = {
            "group_type": options.group_type,
            "group_name": options.group_name,
            "s2_accounts": options.s2_accounts,
            "description": options.description,
        }
        
        return directive
