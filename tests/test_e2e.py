"""
    End to End Tests

    Class designed to contain all the E2E tests pertaining to the
    kytos/sdx_topology napp to verify all its functionalities
"""


import itertools
from napps.kytos.sdx_topology import settings  # pylint: disable=E0401
from napps.kytos.sdx_topology.tests import e2e_support_functions as \
        get_req_to  # pylint: disable=E0401


def end_to_end_test_1_1():
    """Tests that the topology is up, and a basic schema is
    generated after the oxp_url & name are provided"""

    # submit get request and validate 200 response to /v1/topology

    get_req_to.kytos_sdx_topology_api(schema_url=settings.AMLIGHT_TOPOLOGY_URL)


def end_to_end_test_1_2():
    """Tests that the oxp_url endpoint was properly populated"""

    oxp_url = get_req_to.retrieve_oxp_endpoint(
            endpoint_name="oxp_url", schema_url=settings.AMLIGHT_TOPOLOGY_URL)

    if oxp_url == "amlight.net":
        print("Success")


def end_to_end_test_1_3():
    """Tests that the oxp_name endpoint was properly populated"""

    oxp_name = get_req_to.retrieve_oxp_endpoint(
            endpoint_name="oxp_name", schema_url=settings.AMLIGHT_TOPOLOGY_URL)

    if oxp_name == "AmLight":
        print("Success")


def end_to_end_test_1_4():
    """Test that the topology name was successfully added to the schema's 'id'
     attribute after been provided by an admin"""

    # Retrieve "id" from sdx topology

    req = get_req_to.amlight_sdx_topology_api(
            schema_url=settings.AMLIGHT_TOPOLOGY_UR)

    # Validate using .split 4th field populated with the proper topology name
    topo_id = str(req["id"].split(":")[3])
    if topo_id == "amlight.net":
        print("Success")


def end_to_end_test_1_5():
    """Test that the list of links is updated after manually enabling a link"""

    link_id = ""

    # Retrieve one link from kytos topology api
    topo = get_req_to.retrieve_kytos_topology(
            api_url=settings.KYTOS_TOPOLOGY_URL)

    if isinstance(topo, dict):
        for link in itertools.islice(topo['topology']['links'], 0, 1):
            # get only the first link
            link_id = link
    else:
        raise Exception("The returned Kytos topology is not a dictionary")

    # Enable Kytos Link
    get_req_to.enable_kytos_link(link_id=link_id)  # post method

    # Retrieve link list from sdx api and validate that LINK_Id is there
    req = get_req_to.amlight_sdx_topology_api(
            schema_url=settings.AMLIGHT_TOPOLOGY_URL)

    if isinstance(req, dict):
        if len(req['links']) == 1:
            print("Successfully tested that a link was added to the "
                  "list of links in the sdx schema!")
    else:
        raise Exception("returned Amlight-SDX topology is not a dictionary")

    # Disable link_id for future tests
    content = get_req_to.disable_kytos_link(link_id=link_id)  # POST method

    if content['topology']['links'][link_id]["enabled"] is False:
        print("Link_id was set to false in Kytos topology")

    print("Success")


def end_to_end_test_1_6():
    """Test that the list of dictionaries for nodes IS NOT empty upon napp
     initialization for the AMLIGHT node & validate # of switches"""

    # if switches list is empty, return error
    # else: retrieve the list of switches &
    # validate against expected number based on topology

    req = get_req_to.amlight_sdx_topology_api(
            schema_url=settings.AMLIGHT_TOPOLOGY)

    get_req_to.validate_sdx_nodes_number_and_content(
            sdx_topo=req, expected_nodes=11)


def end_to_end_test_1_7():
    """Test that the list of dictionaries for nodes IS NOT empty upon napp
     initialization for the SAX node & validate # of switches"""

    req = get_req_to.amlight_sdx_topology_api(
            schema_url=settings.SAX_TOPOLOGY_URL)

    get_req_to.validate_sdx_nodes_number_and_content(
            sdx_topo=req, expected_nodes=2)


def end_to_end_test_1_8():
    """Test that the list of dictionaries for nodes IS NOT empty upon napp
     initialization for the TENET node & validate # of switches"""

    req = get_req_to.amlight_sdx_topology_api(
            schema_url=settings.TENET_TOPOLOGY_URL)

    get_req_to.validate_sdx_nodes_number_and_content(
            sdx_topo=req, expected_nodes=3)


def end_to_end_test_1_9():
    """Test to confirm the node IDs are correct"""


def end_to_end_test_1_10():
    """Test to confirm ports IDs are correct"""


def end_to_end_test_1_11():
    """Test to confirm inter-domain nni ids are correct"""


def end_to_end_test_1_12():
    """ Tests that the timestamp is properly updated after a Kytos event
    was registered"""


def end_to_end_test_1_13():
    """Tests that the version is properly updated after an operational event
    was registered"""
