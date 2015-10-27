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

class ModifyTagAttributesAction(BaseAction):

    action = 'ModifyTagAttributes'
    command = 'modify-tag-attributes'
    usage = '%(prog)s -t <tag> [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-t', '--tag', dest='tag',
                            action='store', type=str, default='',
                            help='the id of the tag whose attributes you want to modify.')

        parser.add_argument('-N', '--tag_name', dest='tag_name',
                            action='store', type=str, default=None,
                            help='specify the new tag name.')

        parser.add_argument('-D', '--description', dest='description',
                            action='store', type=str, default=None,
                            help='the detailed description of the resource')

    @classmethod
    def build_directive(cls, options):
        if not options.tag:
            return None

        return {'tag': options.tag,
                'tag_name': options.tag_name,
                'description': options.description, }
