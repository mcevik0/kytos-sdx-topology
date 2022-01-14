"""
    End to End Tests

    Class designed to contain all the E2E tests pertaining to the
    Amlight-SDx napp to verify all its functionalities
"""


import itertools
from napps.amlight.sdx.settings import amlight_schema_url, sax_schema_url,\
     tenet_schema_url, kytos_topology_url
from napps.amlight.sdx.tests.e2e_support_functions import submit_get_req_to_amlight_sdx_topology_api
from napps.amlight.sdx.tests.e2e_support_functions import submit_get_req_to_retrieve_oxp_endpoint
from napps.amlight.sdx.tests.e2e_support_functions import submit_get_req_to_retrieve_kytos_topology
from napps.amlight.sdx.tests.e2e_support_functions import submit_post_req_to_enable_kytos_link
from napps.amlight.sdx.tests.e2e_support_functions import submit_post_req_to_disable_kytos_link
from napps.amlight.sdx.tests.e2e_support_functions import validate_sdx_nodes_number_and_content


def end_to_end_test_1_1():
    """Tests that the topology is up, and a basic schema is
    generated after the oxp_url & name are provided"""

    # submit get request and validate 200 response to /v1/topology

    submit_get_req_to_amlight_sdx_topology_api(schema_url=amlight_schema_url)


def end_to_end_test_1_2():
    """Tests that the oxp_url endpoint was properly populated"""

    oxp_url = submit_get_req_to_retrieve_oxp_endpoint(endpoint_name="oxp_url",
                                                      schema_url=amlight_schema_url)

    if oxp_url == "amlight.net":
        print("Success")


def end_to_end_test_1_3():
    """Tests that the oxp_name endpoint was properly populated"""

    oxp_name = submit_get_req_to_retrieve_oxp_endpoint(endpoint_name="oxp_name",
                                                       schema_url=amlight_schema_url)

    if oxp_name == "AmLight":
        print("Success")


def end_to_end_test_1_4():
    """Test that the topology name was successfully added to the schema's 'id'
     attribute after been provided by an admin"""

    # Retrieve "id" from sdx topology

    req = submit_get_req_to_amlight_sdx_topology_api(schema_url=amlight_schema_url)

    # Validate using .split that the 4th field is populated with the proper topology name
    topo_id = str(req["id"].split(":")[3])
    if topo_id == "amlight.net": print("Success")


def end_to_end_test_1_5():
    """Test that the list of links is updated after manually enabling a link"""

    link_id = ""

    # Retrieve one link from kytos topology api
    topo = submit_get_req_to_retrieve_kytos_topology(api_url=kytos_topology_url)

    if isinstance(topo, dict):
        for link in itertools.islice(topo['topology']['links'], 0, 1):  # get only the first link
            link_id = link
    else:
        raise Exception("The returned Kytos topology is not a dictionary")

    # Enable Kytos Link
    submit_post_req_to_enable_kytos_link(link_id=link_id)

    # Retrieve link list from sdx api and validate that LINK_Id is there
    req = submit_get_req_to_amlight_sdx_topology_api(schema_url=amlight_schema_url)

    if isinstance(req, dict):
        if len(req['links']) == 1:
            print("Successfully tested that a link was added to the "
                  "list of links in the sdx schema!")
    else:
        raise Exception("The returned Amlight-SDX topology is not a dictionary")

    # Disable link_id for future tests
    content = submit_post_req_to_disable_kytos_link(link_id=link_id)

    if content['topology']['links'][link_id]["enabled"] is False:
        print("Successfully confirmed that the link_id was set to false again in Kytos topology")

    print("Success")


def end_to_end_test_1_6():
    """Test that the list of dictionaries for nodes IS NOT empty upon napp
     initialization for the AMLIGHT node & validate # of switches"""

    # if switches list is empty, return error
    # else: retrieve the list of switches & validate against expected number based on topology

    req = submit_get_req_to_amlight_sdx_topology_api(schema_url=amlight_schema_url)

    validate_sdx_nodes_number_and_content(sdx_topo=req, expected_nodes=11)


def end_to_end_test_1_7():
    """Test that the list of dictionaries for nodes IS NOT empty upon napp
     initialization for the SAX node & validate # of switches"""

    req = submit_get_req_to_amlight_sdx_topology_api(schema_url=sax_schema_url)

    validate_sdx_nodes_number_and_content(sdx_topo=req, expected_nodes=2)


def end_to_end_test_1_8():
    """Test that the list of dictionaries for nodes IS NOT empty upon napp
     initialization for the TENET node & validate # of switches"""

    req = submit_get_req_to_amlight_sdx_topology_api(schema_url=tenet_schema_url)

    validate_sdx_nodes_number_and_content(sdx_topo=req, expected_nodes=3)


def end_to_end_test_1_9():
    """Test to confirm the node IDs are correct"""
    pass


def end_to_end_test_1_10():
    """Test to confirm ports IDs are correct"""
    pass


def end_to_end_test_1_11():
    """Test to confirm inter-domain nni ids are correct"""
    pass


def end_to_end_test_1_12():
    """ Tests that the timestamp is properly updated after a Kytos event
    was registered"""
    pass


def end_to_end_test_1_13():
    """Tests that the version is properly updated after an operational event
    was registered"""
    pass
