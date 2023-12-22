#!/bin/bash
EVC_API="http://0.0.0.0:8181/api/kytos/mef_eline/v2/evc"
echo "##### kytos evc #####"
curl -H 'Content-Type: application/json' -X GET $EVC_API | jq -r .

