"""
SDX Topology main Unit test
"""
from dataclasses import dataclass
from napps.kytos.sdx_topology.main import Main as AppMain
from tests.unit.helpers import get_controller_mock


@dataclass
class Main(AppMain):
    '''class main
    napps.kytos.sdx_topology.main.storehouse.StoreHouse.save_oxp_url'''
    # print(dir(AppMain))
    main = AppMain(get_controller_mock())


def test_oxp_url(mocker):
    '''function test oxp_name'''

    def mock_oxp_url():
        return 'amlight.net'

    mocker.patch(
            'app.main.StoreHouse.save_oxp_url',
            mock_oxp_url)
    Main().main.oxp_url = 'amlight.net'
    actual = Main().main.oxp_url
    print(actual)
    assert actual == 'amlight.net'
