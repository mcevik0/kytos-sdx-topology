#!/bin/sh
API="http://0.0.0.0:8181/api/kytos/sdx_topology/v1/validate_sdx_topology"
echo "##### validate sdx topology #####"
curl -H "Content-Type: application/json" -X POST $API -d '{"sdx_topology":{}}'
