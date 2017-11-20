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


class GetLeaseInfoAction(BaseAction):
    action = 'GetLeaseInfo'
    command = 'get-lease-info'
    usage = '%(prog)s -r <resource> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument("-r", "--resource", dest="resource",
                            action="store", type=str, default='',
                            help="the ID of resource which lease info you want to get.")

        parser.add_argument("-u", "--user", dest="user",
                            action="store", type=str, default=None,
                            help="the ID of user.")

    @classmethod
    def build_directive(cls, options):

        if options.resource == '':
            print('error: resource should be specified.')
            return None

        directive = {
            "resource": options.resource,
            "user": options.user,
        }

        return directive
