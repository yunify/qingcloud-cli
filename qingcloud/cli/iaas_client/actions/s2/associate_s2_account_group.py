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
import json

from qingcloud.cli.iaas_client.actions.base import BaseAction

class AssociateS2AccountGroupAction(BaseAction):
    action = 'AssociateS2AccountGroup'
    command = 'associate-s2-account-group'
    usage = '%(prog)s -s <s2_group> -S <s2_accounts>  [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-s", "--s2-group", dest="s2_group",
                            action="store", type=str, default=None,
                            help="the ID of group.")

        parser.add_argument("-S", "--s2-accounts", dest="s2_accounts",
                            action="store", type=str, default=None,
                            help="the JSON form of accounts. e.g. '[{\"account_id\": \"s2a-xxxx\", \"rw_flag\": \"rw\"}]'")


    @classmethod
    def build_directive(cls, options):
        for key in ['s2_group', 's2_accounts']:
            if not hasattr(options, key):
                print("error: [%s] should be specified." % key)
                return None
        
        directive = {
            "s2_group": options.s2_group,
            "s2_accounts": json.loads(options.s2_accounts),
        }
        
        return directive
