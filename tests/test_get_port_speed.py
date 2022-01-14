# coding: utf-8

"""
    SDX
"""

import parse_topo


class TestGetPortSpeed:
    """Tests that there is a topology in place"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_speed_modification_100(self):

        speed = parse_topo.get_port_speed(100000000)

        assert speed == "100GE"

    def test_speed_modification_10(self):

        speed = parse_topo.get_port_speed(1250000000)

        assert speed == "10GE"

    def test_speed_modification_1(self):

        speed = parse_topo.get_port_speed(125000000)

        assert speed == "1GE"
