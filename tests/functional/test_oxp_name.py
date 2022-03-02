"""
SDX Topology API test
"""
import json
import requests


def test_oxp_name(api_data):
    """ test a POST and GET request to SDX topology APi to retrieve the current
    oxp_name end_to_end_test_1_3"""
    response = requests.post(
            url=api_data["url"]+"oxp_name", data=json.dumps("Amlight"),
            headers=api_data["headers"])
    assert response.status_code == 200
    response = requests.get(
            url=api_data["url"]+"oxp_name", headers=api_data["headers"])
    assert response.status_code == 200
    assert isinstance(response.json(), str)
    assert "Amlight" in response.json()
