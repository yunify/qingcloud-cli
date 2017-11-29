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


class VerifyNotificationItemAction(BaseAction):

    action = 'VerifyNotificationItem'
    command = 'verify-notification-item'
    usage = '%(prog)s [-c --notification_item_content...] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-c', '--notification-item-content', dest='notification_item_content',
                            action='store', type=str, default='',
                            help='The content of notification item which will be verified.')

        parser.add_argument('-v', '--verification-code', dest='verification_code',
                            action='store', type=str, default='',
                            help='The verification code.')

    @classmethod
    def build_directive(cls, options):
        if options.notification_item_content == '':
            print('error: notification_item_content should be specified.')
            return None
        if options.verification_code == '':
            print('error: verification_code should be specified.')
            return None

        directive = {
            "notification_item_content": options.notification_item_content,
            "verification_code": options.verification_code,
        }

        return directive
