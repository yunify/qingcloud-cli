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

class DescribeS2GroupsAction(BaseAction):
    action = 'DescribeS2Groups'
    command = 'describe-s2-groups'
    usage = '%(prog)s [-s <s2_groups> ...] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-s", "--s2-groups", dest="s2_groups",
                            action="store", type=str, default=None,
                            help="the IDs of s2 groups.")

        parser.add_argument("-T", "--group-types", dest="group_types",
                            action="store", type=str, default=None,
                            help="valid values is NFS_GROUP or SMB_GROUP.")

        parser.add_argument("-n", "--group-name", dest="group_name",
                            action="store", type=str, default=None,
                            help="the name of group.")

        parser.add_argument("-S", "--search-word", dest="search_word",
                            action="store", type=str, default=None,
                            help="you may use this field to search from id or name.")

        parser.add_argument("-v", "--verbose", dest="verbose",
                            action="store", type=int, default=None,
                            help="the number to specify the verbose level, larger the number, the more detailed information will be returned.")


    @classmethod
    def build_directive(cls, options):
        directive = {
            "s2_groups": explode_array(options.s2_groups),
            "group_types": explode_array(options.group_types),
            "group_name": options.group_name,
            "search_word": options.search_word,
            "verbose": options.verbose,
        }
        
        return directive
