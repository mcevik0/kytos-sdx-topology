"""
SDX Topology main Unit test
"""
from napps.kytos.sdx_topology import main  # pylint: disable=E0401


def test_load_topology(event):
    '''test event class'''
    event.name = "kytos/topology.switch.enabled"
    print(event.name, event.timestamp)
    assert event.name == "kytos/topology.switch.enabled"
    print(main.storehouse)
