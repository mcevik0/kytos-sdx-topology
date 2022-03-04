""" flask app for test """
import os
import connexion


def create_app():
    """ flask app for test """
    if "SPEC_PATH" in os.environ:
        openapi_path = os.environ["SPEC_PATH"]
    else:
        abs_file_path = os.path.abspath(os.path.dirname(__file__))
        openapi_path = os.path.join(abs_file_path, "../", "../", "app")
    app = connexion.FlaskApp(
        __name__,
        specification_dir=openapi_path
    )
    app.add_api("validator.yml", strict_validation=True)
    flask_app = app.app

    return flask_app
