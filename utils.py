"""Utility functions."""
from pathlib import Path

from openapi_core import create_spec
from openapi_core.contrib.flask import FlaskOpenAPIRequest
from openapi_core.validation.request.validators import RequestValidator
from openapi_spec_validator import validate_spec
from openapi_spec_validator.readers import read_from_filename
from kytos.core import log
from kytos.core.events import KytosEvent


def emit_event(controller, name, **kwargs):
    """Send an event when something happens with an EVC."""
    event_name = f"kytos/mef_eline.{name}"
    event = KytosEvent(name=event_name, content=kwargs)
    controller.buffers.app.put(event)


def compare_endpoint_trace(endpoint, vlan, trace):
    """Compare and endpoint with a trace step."""
    return (
        endpoint.switch.dpid == trace["dpid"]
        and endpoint.port_number == trace["port"]
        and vlan == trace["vlan"]
    )


def load_spec():
    """Validate openapi spec."""
    napp_dir = Path(__file__).parent
    yml_file = napp_dir / "validator.yml"
    spec_dict, _ = read_from_filename(yml_file)

    validate_spec(spec_dict)

    return create_spec(spec_dict)


def validate(spec, data_request):
    """Decorator to validate a REST endpoint input.

    Uses the schema defined in the openapi.yml file
    to validate.
    """
    validator = RequestValidator(spec)
    openapi_request = FlaskOpenAPIRequest(data_request)
    result = validator.validate(openapi_request)
    print('############ result ####################')
    print(result)
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
        log.info('############ error_response ####################')
        log.info("error response: %s", error_response)
        return {"data": error_response, "code": 400}
    return {"data": data_request.json, "code": 200}
