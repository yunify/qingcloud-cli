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

class CreateTagAction(BaseAction):

    action = 'CreateTag'
    command = 'create-tag'
    usage = '%(prog)s --tag_name <keypair_name> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-N', '--tag_name', dest='tag_name',
                            action='store', type=str, default=None,
                            help='name of the tag.')

    @classmethod
    def build_directive(cls, options):
        required_params = {'tag_name': options.tag_name}
        for param in required_params:
            if required_params[param] is None or required_params[param] == '':
                print('param [%s] should be specified' % param)
                return None

        return {'tag_name': options.tag_name}
