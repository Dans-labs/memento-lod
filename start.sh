#!/bin/bash

#export DOCKER_MACHINE_IP=$(docker-machine ip)
export DOCKER_MACHINE_IP=localhost

echo "**********************************************************************"
echo "**********************************************************************"
echo "Browse to http://${DOCKER_MACHINE_IP}:5000/info to check Elastic status"
echo "**********************************************************************"
echo "**********************************************************************"


docker-compose up
