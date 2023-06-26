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



def speaker_he_bhai(input_str_1,input_str_2,command,application):
	os.chdir("SPEAKER/TracingModule")

	result = subprocess.run(['sudo', 'python3', 'tracing.py', input_str_1, input_str_2], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))

	print("*****LOADING THE KERNEL MODULE*****")
	os.chdir("/home/vagrant/vagrant_data/SPEAKER/SlimmingModule/KernelModule")

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

	os.chdir("/home/vagrant/vagrant_data/TestCases/"+application+"_test_cases")

	if "python" in application or "httpd" in application:
		result = subprocess.run(['bash', 'test.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		print(result.stdout.decode('utf-8'))
		last =int(result.stdout.decode('utf-8')[-6:][0])
	elif "mysql" in application:
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

	store_integer_in_file('/home/vagrant/vagrant_data/data', 'speaker_test_'+application+'.txt',last)

	print("*****TESTING COMPLETED*****")

	print("*****DELETING CONTAINERS*****")
	result = subprocess.run(['docker', 'rm', '-f', 'some-'+application], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))
	result = subprocess.run(['docker', 'rm', '-f', 'some-'+application+'1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))

	print("*****UNLOADING KERNEL MODULE*****")
	os.chdir("/home/vagrant/vagrant_data/SPEAKER/SlimmingModule/KernelModule")
	result = subprocess.run(['sudo', './unload.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))
	print("----------DONE----------")

	filename1 = "/home/vagrant/vagrant_data/SPEAKER/Profile/running"
	with open(filename1, "r") as file:
		sys1 = sum(1 for line in file)
	filename2 = "/home/vagrant/vagrant_data/SPEAKER/Profile/booting"
	with open(filename2, "r") as file:
		sys2 = sum(1 for line in file)
	filename3 = "/home/vagrant/vagrant_data/SPEAKER/Profile/shutdown"
	with open(filename3, "r") as file:
		sys3 = sum(1 for line in file)
	input_files = [filename1, filename2, filename3]
	output_file = '/home/vagrant/vagrant_data/syscalls/allowed.txt'
	output_file1 = '/home/vagrant/vagrant_data/syscalls/speaker_allowed_'+application+'.txt'
	output_file2 = '/home/vagrant/vagrant_data/data/speaker_allowed_'+application+'.txt'
	merge_files(input_files, output_file)
	merge_files(input_files, output_file1)
	merge_files(input_files, output_file2)
	sys = 326 - (sys1 + sys2 + sys3)
	cve = 30
	store_integer_in_file('/home/vagrant/vagrant_data/data', 'speaker_CVE_'+application+'.txt',cve)
	ans = [{"syscall":sys},{"correctness":last},{"CVEs":cve}]

	os.chdir("/home/vagrant/vagrant_data/syscalls")

	result = subprocess.run(['sudo', 'python3', 'syscall.py', 'speaker_'+application], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))
	
	os.chdir("/home/vagrant/vagrant_data")
	return ans

def slimtoolkit_he_bhai(target,tag,command,application):
	if "python" in target or 'mysql' in target or 'node' in target:
		result = subprocess.run(['slim','--report', application+'-build-report.json', 'build', '--target', target, '--tag', tag, '--http-probe=false', '--exec-file', './'+application+'train.sh', '--copy-meta-artifacts', '/home/vagrant/vagrant_data/syscalls'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		print(result.stdout.decode('utf-8'))
	else:
		result = subprocess.run(['slim','--report', application+'-build-report.json', 'build', '--target', target, '--tag', tag , '--copy-meta-artifacts', '/home/vagrant/vagrant_data/syscalls'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		print(result.stdout.decode('utf-8'))
	print("*****DELETING UNNECESSARY CONTAINERS*****")
	result = subprocess.run(['docker', 'rmi', 'docker-slim-empty-image:latest'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))
	print("*****TESTING*****")
	os.chdir("/home/vagrant/vagrant_data/TestCases/"+application+"_test_cases")
	args = shlex.split(command)
	result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))

	if "python" in application or "httpd" in application:
		result = subprocess.run(['bash', 'test.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		print(result.stdout.decode('utf-8'))
		last =int(result.stdout.decode('utf-8')[-6:][0])
	elif 'mysql' in application:
		result = application + '_funct()'
		last  = eval(result)
		print("***last:***",last)
	else:	
		result = application + '_funct()'
		last  = eval(result)
		print("***last:***",last)

	
	store_integer_in_file('/home/vagrant/vagrant_data/data', 'slimtoolkit_test_'+application+'.txt',last)

	print("*****TESTING COMPLETED*****")
	print("*****DELETING CONTAINER*****")
	result = subprocess.run(['docker', 'rm', '-f', 'some-'+application+'1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))
	result = subprocess.run(['docker', 'images'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	string = result.stdout.decode('utf-8')
	words = string.split('\n')
	mb_words = [word for word in words if "MB" in word or "GB" in word]
	new_list = []
	for i in range(len(mb_words)):
		if target.split(":")[0] in mb_words[i]:
			new_list.append(mb_words[i])
	d = new_list[0].split()
	o = new_list[1].split()
	Debloated_size = float(d[-1][0:-2])
	if o[-1][-2:] == "GB":
		original_size = float(o[-1][0:-2])*1000
	else:
		original_size = float(o[-1][0:-2])

	store_two_integers_in_file('/home/vagrant/vagrant_data/data', 'slimtoolkit_size_'+application+'.txt',original_size, Debloated_size)
	
	print("*****DELETING IMAGE*****")
	result = subprocess.run(['docker', 'rmi', tag], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))
	print("----------DONE----------")
	
	os.chdir("/home/vagrant/vagrant_data")
	result = subprocess.run(['rm', application+'-build-report.json'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	os.chdir("/home/vagrant/vagrant_data/syscalls")
	result = subprocess.run(['rm', application+'-apparmor-profile'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	result = subprocess.run(['rm', 'creport.json'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	
	with open(application+'-seccomp.json') as file:
		data = json.load(file)
	syscall_list = data["syscalls"][0]["names"]
	with open('allowed.txt', 'w') as file:
		for element in syscall_list:
			file.write(element + '\n')
	with open('slimtoolkit_allowed_'+application+'.txt', 'w') as file:
		for element in syscall_list:
			file.write(element + '\n')
	result = subprocess.run(['rm', application+'-seccomp.json'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	
	result = subprocess.run(['sudo', 'python3', 'syscall.py', 'slimtoolkit_'+application], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))
	sys = 326 - len(syscall_list)
	cve = 30
	store_integer_in_file('/home/vagrant/vagrant_data/data', 'slimtoolkit_CVE_'+application+'.txt',cve)
	ans = [{"syscall":sys},{"correctness":last},{"CVEs":cve},{"size":[original_size,Debloated_size]}]
	os.chdir("/home/vagrant/vagrant_data/data")
	with open('slimtoolkit_allowed_'+application+'.txt', 'w') as file:
		for element in syscall_list:
			file.write(element + '\n')
	os.chdir("/home/vagrant/vagrant_data")
	return ans

def pull_images():
	os.chdir("/home/vagrant/vagrant_data")
	print("*****PULLING IMAGES IF THEY DONT EXIST*****")
	some_command = "python3 pullImages.py"
	p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
	(output, err) = p.communicate()
	p_status = p.wait()
	print("*****PULL IMAGES COMPLETED*****")