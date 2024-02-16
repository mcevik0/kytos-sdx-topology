#!/bin/sh
TOPOLOGY_API="http://0.0.0.0:8282/api/kytos/sdx_topology/v1/shelve/events"
echo "##### shelve events #####"
curl -H 'Content-Type: application/json' -X GET $TOPOLOGY_API
