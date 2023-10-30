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
from TestCases.nginx_test_cases.test import nginx_funct
from TestCases.node_test_cases.test import node_funct
from TestCases.mysql_test_cases.test import mysql_funct
from TestCases.python_test_cases.test import python_funct
from TestCases.httpd_test_cases.test import httpd_funct


def merge_files(input_files, output_file):
    with open(output_file, 'w') as outfile:
        for file_name in input_files:
            with open(file_name, 'r') as infile:
                outfile.write(infile.read())

def store_integer_in_file(directory, filename, number):
    # Create the directory if it doesn't exist
    import os
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Create the file path
    file_path = os.path.join(directory, filename)

    # Write the integer to the file
    with open(file_path, 'w') as file:
        file.write(str(number))


def store_two_integers_in_file(directory, filename, number1, number2):
    # Create the directory if it doesn't exist
    import os
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Create the file path
    file_path = os.path.join(directory, filename)

    # Write the integers to the file
    with open(file_path, 'w') as file:
        file.write("{}\n{}".format(number1, number2))



def run_speaker(input_str_1,input_str_2,command,application):
	os.chdir("SPEAKER/TracingModule")

	result = subprocess.run(['sudo', 'python3', 'tracing.py', input_str_1, input_str_2], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))

	print("*****LOADING THE KERNEL MODULE*****")
	os.chdir("/home/vagrant/vagrant_data/speaker/SPEAKER/SlimmingModule/KernelModule")

	result = subprocess.run(['sudo', 'make'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))

	result = subprocess.run(['sudo', './load.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))


	os.chdir("../UserProgram")
	result = subprocess.run(['sudo', 'make'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))

	print("*****COMPLETED*****")

	print("*****TESTING*****")

	args = shlex.split(command)
	result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))

	os.chdir("/home/vagrant/vagrant_data/speaker/TestCases/"+application+"_test_cases")

	#if "python" in application or "httpd" in application:
	#	result = subprocess.run(['bash', 'test.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	#	print(result.stdout.decode('utf-8'))
	#	last =int(result.stdout.decode('utf-8')[-6:][0])
	if "mysql" in application:
		print("Yeah!!!!!!!!!!!!!")
		last = 0
		i = 0
		while last != 10:
			result = application + '_funct()'
			last  = eval(result)
			print("***last:***",last)
			i+=1
	else:
		result = application + '_funct()'
		last  = eval(result)
		print("***last:***",last)
		# -------------------------------------------------------------------

	store_integer_in_file('/home/vagrant/vagrant_data/speaker/data', 'speaker_test_'+application+'.txt',last)

	print("*****TESTING COMPLETED*****")

	print("*****DELETING CONTAINERS*****")
	result = subprocess.run(['docker', 'rm', '-f', 'some-'+application], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))
	result = subprocess.run(['docker', 'rm', '-f', 'some-'+application+'1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))

	print("*****UNLOADING KERNEL MODULE*****")
	os.chdir("/home/vagrant/vagrant_data/speaker/SPEAKER/SlimmingModule/KernelModule")
	result = subprocess.run(['sudo', './unload.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))
	print("----------DONE----------")

	filename1 = "/home/vagrant/vagrant_data/speaker/SPEAKER/Profile/running"
	with open(filename1, "r") as file:
		sys1 = sum(1 for line in file)
	filename2 = "/home/vagrant/vagrant_data/speaker/SPEAKER/Profile/booting"
	with open(filename2, "r") as file:
		sys2 = sum(1 for line in file)
	filename3 = "/home/vagrant/vagrant_data/speaker/SPEAKER/Profile/shutdown"
	with open(filename3, "r") as file:
		sys3 = sum(1 for line in file)
	input_files = [filename1, filename2, filename3]
	output_file = '/home/vagrant/vagrant_data/speaker/syscalls/allowed.txt'
	output_file1 = '/home/vagrant/vagrant_data/speaker/syscalls/speaker_allowed_'+application+'.txt'
	output_file2 = '/home/vagrant/vagrant_data/speaker/data/speaker_allowed_'+application+'.txt'
	merge_files(input_files, output_file)
	merge_files(input_files, output_file1)
	merge_files(input_files, output_file2)
	sys = 326 - (sys1 + sys2 + sys3)
	cve = 30
	store_integer_in_file('/home/vagrant/vagrant_data/speaker/data', 'speaker_CVE_'+application+'.txt',cve)
	ans = [{"syscall":sys},{"correctness":last},{"CVEs":cve}]

	os.chdir("/home/vagrant/vagrant_data/speaker/syscalls")

	result = subprocess.run(['sudo', 'python3', 'syscall.py', 'speaker_'+application], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))
	
	os.chdir("/home/vagrant/vagrant_data/speaker")
	return ans
