"""Module to help to create tests."""
from unittest.mock import Mock
from httpx import AsyncClient

from kytos.core import Controller
from kytos.core.config import KytosConfig


def get_controller_mock():
    """Return a controller mock."""
    options = KytosConfig().options['daemon']
    controller = Controller(options)
    controller.log = Mock()
    return controller


def get_test_client(controller, napp) -> AsyncClient:
    """Return an async api test client."""
    controller.api_server.register_napp_endpoints(napp)
    app = controller.api_server.app
    base_url = "http://0.0.0.0/api/"
    return AsyncClient(app=app, base_url=base_url)
