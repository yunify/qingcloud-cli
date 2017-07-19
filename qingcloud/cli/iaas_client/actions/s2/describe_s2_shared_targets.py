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

class DescribeS2SharedTargetsAction(BaseAction):
    action = 'DescribeS2SharedTargets'
    command = 'describe-s2-shared-targets'
    usage = '%(prog)s [-s <shared_targets> ...] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-s", "--shared-targets", dest="shared_targets",
                            action="store", type=str, default=None,
                            help="the IDs of shared targets.")

        parser.add_argument("-T", "--target-types", dest="target_types",
                            action="store", type=str, default=None,
                            help="valid values includes 'ISCSI', 'FCoE','NFS' and 'SMB'.")

        parser.add_argument("-S", "--s2-server-id", dest="s2_server_id",
                            action="store", type=str, default=None,
                            help="the ID of s2 server.")

        parser.add_argument("-n", "--export-name", dest="export_name",
                            action="store", type=str, default=None,
                            help="the name of shared target.")

        parser.add_argument("-w", "--search-word", dest="search_word",
                            action="store", type=str, default=None,
                            help="you may use this field to search from export_name or description.")

        parser.add_argument("-v", "--verbose", dest="verbose",
                            action="store", type=int, default=None,
                            help="the number to specify the verbose level, larger the number, the more detailed information will be returned.")


    @classmethod
    def build_directive(cls, options):
        directive = {
            "shared_targets": explode_array(options.shared_targets),
            "target_types": explode_array(options.target_types),
            "s2_server_id": options.s2_server_id,
            "export_name": options.export_name,
            "search_word": options.search_word,
            "verbose": options.verbose,
        }
        
        return directive
