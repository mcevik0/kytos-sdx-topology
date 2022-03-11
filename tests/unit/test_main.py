"""
SDX Topology main Unit test
"""
from dataclasses import dataclass
import requests
from napps.kytos.sdx_topology.main import Main as AppMain
from napps.kytos.sdx_topology.storehouse import StoreHouse as AppStoreHouse
from .helpers import get_controller_mock


@dataclass
class Main(AppMain):
    '''class main
    napps.kytos.sdx_topology.main.storehouse.StoreHouse.save_oxp_url'''
    main = AppMain(get_controller_mock())


@dataclass
class StoreHouse(AppStoreHouse):
    '''class StoreHouse
    napps.kytos.sdx_topology.main.storehouse.StoreHouse.save_oxp_url'''
    storehouse = AppStoreHouse(get_controller_mock())


def test_setup():
    """Replace the '__init__' method for the KytosNApp subclass."""
    Main().main.setup()
    assert Main().main.topology_loaded is False


def test_mock_oxp_url(mocker):
    '''function test oxp_url'''

    def mock_oxp_url():
        return ''

    mocker.patch(
            'napps.kytos.sdx_topology.main.Main.oxp_url',
            mock_oxp_url)
    Main().main.oxp_url = 'amlight.net'
    assert Main().main.oxp_url == 'amlight.net'


def test_mock_oxp_name(mocker):
    '''function test oxp_name'''

    def mock_oxp_name():
        return ''

    mocker.patch(
            'napps.kytos.sdx_topology.main.Main.oxp_name',
            mock_oxp_name)
    Main().main.oxp_name = 'AmLight'
    assert Main().main.oxp_name == 'AmLight'


def test_get_oxp_name(api_data):
    """ test a GET request to SDX topology APi to retrieve the current
    oxp_name end_to_end_test_1_3"""
    response = requests.get(
            url=api_data["url"]+"oxp_name", headers=api_data["headers"])
    assert response.status_code == 200
    assert isinstance(response.json(), str)
    assert "Amlight" in response.json()


def test_get_validate(mocker, valid_data):
    """ REST to validate the topology following the SDX data model"""

    def mock_validate_request(spec=None, data_request=None):
        data_request = valid_data['payload']
        spec = 200
        return {"data": data_request, "code": spec}

    mocker.patch(
            'napps.kytos.sdx_topology.utils.validate_request',
            mock_validate_request)

    response = Main().main.get_validate()
    assert "data" in response


def test_create_update_topology(mocker, valid_data):
    """ Function that will take care of initializing the namespace
        kytos.storehouse.version within the storehouse and create a
        box object containing the version data that will be updated
        every time a change is detected in the topology."""

    print(dir(Main.main.storehouse))
    response = Main().main.create_update_topology()
    assert "id" in response
