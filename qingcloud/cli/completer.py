import sys

from .iaas_client.actions import ActionManager


def return_choices(choices):
    print('\n'.join(choices))
    sys.exit(0)


def return_no_choices():
    sys.exit(0)


def complete(cmdline, point):
    service_names = ('iaas',)
    action_names = ActionManager.action_table().keys()

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
        if action_name:
            # TODO: complete action's argument
            return_no_choices()
        elif current_word != service_name:
            action_names = [act for act in action_names if act.startswith(current_word)]
        return_choices(action_names)
    else:
        return_choices(service_names)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        complete(sys.argv[1], int(sys.argv[2]))
    else:
        print('usage: %s <cmdline> <point>' % sys.argv[0])
