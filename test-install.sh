#!/bin/bash

# on localhost machine
rm -rf *.rpm
docker build -t build .
docker run -v $(pwd):/work -ti build ./package-dcgm.sh

docker build -t test -f test/Dockerfile .
docker run -v $(pwd):/work -ti build yum localinstall *.rpm -y

