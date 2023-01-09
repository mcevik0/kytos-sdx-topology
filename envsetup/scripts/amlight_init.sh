#!/bin/bash

SDX_API="http://0.0.0.0:8181/api/kytos/sdx_topology/v1"
TOPOLOGY_API="http://0.0.0.0:8181/api/kytos/topology/v3"

# SDX-related variables
echo '########## oxp_name ########## '
curl -H 'Content-Type: application/json' -X POST -d'"AmLight"' $SDX_API/oxp_name
echo '########## oxp_url ########## '
curl -H 'Content-Type: application/json' -X POST -d'"amlight.net"' $SDX_API/oxp_url

# Per-switch variables

# Ampath1
echo '########## Ampath1 ########## '
echo 'aa:00:00:00:00:00:00:01/enable'
curl -H 'Content-Type: application/json' -X POST $TOPOLOGY_API/switches/aa:00:00:00:00:00:00:01/enable
echo 'aa:00:00:00:00:00:00:01/metadata node_name'
curl -H 'Content-Type: application/json' -X POST -d'{"node_name": "Ampath1"}' $TOPOLOGY_API/switches/aa:00:00:00:00:00:00:01/metadata
echo 'aa:00:00:00:00:00:00:01/metadata address'
curl -H 'Content-Type: application/json' -X POST -d'{"address": "Equinix MI1, Miami, FL"}' $TOPOLOGY_API/switches/aa:00:00:00:00:00:00:01/metadata
echo 'aa:00:00:00:00:00:00:01:1/enable'
curl -H 'Content-Type: application/json' -X POST $TOPOLOGY_API/interfaces/aa:00:00:00:00:00:00:01:1/enable
echo 'aa:00:00:00:00:00:00:01:2/enable'
curl -H 'Content-Type: application/json' -X POST $TOPOLOGY_API/interfaces/aa:00:00:00:00:00:00:01:2/enable
echo 'aa:00:00:00:00:00:00:01:40/enable'
curl -H 'Content-Type: application/json' -X POST $TOPOLOGY_API/interfaces/aa:00:00:00:00:00:00:01:40/enable
echo 'aa:00:00:00:00:00:00:01:50/enable'
curl -H 'Content-Type: application/json' -X POST $TOPOLOGY_API/interfaces/aa:00:00:00:00:00:00:01:50/enable
echo 'aa:00:00:00:00:00:00:01:1/metadata eth1'
curl -H 'Content-Type: application/json' -X POST -d'{"mtu": 9000, "port_name": "eth1"}' $TOPOLOGY_API/interfaces/aa:00:00:00:00:00:00:01:1/metadata
echo 'aa:00:00:00:00:00:00:01:2/metadata eth2'
curl -H 'Content-Type: application/json' -X POST -d'{"mtu": 9000, "port_name": "eth2"}' $TOPOLOGY_API/interfaces/aa:00:00:00:00:00:00:01:2/metadata
echo 'aa:00:00:00:00:00:00:01:40/metadata eth40'
curl -H 'Content-Type: application/json' -X POST -d'{"mtu": 9000, "port_name": "eth40"}' $TOPOLOGY_API/interfaces/aa:00:00:00:00:00:00:01:40/metadata
echo 'aa:00:00:00:00:00:00:01:50/metadata eth50'
curl -H 'Content-Type: application/json' -X POST -d'{"mtu": 9000, "port_name": "eth50"}' $TOPOLOGY_API/interfaces/aa:00:00:00:00:00:00:01:50/metadata

# Ampath2
echo '########## Ampath2 ########## '
echo 'aa:00:00:00:00:00:00:02/enable'
curl -H 'Content-Type: application/json' -X POST $TOPOLOGY_API/switches/aa:00:00:00:00:00:00:02/enable
echo 'aa:00:00:00:00:00:00:02/metadata node_name'
curl -H 'Content-Type: application/json' -X POST -d'{"node_name": "Ampath2"}' $TOPOLOGY_API/switches/aa:00:00:00:00:00:00:02/metadata
echo 'aa:00:00:00:00:00:00:02/metadata address'
curl -H 'Content-Type: application/json' -X POST -d'{"address": "Equinix MI1, Miami, FL"}' $TOPOLOGY_API/switches/aa:00:00:00:00:00:00:02/metadata
echo 'aa:00:00:00:00:00:00:02:1/enable'
curl -H 'Content-Type: application/json' -X POST $TOPOLOGY_API/interfaces/aa:00:00:00:00:00:00:02:1/enable
echo 'aa:00:00:00:00:00:00:02:3/enable'
curl -H 'Content-Type: application/json' -X POST $TOPOLOGY_API/interfaces/aa:00:00:00:00:00:00:02:3/enable
echo 'aa:00:00:00:00:00:00:02:40/enable'
curl -H 'Content-Type: application/json' -X POST $TOPOLOGY_API/interfaces/aa:00:00:00:00:00:00:02:40/enable
echo 'aa:00:00:00:00:00:00:02:50/enable'
curl -H 'Content-Type: application/json' -X POST $TOPOLOGY_API/interfaces/aa:00:00:00:00:00:00:02:50/enable
echo 'aa:00:00:00:00:00:00:02:1/metadata eth1'
curl -H 'Content-Type: application/json' -X POST -d'{"mtu": 9000, "port_name": "eth1"}' $TOPOLOGY_API/interfaces/aa:00:00:00:00:00:00:02:1/metadata
echo 'aa:00:00:00:00:00:00:02:3/metadata eth3'
curl -H 'Content-Type: application/json' -X POST -d'{"mtu": 9000, "port_name": "eth3"}' $TOPOLOGY_API/interfaces/aa:00:00:00:00:00:00:02:3/metadata
echo 'aa:00:00:00:00:00:00:02:40/metadata eth40'
curl -H 'Content-Type: application/json' -X POST -d'{"mtu": 9000, "port_name": "eth40"}' $TOPOLOGY_API/interfaces/aa:00:00:00:00:00:00:02:40/metadata
echo 'aa:00:00:00:00:00:00:02:50/metadata eth50'
curl -H 'Content-Type: application/json' -X POST -d'{"mtu": 9000, "port_name": "eth50"}' $TOPOLOGY_API/interfaces/aa:00:00:00:00:00:00:02:50/metadata

# Ampath3
echo '########## Ampath3 ########## '
echo 'aa:00:00:00:00:00:00:03/enable'
curl -H 'Content-Type: application/json' -X POST $TOPOLOGY_API/switches/aa:00:00:00:00:00:00:03/enable
echo 'aa:00:00:00:00:00:00:03/metadata node_name'
curl -H 'Content-Type: application/json' -X POST -d'{"node_name": "Ampath3"}' $TOPOLOGY_API/switches/aa:00:00:00:00:00:00:03/metadata
echo 'aa:00:00:00:00:00:00:03/metadata address'
curl -H 'Content-Type: application/json' -X POST -d'{"address": "Equinix MI1, Miami, FL"}' $TOPOLOGY_API/switches/aa:00:00:00:00:00:00:03/metadata
echo 'aa:00:00:00:00:00:00:03:2/enable'
curl -H 'Content-Type: application/json' -X POST $TOPOLOGY_API/interfaces/aa:00:00:00:00:00:00:03:2/enable
echo 'aa:00:00:00:00:00:00:03:3/enable'
curl -H 'Content-Type: application/json' -X POST $TOPOLOGY_API/interfaces/aa:00:00:00:00:00:00:03:3/enable
echo 'aa:00:00:00:00:00:00:03:50/enable'
curl -H 'Content-Type: application/json' -X POST $TOPOLOGY_API/interfaces/aa:00:00:00:00:00:00:03:50/enable
echo 'aa:00:00:00:00:00:00:03:2/metadata eth2'
curl -H 'Content-Type: application/json' -X POST -d'{"mtu": 9000, "port_name": "eth2"}' $TOPOLOGY_API/interfaces/aa:00:00:00:00:00:00:03:2/metadata
echo 'aa:00:00:00:00:00:00:03:3/metadata eth3'
curl -H 'Content-Type: application/json' -X POST -d'{"mtu": 9000, "port_name": "eth3"}' $TOPOLOGY_API/interfaces/aa:00:00:00:00:00:00:03:3/metadata
echo 'aa:00:00:00:00:00:00:03:50/metadata eth50'
curl -H 'Content-Type: application/json' -X POST -d'{"mtu": 9000, "port_name": "eth50"}' $TOPOLOGY_API/interfaces/aa:00:00:00:00:00:00:03:50/metadata


# AmLight inter-domain port
curl -H 'Content-Type: application/json' -X POST -d'{"nni": "urn:sdx:port:sax.net:Sax01:40"}' $TOPOLOGY_API/interfaces/aa:00:00:00:00:00:00:01:40/metadata
curl -H 'Content-Type: application/json' -X POST -d'{"link_name": "Link_SAX_1"}' $TOPOLOGY_API/interfaces/aa:00:00:00:00:00:00:01:40/metadata

curl -H 'Content-Type: application/json' -X POST -d'{"nni": "urn:sdx:port:sax.net:Sax02:40"}' $TOPOLOGY_API/interfaces/aa:00:00:00:00:00:00:02:40/metadata
curl -H 'Content-Type: application/json' -X POST -d'{"link_name": "Link_SAX_2"}' $TOPOLOGY_API/interfaces/aa:00:00:00:00:00:00:02:40/metadata

# Enable links
sleep 3

for LINK in $(curl -sH 'Content-Type: application/json'  $TOPOLOGY_API/links | python -m json.tool | fgrep "\"link\":" | sed 's/[ |,|"]//g'|cut -d":" -f2 | uniq);
  do
    curl -H 'Content-Type: application/json' -X POST $TOPOLOGY_API/links/$LINK/enable;

    echo '{"link_name": "Link_random"}' |  sed "s/random/${LINK:0:18}/" > /tmp/random.json;
    curl -H 'Content-Type: application/json' -X POST -d@/tmp/random.json $TOPOLOGY_API/links/$LINK/metadata;

    echo '{"packet_loss": 0.00random}' |  sed "s/random/${RANDOM:0:10}/" > /tmp/random.json;
    curl -H 'Content-Type: application/json' -X POST -d@/tmp/random.json $TOPOLOGY_API/links/$LINK/metadata;

    curl -H 'Content-Type: application/json' -X POST -d'{"availability": 99.5}' $TOPOLOGY_API/links/$LINK/metadata;

    echo '{"residual_bandwidth": random}' |  sed "s/random/${RANDOM:0:2}/" > /tmp/random.json;
    curl -H 'Content-Type: application/json' -X POST -d@/tmp/random.json $TOPOLOGY_API/links/$LINK/metadata;

    echo '{"latency": random}' |  sed "s/random/${RANDOM:0:2}/" > /tmp/random.json;
    curl -H 'Content-Type: application/json' -X POST -d@/tmp/random.json $TOPOLOGY_API/links/$LINK/metadata;
  done
