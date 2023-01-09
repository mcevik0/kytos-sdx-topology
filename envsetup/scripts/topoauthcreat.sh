#!/bin/sh
$bearertoken='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NjgzNzc2NiwianRpIjoiNDlmMjFhZTktYjZlZS00NDNiLThlYmUtM2JjZTdhZTg3YzFkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjYzNTllZDAyOTk3NmY0ZjdjNmFmY2Q1MCIsIm5iZiI6MTY2NjgzNzc2NiwiZXhwIjoxNjY3NDQyNTY2fQ.nsf6y-afX1A5FL_CZ5ShnkwfqeW90CNK1DcrIF5NrOA'

curl -H 'Accept: application/json' -H 'Authorization: Bearer $bearertoken' -vvv  http://192.168.0.4:8800/api/topology -d '{ "reference": "urn:sdx:topology:tenet.ac.za","name": "Tenet-OXP","version": 1,"model_version": "1.0.0"}'
