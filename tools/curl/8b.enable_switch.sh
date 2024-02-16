#!/bin/bash

TOPOLOGY_API="http://0.0.0.0:8282/api/kytos/topology/v3"
dpid="dd:00:00:00:00:00:00:01"
# SDX-related variables
echo "##### enable switch #####"
curl -H 'Content-Type: application/json' -X POST $TOPOLOGY_API/switches/$dpid/enable -d '$dpid'
