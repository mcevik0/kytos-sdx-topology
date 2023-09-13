#!/bin/sh
API="http://0.0.0.0:8000/validator/v1/validate"
echo "##### validate sdx topology #####"
curl -H "Content-Type: application/json" -X POST $API -d '{}'
