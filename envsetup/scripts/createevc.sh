#!/bin/sh
curl -H 'Content-type: application/json' -X POST http://44.198.243.137:8181/api/kytos/mef_eline/v2/evc -d '{"name": "my evc1", "dynamic_backup_path": true, "enabled": true, "uni_z": {"tag": {"value": 198, "tag_type": 1}, "interface_id": "00:00:00:00:00:00:00:02:1"}, "uni_a": {"tag": {"value": 198, "tag_type": 1}, "interface_id": "00:00:00:00:00:00:00:01:1"}}'
