"""
Topology validation test
"""
import json
import os

SWAGGER_PATH = "../../swagger/"
FUNCTIONAL_PATH = "/tests/functional/"


def valid_request():
    """Build json_data topology"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "valid_request.json"
    with open(topology_params, encoding="utf8") as json_file:
        data = json.load(json_file)
        json_file.close()
    return data


def valid_data():
    """Build json_data topology"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "sdx_topology.json"
    with open(topology_params, encoding="utf8") as json_file:
        data = json.load(json_file)
        json_file.close()
    return data


def api_data():
    """Build json_data topology"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "valid_api.json"
    with open(topology_params, encoding="utf8") as json_file:
        data = json.load(json_file)
        json_file.close()
    return data


def test_api(client) -> None:
    """
    :except: success
    """
    url = "http://0.0.0.0:8080/sdx/v2/topology"
    response = client.get(url, content_type="application/json")
    assert response.status_code == 200


def test_constructor(client, req_params) -> None:
    """
    :except: success
    """
    url = "http://0.0.0.0:8080/sdx/v2/constructor"
    headers = req_params["headers"]
    payload = {
        "id": req_params["id"],
        "name": req_params["name"],
        "version": req_params["version"],
        "model_version": req_params["model_version"],
        "timestamp": req_params["timestamp"],
        "nodes": req_params["nodes"],
        "links": req_params["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 200


def test_name_required(client, req_params):
    """test should_fail_due_to_missing_name_attribute_on_payload"""
    url = req_params["url"]
    headers = req_params["headers"]
    payload = {
        "id": req_params["id"],
        "version": req_params["version"],
        "model_version": req_params["model_version"],
        "timestamp": req_params["timestamp"],
        "nodes": req_params["nodes"],
        "links": req_params["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    assert "'name' is a required property" in response.json["error_message"]


def test_additional_properties(client):
    """test should_fail_due_to_additional_properties_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
        "active": True,
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    assert (
        "Additional properties are not allowed ('active' was unexpected)"
        in response.json["error_message"]
    )


def test_id_pattern(client):
    """test should_fail_due_to_invalid_id_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    payload = {
        "id": "sdx:topology:amlight.net",
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    message = "'sdx:topology:amlight.net' does not match "
    message += "'^((urn:sdx:topology:)[A-Za-z_.:-]*$)'"
    assert message in response.json["error_message"]


def test_name_pattern(client):
    """test should_fail_due_to_invalid_name_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    payload = {
        "id": json_data["id"],
        "name": "Amlight1",
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    message = "'Amlight1' does not match "
    message += "'^[A-Za-z_.-]*$'"
    assert message in response.json["error_message"]


def test_version_type(client):
    """test should_fail_due_to_invalid_version_type_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": "2",
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    assert "'2' is not of type integer" in response.json["error_message"]


def test_time(client):
    """test should_fail_due_to_invalid_date_time_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": "2021-12-31 21:19:40Z",
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    assert (
        "'2021-12-31 21:19:40Z' is not a 'date-time'" in response.json[
            "error_message"]
    )


def test_node_required(client):
    """test should_fail_due_to_missing_nodes_attribute_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    assert "'nodes' is a required property" in response.json["error_message"]


def test_empty_node_array(client):
    """test should_fail_due_to_empty_node_array_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    json_data["nodes"] = []
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    assert "[] is too short" in response.json["error_message"]


def test_node_additional_properties(client):
    """test should_fail_due_to_additional_properties_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    node = json_data["nodes"][0]
    node["active_node"] = 1
    json_data["nodes"][0] = node
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    assert (
        "Additional properties are not allowed \
            ('active_node' was unexpected)"
        in response.json["error_message"]
    )


def test_node_id_pattern(client):
    """test should_fail_due_to_invalid_id_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    json_data["nodes"][0]["id"] = "sdx:node:amlight.net:Ampath1"
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    message = "'sdx:node:amlight.net:Ampath1' does not match "
    message += "'^((urn:sdx:node:)[A-Za-z_.-\\\\:]*$)'"
    assert message in response.json["error_message"]


def test_node_name_required(client):
    """test should_fail_due_to_missing_name_attribute_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    node = json_data["nodes"][0]
    del node["name"]
    json_data["nodes"][0] = node
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    assert "'name' is a required property" in response.json["error_message"]


def test_node_name_pattern(client):
    """test should_fail_due_to_invalid_name_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    json_data["nodes"][0]["name"] = "Ampath1$"
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    message = "'Ampath1$' does not match '^[A-Za-z0-9_.-]*$'"
    assert message in response.json["error_message"]


def test_empty_node_port_array(client):
    """test should_fail_due_to_empty_node_port_array_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    json_data["nodes"][0]["ports"] = []
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    assert "[] is too short" in response.json["error_message"]


def test_node_port_additional_properties(client):
    """test should_fail_due_to_additional_properties_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    node_port = json_data["nodes"][0]["ports"][0]
    node_port["active_node_port"] = 1
    json_data["nodes"][0]["ports"][0] = node_port
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    assert (
        "Additional properties are not allowed \
            ('active_node_port' was unexpected)"
        in response.json["error_message"]
    )


def test_node_port_id_pattern(client):
    """test should_fail_due_to_invalid_id_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    json_data["nodes"][0]["ports"][0]["id"] = "sdx:port:amlight.net:Ampath1:1"
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    message = "'sdx:port:amlight.net:Ampath1:1' does not match "
    message += "'^((urn:sdx:port:)[A-Za-z_.-\\\\:]*$)'"
    assert message in response.json["error_message"]


def test_node_port_name_required(client):
    """test should_fail_due_to_missing_name_attribute_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    node_port = json_data["nodes"][0]["ports"][0]
    del node_port["name"]
    json_data["nodes"][0]["ports"][0] = node_port
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    assert "'name' is a required property" in response.json["error_message"]


def test_node_port_name_pattern(client):
    """test should_fail_due_to_invalid_name_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    json_data["nodes"][0]["ports"][0]["name"] = "Ampath1$"
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    message = "'Ampath1$' does not match '^[A-Za-z0-9_.-]*$'"
    assert message in response.json["error_message"]


def test_node_port_type_pattern(client):
    """test should_fail_due_to_invalid_type_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    json_data["nodes"][0]["ports"][0]["type"] = "200GE"
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    message = "'200GE' is not one of "
    message += "['100FE', '1GE', '10GE', '25GE', '40GE', '50GE', '100GE',"
    message += " '400GE', 'Other']"
    assert message in response.json["error_message"]


def test_node_port_status_pattern(client):
    """test should_fail_due_to_invalid_status_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    json_data["nodes"][0]["ports"][0]["status"] = "unknow"
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    message = "'unknow' is not one of ['up', 'down', 'error']"
    assert message in response.json["error_message"]


def test_node_port_state_pattern(client):
    """test should_fail_due_to_invalid_state_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    json_data["nodes"][0]["ports"][0]["state"] = "unknow"
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    message = "'unknow' is not one of ['enabled', 'disabled']"
    assert message in response.json["error_message"]


def test_empty_link_array(client):
    """test should_fail_due_to_empty_link_array_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    json_data["links"] = []
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    assert "[] is too short" in response.json["error_message"]


def test_link_additional_properties(client):
    """test should_fail_due_to_additional_properties_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    link = json_data["links"][0]
    link["active_link"] = 1
    json_data["links"][0] = link
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    assert (
        "Additional properties are not allowed \
            ('active_link' was unexpected)"
        in response.json["error_message"]
    )


def test_link_id_pattern(client):
    """test should_fail_due_to_invalid_id_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    json_data["links"][0]["id"] = "sdx:link:amlight.net:Ampath3/2_Ampath1/2"
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    message = "'sdx:link:amlight.net:Ampath3/2_Ampath1/2' does not match "
    message += "'^((urn:sdx:link:)[A-Za-z_.-\\\\:]*$)'"
    assert message in response.json["error_message"]


def test_link_name_required(client):
    """test should_fail_due_to_missing_name_attribute_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    link = json_data["links"][0]
    del link["name"]
    json_data["links"][0] = link
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    assert "'name' is a required property" in response.json["error_message"]


def test_link_name_pattern(client):
    """test should_fail_due_to_invalid_name_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    json_data["links"][0]["name"] = "Ampath1$"
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    message = "'Ampath1$' does not match '^[A-Za-z0-9_.-/]*$'"
    assert message in response.json["error_message"]


def test_empty_link_port_array(client):
    """test should_fail_due_to_empty_link_port_array_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    json_data["links"][0]["ports"] = []
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    assert "[] is too short" in response.json["error_message"]


def test_link_port_pattern(client):
    """test should_fail_due_to_invalid_port_pattern_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    json_data["links"][0]["ports"][0] = "sdx:port:amlight.net:Ampath1:1"
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    message = "'sdx:port:amlight.net:Ampath1:1' does not match "
    message += "'^((urn:sdx:port:)[A-Za-z_.-\\\\:]*$)'"
    assert message in response.json["error_message"]


def test_link_type_pattern(client):
    """test should_fail_due_to_invalid_type_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    json_data["links"][0]["type"] = "extra"
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    message = "'extra' is not one of "
    message += "['intra', 'inter']"
    assert message in response.json["error_message"]


def test_link_bandwidth_out_range(client):
    """test should_fail_due_to_bandwidth_out_of_range_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    json_data["links"][0]["bandwidth"] = 0
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    message = "0 is less than the minimum of 125000000"
    assert message in response.json["error_message"]


def test_link_residual_out_range(client):
    """test should_fail_due_to_residual_out_of_range_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    json_data["links"][0]["residual_bandwidth"] = 500
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    message = "500 is greater than the maximum of 100"
    assert message in response.json["error_message"]


def test_link_latency_out_range(client):
    """test should_fail_due_to_latency_out_of_range_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    json_data["links"][0]["latency"] = 125000000000
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    message = "125000000000 is greater than the maximum of 5000000000"
    assert message in response.json["error_message"]


def test_link_packet_loss_out_range(client):
    """test should_fail_due_to_bandwidth_out_of_range_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    json_data["links"][0]["packet_loss"] = 500
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    message = "500 is greater than the maximum of 100"
    assert message in response.json["error_message"]


def test_link_status_pattern(client):
    """test should_fail_due_to_invalid_status_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    json_data["links"][0]["status"] = "unknow"
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    message = "'unknow' is not one of ['up', 'down', 'error']"
    assert message in response.json["error_message"]


def test_state_pattern(client):
    """test should_fail_due_to_invalid_state_on_payload"""
    actual_dir = os.getcwd()
    topology_params = actual_dir + FUNCTIONAL_PATH + "topology_params.json"
    with open(topology_params, encoding="utf8") as json_file:
        json_data = json.load(json_file)
        json_file.close()
    url = json_data["url"]
    headers = json_data["headers"]
    json_data["links"][0]["state"] = "unknow"
    payload = {
        "id": json_data["id"],
        "name": json_data["name"],
        "version": json_data["version"],
        "model_version": json_data["model_version"],
        "timestamp": json_data["timestamp"],
        "nodes": json_data["nodes"],
        "links": json_data["links"],
    }
    request_data = json.dumps(payload)
    response = client.post(url, data=request_data, headers=headers)
    assert response.status_code == 400
    message = "'unknow' is not one of ['enabled', 'disabled', 'maintenance']"
    assert message in response.json["error_message"]
