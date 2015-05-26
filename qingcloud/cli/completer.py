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

import sys

from .iaas_client.actions import ActionManager


def return_choices(choices):
    print('\n'.join(choices))
    sys.exit(0)


def return_no_choices():
    sys.exit(0)


def complete(cmdline, point):
    service_names = ('iaas',)
    action_names = ActionManager.action_table.keys()

    service_name = None
    action_name = None
    words = cmdline[0:point].split()
    if not words:
        return
    current_word = words[-1]

    # First find all non-options words in command line
    non_options = [w for w in words if not w.startswith('-')]

    # Look for service name and action name in non_options
    for w in non_options:
        if w in service_names:
            service_name = w
        elif w in action_names:
            action_name = w

    # If we found service name, complete the action name
    if service_name:
        if current_word != service_name:
            action_names = [act for act in action_names if act.startswith(current_word)]
            if action_name and len(action_names) == 1:
                return_no_choices()
        return_choices(action_names)
    else:
        return_choices(service_names)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        complete(sys.argv[1], int(sys.argv[2]))
    else:
        print('usage: %s <cmdline> <point>' % sys.argv[0])
