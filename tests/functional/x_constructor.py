from json import JSONEncoder

import pytest
from connexion import App

SWAGGER_PATH = "path_to_directory_that_containes_swagger_file"


@pytest.fixture
def app():
    app = App(__name__, specification_dir=SWAGGER_PATH)
    app.app.json_encoder = JSONEncoder
    app.add_api("swagger.yaml")
    app_client = app.app.test_client()
    return app_client


def test_health(app) -> None:
    """
    :except: success
    """
    response = app.get("/health", content_type="application/json")
    assert response.status_code == 200
