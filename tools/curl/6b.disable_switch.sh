#!/bin/bash

TOPOLOGY_API="http://0.0.0.0:8282/api/kytos/topology/v3"
dpid="dd:00:00:00:00:00:00:05"
# SDX-related variables
echo "##### disable switch #####"
curl -H 'Content-Type: application/json' -X POST $TOPOLOGY_API/switches/$dpid/disable -d '$dpid'
