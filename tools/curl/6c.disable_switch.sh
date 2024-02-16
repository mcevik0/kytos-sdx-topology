#!/bin/bash

TOPOLOGY_API="http://0.0.0.0:8383/api/kytos/topology/v3"
dpid="cc:00:00:00:00:00:00:06"
# SDX-related variables
echo "##### disable switch #####"
curl -H 'Content-Type: application/json' -X POST $TOPOLOGY_API/switches/$dpid/disable -d '$dpid'
