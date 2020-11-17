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

from qingcloud.cli.misc.utils import explode_array
from qingcloud.cli.iaas_client.actions.base import BaseAction


class DescribeBorderStaticsAction(BaseAction):

    action = 'DescribeBorderStatics'
    command = 'describe_border_statics'
    usage = '%(prog)s [-s "border_static_id, ..."] [-o <owner>] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-b', '--border', dest='border',
                            action='store', type=str, default=None,
                            help='filter by owner.')

        parser.add_argument('-s', '--border_statics', dest='border_statics',
                            action='store', type=str, default='',
                            help='the comma separated IDs of border_statics you want to list.')

        parser.add_argument("-t", "--static_type", dest="static_type",
                            action="store", type=str, default=None,
                            help='''the comma separated type of static. 0: route.''')

        parser.add_argument("-o", "--owner",  dest="owner",
                            action="store", type=str, default=None,
                            help='''filter by owner.''')

        parser.add_argument("-V", "--verbose", dest="verbose",
                            action="store", type=int, default=0,
                            help="the number to specify the verbose level, "
                                 "larger the number, the more detailed information will be returned.")

    @classmethod
    def build_directive(cls, options):
        directive = {"border_statics": explode_array(options.border_statics),
                     "border": options.border,
                     "owner": options.owner,
                     "offset": options.offset,
                     "limit": options.limit,
                     "verbose": options.verbose}
        if options.static_type is not None:
            directive.update(
                {"static_type": explode_array(options.static_type)})
        return directive
