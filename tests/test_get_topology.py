"""
    SDX
"""

import parse_topo
from tests import helper
import pytest


class TestGetTopology:
    """Tests that there is a topology in place"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_topology_incorrect_type_empty(self):
        """ Test empty type """
        _version = 1
        with pytest.raises(Exception) as valueerror:
            parse_topo.get_topology(kytos_topology="", version=_version, oxp_url="Amlight.net")
        assert str(valueerror.typename) == "ValueError"
        assert str(valueerror.value) == "Kytos_topology CANNOT be empty"

    def test_get_topology_incorrect_type_none(self):
        """ Test None type"""
        _version = 1
        with pytest.raises(Exception) as typeError:
            parse_topo.get_topology(kytos_topology=None, version=_version, oxp_url="Amlight.net")
        assert str(typeError.typename) == "TypeError"

    def test_get_topology_incorrect_type_list(self):
        """ Test list instead of dict """
        _version = 1
        with pytest.raises(Exception) as typeError:
            parse_topo.get_topology(kytos_topology=[], version=_version, oxp_url="Amlight.net")
        assert str(typeError.typename) == "TypeError"

    def test_get_topology_correct_return_type_dict(self):
        """ Test correct node object as a dict return case """

        result = parse_topo.get_topology(kytos_topology=helper._kytos_topology, version=helper._version,
                                         oxp_url="Amlight.net")

        assert result.__class__ == dict
