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


class ModifyNotificationListAttributesAction(BaseAction):

    action = 'ModifyNotificationListAttributes'
    command = 'modify-notification-list-attributes'
    usage = '%(prog)s [-l --notification_list] [options] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-l', '--notification-list', dest='notification_list',
                            action='store', type=str, default='',
                            help='The ID of notification list which attributes you want to modify.')

        parser.add_argument('-n', '--notification-list-name', dest='notification_list_name',
                            action='store', type=str, default=None,
                            help='The new name of the notification list which will be modified.')

        parser.add_argument('-i', '--notification-items', dest='notification_items',
                            action='store', type=str, default=None,
                            help=' An array including IDs of notification items.')

    @classmethod
    def build_directive(cls, options):
        if options.notification_list == '':
            print('error: notification_list_id should be specified.')
            return None

        directive = {
            'notification_list': options.notification_list,
            'notification_list_name': options.notification_list_name,
            'notification_items': explode_array(options.notification_items)
        }

        return directive
