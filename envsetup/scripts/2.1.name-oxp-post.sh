#!/bin/bash

SDX_API="http://192.168.0.2:8181/api/kytos/sdx_topology/v1"

# SDX-related variables
echo '########## oxp_name ########## '
curl -H 'Content-Type: application/json' -X POST -d'"AmLight-OXP"' $SDX_API/oxp_name
