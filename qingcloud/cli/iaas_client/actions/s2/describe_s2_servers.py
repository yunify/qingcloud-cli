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

class DescribeS2ServersAction(BaseAction):
    action = 'DescribeS2Servers'
    command = 'describe-s2-servers'
    usage = '%(prog)s [-s <s2_servers> ...] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-s", "--s2-servers", dest="s2_servers",
                            action="store", type=str, default=None,
                            help="the IDs of s2 server you want to describe.")

        parser.add_argument("-T", "--service-types", dest="service_types",
                            action="store", type=str, default=None,
                            help="the type of service, valid value is 'vsan' or 'vnas'.")

        parser.add_argument("-S", "--status", dest="status",
                            action="store", type=str, default=None,
                            help="valid values include pending, active, poweroffed, suspended, deleted, ceased.")

        parser.add_argument("-w", "--search-word", dest="search_word",
                            action="store", type=str, default=None,
                            help="you may use this field to search from id, name and description.")

        parser.add_argument("-t", "--tags", dest="tags",
                            action="store", type=str, default=None,
                            help="the array of IDs of tags.")

        parser.add_argument("-v", "--verbose", dest="verbose",
                            action="store", type=int, default=None,
                            help="the number to specify the verbose level, larger the number, the more detailed information will be returned.")


    @classmethod
    def build_directive(cls, options):
        directive = {
            "s2_servers": explode_array(options.s2_servers),
            "service_types": explode_array(options.service_types),
            "status": explode_array(options.status),
            "search_word": options.search_word,
            "tags": explode_array(options.tags),
            "verbose": options.verbose,
        }
        
        return directive
