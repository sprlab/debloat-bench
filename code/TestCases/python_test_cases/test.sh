#! /bin/bash


<<comment
STEPS TO USE THIS TEST FILE

STEP_1:
Pull the image using the below command
docker pull python:3.9.16

STEP-2:
After debloating the above image, create the container from it. don't forget to add the new seccomp profile

STEP-3:
Start the container

STEP-4:
Replace the container name with your python debloated container in the script below. Line 30

STEP-5:
The following command will run the file:
bash python_test.sh

comment


totalscore=7
passed=0

container="some-python1"

echo "<============ Testing Python ============>"

docker cp hello.py $container:/hello.py
docker cp test1.py $container:/test1.py
docker cp test_save.py $container:/test_save.py
docker cp test_u.py $container:/test_u.py



docker exec -it $container python -h /bin/bash >/dev/null
if [ $? -eq 0 ] 
    then
        echo "===> Test flag h passed"
        let passed=passed+1
    else
        echo "===> Test flag h failed"
fi

docker exec -it $container python --version /bin/bash >/dev/null
if [ $? -eq 0 ] 
    then
        echo "===> Test flag v passed"
        let passed=passed+1
    else
        echo "===> Test flag v failed"
fi

docker exec -it $container python -I hello.py /bin/bash >/dev/null
if [ $? -eq 0 ] 
    then
        echo "===> Test flag I passed"
        let passed=passed+1
    else
        echo "===> Test flag I failed"
fi

docker exec -it $container python test_u.py /bin/bash >/dev/null
if [ $? -eq 0 ] 
    then
        echo "===> Test flag u passed"
        let passed=passed+1
    else
        echo "===> Test flag u failed"
fi


# testing with no arguments
docker exec -it $container python hello.py /bin/bash >/dev/null
if [ $? -eq 0 ] 
    then
        echo "===> Testing hello world passed"
        let passed=passed+1
    else
        echo "===> Test hello world failed"
fi

# testing with arguments
docker exec -it $container python test1.py hello hello /bin/bash >/dev/null
if [ $? -eq 0 ] 
    then
        echo "===> Testing command line arguments passed"
        let passed=passed+1
    else
        echo "===> Test command line arguments failed"
fi

# save the file in the container and check if it exists
docker exec -it $container python test_save.py /bin/bash >/dev/null
if [ $? -eq 0 ] 
    then
        echo "===> Test file saving passed"
        let passed=passed+1
    else
        echo "===> Test file saving failed"
fi

echo ""

echo "Total passed" $passed / $totalscore
