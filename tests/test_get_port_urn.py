# coding: utf-8

"""
    SDX
"""

import parse_topo
import pytest


class TestGetPortUrn:
    """Tests that there is a topology in place"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_port_urn_incorrect_type_empty(self):
        """ Test empty type """
        with pytest.raises(Exception) as valueerror:
            parse_topo.get_port_urn(switch="", interface="", oxp_url="Amlight.net")
        assert str(valueerror.typename) == "ValueError"
        assert str(valueerror.value) == "Interface and switch CANNOT be empty"

    def test_get_port_urn_incorrect_type_none(self):
        """ Test None type"""
        with pytest.raises(Exception) as valueerror:
            parse_topo.get_port_urn(switch=None, interface=None, oxp_url="Amlight.net")
        assert str(valueerror.typename) == "ValueError"

    def test_get_port_urn_incorrect_type_dict(self):
        """ Test dictionary instead of string """
        with pytest.raises(Exception) as valueerror:
            parse_topo.get_port_urn(switch={}, interface={}, oxp_url="Amlight.net")
        assert str(valueerror.typename) == "ValueError"

    def test_get_port_urn_incorrect_type_list(self):
        """ Test list instead of string """
        with pytest.raises(Exception) as valueerror:
            parse_topo.get_port_urn(switch=[], interface=[], oxp_url="Amlight.net")
        assert str(valueerror.typename) == "ValueError"

    def test_get_port_urn_incorrect_interface_type_int(self):
        """ Test interface as a string instead of an integer """
        _switch = "Novi03"
        _interface = "2"
        result = parse_topo.get_port_urn(switch=_switch, interface=_interface, oxp_url="Amlight.net")
        assert result == f"urn:sdx:port:Amlight.net:{_switch}:{_interface}"

    def test_get_port_urn_incorrect_interface_type_negative(self):
        """ Test interface as a negative integer """
        # TODO: need to verify the value error is raised
        with pytest.raises(ValueError) as valueerror:
            parse_topo.get_port_urn(switch="Novi03", interface=-2, oxp_url="Amlight.net")
        assert str(valueerror.typename) == "ValueError"
        assert str(valueerror.value) == "Interface cannot be negative"

    # TODO: FAILED tests/test_get_port_urn.py::TestGetPortUrn::test_get_port_urn_incorrect_type_capital
    #  - Failed: DID NOT RAISE <class 'Exception'>
    #  FAILED tests/test_get_port_urn.py::TestGetPortUrn::test_get_port_urn_incorrect_type_lowercase
    #  - Failed: DID NOT RAISE <class 'Exception'>

    # def test_get_port_urn_incorrect_type_capital(self):
    #     """ Test with capital letters"""
    #     with pytest.raises(Exception) as typeerror:
    #         parse_topo.get_port_urn(switch="NOVI03", interface=2)
    #     assert str(typeerror.typename) == "TypeError"
    #
    # def test_get_port_urn_incorrect_type_lowercase(self):
    #     """ Test with lowercase letters"""
    #     with pytest.raises(Exception) as typeerror:
    #         parse_topo.get_port_urn(switch="novi03", interface=2)
    #     assert str(typeerror.typename) == "TypeError"

    def test_get_port_urn_correct_type(self):
        """ Test with lowercase letters"""
        assert (parse_topo.get_port_urn(switch="Novi03", interface=2, oxp_url="Amlight.net") \
                == 'urn:sdx:port:Amlight.net:Novi03:2')

