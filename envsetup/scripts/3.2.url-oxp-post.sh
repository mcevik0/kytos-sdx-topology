#!/bin/bash

SDX_API="http://192.168.0.3:8181/api/kytos/sdx_topology/v1"

echo '########## oxp_url ########## '
curl -H 'Content-Type: application/json' -X POST -d'"ampath.net"' $SDX_API/oxp_url
