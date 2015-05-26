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

import argparse
import sys
from difflib import get_close_matches

from .iaas_client.actions import ActionManager

SERVICES = ('iaas')
valid_actions = list(ActionManager.action_table.keys())
valid_actions.sort()

INDENT = ' ' * 2
NEWLINE = '\n' + INDENT

def exit_due_to_invalid_args(suggest_actions=None):
    usage = NEWLINE + '%(prog)s iaas <action> [parameters]\n\nHere are valid actions:\n\n'
    usage += INDENT + NEWLINE.join(valid_actions)
    if suggest_actions:
        usage += '\n\nInvalid action, maybe you meant:\n'
        usage += NEWLINE.join(suggest_actions)

    parser = argparse.ArgumentParser(
        prog = 'qingcloud',
        usage = usage,
    )
    parser.print_help()
    sys.exit(-1)

def check_argument(args):
    if len(args) < 3:
        exit_due_to_invalid_args()
    if args[1] not in SERVICES:
        exit_due_to_invalid_args()
    if args[2].lower() in ('--version', '-v'):
        import pkg_resources
        version = pkg_resources.require("qingcloud-cli")[0].version
        print('qingcloud-cli %s' % version)
        sys.exit(0)
    if args[2] not in valid_actions:
        suggest_actions = get_close_matches(args[2], valid_actions)
        exit_due_to_invalid_args(suggest_actions)

def get_action(service, action):
    if service == 'iaas':
        return ActionManager.get_action(action)
    exit_due_to_invalid_args()

def main():
    args = sys.argv
    check_argument(args)

    service = args[1]
    action = get_action(service, args[2])
    action.main(args[3:])
