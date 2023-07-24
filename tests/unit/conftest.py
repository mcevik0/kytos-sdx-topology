"""
Topology validation test
"""
import json
import os
import pytest
from swagger_server.__main__ import app

SWAGGER_PATH = "../../swagger/"
FUNCTIONAL_PATH = "/tests/functional/"


@pytest.fixture(scope="module")
def req_params():
    """setup function with json data"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    return json_data


@pytest.fixture(scope="module")
def client():
    """ creating connexion app """
    app_client = app.app.test_client()
    return app_client
