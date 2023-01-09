#!/bin/sh

SDX_API="http://192.168.0.3:8800/api/topology"

curl -H 'Content-type: application/json' -X POST $SDX_API -d '{ "reference": "urn:sdx:topology:ampath.net","name": "Ampath-OXP","version": 1,"model_version": "1.0.0"}'
