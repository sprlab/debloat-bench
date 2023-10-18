# pull image using docker pull mysql:debian
# create container using docker run -p 13306:3306 --name mysqltest -eMYSQL_ROOT_PASSWORD=pas -d mysql:debian
# Make sure that this command is not giving any error:   mysql -uroot -ppas -h127.0.0.1 -P13306 -e 'show global variables like "max_connections"';  most probably it will return 151 connections as output
# debloat the image/container.
# Start the container before running this test file.
# open terminal in the same directory i.e. mysql_testing directory
# run the file using:   python3 test.py 


import os
import subprocess
import filecmp
from tempfile import TemporaryDirectory
import shlex
import time



passed = 0
total = 10
container_id = "some-mysql1"

some_command = "docker start some-mysql1"
p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p_status = p.wait()

time.sleep(15)
#args = shlex.split('docker exec -i ' + container_id+ ' mysql -uroot -ppas mysql -e "SHOW DATABASES;"')
#result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#print(result.stdout.decode('utf-8'))


some_command = "mysql -h 127.0.0.1 -P 3306 -u root -ppas mysql < showdb.sql > showdb.tab"
p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p_status = p.wait()
if filecmp.cmp('original_showdb.tab', 'showdb.tab'):
    print("==========")
    passed+=1
else:
    # print("FAILED")
    print("==========")


some_command = "mysql -h 127.0.0.1 -P 3306 -u root -ppas mysql < createdb.sql > createdb.tab"
p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p_status = p.wait()
if filecmp.cmp('original_createdb.tab', 'createdb.tab'):
    print("==========")
    passed+=1
else:
    print("==========")



some_command = "mysql -h 127.0.0.1 -P 3306 -u root -ppas mysql < createtable.sql > createtable.tab"
p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p_status = p.wait()
if filecmp.cmp('original_createtable.tab', 'createtable.tab'):
    print("==========")
    passed+=1
else:
    print("==========")

some_command = "mysql -h 127.0.0.1 -P 3306 -u root -ppas mysql < insert.sql > insert.tab"
p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p_status = p.wait()
if filecmp.cmp('original_insert.tab', 'insert.tab'):
    print("==========")
    passed+=1
else:
    print("==========")


some_command = "mysql -h 127.0.0.1 -P 3306 -u root -ppas mysql < update.sql > update.tab"
p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p_status = p.wait()
if filecmp.cmp('original_update.tab', 'update.tab'):
    print("==========")
    passed+=1
else:
    print("==========")


some_command = "mysql -h 127.0.0.1 -P 3306 -u root -ppas mysql < delete.sql > delete.tab"
p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p_status = p.wait()
if filecmp.cmp('original_delete.tab', 'delete.tab'):
    print("==========")
    passed+=1
else:
    print("==========")



some_command = "mysql -h 127.0.0.1 -P 3306 -u root -ppas mysql < complexDB.sql > complexDB.tab"
p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p_status = p.wait()


some_command = "mysql -h 127.0.0.1 -P 3306 -u root -ppas mysql < complex_query1.sql > complexquery1.tab"
p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p_status = p.wait()
if filecmp.cmp('original_complexquery1.tab', 'complexquery1.tab'):
    print("==========")
    passed+=1
else:
    print("==========")


some_command = "mysql -h 127.0.0.1 -P 3306 -u root -ppas mysql < complex_query2.sql > complexquery2.tab"
p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p_status = p.wait()
if filecmp.cmp('original_complexquery2.tab', 'complexquery2.tab'):
    print("==========")
    passed+=1
else:
    print("==========")


some_command = "mysql -h 127.0.0.1 -P 3306 -u root -ppas mysql < complex_query3.sql > complexquery3.tab"
p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p_status = p.wait()
if filecmp.cmp('original_complexquery3.tab', 'complexquery3.tab'):
    print("==========")
    passed+=1
else:
    print("==========")



some_command = "mysql -h 127.0.0.1 -P 3306 -u root -ppas mysql < drop.sql > drop.tab"
p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p_status = p.wait()
if filecmp.cmp('original_drop.tab', 'drop.tab'):
    print("==========")
    passed+=1
else:
    print("==========")
