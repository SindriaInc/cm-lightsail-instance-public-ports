#!/usr/bin/env python3

import subprocess
import os
import helpers
import json


# Pycharm pydevd
PYCHARM_PYDEVD_ENABLED = int(os.getenv('PYCHARM_PYDEVD_ENABLED'))
PYCHARM_PYDEVD_HOST = str(os.getenv('PYCHARM_PYDEVD_HOST'))
PYCHARM_PYDEVD_PORT = int(os.getenv('PYCHARM_PYDEVD_PORT'))

# Enable pydevd debugger
if (PYCHARM_PYDEVD_ENABLED):
    import pydevd_pycharm
    pydevd_pycharm.settrace(PYCHARM_PYDEVD_HOST, port=PYCHARM_PYDEVD_PORT, stdoutToServer=True, stderrToServer=True)


# Get all rules of instance - return dict
def get_instance_rules(name):
    stdout = subprocess.check_output(['aws', 'lightsail', 'get-instance-port-states', '--instance-name', name], universal_newlines=True)
    data = json.loads(stdout)
    return data


def process_rules(instance, current_rules):
    pass


def process_instance(instance):
    subprocess.call(['aws', 'lightsail', 'open-instance-public-ports', '--instance-name', instance['name'], '--port-info', instance['rule']])


# Main
def main():
    data = helpers.app()

    # Process lightsail instances
    for k,instance in data['lightsail'].items():
        current_rules = get_instance_rules(instance['name'])
        process_rules(instance, current_rules)



        print(current_rules)

        #print("test")
        #process_instance(instance)

# Execute
if __name__ == '__main__':
    main()