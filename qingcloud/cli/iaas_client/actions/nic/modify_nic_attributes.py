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

class ModifyNicAttributesAction(BaseAction):

    action = 'ModifyNicAttributes'
    command = 'modify-nic-attributes'
    usage = '%(prog)s -v nic_id [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):

        parser.add_argument('-n', '--nic', dest='nic',
                            action='store', type=str, default='',
                            help='the id of the nic whose attributes you want to modify.')

        parser.add_argument('-N', '--nic-name', dest='nic_name',
                            action='store', type=str, default=None,
                            help='specify the new nic name.')

        parser.add_argument('-p', '--private-ip', dest='private_ip',
                            action='store', type=str, default=None,
                            help='the new private ip of nic.')

    @classmethod
    def build_directive(cls, options):
        if not options.nic:
            print('error: [nic] should be specified')
            return None

        return {
            'nic': options.nic,
            'nic_name': options.nic_name,
            'private_ip': options.private_ip,
        }
