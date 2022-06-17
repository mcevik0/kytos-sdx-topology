"""SDX topology Utility functions"""
from datetime import datetime
from pathlib import Path
from openapi_core import create_spec
from openapi_core.contrib.flask import FlaskOpenAPIRequest
from openapi_core.validation.request.validators import RequestValidator
from openapi_spec_validator import validate_spec
from openapi_spec_validator.readers import read_from_filename
import pytz
from kytos.core import log


def get_timestamp(timestamp=None):
    """Function to obtain the current time_stamp in a specific format"""
    if timestamp is not None:
        if isinstance(timestamp, datetime):
            timestamp = timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif len(timestamp) >= 19:
            timestamp = timestamp[:10]+"T"+timestamp[11:19]+"Z"
    else:
        timestamp = datetime.now(
            pytz.timezone("America/New_York")).strftime("%Y-%m-%dT%H:%M:%SZ")
    return timestamp


def load_spec():
    """Validate openapi spec."""
    napp_dir = Path(__file__).parent
    yml_file = napp_dir / "validator.yml"
    spec_dict, _ = read_from_filename(yml_file)

    validate_spec(spec_dict)

    return create_spec(spec_dict)


def validate_request(spec, data_request):
    """Decorator to validate a REST endpoint input.

    Uses the schema defined in the openapi.yml file
    to validate.
    """
    validator = RequestValidator(spec)
    openapi_request = FlaskOpenAPIRequest(data_request)
    result = validator.validate(openapi_request)
    error_response = {}
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
        return (error_response, 400)
    return (data_request.json, 200)
