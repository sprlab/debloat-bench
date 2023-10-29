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


application = input("app:")
with open(application+'-seccomp.json') as file:
	data = json.load(file)
syscall_list = data["syscalls"][0]["names"]
print(syscall_list)
with open('slimtoolkit_'+application+'.txt', 'w') as file:
    for element in syscall_list:
        file.write(element + '\n')