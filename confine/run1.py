import os
import glob
import subprocess
import json
from shutil import copy
import time

from TestCases.nginx_test_cases.test import nginx_funct 
from TestCases.node_test_cases.test import node_funct
from TestCases.redis_test_cases.test import redis_funct
from TestCases.httpd_test_cases.test import httpd_funct
from TestCases.python_test_cases.test import python_funct
from TestCases.mysql_test_cases.test import mysql_funct
from TestCases.mongo_test_cases.test import mongo_funct
# Define the folder name and commands




current_directory = os.getcwd()

configurations_directory = os.path.join(current_directory, "confine_configurations")


if os.path.exists(configurations_directory) and os.path.isdir(configurations_directory):
    # Use glob to find all JSON files in the "configurations" directory
    json_files = glob.glob(os.path.join(configurations_directory, "*.json"))

    # Extract the application names from the file paths and store them in the "apps" list
    apps = [os.path.splitext(os.path.basename(json_file))[0] for json_file in json_files]
    
    # Print the list of application names
    print(apps)
    
    # Print the list of JSON file paths
    for json_file in json_files:
        print(json_file)


# for i in range(len(apps)):
#     print(apps[i])
#     some_command = "docker pull "+ apps[i]
#     p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
#     (output, err) = p.communicate()
#     p_status = p.wait()


print("Completed")
folder_name = "confine"


# Get the current directory
current_directory = os.getcwd()

# Create the full path to the folder
folder_path = os.path.join(current_directory, folder_name)

# Check if the folder exists
if os.path.exists(folder_path):
    # Change the current directory to the 'confine' folder
    os.chdir(folder_path)

    # Run the first command inside the 'confine' folder

    for i in range(len(json_files)):

        output_json_path = "myimages.json"  # The output file where you want to store the first JSON object

        # Read the content of the input JSON file
        with open(json_files[i], "r") as input_file:
            json_data = json.load(input_file)

        # Extract the first JSON object from the dictionary
        first_json_object = {key: value for key, value in json_data.items() if key != "cmd"}

        # Write the first JSON object to the output JSON file
        with open(output_json_path, "w") as output_file:
            json.dump(first_json_object, output_file, indent=4)

        print(f"The first JSON object has been written to {output_json_path}")

        command1 = "sudo python3 confine.py -l libc-callgraphs/glibc.callgraph -m libc-callgraphs/musllibc.callgraph -i myimages.json -o output/ -p default.seccomp.json -r results/ -g go.syscalls/"

        process1 = subprocess.Popen(command1, shell=True)
    
        # Wait for the first command to complete
        process1.wait()

        current_directory = os.path.dirname(os.path.abspath(__file__))
        print("Nice")

        print("*****GENERATING CONTAINER FROM NEW SECCOMP PROFILE*****")
        # co = "docker run --entrypoint='' --name some-nginx1 --security-opt seccomp=results/" + apps[i]+".seccomp.json -d -p 8080:80 nginx sleep infinity"
        co = json_data.get("cmd", "")
        subprocess.check_call(co, shell=True)

        time.sleep(2)  # Pause for 2 seconds.

        print("*****RUNNING TEST CASES*****")
        result = eval(apps[i] + '_funct()')
        # pythn3 test.py confine
        # bash test.sh confine
        print("Total tests passed:", result)

        # Write syscall names to confine_nginx.txt in the script's directory
        seccomp_file_path = os.path.join(current_directory, "results", apps[i]+".seccomp.json")
        syscall_names = []

        try:
            with open(seccomp_file_path, "r") as seccomp_file:
                seccomp_data = json.load(seccomp_file)
                syscall_names = [syscall["name"] for syscall in seccomp_data.get("syscalls", [])]

            with open(os.path.join(current_directory, "confine_"+apps[i]+".txt"), "w") as syscall_file:
                syscall_file.write("\n".join(syscall_names))

            print("Syscall names in the seccomp profile:", syscall_names)
            print("Total number of syscalls:", len(syscall_names))
        except FileNotFoundError:
            print(f"File not found: {seccomp_file_path}")

        # Write result to confine_test_nginx.txt in the script's directory
        with open(os.path.join(current_directory, "confine_test_"+apps[i]+".txt"), "w") as result_file:
            result_file.write(str(result))
        
        result = subprocess.run(['docker', 'rm', '-f', 'some-'+apps[i]+'1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))


else:
    print(f"The '{folder_name}' folder does not exist in the current directory.")


if os.path.exists(folder_path):

    for i in range(len(json_files)):

        # Copy confine_test_{app}.txt and confine_{app}.txt to the results directory
        results_directory = os.path.abspath(os.path.join(os.path.dirname(current_directory), "results"))

        # Copy confine_test_{app}.txt
        copy(os.path.join(current_directory, "confine_test_" + apps[i] + ".txt"), results_directory)

        # Copy confine_{app}.txt
        copy(os.path.join(current_directory, "confine_" + apps[i] + ".txt"), results_directory)

        print("Files copied to the results directory.")

else:
    print(f"The '{folder_name}' folder does not exist in the current directory.")
