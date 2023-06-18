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
    if application.split(":")[0] in s:
        print(application + " image already exist")
    else:
        print("Pulling "+application+" latest docker image")
        some_command = "docker pull "+ application
        p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p_status = p.wait()
    return True
