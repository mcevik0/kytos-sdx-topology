"""
Fixtures for Topology validation test
"""
import os
import json
import pytest


@pytest.fixture
def valid_data():
    """ Build json_data topology """
    actual_dir = os.getcwd()
    topology_params = actual_dir + "/tests/sdx_topology_validate.json"
    with open(topology_params, encoding="utf8") as json_file:
        data = json.load(json_file)
        json_file.close()
    return data


@pytest.fixture
def api_data():
    """ Build json_data topology """
    actual_dir = os.getcwd()
    topology_params = actual_dir + "/tests/sdx_topology_api.json"
    with open(topology_params, encoding="utf8") as json_file:
        data = json.load(json_file)
        json_file.close()
    return data
