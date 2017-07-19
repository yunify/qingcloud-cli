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

class ModifyS2AccountAction(BaseAction):
    action = 'ModifyS2Account'
    command = 'modify-s2-account'
    usage = '%(prog)s -s <s2_account> [-o <opt_parameters> ...] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-s", "--s2-account", dest="s2_account",
                            action="store", type=str, default=None,
                            help="the ID of account.")

        parser.add_argument("-o", "--opt-parameters", dest="opt_parameters",
                            action="store", type=str, default=None,
                            help="the options parameters.")

        parser.add_argument("-n", "--account-name", dest="account_name",
                            action="store", type=str, default=None,
                            help="the new value of account name.")

        parser.add_argument("-S", "--smb-passwd", dest="smb_passwd",
                            action="store", type=str, default=None,
                            help="the new password.")

        parser.add_argument("-N", "--nfs-ipaddr", dest="nfs_ipaddr",
                            action="store", type=str, default=None,
                            help="the new ip address.")

        parser.add_argument("-d", "--description", dest="description",
                            action="store", type=str, default=None,
                            help="the new value of description.")


    @classmethod
    def build_directive(cls, options):
        for key in ['s2_account']:
            if not hasattr(options, key):
                print("error: [%s] should be specified." % key)
                return None
        
        directive = {
            "s2_account": options.s2_account,
            "opt_parameters": options.opt_parameters,
            "account_name": options.account_name,
            "smb_passwd": options.smb_passwd,
            "nfs_ipaddr": options.nfs_ipaddr,
            "description": options.description,
        }
        
        return directive
