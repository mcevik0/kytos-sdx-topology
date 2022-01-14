# coding: utf-8

"""
    SDX
"""

import parse_topo
import pytest
from tests import helper


class TestGetNodes:
    """Tests that there is a topology in place"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_nodes_incorrect_type_empty(self):
        """ Test empty type """
        with pytest.raises(Exception) as valueerror:
            parse_topo.get_nodes(switches="", oxp_url="Amlight.net")
        assert str(valueerror.typename) == "ValueError"
        assert str(valueerror.value) == "Switches CANNOT be empty"

    def test_get_nodes_incorrect_type_none(self):
        """ Test None type"""
        with pytest.raises(Exception) as attributeError:
            parse_topo.get_nodes(switches=None, oxp_url="Amlight.net")
        assert str(attributeError.typename) == "AttributeError"

    def test_get_nodes_incorrect_type_list(self):
        """ Test list instead of dict """
        with pytest.raises(Exception) as attributeError:
            parse_topo.get_nodes(switches=[], oxp_url="Amlight.net")
        assert str(attributeError.typename) == "AttributeError"

    def test_get_nodes_incorrect_type_int(self):
        """ Test int instead of dictionary  """
        with pytest.raises(Exception) as attributeError:
            parse_topo.get_nodes(switches=2, oxp_url="Amlight.net")
        assert str(attributeError.typename) == "AttributeError"

    def test_get_nodes_correct_return_type_list(self):
        """ Test correct node object as a list return case """

        result = parse_topo.get_nodes(switches=helper._switches, oxp_url="Amlight.net")

        assert result.__class__ == list
