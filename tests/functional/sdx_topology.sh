#!/bin/sh

echo "### test amlight topology ###"
SDX_API="http://0.0.0.0:8081/v2/topology"
curl -vvv -H 'Content-type: application/json' $SDX_API
echo "### test tenet topology ###"
SDX_API="http://0.0.0.0:8082/v2/topology"
curl -vvv -H 'Content-type: application/json' $SDX_API
echo "### test sax topology ###"
SDX_API="http://0.0.0.0:8083/v2/topology"
curl -vvv -H 'Content-type: application/json' $SDX_API
echo "### test sdx-test topology ###"
SDX_API="http://0.0.0.0:8084/v2/topology"
curl -vvv -H 'Content-type: application/json' $SDX_API
