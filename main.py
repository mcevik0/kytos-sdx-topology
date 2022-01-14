"""
Main module of amlight/sdx Kytos Network Application.

SDX API
"""

import requests
import napps.amlight.sdx.storehouse
from napps.amlight.sdx import settings
from napps.amlight.sdx.topology_class import ParseTopology
from flask import jsonify, request
from kytos.core import rest
from kytos.core import KytosNApp, log
from kytos.core.helpers import listen_to
from kytos.core.napps import NAppsManager
from openapi_core import create_spec
from openapi_core.contrib.flask import FlaskOpenAPIRequest
from openapi_core.validation.request.validators import RequestValidator
from openapi_spec_validator import validate_spec
from openapi_spec_validator.readers import read_from_filename
from werkzeug.exceptions import (BadRequest, Conflict, Forbidden,
                                 MethodNotAllowed, NotFound,
                                 UnsupportedMediaType)

class Main(KytosNApp):
    """Main class of amlight/sdx NApp.

    This class is the entry point for this NApp.
    """

    def setup(self):
        """Replace the '__init__' method for the KytosNApp subclass.

        The setup method is automatically called by the controller when your
        application is loaded.

        So, if you have any setup routine, insert it here.
        """
        self.topology_loaded = False
        self.storehouse = None


    def execute(self):
        """Run after the setup method execution.

        You can also use this method in loop mode if you add to the above setup
        method a line like the following example:

            self.execute_as_loop(30)  # 30-second interval.
        """
        self.load_storehouse()

    def shutdown(self):
        """Run when your NApp is unloaded.

        If you have some cleanup procedure, insert it here.
        """
        pass

    @property
    def oxp_url(self):
        """ Property for OXP_URL """
        try:
            self.load_storehouse()
            return self.storehouse.get_data()["oxp_url"]
        except:
            return ""

    @oxp_url.setter
    def oxp_url(self, oxp_url):
        """ Property for OXP_URL """
        self.storehouse.save_oxp_url(oxp_url)

    @property
    def oxp_name(self):
        """ Property for OXP_NAME """
        try:
            self.load_storehouse()
            return self.storehouse.get_data()["oxp_name"]
        except:
            return ""

    @oxp_name.setter
    def oxp_name(self, oxp_name):
        """ Property for OXP_URL """
        self.storehouse.save_oxp_name(oxp_name)

    @listen_to('kytos/storehouse.loaded')
    def load_storehouse(self, event=None):  # pylint: disable=W0613
        """Function meant for validation, to make sure that the storehouse napp has been loaded
        before all the other functions that use it begins to call it."""
        log.info("Loading Storehouse")
        self.storehouse = napps.amlight.sdx.storehouse.StoreHouse(self.controller)

    @listen_to('kytos/topology.*')
    def load_topology(self, event=None):  # pylint: disable=W0613
        """Function meant for validation, to make sure that the storehouse napp has been loaded
        before all the other functions that use it begins to call it."""
        if not self.topology_loaded:
            if self.storehouse:
                if self.storehouse.box is not None:
                    self.create_update_topology()
                    self.topology_loaded = True
            else:
                self.topology_loaded = True

    @listen_to('kytos/topology.unloaded')
    def unload_topology(self):  # pylint: disable=W0613
        """Function meant for validation, to make sure that the storehouse napp has been loaded
        before all the other functions that use it begins to call it."""
        self.topology_loaded = False

    def test_kytos_topology(self):
        """ Test if the Topology napp has loaded """
        try:
            _ = self.get_kytos_topology()
            return True
        except Exception as err:
            log.info(err)
            return False

    @staticmethod
    def get_kytos_topology():
        """retrieve topology from API"""
        kytos_topology = requests.get(settings.topology_url).json()
        return kytos_topology["topology"]

    @rest('v1/oxp_url', methods=['GET'])
    def get_oxp_url(self):
        """ REST endpoint to RETRIEVE the SDX napp oxp_url"""
        return jsonify(self.oxp_url), 200

    @rest('v1/oxp_url', methods=['POST'])
    def set_oxp_url(self):
        """ REST endpoint to provide the SDX napp with the url provided by the operator"""
        try:
            self.oxp_url = request.get_json()

        except Exception as err:  # pylint: disable=W0703
            log.info(err)
            return jsonify(err), 401

        if not isinstance(self.oxp_url, str):
            return jsonify("Incorrect Type submitted"), 401

        return jsonify(self.oxp_url), 200

    @rest('v1/oxp_name', methods=['GET'])
    def get_oxp_name(self):
        """ REST endpoint to RETRIEVE the SDX napp domain_name"""
        return jsonify(self.oxp_name), 200

    @rest('v1/oxp_name', methods=['POST'])
    def set_oxp_name(self):
        """ REST endpoint to provide the SDX napp with the domain_name provided by the operator"""
        try:
            self.oxp_name = request.get_json()

        except Exception as err:  # pylint: disable=W0703
            log.info(err)
            return jsonify(err), 401

        if not isinstance(self.oxp_name, str):
            return jsonify("Incorrect Type submitted"), 401

        return jsonify(self.oxp_name), 200


    @rest('v1/topology')
    def get_topology_version(self):
        """ REST to return the topology following the SDX data model"""
        if not self.oxp_url:
            return jsonify\
                    ("Submit oxp_url previous to requesting topology schema"),\
                    401

        if not self.oxp_name:
            return jsonify\
                    ("Submit oxp_name previous to requesting topology schema"),\
                    401

        if self.topology_loaded or self.test_kytos_topology():
            try:
                topology_update = self.create_update_topology()
                topology_dict={
                        "id": topology_update["id"] ,
                        "name": topology_update["name"],
                        "version": topology_update["version"],
                        "model_version": topology_update["model_version"],
                        "timestamp": topology_update["timestamp"],
                        "nodes": topology_update["nodes"],
                        "links": topology_update["links"]
                        }
                validate_topology = requests.post(settings.validate_topology, json=topology_dict)
                if validate_topology.status_code == 200:
                    return jsonify(topology_update), 200
                else:
                    return jsonify(validate_topology.json()), 400
            except Exception as err:
                log.info(err)
                return jsonify("Validation Error"), 400

        # debug only
        log.info(self.topology_loaded)
        log.info(self.test_kytos_topology())
        return jsonify("Topology napp has not loaded"), 401


    def create_update_topology(self):
        """ Function that will take care of initializing the namespace
         kytos.storehouse.version within the storehouse and create a
         box object containing the version data that will be updated
         every time a change is detected in the topology."""
        self.storehouse.update_box()
        version = self.storehouse.get_data()["version"]
        return ParseTopology(topology=self.get_kytos_topology(),
                             version=version,
                             model_version="1.0.0",
                             oxp_name=self.oxp_name,
                             oxp_url=self.oxp_url).get_sdx_topology()
