#!/bin/sh
for repo in python-openflow kytos-utils kytos flow_manager mef_eline of_core of_lldp pathfinder storehouse topology; do
  cd ${repo}
  python3 setup.py develop
  cd ..
done
cd sdx_topology/app
python3 setup.py develop
cd ..
