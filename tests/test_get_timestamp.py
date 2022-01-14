# coding: utf-8

"""
    SDX
"""


import parse_topo
import datetime


class TestGetTimeStamp:
    """Tests that there is a topology in place"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_correct_timestamp(self):

        current_timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        timestamp = parse_topo.get_time_stamp()

        assert timestamp == current_timestamp