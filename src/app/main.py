#!/usr/bin/env python3

import subprocess
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


# Check if entry rule already exists - return boolean
def check_entry_rule(entry, port):
    if (entry['fromPort'] == port):
        return True
    return False


def process_rules(rules, current_rules):

    print("X")
    #print(current_rules)

    for rule in rules:
        #print(rule)

        i = 0

        for k,entry in current_rules.items():
            #print(entry[i])
            if (check_entry_rule(entry[i], rule['port_info']['fromPort'])):
                print("test")
                #delete_rule()

            i =+1



def process_instance(instance):
    subprocess.call(['aws', 'lightsail', 'open-instance-public-ports', '--instance-name', instance['name'], '--port-info', instance['rule']])


# Main
def main():
    data = helpers.app()

    # Process lightsail instances
    for k,instance in data['lightsail'].items():
        current_rules = service.get_rules(instance['name'])
        process_rules(instance['rules'], current_rules)



        #print(current_rules)

        #print("test")
        #process_instance(instance)

# Execute
if __name__ == '__main__':
    main()