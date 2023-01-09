#!/bin/sh
curl -H 'Content-type: application/json' -X POST http://192.168.0.6:8800/api/auth/signup -d '{"email":"felipe@example.com", "password": "pass_123"}'
