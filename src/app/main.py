#!/usr/bin/env python3

import os

import helpers
import service


# Pycharm pydevd
PYCHARM_PYDEVD_ENABLED = int(os.getenv('PYCHARM_PYDEVD_ENABLED'))
PYCHARM_PYDEVD_HOST = str(os.getenv('PYCHARM_PYDEVD_HOST'))
PYCHARM_PYDEVD_PORT = int(os.getenv('PYCHARM_PYDEVD_PORT'))

# Enable pydevd debugger
if (PYCHARM_PYDEVD_ENABLED):
    import pydevd_pycharm
    pydevd_pycharm.settrace(PYCHARM_PYDEVD_HOST, port=PYCHARM_PYDEVD_PORT, stdoutToServer=True, stderrToServer=True)


def process_rules(name, rules):
    print("X")
    for rule in rules:
        if (service.find_rule(name, rule)):
            service.delete_rule(name, rule)


def process_instance(instance):
    pass


# Main
def main():
    data = helpers.app()

    # Process lightsail instances
    for k,instance in data['lightsail'].items():
        process_rules(instance['name'], instance['rules'])


# Execute
if __name__ == '__main__':
    main()