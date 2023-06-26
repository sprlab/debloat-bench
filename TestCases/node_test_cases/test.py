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


# passed = 0

# container_name = "some-node1"

# # START the container
# os.system("docker start " + container_name)

# #copy required files into container
# os.system("docker cp ./correct.js "+ container_name + ":/")
# os.system("docker cp ./wrong.js "+ container_name + ":/")

# read_sync = "readSync.js"
# read_async = "readAsync.js"
# os.system("docker cp ./" + read_sync + " " + container_name + ":/")
# os.system("docker cp ./" + read_async + " " + container_name + ":/")
# os.system("docker cp ./" + "write.js" + " " + container_name + ":/")

# os.system("docker cp ./" + "server.js" + " " + container_name + ":/")





# def test_c():
#     print(" ")
#     print("======= TEST CASE: Syntax flag -c ============")
#     flag = True
#     global passed

#     p = subprocess.Popen(['docker', 'exec', container_name, 'node', '-c', 'correct.js'], stdout=PIPE, stderr=PIPE)
#     output, error = p.communicate()
#     if p.returncode != 0:
#         flag = False
        
#     p = subprocess.Popen(['docker', 'exec', container_name, 'node', '-c',  'wrong.js'], stdout=PIPE, stderr=PIPE)
#     output, error = p.communicate()
#     if flag and p.returncode != 0 and ("Unexpected token" in str(error)):
#         passed+=1    
#     else:
#         flag=False
        
#     if(flag):
#         print("TEST -c PASSED")
#     else:
#         print("TEST -c FAILED")

# def test_p():
#     print(" ")
#     print("======= TEST CASE: Evaluation Flag -p ============")
#     flag = True
#     global passed

#     p = subprocess.Popen(['docker', 'exec', container_name, 'node',  '-p', '1+1'], stdout=PIPE, stderr=PIPE)
#     output, error = p.communicate()
#     if p.returncode != 0 or ("2" not in str(output)):
#         print("TEST -p FAILED")
#         # print("DEBUG")
#         return
        
#     p = subprocess.Popen(['docker', 'exec', container_name, 'node',  '-p', '3>2 ? 1 : 0'], stdout=PIPE, stderr=PIPE)
#     output, error = p.communicate()
#     # print("return code: ", p.returncode)
#     # print("Output: ", output)
#     # print("Error: ", error)

#     if (p.returncode != 0 or ("1" not in str(output))):
#         print("TEST -p FAILED")
#         # print("DEBUG")
#         return
    
#     cmd = "console.log('This returns')"
#     p = subprocess.Popen(['docker', 'exec', container_name, 'node',  '-p', cmd], stdout=PIPE, stderr=PIPE)
#     output, error = p.communicate()
#     # print("return code: ", p.returncode)
#     # print("Output: ", output)
#     # print("Error: ", error)

#     if (p.returncode != 0 or ("This" not in str(output))):
#         print("TEST -p FAILED")
#         return
        
#     print("TEST -p PASSED")
#     passed+=1

# def test_e():
#     print(" ")
#     print("======= TEST CASE: Evaluation Flag -e ============")
#     flag = True
#     global passed

#     # When there is a syntax error
#     p = subprocess.Popen(['docker', 'exec', container_name, 'node',  '-e', '1+'], stdout=PIPE, stderr=PIPE)
#     output, error = p.communicate()
#     # print("return code: ", p.returncode)
#     # print("Output: ", output)
#     # print("Error: ", error)

#     if p.returncode == 0 or ("SyntaxError" not in str(error)):
#         print("TEST -e FAILED")
#         # print("DEBUG")
#         return
    
#     # For correct expression
#     p = subprocess.Popen(['docker', 'exec', container_name, 'node',  '-e', '3>2 ? 1 : 0'], stdout=PIPE, stderr=PIPE)
#     output, error = p.communicate()
#     # print("return code: ", p.returncode)
#     # print("Output: ", output)
#     # print("Error: ", error)

#     if (p.returncode != 0):
#         print("TEST -e FAILED")
#         # print("DEBUG")
#         return
        
#     print("TEST -e PASSED")
#     passed+=1

# def test_read_sync():
#     print(" ")
#     print("======= TEST CASE: Synchronus Reading ============")
#     flag = True
#     global passed

#     p = subprocess.Popen(['docker', 'exec', container_name, 'node', read_sync], stdout=PIPE, stderr=PIPE)
#     output, error = p.communicate()
#     # print("return code: ", p.returncode)
#     # print("Output: ", output)
#     # print("Error: ", error)

#     if p.returncode != 0 or ("SAD" not in str(output)):
#         print("TEST Synchronus Reading FAILED")
#         # print("DEBUG")
#         return
        
#     print("TEST Synchronus Reading PASSED")
#     passed+=1

# def test_read_async():
#     print(" ")
#     print("======= TEST CASE: Asynchronus Reading ============")
#     flag = True
#     global passed

#     p = subprocess.Popen(['docker', 'exec', container_name, 'node', read_async], stdout=PIPE, stderr=PIPE)
#     output, error = p.communicate()
#     # print("return code: ", p.returncode)
#     # print("Output: ", output)
#     # print("Error: ", error)

#     if p.returncode != 0 or ("called" not in str(output)) or ("SAD" not in str(output)):
#         print("TEST Asynchronus Reading FAILED")
#         # print("DEBUG")
#         return
        
#     print("TEST Asynchronus Reading PASSED")
#     passed+=1

# def test_write():
#     print(" ")
#     print("======= TEST CASE: Writing ============")
#     flag = True
#     global passed

#     p = subprocess.Popen(['docker', 'exec', container_name, 'node', 'write.js'], stdout=PIPE, stderr=PIPE)
#     output, error = p.communicate()
#     # print("return code: ", p.returncode)
#     # print("Output: ", output)
#     # print("Error: ", error)

#     if p.returncode != 0:
#         print("TEST Writing FAILED")
#         # print("DEBUG")
#         return
        
#     print("TEST Writing PASSED")
#     passed+=1
    

def node_funct():

    passed = 0

    container_name = "some-node1"

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

    print(" ")
    print("======= TEST CASE: Syntax flag -c ============")
    flag = True
    # global passed

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
        print("TEST -c PASSED")
    else:
        print("TEST -c FAILED")
    print(" ")
    print("======= TEST CASE: Evaluation Flag -p ============")
    flag = True
    # global passed

    p = subprocess.Popen(['docker', 'exec', container_name, 'node',  '-p', '1+1'], stdout=PIPE, stderr=PIPE)
    output, error = p.communicate()
    if p.returncode != 0 or ("2" not in str(output)):
        print("TEST -p FAILED")
        # print("DEBUG")
        return
        
    p = subprocess.Popen(['docker', 'exec', container_name, 'node',  '-p', '3>2 ? 1 : 0'], stdout=PIPE, stderr=PIPE)
    output, error = p.communicate()
    # print("return code: ", p.returncode)
    # print("Output: ", output)
    # print("Error: ", error)

    if (p.returncode != 0 or ("1" not in str(output))):
        print("TEST -p FAILED")
        # print("DEBUG")
        return
    
    cmd = "console.log('This returns')"
    p = subprocess.Popen(['docker', 'exec', container_name, 'node',  '-p', cmd], stdout=PIPE, stderr=PIPE)
    output, error = p.communicate()
    # print("return code: ", p.returncode)
    # print("Output: ", output)
    # print("Error: ", error)

    if (p.returncode != 0 or ("This" not in str(output))):
        print("TEST -p FAILED")
        return
        
    print("TEST -p PASSED")
    passed+=1
    
    print(" ")
    print("======= TEST CASE: Evaluation Flag -e ============")
    flag = True
    # global passed

    # When there is a syntax error
    p = subprocess.Popen(['docker', 'exec', container_name, 'node',  '-e', '1+'], stdout=PIPE, stderr=PIPE)
    output, error = p.communicate()
    # print("return code: ", p.returncode)
    # print("Output: ", output)
    # print("Error: ", error)

    if p.returncode == 0 or ("SyntaxError" not in str(error)):
        print("TEST -e FAILED")
        # print("DEBUG")
        return
    
    # For correct expression
    p = subprocess.Popen(['docker', 'exec', container_name, 'node',  '-e', '3>2 ? 1 : 0'], stdout=PIPE, stderr=PIPE)
    output, error = p.communicate()
    # print("return code: ", p.returncode)
    # print("Output: ", output)
    # print("Error: ", error)

    if (p.returncode != 0):
        print("TEST -e FAILED")
        # print("DEBUG")
        return
        
    print("TEST -e PASSED")
    passed+=1

    print(" ")
    print("======= TEST CASE: Synchronus Reading ============")
    flag = True
    # global passed

    p = subprocess.Popen(['docker', 'exec', container_name, 'node', read_sync], stdout=PIPE, stderr=PIPE)
    output, error = p.communicate()
    # print("return code: ", p.returncode)
    # print("Output: ", output)
    # print("Error: ", error)

    if p.returncode != 0 or ("SAD" not in str(output)):
        print("TEST Synchronus Reading FAILED")
        # print("DEBUG")
        return
        
    print("TEST Synchronus Reading PASSED")
    passed+=1

    print(" ")
    print("======= TEST CASE: Asynchronus Reading ============")
    flag = True
    # global passed

    p = subprocess.Popen(['docker', 'exec', container_name, 'node', read_async], stdout=PIPE, stderr=PIPE)
    output, error = p.communicate()
    # print("return code: ", p.returncode)
    # print("Output: ", output)
    # print("Error: ", error)

    if p.returncode != 0 or ("called" not in str(output)) or ("SAD" not in str(output)):
        print("TEST Asynchronus Reading FAILED")
        # print("DEBUG")
        return
        
    print("TEST Asynchronus Reading PASSED")
    passed+=1

    print(" ")
    print("======= TEST CASE: Writing ============")
    flag = True
    # global passed

    p = subprocess.Popen(['docker', 'exec', container_name, 'node', 'write.js'], stdout=PIPE, stderr=PIPE)
    output, error = p.communicate()
    # print("return code: ", p.returncode)
    # print("Output: ", output)
    # print("Error: ", error)

    if p.returncode != 0:
        print("TEST Writing FAILED")
        # print("DEBUG")
        return
        
    print("TEST Writing PASSED")
    passed+=1
    
    return passed

        



