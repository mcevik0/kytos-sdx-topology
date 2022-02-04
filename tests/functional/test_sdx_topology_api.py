"""
SDX Topology API test
"""
import json
# from urllib.parse import quote
import requests

KYTOS_TOPOLOGY_URL = "http://localhost:8181/api/kytos/topology/v3/"


def test_kytos_topology(api_data):
    """ test a GET request to SDX validate end_to_end_test_1_1"""
    response = requests.get(
            url=KYTOS_TOPOLOGY_URL, headers=api_data["headers"])
    assert response.status_code == 200
    assert "topology" in response.json()


def test_oxp_url(api_data):
    """ test a POST and GET request to SDX topology APi to retrieve the current
    oxp_url end_to_end_test_1_2"""
    response = requests.post(
            url=api_data["url"]+"oxp_url", data=json.dumps("amlight.net"),
            headers=api_data["headers"])
    assert response.status_code == 200
    response = requests.get(
            url=api_data["url"]+"oxp_url", headers=api_data["headers"])
    assert response.status_code == 200
    assert isinstance(response.json(), str)
    assert "amlight.net" in response.json()


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


def test_sdx_topology_id(api_data):
    """ test the SDX topology id get request end_to_end_test_1_4 """
    response = requests.get(
            url=api_data["url"]+"topology", headers=api_data["headers"])
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["id"].split(":")[3] == "amlight.net"


def test_sdx_topology_link(api_data):
    """ test the SDX topology link get request end_to_end_test_1_5 """
    response = requests.get(
            url=KYTOS_TOPOLOGY_URL, headers=api_data["headers"])
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "links" in response.json()['topology']
    link_id = next(iter(response.json()['topology']['links']))
    url = f'{KYTOS_TOPOLOGY_URL}links/{link_id}/enable'
    response = requests.post(url=url, headers=api_data["headers"])
    assert response.status_code == 201


def test_validate(valid_data):
    """ test a GET request to SDX validate"""
    response = requests.post(
            url=valid_data["url"], data=json.dumps(valid_data["payload"]),
            headers=valid_data["headers"])
    assert response.status_code == 200
