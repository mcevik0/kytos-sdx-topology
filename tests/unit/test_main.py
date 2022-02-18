"""
SDX Topology main Unit test
"""


def test_load_topology(event):
    '''test event class'''
    event.name = "kytos/topology.switch.enabled"
    print(event.name, event.timestamp)
    assert event.name == "kytos/topology.switch.enabled"
