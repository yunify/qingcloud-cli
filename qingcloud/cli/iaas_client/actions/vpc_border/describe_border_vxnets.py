# =========================================================================
# Copyright 2012-present Yunify, Inc.
# -------------------------------------------------------------------------
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this work except in compliance with the License.
# You may obtain a copy of the License in the LICENSE file, or at:
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========================================================================

from qingcloud.cli.iaas_client.actions.base import BaseAction


class DescribeBorderVxnetsAction(BaseAction):

    action = 'DescribeBorderVxnets'
    command = 'describe_border_vxnets'
    usage = '%(prog)s [-b "border_id, ..."] [-o <owner>] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-b', '--border', dest='border',
                            action='store', type=str, default=None,
                            help='filter by border.')

        parser.add_argument('-v', '--vxnet', dest='border_statics',
                            action='store', type=str, default=None,
                            help='filter by vxnet ID.')

        parser.add_argument("-o", "--owner",  dest="owner",
                            action="store", type=str, default=None,
                            help='''filter by owner.''')

    @classmethod
    def build_directive(cls, options):
        return {"border": options.border,
                "vxnet": options.vxnet,
                "owner": options.owner,
                "offset": options.offset,
                "limit": options.limit}
