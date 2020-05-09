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


class DescribeWanAccesssAction(BaseAction):

    action = 'DescribeWanAccesss'
    command = 'describe-wan-accesss'
    usage = '%(prog)s [-a "wan_access_id, ..."] [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-a', '--wan_accesss', dest='wan_accesss',
                            action='store', type=str, default=None,
                            help='the comma separated IDs of wan_accesss you want to list.')

        parser.add_argument('-n', '--wan_access_name', dest='wan_access_name',
                            action="store", type=str,  default=None,
                            help='the name of wan_access you want to list.')

        parser.add_argument('-N', '--wan_nets', dest='wan_nets',
                            action="store", type=str, default=None,
                            help='the comma separated IDs of wan_nets you want to list.')

        parser.add_argument('-P', '--wan_pops', dest='wan_pops',
                            action="store", type=str, default=None,
                            help='the comma separated IDs of wan_pops you want to list.')

        parser.add_argument('-s', '--status', dest='status',
                            action="store", type=str, default=None,
                            help='status of the wan_access.')

        parser.add_argument('-t', '--access_type', dest='access_type',
                            action="store", type=str, default=None,
                            help='The access type. eg: line, vpc, cpe.')

        parser.add_argument('--location_nation', dest='location_nation',
                            action="store", type=str, default=None,
                            help='The nation of access location.')

        parser.add_argument('--location_province', dest='location_province',
                            action="store", type=str, default=None,
                            help='The province of access location.')

        parser.add_argument('--location_city', dest='location_city',
                            action="store", type=str, default=None,
                            help='The city of access location.')

        parser.add_argument('-o', '--owner', dest='owner',
                            action="store", type=str, default=None,
                            help='the owner IDs of resource.')

        parser.add_argument('--search_word', dest='search_word',
                            action="store", type=str, default=None,
                            help='the search_word of resource.')

        parser.add_argument('-V', '--verbose', dest='verbose',
                            action="store", type=int, default=0,
                            help='the number to specify the verbose level, larger the number, '
                                 'the more detailed information will be returned.')

    @classmethod
    def build_directive(cls, options):
        directive = {"verbose": options.verbose}

        if options.wan_accesss is not None:
            directive['wan_accesss'] = explode_array(options.wan_accesss)
        if options.wan_access_name is not None:
            directive['wan_access_name'] = options.wan_access_name
        if options.wan_nets is not None:
            directive['wan_nets'] = explode_array(options.wan_nets)
        if options.wan_pops is not None:
            directive['wan_pops'] = explode_array(options.wan_pops)
        if options.status is not None:
            directive['status'] = explode_array(options.status)
        if options.access_type is not None:
            directive['access_type'] = explode_array(options.access_type)
        if options.location_nation is not None:
            directive['location_nation'] = options.location_nation
        if options.location_province is not None:
            directive['location_province'] = options.location_province
        if options.location_city is not None:
            directive['location_city'] = options.location_city
        if options.owner is not None:
            directive['owner'] = explode_array(options.owner)
        if options.search_word is not None:
            directive['search_word'] = options.search_word

        return directive
