"""
SDX Topology API test
"""
import requests


def test_sdx_topology_id(api_data):
    """ test the SDX topology id get request end_to_end_test_1_4 """
    response = requests.get(
            url=api_data["url"]+"topology", headers=api_data["headers"])
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["id"].split(":")[3] == "amlight.net"
