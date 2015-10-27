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

class AttachTagsAction(BaseAction):

    action = 'AttachTags'
    command = 'attach-tags'
    usage = '%(prog)s --resource_tag_pairs "tag_id1:resource_type1:resource_id1;tag_id2:resource_type2:resource_id2..." [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-p', '--resource_tag_pairs', dest='resource_tag_pairs',
                            action='store', type=str, default='',
                            help='tag_id1:resource_type1:resource_id1;tag_id2:resource_type2:resource_id2...')

    @classmethod
    def build_directive(cls, options):
        resource_tag_pairs = explode_array(options.resource_tag_pairs, ";")

        for i, p in enumerate(resource_tag_pairs):
            tag_id, resource_type, resource_id = explode_array(p, ":")
            resource_tag_pairs[i] = {"tag_id": tag_id,
                                     "resource_type": resource_type,
                                     "resource_id": resource_id}

        directive = {"resource_tag_pairs": resource_tag_pairs}
        return directive
