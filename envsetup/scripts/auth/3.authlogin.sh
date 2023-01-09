#!/bin/sh
curl -H 'Content-type: application/json' http://192.168.0.6:8800/api/auth/login -d '{"email":"felipe@example.com", "password": "pass_123"}'
