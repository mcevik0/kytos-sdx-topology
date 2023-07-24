"""SDX Topology Utility functions"""
from flask import Request
from napps.kytos.sdx_topology import utils  # pylint: disable=E0401


def test_get_timestamp():
    """Function to obtain the current time_stamp in a specific format"""
    timestamp = "2022-02-18 14:41:10"
    assert utils.get_timestamp(timestamp) == "2022-02-18T14:41:10Z"
    assert len(utils.get_timestamp()) >= 19


def test_diff_pd(df_data):
    """Identify differences between two pandas DataFrames"""
    json_a, json_b, json_xb = df_data
    result_a = utils.diff_pd(json_a, json_b)
    result_x = utils.diff_pd(json_a, json_xb)
    assert result_a["from"] == result_a["to"]
    assert result_x["from"] != result_a["to"]


def test_load_spec():
    """Validate openapi spec."""
    content = utils.load_spec().content()
    assert content["servers"][0]["url"] == "/api/kytos/sdx_topology"


def test_validate_request(valid_data):
    """Decorator to validate a REST endpoint input.

    Uses the schema defined in the openapi.yml file
    to validate.
    """
    spec = utils.load_spec()
    data = valid_data["payload"]
    request = Request.from_values(
        "/api/kytos/sdx_topology/v1/validate",
        json=data,
        content_length=len(data),
        content_type="application/json",
        method="POST",
    )
    _, status_code = utils.validate_request(spec, request)
    assert status_code == 200
