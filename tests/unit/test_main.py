"""
SDX Topology main Unit test
"""
from dataclasses import dataclass
from napps.kytos.sdx_topology.main import Main
from tests.unit.helpers import get_controller_mock


@dataclass
class TestMain(Main):
    '''class main'''
    napp = Main(get_controller_mock())
    print(dir(napp))
    napp.oxp_name = 'amlight'
    print(napp.oxp_name)
    assert 2 == 1
    # name = napp.get_oxp_name()


def test_class():
    '''class main'''
    test = TestMain()
    print(test)
