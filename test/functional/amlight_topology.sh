#!/bin/sh

echo "### test amlight topology ###"
KYTOS_API="http://0.0.0.0:6653/api/kytos/topology/v3/"
curl -vvv -H 'Content-type: application/json' $KYTOS_API
