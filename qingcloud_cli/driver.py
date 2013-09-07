# coding: utf-8

import argparse
import sys

from qingcloud_cli.iaas_client.actions import ActionManager

SERVICES = ('iaas')
valid_actions = ActionManager.action_table().keys()
valid_actions.sort()

def exit_due_to_invalid_args():
    usage = '%(prog)s iaas <action> [parameters]\n\nHere are valid actions:\n\n'
    usage += '\n'.join(valid_actions)
    parser = argparse.ArgumentParser(
        prog = 'qingcloud',
        usage = usage,
    )
    parser.print_help()
    sys.exit(-1)

def check_argument(args):
    if len(args) < 3:
        exit_due_to_invalid_args()
    if args[1] not in SERVICES or args[2] not in valid_actions:
        exit_due_to_invalid_args()

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
