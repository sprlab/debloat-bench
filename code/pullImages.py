import os
import subprocess
import filecmp
from tempfile import TemporaryDirectory
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

print("Checking already existing images")


some_command = "docker images"
p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p_status = p.wait()

s = output.decode('utf-8')
def pullimg(application):
    if application in s:
        print(application + " image already exist")
    else:
        print("Pulling "+application+" latest docker image")
        some_command = "docker pull "+ application
        p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p_status = p.wait()
    return True
    # if 'httpd' in s:
    #     print("HTTPD image already exist")
    # else:
    #     print("Pulling Httpd latest docker image")
    #     some_command = "docker pull httpd:bullseye"
    #     p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
    #     (output, err) = p.communicate()
    #     p_status = p.wait()

    # if 'python' in s:
    #     print("PYTHON image already exist")
    # else:
    #     print("Pulling python latest docker image")
    #     some_command = "docker pull python:3.9.16"
    #     p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
    #     (output, err) = p.communicate()
    #     p_status = p.wait()
        
    # if 'mysql' in s:
    #     print("Mysql image already exist")
    # else:
    #     print("Pulling mysql latest docker image")
    #     some_command = "docker pull mysql"
    #     p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
    #     (output, err) = p.communicate()
    #     p_status = p.wait()
    # if 'node' in s:
    #     print("Node image already exist")
    # else:
    #     print("Pulling node latest docker image")
    #     some_command = "docker pull node"
    #     p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
    #     (output, err) = p.communicate()
    #     p_status = p.wait()