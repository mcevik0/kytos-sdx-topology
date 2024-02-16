#!/bin/bash

# VLAN 107 - same VLAN
docker exec -it mininet bash -c 'mnexec -a $(pgrep -f -x bash.*mininet:h8) ip link add link h8-eth1 name vlan107 type vlan id 107'
docker exec -it mininet bash -c 'mnexec -a $(pgrep -f -x bash.*mininet:h8) ip link set up vlan107'
docker exec -it mininet bash -c 'mnexec -a $(pgrep -f -x bash.*mininet:h8) ip addr add 10.1.7.8/24 dev vlan107'
docker exec -it mininet bash -c 'mnexec -a $(pgrep -f -x bash.*mininet:h3) ip link add link h3-eth1 name vlan107 type vlan id 107'
docker exec -it mininet bash -c 'mnexec -a $(pgrep -f -x bash.*mininet:h3) ip link set up vlan107'
docker exec -it mininet bash -c 'mnexec -a $(pgrep -f -x bash.*mininet:h3) ip addr add 10.1.7.3/24 dev vlan107'
docker exec -it mininet bash -c 'mnexec -a $(pgrep -f -x bash.*mininet:h3) ping -c4 10.1.7.8'

# VLAN 201 - VLAN translation
docker exec -it mininet bash -c 'mnexec -a $(pgrep -f -x bash.*mininet:h8) ip link add link h8-eth1 name vlan201 type vlan id 201'
docker exec -it mininet bash -c 'mnexec -a $(pgrep -f -x bash.*mininet:h8) ip link set up vlan201'
docker exec -it mininet bash -c 'mnexec -a $(pgrep -f -x bash.*mininet:h8) ip addr add 10.2.1.8/24 dev vlan201'
docker exec -it mininet bash -c 'mnexec -a $(pgrep -f -x bash.*mininet:h3) ip link add link h3-eth1 name vlan201 type vlan id 201'
docker exec -it mininet bash -c 'mnexec -a $(pgrep -f -x bash.*mininet:h3) ip link set up vlan201'
docker exec -it mininet bash -c 'mnexec -a $(pgrep -f -x bash.*mininet:h3) ip addr add 10.2.1.3/24 dev vlan201'
docker exec -it mininet bash -c 'mnexec -a $(pgrep -f -x bash.*mininet:h3) ping -c4 10.2.1.8'
