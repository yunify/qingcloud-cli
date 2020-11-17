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


class ModifyBorderStaticAttributesAction(BaseAction):

    action = 'ModifyBorderStaticAttributes'
    command = 'modify_border_static_attributes'
    usage = '%(prog)s -s <border_static_id> [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-N', '--border_static_name',
                            dest='border_static_name',
                            action='store', type=str, default=None,
                            help='the name of border_static..')

        parser.add_argument('-s', '--border_static', dest='border_static',
                            action='store', type=str, default=None,
                            help='the ID of border_static whose attributes you want to update.')

        parser.add_argument("--val1", dest="val1",
                            action="store", type=str, default=None,
                            help='val1')

        parser.add_argument("--val2", dest="val2",
                            action="store", type=str, default=None,
                            help='val3')

        parser.add_argument("--val3", dest="val3",
                            action="store", type=str, default=None,
                            help='val1')

        parser.add_argument("-D", "--disabled", dest="disabled",
                            action="store", type=int, default=None,
                            help='disable a border static')

    @classmethod
    def build_directive(cls, options):

        required_params = {"border_static": options.border_static}
        for param in required_params:
            if required_params[param] is None or required_params[param] == "":
                print('error: [%s] should be specified' % param)
                return None

        return {"border_static": options.border_static,
                "border_static_name": options.border_static_name,
                "disabled": options.disabled,
                "val1": options.val1,
                "val2": options.val2,
                "val3": options.val3}

