"""
SDX Topology API test
"""
import requests

KYTOS_TOPOLOGY_URL = "http://localhost:8181/api/kytos/topology/v3/"


def test_kytos_topology(api_data):
    """ test a GET request to SDX validate end_to_end_test_1_1"""
    response = requests.get(
            url=KYTOS_TOPOLOGY_URL, headers=api_data["headers"])
    assert response.status_code == 200
    assert "topology" in response.json()
