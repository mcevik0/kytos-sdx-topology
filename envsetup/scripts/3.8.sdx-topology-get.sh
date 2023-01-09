#!/bin/bash

SDX_API="http://192.168.0.3:8181/api/kytos/sdx_topology/v1/topology"

echo "##### sdx topology #####"
curl -H 'Content-Type: application/json' -X GET $SDX_API

