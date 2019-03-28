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


class CreateInstanceGroupsAction(BaseAction):

    action = 'CreateInstanceGroups'
    command = 'create-instance-groups'
    usage = '%(prog)s --relation <relation> --name <name> [options] [-f <config_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-r', '--relation', dest='relation',
                            action='store', type=str,
                             help='relation between instances.')

        parser.add_argument('-n', '--name', dest='instance_group_name',
                            action='store', type=str,
                            help='the name of group.')

        parser.add_argument('-d', '--description', dest='description',
                            action='store', type=str,
                            help='the description of group')
        return parser

    @classmethod
    def build_directive(cls, options):

        required_params = {
            'relation': options.relation
        }
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('error: [%s] should be specified' % param)
                return None

        return {
            'relation': options.relation,
            'instance_group_name': options.instance_group_name,
            'description': options.description
        }
