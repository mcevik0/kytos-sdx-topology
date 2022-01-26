"""
Fixtures for Topology validation test
"""
import os
import json
import pytest


@pytest.fixture
def json_data():
    """ Build json_data topology """
    actual_dir = os.getcwd()
    topology_params = actual_dir + "/tests/topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        data = json.load(json_file)
        json_file.close()
    return data
