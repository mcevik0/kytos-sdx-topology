#!/bin/sh
API="http://0.0.0.0:8181/api/kytos/sdx_topology/v1"
event_type="0"
timestamp="None"

echo "##### post sdx topology #####"
curl -H "Content-Type: application/json" -X GET $API/convert_topology/$event_type/$timestamp
