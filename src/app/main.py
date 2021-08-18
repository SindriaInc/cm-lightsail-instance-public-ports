#!/usr/bin/env python3

import subprocess
import os
import sys

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

# Generate cidrs for rule create - return string
def process_cidrs():
    pass

# Get all rules of instance - return dict
def get_instance_rules(name):
    stdout = subprocess.check_output(['aws', 'lightsail', 'get-instance-port-states', '--instance-name', name], universal_newlines=True)
    data = json.loads(stdout)
    return data

# Check if entry rule already exists - return boolean
def check_entry_rule(entry, port):
    if (entry['fromPort'] == port):
        return True
    return False

# Create a rule - return void
def create_rule(name, rule):
    subprocess.call(['aws', 'lightsail', 'open-instance-public-ports', '--instance-name', name, '--port-info', 'fromPort='+rule['fromPort']+',protocol='+rule['protocol']+',toPort='+rule['toPort']+''])

# Create a rule with restricted cidrs - return void
def create_rule_with_cidrs(name, rule):

    # TODO: implement process cidrs

    cidrs = "23.65.80.239/32,3.63.182.178/32"
    subprocess.call(['aws', 'lightsail', 'open-instance-public-ports', '--instance-name', name, '--port-info', 'fromPort='+rule['fromPort']+',protocol='+rule['protocol']+',toPort='+rule['toPort']+',cidrs='+cidrs+''])

# Delete existing rule - return void
def delete_rule(name, rule):
    subprocess.call(['aws', 'lightsail', 'close-instance-public-ports', '--instance-name', name, '--port-info', 'fromPort='+rule['fromPort']+',protocol='+rule['protocol']+',toPort='+rule['toPort']+''])

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
        current_rules = get_instance_rules(instance['name'])
        process_rules(instance['rules'], current_rules)



        #print(current_rules)

        #print("test")
        #process_instance(instance)

# Execute
if __name__ == '__main__':
    main()