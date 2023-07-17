import argparse
import os
import subprocess
import filecmp
from tempfile import TemporaryDirectory
import time
import shlex
import pickle
import re
import json
from speaker import speaker_he_bhai
from slimtoolkit import slimtoolkit_he_bhai
# from runningscripts import speaker_he_bhai
# from runningscripts import slimtoolkit_he_bhai
from pullImages import pullimg


with open('configurations/applications_conf.json') as file:
    config_data = json.load(file)
# Create a list of applications from the configuration data
applications = ["{}:{}".format(app, data['tag']) for app, data in config_data['applications'].items()]
print(applications)

application_names = [app.split(':')[0] for app in applications]
for i in applications:
	a = pullimg(i)


def get_arguments(tool, application):
    # Construct the path to the tool's configuration file
    config_path = "configurations/" + tool + "/" + application.split(":")[0]+".json"
    print(config_path)

    # Check if the tool configuration file exists
    if os.path.exists(config_path):
        # Load the contents of the tool's configuration file
        with open(config_path) as file:
            config_data = json.load(file)

        # Extract the arguments for the specified application
        arguments = [config_data['applications'][application]['arg' + str(i+1)] for i in range(4)]

        # Return the arguments as a list
        return arguments
    else:
        print("Configuration file for tool '{}' not found.".format(tool))
        return []

def run_tool(tool, tool_function):
    ans = {}
    print("*****" + tool.upper() + "*****")

    for i in application_names:
        arguments = get_arguments(tool, i)
        if arguments:
            print(arguments)
            print(*arguments)
            ans[i] = tool_function(*arguments)
			
    return ans


parser = argparse.ArgumentParser(description='Description of your script')
parser.add_argument('-t', '--tool', help='Specify tool', required=False)
args = parser.parse_args()


if args.tool == 'all':
	a = {"speaker":run_tool('speaker', speaker_he_bhai)}
	b = {"slimtoolkit":run_tool('slimtoolkit', slimtoolkit_he_bhai)}
	c = [a,b]
	print(c)

elif args.tool == 'speaker':
	a = {"speaker":run_tool('speaker', speaker_he_bhai)}
	print(a)

elif args.tool == 'slimtoolkit':
	a = {"slimtoolkit":run_tool('slimtoolkit', slimtoolkit_he_bhai)}
	print(a)

else:
	parser.print_help()


