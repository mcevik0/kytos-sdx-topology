#!/bin/bash

TOPOLOGY_API="http://3.218.56.104:8181/api/kytos/topology/v3"
# SDX-related variables
echo "##### get switches #####"
curl -H 'Content-Type: application/json' -X GET $TOPOLOGY_API/switches
