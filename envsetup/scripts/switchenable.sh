#!/bin/bash
IP=44.198.243.137;
for sw in $(curl -s http://$IP:8181/api/kytos/topology/v3/switches |  jq -r '.switches[].id'); 
  do 
    curl -H 'Content-type: application/json' -X POST http://$IP:8181/api/kytos/topology/v3/switches/$sw/enable; 
    curl -H 'Content-type: application/json' -X POST http://$IP:8181/api/kytos/topology/v3/interfaces/switch/$sw/enable; 
  done
sleep 10
for l in $(curl -s http://$IP:8181/api/kytos/topology/v3/links | jq -r '.links[].id'); 
  do curl -H 'Content-type: application/json' -X POST http://$IP:8181/api/kytos/topology/v3/links/$l/enable; 
done
