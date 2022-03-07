"""
SDX Topology util Unit test
"""
from datetime import datetime
from pathlib import Path
from flask import Request
import numpy as np
import pandas as pd
import pytz
from openapi_core import create_spec
from openapi_core.contrib.flask import FlaskOpenAPIRequest
from openapi_core.validation.request.validators import RequestValidator
from openapi_spec_validator import validate_spec
from openapi_spec_validator.readers import read_from_filename
from napps.kytos.sdx_topology import utils  # pylint: disable=E0401

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def test_get_timestamp():
    '''test get_timestamp'''
    timestamp = '2022-02-18 14:41:10'
    if timestamp is not None:
        if len(timestamp) >= 19:
            timestamp = timestamp[:10]+"T"+timestamp[11:19]+"Z"
            assert timestamp == '2022-02-18T14:41:10Z'
        else:
            timestamp = datetime.now(
                    pytz.timezone(
                        "America/New_York")).strftime("%Y-%m-%dT%H:%M:%SZ")
    assert len(timestamp) >= 19


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
    root_dir = (Path(__file__).resolve().parent.parent.parent)
    yml_file = root_dir / "app" / "validator.yml"
    spec_dict, _ = read_from_filename(yml_file)
    content = create_spec(spec_dict).content()
    assert validate_spec(spec_dict) is None
    assert content['servers'][0]['url'] == '/api/kytos/sdx_topology'


def test_validate_request(valid_data):
    ''' test_validate_request '''
    spec = utils.load_spec()
    data = valid_data['payload']
    request = Request.from_values(
            '/api/kytos/sdx_topology/v1/validate',
            json=data,
            content_length=len(data),
            content_type='application/json',
            method='POST')
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
    assert error_response["errors"] == "no errors"
