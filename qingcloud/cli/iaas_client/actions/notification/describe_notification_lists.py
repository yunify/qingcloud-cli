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

from qingcloud.cli.misc.utils import explode_array


class DescribeNotificationListsAction(BaseAction):

    action = 'DescribeNotificationLists'
    command = 'describe-notification-lists'
    usage = '%(prog)s [-l --notification_lists...] [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument('-l', '--notification-lists', dest='notification_lists',
                            action='store', type=str, default=None,
                            help='an array including the IDs of the notification lists.')

        parser.add_argument('-s', '--search-word', dest='search_word',
                            action='store', type=str, default=None,
                            help=' the search word of notification list name.')

    @classmethod
    def build_directive(cls, options):
        directive = {
            'notification_lists': explode_array(options.notification_lists),
            'search_word': options.search_word,
            'offset': options.offset,
            'limit': options.limit
        }

        return directive
