#!/bin/bash

TOPOLOGY_API="http://0.0.0.0:8181/api/kytos/topology/v3"
dpid="aa:00:00:00:00:00:00:01"
# SDX-related variables
echo "##### disable switch #####"
curl -H 'Content-Type: application/json' -X POST $TOPOLOGY_API/switches/$dpid/disable -d '$dpid'
