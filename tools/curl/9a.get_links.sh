#!/bin/bash

TOPOLOGY_API="http://0.0.0.0:8181/api/kytos/topology/v3"
# SDX-related variables
echo "##### get links #####"
curl -H 'Content-Type: application/json' -X GET $TOPOLOGY_API/links | jq -r .
