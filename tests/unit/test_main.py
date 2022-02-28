"""
SDX Topology main Unit test
"""
from dataclasses import dataclass
from napps.kytos.sdx_topology.main import Main as AppMain
from .helpers import get_controller_mock


@dataclass
class Main(AppMain):
    '''class main
    napps.kytos.sdx_topology.main.storehouse.StoreHouse.save_oxp_url'''
    # print(dir(AppMain))
    main = AppMain(get_controller_mock())


def test_oxp_url(mocker):
    '''function test oxp_name'''

    def mock_save_oxp_url():
        return 'amlight.net'

    mocker.patch(
            'napps.kytos.sdx_topology.main.storehouse.StoreHouse.save_oxp_url',
            mock_save_oxp_url)
    main = Main().main
    print(dir(main))
    main.oxp_url = 'amlight.net'
    actual = main.oxp_url
    assert actual == 'amlight.net'
