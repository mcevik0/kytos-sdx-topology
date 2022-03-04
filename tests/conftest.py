"""
Fixtures for Topology validation test
"""
import os
import json
import pytest
from kytos.core.events import KytosEvent
from .run import create_app


@pytest.fixture(scope="session")
def flask_app():
    ''' flask app '''
    abs_file_path = os.path.abspath(os.path.dirname(__file__))
    openapi_path = os.path.join(abs_file_path, "../", "app")
    os.environ["SPEC_PATH"] = openapi_path

    app = create_app()
    return app


@pytest.fixture
def event():
    '''Returns a KytosEvents instance'''
    kevent = KytosEvent()
    return kevent


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


@pytest.fixture
def df_data():
    """ Build dataframe compare data """
    actual_dir = os.getcwd()
    file_a = actual_dir + "/tests/df1.json"
    file_b = actual_dir + "/tests/df2.json"
    with open(file_a, encoding="utf8") as encoded_a:
        json_a = json.load(encoded_a)
        encoded_a.close()
    with open(file_b, encoding="utf8") as encoded_b:
        json_b = json.load(encoded_b)
        encoded_b.close()
    return (json_a, json_b)
