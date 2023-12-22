#!/bin/bash

TOPOLOGY_API="http://0.0.0.0:8282/api/kytos/topology/v3"
# SDX-related variables
echo "##### get switches #####"
curl -H 'Content-Type: application/json' -X GET $TOPOLOGY_API/switches | jq -r .
