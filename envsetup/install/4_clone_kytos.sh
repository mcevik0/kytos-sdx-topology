#!/bin/sh
for repo in python-openflow kytos-utils kytos flow_manager mef_eline of_core of_lldp pathfinder storehouse topology; do
  git clone https://github.com/kytos-ng/${repo}
done
git clone https://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@github.com/atlanticwave-sdx/kytos-sdx-topology sdx_topology
