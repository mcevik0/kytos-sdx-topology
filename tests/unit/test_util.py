"""
SDX Topology util Unit test
"""
import numpy as np
import pandas as pd
from openapi_core.contrib.flask import FlaskOpenAPIRequest
from openapi_core.validation.request.validators import RequestValidator
from napps.kytos.sdx_topology import utils  # pylint: disable=E0401

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def test_get_timestamp():
    '''test get_timestamp'''
    timestamp = '2022-02-18 14:41:10'
    assert utils.get_timestamp(timestamp) == '2022-02-18T14:41:10Z'


def test_diff_pd(df_data):
    """Identify differences between two pandas DataFrames"""
    current_dict = [v for (k, v) in df_data[0].items()]
    current_df = pd.json_normalize(current_dict)
    initial_dict = [v for (k, v) in df_data[1].items()]
    initial_df = pd.json_normalize(initial_dict)

    assert (current_df.columns == initial_df.columns).all(), \
        "DataFrame column names are different"
    if any(current_df.dtypes != initial_df.dtypes):
        # Data Types are different, trying to convert
        initial_df = initial_df.astype(current_df.dtypes)
    if current_df.equals(initial_df):
        assert True
    else:
        diff_mask = (current_df != initial_df) & \
                ~(current_df.isnull() & initial_df.isnull())
        ne_stacked = diff_mask.stack()
        changed = ne_stacked[ne_stacked]
        changed.index.names = ['id', 'col']
        difference_locations = np.where(diff_mask)
        changed_from = current_df.values[difference_locations]
        changed_to = initial_df.values[difference_locations]
        assert changed_from[0] != changed_to[0]


def test_load_spec():
    '''test load_spec'''
    content = utils.load_spec().content()
    assert content['servers'][0]['url'] == '/api/kytos/sdx_topology'


def test_validate_request(requests_mock):
    ''' test_validate_request '''
    request_url = 'http://0.0.0.0:8181/api/kytos/sdx_topology/v1/validate'
    request = requests_mock.post(request_url, json={})
    print(request)
    spec = utils.load_spec()
    validator = RequestValidator(spec)
    openapi_request = FlaskOpenAPIRequest(request)
    result = validator.validate(openapi_request)
    error_response = {"errors": "no errors"}
    if result.errors:
        errors = result.errors[0]
        if hasattr(errors, "schema_errors"):
            schema_errors = errors.schema_errors[0]
            error_response = {
                "error_message": schema_errors.message,
                "error_validator": schema_errors.validator,
                "error_validator_value": schema_errors.validator_value,
                "error_path": list(schema_errors.path),
                "error_schema": schema_errors.schema,
                "error_schema_path": list(schema_errors.schema_path),
                }
        else:
            error_response = {"errors": errors}
    print(error_response)
    assert error_response["errors"] == "no errors"
