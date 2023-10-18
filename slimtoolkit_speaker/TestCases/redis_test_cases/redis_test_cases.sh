#! /bin/bash

<<comment
STEPS TO USE THIS TEST FILE

STEP_1:
Pull the image using the below command
docker pull redis:7-bullseye

STEP-2:
After debloating the above image, create the container from it. don't forget to add the new seccomp profile

STEP-3:
Start the container

STEP-4:
Install the redis on your host machine using:
sudo apt-get install redis

STEP-5:
The following command will run the file:
bash redis_test_cases.sh

comment


PASS=0
IP="172.17.0.2"
PORT="6379"
NUM_REQUESTS="10000"
NUM_CLIENTS="5"
DATA_SIZE="3"

CMDs=("SET" "GET" "PING" "LPUSH" "RPUSH" "LPOP" "RPOP" "MSET" "LRANGE_100")
TOTAL=10

function test1() {

    for cmd in ${CMDs[@]}; do
        echo "=== Redis ${cmd} command Test Case ==="
        redis-benchmark -h $IP -p $PORT -t $cmd -n $NUM_REQUESTS -c $NUM_CLIENTS -d $DATA_SIZE -q

        if [ $? -eq 0 ] 
        then
            echo "Test ${cmd} passed"
            let PASS=PASS+1
        else
            echo "Test ${cmd} failed"
        fi

        echo ""
    done


    echo "=== Redis FLUSHDB command Test Case ==="
    redis-benchmark -h $IP -p $PORT -n $NUM_REQUESTS -c $NUM_CLIENTS -d $DATA_SIZE -q script load "redis.call('FLUSHDB')"
    if [ $? -eq 0 ] 
    then
        echo "Test FLUSHDB passed"
        let PASS=PASS+1
    else
        echo "Test FLUSHDB failed"
    fi

    echo ""

    echo "==== Results ===="
    echo ${PASS}

}

test1
