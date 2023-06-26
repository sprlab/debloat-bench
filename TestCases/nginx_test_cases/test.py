# Create your container with the following command
# docker run -it --entrypoint="" --name some-nginx -d -p 8080:80 1403e55ab369 bash
# After debloating the container, note down the container_id of the debloated container
# Keep the wrong_nginx.conf file in the same directory
# run this file using python3 test.py
# Enter the id of debloated container as input

import os
import subprocess

from tempfile import TemporaryDirectory
#container_id = input("Enter container_id:")
def nginx_funct():
    container_id = "some-nginx1"
    passed = 0
    total = 7
    # print("CONTAINER_ID: ",container_id)
    print("TESTING IF NGINX is working")
    command = 'ps aux | grep nginx'
    s = subprocess.getstatusoutput(command)
    l1 = len(s[1].split('\n'))
    os.system("docker start "+container_id)
    os.system("docker exec -d " + container_id+ " nginx")
    command = 'ps aux | grep nginx'
    s = subprocess.getstatusoutput(command)
    l2 = len(s[1].split('\n'))
    if l2>=l1:
        print("PASSED")
        passed+=1
    else:
        print("FAILED")

    print("TESTING STOP NGINX")
    required = 'signal process started'
    a  = os.popen('docker exec -ti ' + container_id+ ' nginx -s stop').readlines()
    # print(a)
    if required == a[-1].split(':')[-1][1:-1]:
        print("PASSED")
        passed+=1
    else:
        print("FAILED")


    print("TESTING STOP WITHOUT STARTING NGINX")
    required = 'nginx: [error] open() "/var/run/nginx.pid" failed (2: No such file or directory)\n'
    a  = os.popen('docker exec -ti ' + container_id+ " nginx -s stop").readlines()
    if required == a[-1]:
        print("PASSED")
        passed+=1
    else:
        print("FAILED")

    print("starting nginx again")
    os.system("docker exec -d " + container_id+ " nginx")

    print("TESTING -t flag")
    required1 = 'nginx: the configuration file /etc/nginx/nginx.conf syntax is ok\n'
    required2 = 'nginx: configuration file /etc/nginx/nginx.conf test is successful\n'
    a  = os.popen('docker exec -ti ' + container_id+ ' nginx -t').readlines()
    if a[0] == required1 and a[1] == required2:
        print("PASSED")
        passed+=1
    else:
        print("FAILED")

    print("adding wrong conf file in container")
    os.system("docker cp wrong_nginx.conf "+container_id+ ":/etc/nginx/wrong_nginx.conf")

    print("TESTING -c flag with wrong config file")
    required = 'nginx: configuration file /etc/nginx/wrong_nginx.conf test failed\n'
    a  = os.popen('docker exec -ti ' + container_id+ ' nginx -t -c /etc/nginx/wrong_nginx.conf').readlines()
    if a[-1] == required:
        print("PASSED")
        passed+=1
    else:
        print("FAILED")

    print("TESTING -c flag with correct config file")
    required1 = 'nginx: the configuration file /etc/nginx/nginx.conf syntax is ok\n'
    required2 = 'nginx: configuration file /etc/nginx/nginx.conf test is successful\n'
    a  = os.popen('docker exec -ti ' + container_id+ ' nginx -t -c /etc/nginx/nginx.conf').readlines()
    if a[0] == required1 and a[1] == required2:
        print("PASSED")
        passed+=1
    else:
        print("FAILED")

    print("TESTING -p flag using tmp folder")
    os.system("docker exec -d " + container_id+ " nginx -s stop")
    command = 'ps aux | grep nginx'
    s = subprocess.getstatusoutput(command)
    l4 = len(s[1].split('\n'))
    if l4 > l1:
        os.system("docker exec -d " + container_id+ " nginx -p tmp/")
        s = subprocess.getstatusoutput(command)
        l5 = len(s[1].split('\n'))
        if l5>l1:
            print("PASSED")
            passed+=1
        else:
            print("FAILED")
    else:
        print("FAILED")

    print("TESTS PASSED: ",passed,"/",total)
    
    return passed
    #print("-------", passed, "--------")