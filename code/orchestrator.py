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
from runningscripts import speaker_he_bhai
from runningscripts import slimtoolkit_he_bhai
from pullImages import pullimg


applications = ['nginx', 'httpd:bullseye', 'python:3.9.16','mysql', 'node'] 

def run_speaker():
	ans = {}
	for i in applications:
		a = pullimg(i)
	print("*****SPEAKER*****")
	ans["nginx"] = speaker_he_bhai("docker run --security-opt seccomp:./log.json -it --entrypoint='' --name some-nginx -d -p 8080:80 nginx:latest sleep infinity","docker stop some-nginx","sudo ./speakeru -service nginx -cmd 'docker run -it --entrypoint="" --name some-nginx1 -d -p 8080:80 nginx:latest sleep infinity'","nginx")
	ans["httpd"] = speaker_he_bhai("docker run --security-opt seccomp:./log.json -it -d --name some-httpd httpd:bullseye","docker stop some-httpd","sudo ./speakeru -service httpd -cmd 'docker run -it -d --name some-httpd1 httpd:bullseye'","httpd")
	ans["python"] = speaker_he_bhai("docker run --security-opt seccomp:./log.json -it -d --name some-python python:3.9.16 sh","docker stop some-python","sudo ./speakeru -service python -cmd 'docker run -it -d --name some-python1 python:3.9.16 sh'","python")
	ans["mysql"] = speaker_he_bhai("docker run --security-opt seccomp:./log.json -d -p 3306:3306 --name some-mysql -e MYSQL_ROOT_PASSWORD=pas mysql","docker stop some-mysql","sudo ./speakeru -service mysqld -cmd 'docker run -d -p 3306:3306 --name some-mysql1 -e MYSQL_ROOT_PASSWORD=pas mysql'","mysql")
	ans["node"] = speaker_he_bhai("docker run --security-opt seccomp:./log.json -it --entrypoint="" --name some-node -d node sh","docker stop some-node","sudo ./speakeru -service node -cmd 'docker run -it --entrypoint="" --name some-node1 -d node sh'","node")
	return ans

def run_slim():
	ans = {}
	# pullimg()

	print("*****SLIMTOOLKIT*****")
	ans["nginx"] = slimtoolkit_he_bhai('nginx:latest','new-nginx:curl',"docker run -it --entrypoint='' --name some-nginx1 -d -p 8080:80 new-nginx:curl sh",'nginx')
	ans["httpd"] = slimtoolkit_he_bhai('httpd:bullseye','new-httpd:curl',"docker run -it -d --name some-httpd1 new-httpd:curl sh",'httpd')
	ans["python"] = slimtoolkit_he_bhai('python:3.9.16','new-python:curl',"docker run -it -d --name some-python1 new-python:curl sh",'python')
	ans["mysql"] = slimtoolkit_he_bhai('mysql:latest','new-mysql:curl','docker run -d -p 3306:3306 --name some-mysql1 -e MYSQL_ROOT_PASSWORD=pas new-mysql:curl','mysql' )
	ans["node"] = slimtoolkit_he_bhai('node:latest','new-node:curl','docker run -it --entrypoint="" --name some-node1 -d new-node:curl sh','node' )
	return ans
	
parser = argparse.ArgumentParser(description='Description of your script')
parser.add_argument('-t', '--tool', help='Specify tool', required=False)
args = parser.parse_args()


if args.tool == 'all':
	a = {"speaker":run_speaker()}
	b = {"slimtoolkit":run_slim()}
	c = [a,b]
	print(c)
	os.chdir("/home/vagrant/vagrant_data")
	with open('temp.pkl', 'wb') as f:
		pickle.dump(c, f)
	print("*****CREATING REPORT*****")
	result = subprocess.run(['python3', 'Debloating.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))
	os.chdir("/home/vagrant/vagrant_data/syscalls")
	result = subprocess.run(['python3', 'report.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))
	os.chdir("/home/vagrant/vagrant_data")

elif args.tool == 'speaker':
	a = {"speaker":run_speaker()}
	print(a)
	os.chdir("/home/vagrant/vagrant_data")
	with open('temp.pkl', 'wb') as f:
		pickle.dump(a, f)
	print("*****CREATING REPORT*****")
	result = subprocess.run(['python3', 'Debloating.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))
	os.chdir("/home/vagrant/vagrant_data/syscalls")
	result = subprocess.run(['python3', 'report.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))
	os.chdir("/home/vagrant/vagrant_data")

elif args.tool == 'slimtoolkit':
	a = {"slimtoolkit":run_slim()}
	print(a)
	os.chdir("/home/vagrant/vagrant_data")
	with open('temp.pkl', 'wb') as f:
		pickle.dump(a, f)
	print("*****CREATING REPORT*****")
	result = subprocess.run(['python3', 'Debloating.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))
	os.chdir("/home/vagrant/vagrant_data/syscalls")
	result = subprocess.run(['python3', 'report.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))
	os.chdir("/home/vagrant/vagrant_data")

else:
	parser.print_help()


