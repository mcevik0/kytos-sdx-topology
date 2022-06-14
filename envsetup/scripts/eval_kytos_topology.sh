#!/bin/bash

SDX_API="http://3.218.56.104:8181/api/kytos/sdx_topology/v1"
TOPOLOGY_API="http://3.218.56.104:8181/api/kytos/topology/v3"
# SDX-related variables
echo "##### eval topology #####"
curl -H 'Content-Type: application/json' -X POST $SDX_API/eval_kytos_topology -d '"links"'
