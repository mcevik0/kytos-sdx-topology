#!/bin/sh

echo "### test amlight topology ###"
KYTOS_API="http://0.0.0.0:8081/api/kytos/topology/v3/"
curl -vvv -H 'Content-type: application/json' $KYTOS_API
echo "### test tenet topology ###"
KYTOS_API="http://0.0.0.0:8082/api/kytos/topology/v3/"
curl -vvv -H 'Content-type: application/json' $KYTOS_API
echo "### test sax topology ###"
KYTOS_API="http://0.0.0.0:8083/api/kytos/topology/v3/"
curl -vvv -H 'Content-type: application/json' $KYTOS_API
echo "### test sdx-test topology ###"
KYTOS_API="http://0.0.0.0:8084/api/kytos/topology/v3/"
curl -vvv -H 'Content-type: application/json' $KYTOS_API
