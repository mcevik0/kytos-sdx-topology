#!/bin/bash
# Creates a circuit between AmLight (h3) and TENET (h8) -- using VLAN translation, i.e., endpoints will be VLAN 201, intermediate VLANs will be 202 and 203

# Amlight domain
curl -H 'Content-type: application/json' 'http://0.0.0.0:8181/api/kytos/mef_eline/v2/evc/' -d '{"name": "AMLIGHT_vlan_201_202_Ampath_Tenet", "dynamic_backup_path": true, "uni_a": {"tag": {"value": 201, "tag_type": 1}, "interface_id": "aa:00:00:00:00:00:00:03:50"}, "uni_z": {"tag": {"value": 202, "tag_type": 1}, "interface_id": "aa:00:00:00:00:00:00:01:40"}}'

# SAX domain
curl -H 'Content-type: application/json' 'http://0.0.0.0:8282/api/kytos/mef_eline/v2/evc/' -d '{"name": "SAX_vlan_202_203_Ampath_Tenet", "dynamic_backup_path": true, "uni_a": {"tag": {"value": 202, "tag_type": 1}, "interface_id": "dd:00:00:00:00:00:00:04:40"}, "uni_z": {"tag": {"value": 203, "tag_type": 1}, "interface_id": "dd:00:00:00:00:00:00:05:41"}}'

# TENET domain
curl -H 'Content-type: application/json' 'http://0.0.0.0:8383/api/kytos/mef_eline/v2/evc/' -d '{"name": "TENET_vlan_201_203_Ampath_Tenet", "dynamic_backup_path": true, "uni_a": {"tag": {"value": 203, "tag_type": 1}, "interface_id": "cc:00:00:00:00:00:00:07:41"}, "uni_z": {"tag": {"value": 201, "tag_type": 1}, "interface_id": "cc:00:00:00:00:00:00:08:50"}}'
