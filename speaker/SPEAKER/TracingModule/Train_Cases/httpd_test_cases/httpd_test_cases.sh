#! /bin/bash


<<comment
STEPS TO USE THIS TEST FILE

STEP_1:
Pull the image using the below command
docker pull httpd:bullseye

STEP-2:
After debloating the above image, create the container from it. don't forget to add the new seccomp profile

STEP-3:
Start the container

STEP-4:
Replace the container name with your httpd debloated container in the script below. Line 30

STEP-5:
The following command will run the file:
bash httpd_test_cases.sh

comment


totalscore=8
passed=0

container="some-httpd"

echo "<========================>"

docker exec -it $container httpd -v /bin/bash >/dev/null
if [ $? -eq 0 ] 
    then
        echo "<========================>"
        let passed=passed+1
    else
        echo "<========================>"
fi


docker exec -it $container httpd -h >/dev/null
if [ $? -eq 1 ] 
    then
        echo "<========================>"
        let passed=passed+1
    else
        echo "<========================>"
fi

docker exec -it $container httpd -t >/dev/null
if [ $? -eq 0 ] 
    then
        echo "<========================>"
        let passed=passed+1
    else
        echo "<========================>"
fi


docker exec -it $container httpd -k restart >/dev/null
if [ $? -eq 0 ] 
    then
        echo "<========================>"
        let passed=passed+1
    else
        echo "<========================>"
fi

docker exec -it $container httpd -V >/dev/null
if [ $? -eq 0 ] 
    then
        echo "<========================>"
        let passed=passed+1
    else
        echo "<========================>"
fi

docker exec -it $container httpd -X >/dev/null
if [ $? -eq 0 ] 
    then
        echo "<========================>"
        let passed=passed+1
    else
        echo "<========================>"
fi

docker exec -it $container httpd -L >/dev/null
if [ $? -eq 0 ] 
    then
        echo "<========================>"
        let passed=passed+1
    else
        echo "<========================>"
fi

docker exec -it $container httpd -l >/dev/null
if [ $? -eq 0 ] 
    then
        echo "<========================>"
        let passed=passed+1
    else
        echo "<========================>"
fi


echo "<========================>"
