# coding: utf-8

"""
    SDX
"""

import parse_topo
import pytest
from tests import helper


class TestGetPort:
    """Tests that there is a topology in place"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_port_incorrect_type_empty(self):
        """ Test empty type """
        with pytest.raises(Exception) as valueerror:
            parse_topo.get_port(node="", interface="", oxp_url="Amlight.net")
        assert str(valueerror.typename) == "ValueError"
        assert str(valueerror.value) == "Interface and node CANNOT be empty"

    def test_get_port_incorrect_type_none(self):
        """ Test None type"""
        with pytest.raises(Exception) as typeError:
            parse_topo.get_port(node=None, interface=None, oxp_url="Amlight.net")
        assert str(typeError.typename) == "TypeError"

    def test_get_port_incorrect_type_list(self):
        """ Test list instead of string """
        with pytest.raises(Exception) as typeerror:
            parse_topo.get_port(node=[], interface=[], oxp_url="Amlight.net")
        assert str(typeerror.typename) == "TypeError"

    def test_get_port_incorrect_type_int(self):
        """ Test int instead of dictionary  """
        with pytest.raises(Exception) as typeError:
            parse_topo.get_port(node=1, interface=2, oxp_url="Amlight.net")
        assert str(typeError.typename) == "TypeError"

    def test_get_port_enabled_interface_case(self):
        """ Test that you get the proper value when interface value == disabled"""
        result = parse_topo.get_port(node=helper._node, interface=helper._interface, oxp_url="Amlight.net")
        assert result["state"] in ["enabled"]

    def test_get_port_correct_attributes_types(self):
        """ Test correct string node attribute, and dictionary interface object """

        result = parse_topo.get_port(node=helper._node, interface=helper._interface, oxp_url="Amlight.net")
        print(result)
        assert result == {'id': 'urn:sdx:port:Amlight.net:s1:1', 'name': 's1-eth1',
                          'node': 'urn:sdx:node:Amlight.net:s1', 'type': '10GE', 'nni':'False',
                          'mtu': '1500', 'status': 'up', 'state': 'enabled', 'services': 'l2vpn'}

    def test_get_port_correct_return_type_dict(self):
        """ Test correct port object as a dictionary return case """

        result = parse_topo.get_port(node=helper._node, interface=helper._interface, oxp_url="Amlight.net")

        assert result.__class__ == dict

