#!/bin/sh

SDX_API="http://0.0.0.0:8084/sdx/v2/constructor"

curl -v -H 'Content-type: application/json' $SDX_API -d '{"event":[{}], "kytostopology":{}}'

