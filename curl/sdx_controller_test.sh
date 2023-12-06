curl -X 'POST' \
  'http://localhost:8080/SDX-Controller/1.0.0/conection' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": "test-connection-request",
    "name": "Test connection request",
    "start_time": "2000-01-23T04:56:07.000Z",
    "end_time": "2000-01-23T04:56:07.000Z",
    "bandwidth_required": 10,
    "latency_required": 300,
    "egress_port": {
        "id": "urn:sdx:port:ampath.net:A1:1",
        "name": "Novi100:1",
        "node": "urn:sdx:node:amlight.net:A1",
        "status": "up"
    },
    "ingress_port": {
        "id": "urn:ogf:network:sdx:port:tenet.ac.za:A1:2",
        "name": "Novi100:2",
        "node": "urn:ogf:network:sdx:node:tenet:A1",
        "status": "up"
    }
}'
