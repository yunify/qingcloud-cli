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
import json


class CreateNotificationItemsAction(BaseAction):

    action = 'CreateNotificationItems'
    command = 'create-notification-items'
    usage = '%(prog)s [-i --notification-items...] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-i', '--notification-items', dest='notification_items',
                            action='store', type=str, default='',
                            help="A list of JSON Objects which contains 'content',\
                                 'notification_item_type' and 'remarks'. \
                                 'For Example:' \
                                 '[{'content':'xxxxxx@yunify.com','notification_item_type':'email','remarks':'qem'}]'.")

    @classmethod
    def build_directive(cls, options):
        if options.notification_items == '':
            print('error: notification_items should be specified.')
            return None

        directive = {
            "notification_items": json.loads(options.notification_items),
        }

        return directive
