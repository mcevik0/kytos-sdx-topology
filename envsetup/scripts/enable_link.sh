#!/bin/bash

TOPOLOGY_API="http://3.218.56.104:8181/api/kytos/topology/v3"
link_id="2547e1a4e514b06cc9e346e20d0dbd199da83340e78031d632ce398edc5c0453"
# SDX-related variables
echo "##### enable switch #####"
curl -H 'Content-Type: application/json' -X POST $TOPOLOGY_API/links/$link_id/enable -d '$dpid'
