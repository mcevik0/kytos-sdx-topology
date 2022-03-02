"""
SDX Topology API test
"""
import requests

KYTOS_TOPOLOGY_URL = "http://localhost:8181/api/kytos/topology/v3/"


def test_sdx_topology_nodes(api_data):
    """ test the SDX topology nodes get request end_to_end_test_1_6 """
    response = requests.get(
            url=api_data["url"]+"topology", headers=api_data["headers"])
    assert response.status_code == 200
    assert "nodes" in response.json()
    assert isinstance(response.json()["nodes"], list)
    assert len(response.json()["nodes"]) != 0
