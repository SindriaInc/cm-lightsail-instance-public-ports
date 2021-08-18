import subprocess
import json
import helpers

# Get all rules of instance - return dict
def get_rules(name):
    stdout = subprocess.check_output(['aws', 'lightsail', 'get-instance-port-states', '--instance-name', name], universal_newlines=True)
    data = json.loads(stdout)
    return data

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

# Find specific rule by port - return boolean
def find_rule(name, rule):
    current_rules = get_rules(name)
    i = 0
    for k, entry in current_rules.items():

        #print(entry[i])
        #print(rule)

        if (entry[i]['fromPort'] == rule['port_info']['fromPort']):
            return True

        i=+1

    return False