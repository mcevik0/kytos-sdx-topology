"""
SDX Topology util Unit test
"""
import flask
from openapi_core.validation.request.validators import RequestValidator


def test_validate_request(flask_app):
    """test_validate_request"""
    spec = utils.load_spec()
    flask_app.test_request_context("/api/kytos/sdx_topology/v1/validate")
    validator = RequestValidator(spec)
    result = validator.validate(flask.request)
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
