#!/bin/bash

SDX_API="http://3.218.56.104:8181/api/kytos/sdx_topology/v1"

echo '########## oxp_url ########## '
curl -H 'Content-Type: application/json' -X POST -d'"amlight.net"' $SDX_API/oxp_url
