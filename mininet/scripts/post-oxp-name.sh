#!/bin/bash

SDX_API="http://3.218.56.104:8181/api/kytos/sdx_topology/v1"

# SDX-related variables
echo '########## oxp_name ########## '
curl -H 'Content-Type: application/json' -X POST -d'"AmLight"' $SDX_API/oxp_name
