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


class CreateNotificationListAction(BaseAction):

    action = 'CreateNotificationList'
    command = 'create-notification-list'
    usage = '%(prog)s [-n --notification_list_name...] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-n', '--notification-list-name', dest='notification_list_name',
                            action='store', type=str, default='',
                            help='the name of the notification list.')

        parser.add_argument('-i', '--notification-items', dest='notification_items',
                            action='store', type=str, default='',
                            help='an array including IDs of the notification items.')

    @classmethod
    def build_directive(cls, options):

        if options.notification_list_name == '':
            print('error: notification_list_name should be specified.')
            return None
        notification_items = explode_array(options.notification_items)
        if not notification_items:
            print('error: notification_items should be specified.')
            return None

        directive = {
            "notification_list_name": options.notification_list_name,
            "notification_items": notification_items,
        }

        return directive
