#!/bin/sh

SDX_API="http://192.168.0.4:8800/api/topology/$1"

curl -H 'Content-type: application/json' -X PUT $SDX_API -d '{ "id": "urn:sdx:topology:tenet.ac.za","name": "Tenet-OXP","version": 2,"model_version": "2.0.0","timestamp": "2000-01-23T04:56:07Z"}'
