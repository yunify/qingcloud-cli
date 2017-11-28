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


class DescribeNotificationItemsAction(BaseAction):

    action = 'DescribeNotificationItems'
    command = 'describe-notification-items'
    usage = '%(prog)s [-i --notification_items...] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-i', '--notification-items', dest='notification_items',
                            action='store', type=str, default=None,
                            help='An array including IDs of notification items.')

        parser.add_argument('-l', '--notification-list', dest='notification_list',
                            action='store', type=str, default=None,
                            help='The ID of notification list.')

        parser.add_argument('-t', '--notification-item-type', dest='notification_item_type',
                            action='store', type=str, default=None,
                            help='The type of notification item, including email, phone and webhook.')

    @classmethod
    def build_directive(cls, options):
        directive = {
            "notification_items": options.notification_items,
            "notification_list": options.notification_list,
            "notification_item_type": options.notification_item_type
        }

        return directive
