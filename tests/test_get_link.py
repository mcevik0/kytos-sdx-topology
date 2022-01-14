"""
    SDX
"""

import parse_topo
import pytest
from tests import helper


class TestGetLink:
    """Tests that there is a topology in place"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_link_incorrect_type_empty(self):
        """ Test empty type """
        with pytest.raises(Exception) as valueerror:
            parse_topo.get_link(kytos_link="", oxp_url=helper._oxp_url)
        assert str(valueerror.typename) == "ValueError"
        assert str(valueerror.value) == "Kytos_link CANNOT be empty"

    def test_get_link_incorrect_type_none(self):
        """ Test None type"""
        with pytest.raises(Exception) as typeError:
            parse_topo.get_link(kytos_link=None, oxp_url=helper._oxp_url)
        assert str(typeError.typename) == "TypeError"

    def test_get_link_incorrect_type_list(self):
        """ Test list instead of dict """
        with pytest.raises(Exception) as typeError:
            parse_topo.get_link(kytos_link=[], oxp_url=helper._oxp_url)
        assert str(typeError.typename) == "TypeError"

    def test_get_link_incorrect_type_int(self):
        """ Test int instead of dictionary  """
        with pytest.raises(Exception) as typeerror:
            parse_topo.get_link(kytos_link=2, oxp_url=helper._oxp_url)
        assert str(typeerror.typename) == "TypeError"

    def test_get_link_correct_return_type_dict(self):
        """ Test correct node object as a list return case """

        result = parse_topo.get_link(kytos_link=helper._kytos_link, oxp_url=helper._oxp_url)

        assert result.__class__ == dict
