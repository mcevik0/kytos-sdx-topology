#!/bin/sh
API="http://192.168.0.14:8000/validator/v1/validate"
echo "##### validate sdx topology #####"
curl -H "Content-Type: application/json" -X POST $API -d '{}'
