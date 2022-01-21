"""
    End to End Tests Support Functions

    Class designed to contain all the functions needed to run
    all E2E tests pertaining to the kytos/sdx_topology napp
"""

import sys
import requests
from flask import jsonify
from napps.kytos.sdx_topology import settings  \
        # pylint: disable=E0401


def kytos_sdx_topology_api(schema_url):
    """ Connects to kytos/sdx_topology topology API, looks for 200 status code,
     and returns sdx topology in json format"""

    response = requests.get(
                schema_url + "topology", headers=settings.HEADERS)
    if response.status_code != 200:
        print("Error connecting to kytos/sdx_topology API")
    else:
        print("Success")
    return response.json()


def retrieve_oxp_endpoint(endpoint_name, schema_url):
    """ Submits request to SDX API to retrieve and validate the oxp_name &
    oxp_url"""

    response = requests.get(
            schema_url + endpoint_name, headers=settings.HEADERS)
    if response.status_code != 200:
        print("Error connecting to kytos/sdx_topology API")
    else:
        print("Success")
    return response.json()


def retrieve_kytos_topology(api_url):
    """ Submits a GET request to Kytos APi to retrieve the current Kytos
    topology"""

    response = requests.get(api_url, headers=settings.HEADERS)
    if response.status_code != 200:
        print("Error connecting to Kytos API to retrieve topology")
    else:
        print("Success")
    return response.json()


def enable_kytos_link(link_id):
    """ Submits a POST request to Kytos API to enable a specific link"""

    enable_api_url = settings.KYTOS_TOPOLOGY_URL+"/links/"+link_id+"/enable"
    response = requests.post(enable_api_url, headers=settings.HEADERS)
    if response.status_code != 201:
        print("Error connecting to Kytos API to retrieve topology")
    else:
        print("Success")
    return response.json()


def disable_kytos_link(link_id):
    """ Submits a POST request to Kytos API to disable a specific link"""

    disable_api_url = settings.KYTOS_TOPOLOGY_URL+"/links/"+link_id+"/disable"
    response = requests.post(disable_api_url, headers=settings.HEADERS)
    if response.status_code != 201:
        print("Error connecting to Kytos API to retrieve topology")
    else:
        print("Success")
    content = requests.get(
            settings.KYTOS_TOPOLOGY_URL, headers=settings.HEADERS)
    if content.status_code != 200:
        print("Error connecting to Kytos topology API to disable link")

    return content.json()


def validate_sdx_nodes_number_and_content(sdx_topo, expected_nodes):
    """ Receives the sdx_topology and number of expected nodes to be found
    in either the amlight, sax, or tenet topologies and validates that the
    nodes list is NOT empty and contains the expected amount of nodes"""

    message = {"error": ""}
    status_code = 200

    if len(sdx_topo['nodes']) == 0:
        message = {"error": "List of nodes is EMPTY after Napp initialization"}
        status_code = 400
    elif isinstance(sdx_topo, dict):
        if len(sdx_topo['nodes']) != expected_nodes:
            message = {"error": "Unexpected number of nodes"}
            status_code = 400
    else:
        message = {"error": "Amlight-SDX topology isn't a dictionary"}
        status_code = 400
    return jsonify(message), status_code
