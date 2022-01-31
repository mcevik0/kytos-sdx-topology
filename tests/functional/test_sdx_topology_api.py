"""
SDX Topology API test
"""
import json
import requests

KYTOS_TOPOLOGY_URL = "http://localhost:8181/api/kytos/topology/v3/"


def test_kytos_topology(api_data):
    """ test a GET request to SDX validate"""
    response = requests.get(
            url=KYTOS_TOPOLOGY_URL, headers=api_data["headers"])
    print(response.json())
    assert response.status_code == 200
    assert "topology" in response.json()


def test_oxp_url(api_data):
    """ test a POST and GET request to SDX topology APi to retrieve the current
    oxp_url"""
    response = requests.post(
            url=api_data["url"]+"oxp_url", data=json.dumps("amlight.net"),
            headers=api_data["headers"])
    assert response.status_code == 200
    response = requests.get(
            url=api_data["url"]+"oxp_url", headers=api_data["headers"])
    assert response.status_code == 200
    assert "amlight.net" in response.json()


def test_oxp_name(api_data):
    """ test a POST and GET request to SDX topology APi to retrieve the current
    oxp_name"""
    response = requests.post(
            url=api_data["url"]+"oxp_name", data=json.dumps("Amlight"),
            headers=api_data["headers"])
    assert response.status_code == 200
    response = requests.get(
            url=api_data["url"]+"oxp_name", headers=api_data["headers"])
    assert response.status_code == 200
    assert isinstance(response.json(), str)
    assert "Amlight" in response.json()


def test_validate(valid_data):
    """ test a GET request to SDX validate"""
    response = requests.post(
            url=valid_data["url"], data=json.dumps(valid_data["payload"]),
            headers=valid_data["headers"])
    assert response.status_code == 200
