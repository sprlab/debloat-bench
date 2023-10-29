"""
============
INSTRUCTIONS
============

STEP-1:
Pull the following image from docker hub: node:19-bullseye
docker pull node:19-bullseye

STEP-2:
create a container from your debloated image
docker run -it --entrypoint="" --name <containerName> --security-opt seccomp=<path to your seccomp file> <imageName> sh

STEP-3:
simply run this python file

"""

import os
import subprocess
from subprocess import PIPE


passed = 0

container_name = "some-node"

# START the container
os.system("docker start " + container_name)

#copy required files into container
os.system("docker cp ./correct.js "+ container_name + ":/")
os.system("docker cp ./wrong.js "+ container_name + ":/")

read_sync = "readSync.js"
read_async = "readAsync.js"
os.system("docker cp ./" + read_sync + " " + container_name + ":/")
os.system("docker cp ./" + read_async + " " + container_name + ":/")
os.system("docker cp ./" + "write.js" + " " + container_name + ":/")

os.system("docker cp ./" + "server.js" + " " + container_name + ":/")





def test_c():
 
    flag = True
    global passed

    p = subprocess.Popen(['docker', 'exec', container_name, 'node', '-c', 'correct.js'], stdout=PIPE, stderr=PIPE)
    output, error = p.communicate()
    if p.returncode != 0:
        flag = False
        
    p = subprocess.Popen(['docker', 'exec', container_name, 'node', '-c',  'wrong.js'], stdout=PIPE, stderr=PIPE)
    output, error = p.communicate()
    if flag and p.returncode != 0 and ("Unexpected token" in str(error)):
        passed+=1    
    else:
        flag=False
        
    if(flag):
        print("==========")
    else:
        print("==========")

def test_p():
    flag = True
    global passed

    p = subprocess.Popen(['docker', 'exec', container_name, 'node',  '-p', '1+1'], stdout=PIPE, stderr=PIPE)
    output, error = p.communicate()
    if p.returncode != 0 or ("2" not in str(output)):
        print("==========")
        # print("DEBUG")
        return
        
    p = subprocess.Popen(['docker', 'exec', container_name, 'node',  '-p', '3>2 ? 1 : 0'], stdout=PIPE, stderr=PIPE)
    output, error = p.communicate()
    # print("return code: ", p.returncode)
    # print("Output: ", output)
    # print("Error: ", error)

    if (p.returncode != 0 or ("1" not in str(output))):
        print("==========")
        # print("DEBUG")
        return
    
    cmd = "console.log('This returns')"
    p = subprocess.Popen(['docker', 'exec', container_name, 'node',  '-p', cmd], stdout=PIPE, stderr=PIPE)
    output, error = p.communicate()
    # print("return code: ", p.returncode)
    # print("Output: ", output)
    # print("Error: ", error)

    if (p.returncode != 0 or ("This" not in str(output))):
        print("==========")
        return
        
    print("==========")
    passed+=1

def test_e():
    flag = True
    global passed

    # When there is a syntax error
    p = subprocess.Popen(['docker', 'exec', container_name, 'node',  '-e', '1+'], stdout=PIPE, stderr=PIPE)
    output, error = p.communicate()
    # print("return code: ", p.returncode)
    # print("Output: ", output)
    # print("Error: ", error)

    if p.returncode == 0 or ("SyntaxError" not in str(error)):
        print("==========")
        # print("DEBUG")
        return
    
    # For correct expression
    p = subprocess.Popen(['docker', 'exec', container_name, 'node',  '-e', '3>2 ? 1 : 0'], stdout=PIPE, stderr=PIPE)
    output, error = p.communicate()
    # print("return code: ", p.returncode)
    # print("Output: ", output)
    # print("Error: ", error)

    if (p.returncode != 0):
        print("==========")
        # print("DEBUG")
        return
        
    print("==========")
    passed+=1

def test_read_sync():
    flag = True
    global passed

    p = subprocess.Popen(['docker', 'exec', container_name, 'node', read_sync], stdout=PIPE, stderr=PIPE)
    output, error = p.communicate()
    # print("return code: ", p.returncode)
    # print("Output: ", output)
    # print("Error: ", error)

    if p.returncode != 0 or ("SAD" not in str(output)):
        print("==========")
        # print("DEBUG")
        return
        
    print("==========")
    passed+=1

def test_read_async():
    flag = True
    global passed

    p = subprocess.Popen(['docker', 'exec', container_name, 'node', read_async], stdout=PIPE, stderr=PIPE)
    output, error = p.communicate()
    # print("return code: ", p.returncode)
    # print("Output: ", output)
    # print("Error: ", error)

    if p.returncode != 0 or ("called" not in str(output)) or ("SAD" not in str(output)):
        print("==========")
        # print("DEBUG")
        return
        
    print("==========")
    passed+=1

def test_write():
    flag = True
    global passed

    p = subprocess.Popen(['docker', 'exec', container_name, 'node', 'write.js'], stdout=PIPE, stderr=PIPE)
    output, error = p.communicate()
    # print("return code: ", p.returncode)
    # print("Output: ", output)
    # print("Error: ", error)

    if p.returncode != 0:
        print("==========")
        # print("DEBUG")
        return
        
    print("==========")
    passed+=1
    


test_c()
test_p()
test_e()
test_read_sync()
test_read_async()
test_write()

print("========================")

        



