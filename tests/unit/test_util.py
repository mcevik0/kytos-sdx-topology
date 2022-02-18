"""
SDX Topology util Unit test
"""
from app import utils  # pylint: disable=E0401


def test_get_timestamp():
    '''test get_timestamp'''
    timestamp = '2022-02-18 14:41:10'
    assert utils.get_timestamp(timestamp) == '2022-02-18T14:41:10Z'
