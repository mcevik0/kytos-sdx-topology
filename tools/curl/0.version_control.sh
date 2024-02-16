#!/bin/sh
TOPOLOGY_API_1="http://0.0.0.0:8181/api/kytos/sdx_topology/v1/version/control"
TOPOLOGY_API_2="http://0.0.0.0:8181/api/kytos/sdx_topology/v1/version/control"
TOPOLOGY_API_3="http://0.0.0.0:8181/api/kytos/sdx_topology/v1/version/control"
echo "##### version control init #####"
curl -H 'Content-Type: application/json' -X GET $TOPOLOGY_API_1
curl -H 'Content-Type: application/json' -X GET $TOPOLOGY_API_2
curl -H 'Content-Type: application/json' -X GET $TOPOLOGY_API_3
