#!/bin/sh

SDX_API="http://0.0.0.0:8080/sdx/v2/constructor"

curl -vvv -H 'Content-type: application/json' $SDX_API -d '"event":{}, "kytostopology":{ "id": "urn:sdx:topology:amlight.net","name": "Amlight-OXP","version": 2,"model_version": "1.0.0","timestamp":"2021-12-31T21:19:40Z"}'
