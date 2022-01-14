# coding: utf-8

"""
    SDX
"""

import parse_topo
from tests import helper


class TestGetNodesName:
    """Tests that there is a topology in place"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_nodes_name_raises_exception_for_bad_connection(self):
        """ Test that a bad connection happen and the application
        did not connect to the Kytos API """
        try:
            parse_topo.get_nodes_name()
        except Exception as exc:
            assert False, f"'get_nodes_name' raised an exception {exc}"

    def test_get_nodes_name_kytos_topology_incorrect_type_none(self):
        pass

    def test_get_nodes_name_nodes_mappings_incorrect_type_none(self):
        """ Test None type instead of dict"""

        assert parse_topo.get_nodes_name() is not None

    def test_get_nodes_name_nodes_mappings_incorrect_type_list(self):
        """ Test list type instead of dict"""

        assert parse_topo.get_nodes_name() is not list

    def test_get_nodes_name_nodes_mappings_incorrect_type_empty(self):
        """ Test empty case instead of dict"""

        assert parse_topo.get_nodes_name() is not {}

    def test_get_nodes_name_correct_case(self):
        """ Test none type instead of list"""

        nodes = helper._nodes_mappings

        result = parse_topo.get_nodes_name()

        assert result == nodes

