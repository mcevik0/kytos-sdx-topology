#!/bin/sh

SDX_API="http://0.0.0.0:8080/sdx/v2/topology"

curl -vvv -H 'Content-type: application/json' $SDX_API
