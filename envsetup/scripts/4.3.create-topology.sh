#!/bin/sh

SDX_API="http://192.168.0.4:8800/api/topology"

curl -H 'Content-type: application/json' -X POST $SDX_API -d '{ "reference": "urn:sdx:topology:tenet.ac.za","name": "Tenet-OXP","version": 1,"model_version": "1.0.0"}'
