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
import argparse
import pkg_resources
from difflib import get_close_matches

from .iaas_client.actions import ActionManager as IaaSActionManager
from .qs_client.actions import ActionManager as QSActionManager

SERVICES = ('iaas', 'qs')

INDENT = ' ' * 2
NEWLINE = '\n' + INDENT

def exit_due_to_invalid_service(suggest_services=None):
    usage = NEWLINE + '%(prog)s <service> <action> [parameters]\n\n' \
                + 'Here are valid services:\n\n' \
                + INDENT + NEWLINE.join(SERVICES)

    if suggest_services:
        usage += '\n\nInvalid service, maybe you meant:' \
                + ','.join(suggest_services)

    parser = argparse.ArgumentParser(
        prog = 'qingcloud',
        usage = usage,
    )
    parser.print_help()
    sys.exit(-1)

def exit_due_to_invalid_action(service, suggest_actions=None):
    usage = NEWLINE + '%(prog)s <action> [parameters]\n\n' \
                + 'Here are valid actions:\n\n' \
                + INDENT + NEWLINE.join(get_valid_actions(service))

    if suggest_actions:
        usage += '\n\nInvalid action, maybe you meant:\n' \
                + NEWLINE.join(suggest_actions)

    parser = argparse.ArgumentParser(
        prog = 'qingcloud %s' % service,
        usage = usage,
    )
    parser.print_help()
    sys.exit(-1)

def get_valid_actions(service):
    if service == 'iaas':
        return IaaSActionManager.get_valid_actions()
    elif service == 'qs':
        return QSActionManager.get_valid_actions()

def get_action(service, action):
    if service == 'iaas':
        return IaaSActionManager.get_action(action)
    elif service == 'qs':
        return QSActionManager.get_action(action)

def check_argument(args):

    if len(args) < 2:
        exit_due_to_invalid_service()

    if args[1].lower() in ('--version', '-v'):
        version = pkg_resources.require("qingcloud-cli")[0].version
        print('qingcloud-cli version %s' % version)
        sys.exit(0)

    service = args[1]

    if service not in SERVICES:
        suggest_services = get_close_matches(service, SERVICES)
        exit_due_to_invalid_service(suggest_services)

    if len(args) < 3:
        exit_due_to_invalid_action(service)

    valid_actions = get_valid_actions(service)
    if args[2] not in valid_actions:
        suggest_actions = get_close_matches(args[2], valid_actions)
        exit_due_to_invalid_action(service, suggest_actions)

def main():
    args = sys.argv
    check_argument(args)
    action = get_action(args[1], args[2])
    action.main(args[3:])
