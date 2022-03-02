"""
SDX Topology API test
"""
import requests

KYTOS_TOPOLOGY_URL = "http://localhost:8181/api/kytos/topology/v3/"


def test_sdx_topology_links(api_data):
    """ test the SDX topology links get request end_to_end_test_1_7 """
    response = requests.get(
            url=api_data["url"]+"topology", headers=api_data["headers"])
    assert response.status_code == 200
    assert "links" in response.json()
    assert isinstance(response.json()["links"], list)
    assert len(response.json()["links"]) != 0
