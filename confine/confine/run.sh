#!/bin/bash

# First command
sudo python3 confine.py -l libc-callgraphs/glibc.callgraph -m libc-callgraphs/musllibc.callgraph -i myimages.json -o output/ -p default.seccomp.json -r results/ -g go.syscalls/

# Second command (executed after the first command completes)
sudo docker run --name container-hardened --security-opt seccomp=results/nginx.seccomp.json -td nginx
