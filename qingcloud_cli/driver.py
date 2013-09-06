# coding: utf-8

import argparse
import sys
#from difflib import get_close_matches

from qingcloud_cli.iaas_client.actions import ActionManager

SERVICES = ('iaas')

parser = argparse.ArgumentParser(
    prog = 'qingcloud',
    usage = '''%(prog)s iaas <action> [parameters]

    Here are valid actions:
    ## instance
    run-instances, start-instances, stop-instances
    ''',
)

def exit_due_to_invalid_args():
    parser.print_help()
    sys.exit(-1)

def check_argument(args):
    if len(args) < 3:
        exit_due_to_invalid_args()
    if args[1] not in SERVICES or args[2] not in ActionManager.action_table():
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
