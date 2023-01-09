#!/bin/sh

SDX_API="http://192.168.0.3:8800/api/topology/$1"

curl -H 'Content-type: application/json' -X DELETE $SDX_API
