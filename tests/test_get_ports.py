# coding: utf-8

"""
    SDX
"""

import parse_topo
import pytest


class TestGetPorts:
    """Tests that there is a topology in place"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_ports_incorrect_type_empty(self):
        """ Test empty type """
        with pytest.raises(Exception) as attributeerror:
            parse_topo.get_ports(node="", interfaces="", oxp_url="Amlight.net")
        assert str(attributeerror.typename) == "AttributeError"

    def test_get_ports_incorrect_type_none(self):
        """ Test None type"""
        with pytest.raises(Exception) as attributeError:
            parse_topo.get_ports(node=None, interfaces=None, oxp_url="Amlight.net")
        assert str(attributeError.typename) == "AttributeError"

    def test_get_ports_incorrect_type_list(self):
        """ Test list instead of dictionary  """
        with pytest.raises(Exception) as attributeerror:
            parse_topo.get_ports(node=[], interfaces=[], oxp_url="Amlight.net")
        assert str(attributeerror.typename) == "AttributeError"

    def test_get_ports_incorrect_type_int(self):
        """ Test list instead of dictionary  """
        with pytest.raises(Exception) as attributeerror:
            parse_topo.get_ports(node=1, interfaces=2, oxp_url="Amlight.net")
        assert str(attributeerror.typename) == "AttributeError"

    def test_get_ports_correct_return_type_list_with_proper_attrbibutes(self):
        """ Test correct string node attribute, and dictionary interfaces object """

        _node = "s1"
        _interfaces = {}  # TODO save full printout when kytos wants to work again to helper file

        result = parse_topo.get_ports(node=_node, interfaces=_interfaces, oxp_url="Amlight.net")
        assert result.__class__ == list
