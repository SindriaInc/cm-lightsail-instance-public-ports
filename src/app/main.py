#!/usr/bin/env python3

import os
import sys

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

    current_rules = service.get_rules(name)

    i = 0

    #print(current_rules)

    for rule in rules:

        #print(i)

        #print(rules)
        #print("\n\n")

        j = 0

        for entry in current_rules['portStates']:

            #print("debug entry:")

            #print(rules[0]['port_info'])

            #print(k)

            #print(current_rules['portStates'][0])

            print("check:")
            print(rule)
            print("\n")

            print("with")
            print(entry)

            print("\n")
            print(j)
            print("\n")

            #i += 1
            #print(i)

            #sys.exit(0)
            #print("\n\n")

            if (entry['fromPort'] == rule['port_info']['fromPort']):

                #return True

                #service.delete_rule(name, rule)
                #service.create_rule(name, rule)

                print("found, deleting...")
                print("\n")
                #print(rule)
            else:
                print("\n")
                print("not found, skipping...")
                print(rule)
                print("\n")

                # service.create_rule(name, rule)



            j += 1

            #print("\n\n")
            #print(i)





        print("\n")
        print("External count is: " + str(i))
        print("\n")

        print("####################################################################################################")

        i += 1





# Main
def main():
    data = helpers.app()

    # Process lightsail instances
    for k,instance in data['lightsail'].items():
        process_rules(instance['name'], instance['rules'])
        #sys.exit(0)


# Execute
if __name__ == '__main__':
    main()