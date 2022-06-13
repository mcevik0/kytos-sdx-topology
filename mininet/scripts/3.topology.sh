#!/bin/bash
TOPOLOGY_API="http://0.0.0.0:8181/api/kytos/sdx_topology/v1/topology"
echo "##### sdx topology #####"
curl -H 'Content-Type: application/json' -X GET $TOPOLOGY_API

