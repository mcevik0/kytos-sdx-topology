"""
SDX Topology API test
"""
import json
import requests


def test_validate(valid_data):
    """ test a GET request to SDX validate"""
    response = requests.post(
            url=valid_data["url"], data=json.dumps(valid_data["payload"]),
            headers=valid_data["headers"])
    assert response.status_code == 200
