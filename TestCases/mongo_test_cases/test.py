import os
import subprocess
import filecmp
from tempfile import TemporaryDirectory


def mongo_funct():

    passed = 0
    total = 8

    print("Testing show database")
    some_command = "mongo --port 27018 -u rootUser -p talha <show> show2"
    p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    with open("show2", "r") as input_file:
        lines = input_file.readlines()
    with open("show2", "w") as output_file:
        output_file.writelines(lines[12:])
    if filecmp.cmp('show1', 'show2'):
        print("PASSED")
        passed+=1
    else:
        print("FAILED")

    print("Testing create database and collections")
    some_command = "mongo --port 27018 -u rootUser -p talha <use> use2"
    p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    with open("use2", "r") as input_file:
        lines = input_file.readlines()
    with open("use2", "w") as output_file:
        output_file.writelines(lines[12:])
    if filecmp.cmp('use1', 'use2'):
        print("PASSED")
        passed+=2
    else:
        print("FAILED")

    print("Testing drop database")
    some_command = "mongo --port 27018 -u rootUser -p talha <drop> drop2"
    p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    with open("drop2", "r") as input_file:
        lines = input_file.readlines()
    with open("drop2", "w") as output_file:
        output_file.writelines(lines[12:])
    if filecmp.cmp('drop1', 'drop2'):
        print("PASSED")
        passed+=1
    else:
        print("FAILED")


    print("Testing Insert and find")
    some_command = "mongo --port 27018 -u rootUser -p talha <insert> insert2"
    p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    with open("insert2", "r") as input_file:
        lines = input_file.readlines()
    with open("insert2", "w") as output_file:
        output_file.writelines(lines[12:])
    if filecmp.cmp('insert1', 'insert2'):
        print("PASSED")
        passed+=2
    else:
        print("FAILED")

    print("Testing ComplexDB")
    some_command = "mongo --port 27018 -u rootUser -p talha <ComplexDB> ComplexDB2"
    p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    with open("ComplexDB2", "r") as input_file:
        lines = input_file.readlines()
    with open("ComplexDB2", "w") as output_file:
        output_file.writelines(lines[12:])
    if filecmp.cmp('ComplexDB1', 'ComplexDB2'):
        print("FAILED")
    else:
        print("PASSED")
        passed+=1


    print("Testing ComplexQuery")
    some_command = "mongo --port 27018 -u rootUser -p talha <ComplexQuery> ComplexQuery2"
    p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    with open("ComplexQuery2", "r") as input_file:
        lines = input_file.readlines()
    with open("ComplexQuery2", "w") as output_file:
        output_file.writelines(lines[12:])
    if filecmp.cmp('ComplexQuery1', 'ComplexQuery2'):
        print("PASSED")
        passed+=1
    else:
        print("FAILED")

    some_command = "mongo --port 27018 -u rootUser -p talha <flushing> flushing2"
    p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()


    print("TESTS PASSED: ",passed,"/",total)

    return passed

def main():
    result = mongo_funct()

if __name__ == "__main__":
    main()
