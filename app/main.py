"""
Main module of amlight/sdx Kytos Network Application.

SDX API
"""

import requests
from flask import jsonify, request
from werkzeug.exceptions import BadRequest, UnsupportedMediaType

from kytos.core import KytosNApp, log, rest
from kytos.core.helpers import listen_to
from napps.kytos.sdx_topology import settings  # pylint: disable=E0401
from napps.kytos.sdx_topology import storehouse  # pylint: disable=E0401
from napps.kytos.sdx_topology.topology_class import (ParseTopology) \
        # pylint: disable=E0401
from napps.kytos.sdx_topology import utils  # pylint: disable=E0401

spec = utils.load_spec()


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
        self.initial_kytos_topology = self.current_kytos_topology \
            # pylint: disable=W0201

    def shutdown(self):
        """Run when your NApp is unloaded.

        If you have some cleanup procedure, insert it here.
        """

    @property
    def oxp_url(self):
        """ Property for OXP_URL"""
        try:
            data = self.storehouse.get_data()
        except Exception:  # pylint: disable=W0703
            return ""
        if "oxp_url" in data:
            return data["oxp_url"]
        return ""

    @oxp_url.setter
    def oxp_url(self, oxp_url):
        """ Setter for OXP_URL """
        self.storehouse.save_oxp_url(oxp_url)

    @property
    def oxp_name(self):
        """ Property for OXP_NAME """
        try:
            data = self.storehouse.get_data()
        except Exception:  # pylint: disable=W0703
            return ""
        if "oxp_name" in data:
            return data["oxp_name"]
        return ""

    @oxp_name.setter
    def oxp_name(self, oxp_name):
        """ Property for OXP_URL """
        self.storehouse.save_oxp_name(oxp_name)

    @property
    def current_kytos_topology(self):
        """ Property for Topology """
        return self.get_kytos_topology

    @listen_to('kytos/storehouse.loaded')
    def load_storehouse(self, event=None):  # pylint: disable=W0613
        """Function meant for validation, to make sure that the storehouse napp
        has been loaded before all the other functions that use it begins to
        call it."""
        if self.storehouse is None:
            self.storehouse = storehouse.StoreHouse(self.controller)  \
                    # pylint: disable=W0201

    @listen_to("kytos/topology.*")
    def load_topology(self, event=None):  # pylint: disable=W0613
        """Function meant for validation, to make sure that the storehouse
        napp has been loaded before all the other functions that use it begins
        to call it."""
        event_type = 0
        if event.name in settings.ADMIN_EVENTS:
            event_type = 1
        elif (
                event.name in settings.OPERATIONAL_EVENTS and
                event.timestamp is not None):
            event_type = 2
        else:
            return {"error": "None"}

        if self.storehouse:
            if self.storehouse.box is not None:
                self.topology_loaded = True  # pylint: disable=W0201
                return self.create_update_topology(event_type, event.timestamp)
            return {"error": "not self.storehouse.box"}
        return {"error": "not self.storehouse"}

    @listen_to("kytos/topology.unloaded")
    def unload_topology(self):  # pylint: disable=W0613
        """Function meant for validation, to make sure that the storehouse napp
        has been loaded before all the other functions that use it begins to
        call it."""
        self.topology_loaded = False  # pylint: disable=W0201

    def test_kytos_topology(self):
        """ Test if the Topology napp has loaded """
        try:
            _ = self.get_kytos_topology()
            return True
        except Exception as err:  # pylint: disable=W0703
            log.info(err)
            return False

    @staticmethod
    def get_kytos_topology():
        """retrieve topology from API"""
        kytos_topology = requests.get(settings.KYTOS_TOPOLOGY_URL).json()
        return kytos_topology["topology"]

    @rest("v1/oxp_url", methods=["GET"])
    def get_oxp_url(self):
        """ REST endpoint to RETRIEVE the SDX napp oxp_url"""
        return jsonify(self.oxp_url), 200

    @rest("v1/oxp_url", methods=["POST"])
    def set_oxp_url(self):
        """REST endpoint to provide the SDX napp with the url provided by the
        operator"""
        try:
            self.oxp_url = request.get_json()

        except Exception as err:  # pylint: disable=W0703
            log.info(err)
            return jsonify(err), 401

        if not isinstance(self.oxp_url, str):
            return jsonify("Incorrect Type submitted"), 401

        return jsonify(self.oxp_url), 200

    @rest("v1/oxp_name", methods=["GET"])
    def get_oxp_name(self):
        """ REST endpoint to RETRIEVE the SDX napp domain_name"""
        return jsonify(self.oxp_name), 200

    @rest("v1/oxp_name", methods=["POST"])
    def set_oxp_name(self):
        """REST endpoint to provide the SDX napp with the domain_name provided
        by the operator"""
        try:
            oxp_name = request.get_json()

        except BadRequest:
            result = "The request body is not a well-formed JSON."
            log.info("oxp_name result %s %s", result, 400)
            raise BadRequest(result) from BadRequest

        if not isinstance(oxp_name, str):
            return jsonify("Incorrect Type submitted"), 401
        self.oxp_name = oxp_name
        return jsonify(oxp_name), 200

    @rest("v1/validate", methods=["POST"])
    def get_validate(self):
        """ REST to validate the topology following the SDX data model"""
        if self.topology_loaded or self.test_kytos_topology():
            try:
                data = request.json
            except BadRequest:
                result = "The request body is not a well-formed JSON."
                log.info("Validate data result %s %s", result, 400)
                raise BadRequest(result) from BadRequest
            if data is None:
                result = "The request body mimetype is not application/json."
                log.info("update result %s %s", result, 415)
                raise UnsupportedMediaType(result)
            response = utils.validate_request(spec, request)
            return jsonify(response["data"]), response["code"]
        # debug only
        log.info(self.topology_loaded)
        log.info(self.test_kytos_topology())
        return jsonify("Topology napp has not loaded"), 401

    @rest("v1/topology")
    def get_topology_version(self):
        """ REST to return the topology following the SDX data model"""
        log.info("######### v1/topology ##########")
        if not self.oxp_url:
            log.info("######### not self.oxp_url ##########")
            return (
                jsonify("Submit oxp_url previous to request topology schema"),
                401,
            )

        if not self.oxp_name:
            log.info("######### not self.oxp_name ##########")
            return (
                jsonify("Submit oxp_name previous to request topology schema"),
                401,
            )

        if self.topology_loaded or self.test_kytos_topology():
            try:
                log.info("########## topology update ##########")
                topology_update = self.create_update_topology()
                log.info(topology_update)
                topology_dict = {
                    "id": topology_update["id"],
                    "name": topology_update["name"],
                    "version": topology_update["version"],
                    "model_version": topology_update["model_version"],
                    "timestamp": topology_update["timestamp"],
                    "nodes": topology_update["nodes"],
                    "links": topology_update["links"],
                }
                validate_topology = requests.post(
                    settings.VALIDATE_TOPOLOGY, json=topology_dict
                )
                if validate_topology.status_code == 200:
                    return jsonify(topology_update), 200
                return jsonify(validate_topology.json()), 400
            except Exception as err:  # pylint: disable=W0703
                log.info(err)
                return jsonify("Validation Error"), 400

        # debug only
        log.info(self.topology_loaded)
        log.info(self.test_kytos_topology())
        return jsonify("Topology napp has not loaded"), 401

    @rest("v1/eval_kytos_topology", methods=["POST"])
    def get_df_diff(self):
        """ REST to return the kytos topology with pandas df """
        eval_param = request.get_json()
        current_params = self.current_kytos_topology()[eval_param]
        initial_params = self.initial_kytos_topology()[eval_param]
        params_diff = {}
        if current_params and initial_params:
            params_diff = utils.diff_pd(current_params, initial_params)
        return jsonify(params_diff), 200

    def create_update_topology(self, event_type=0, event_timestamp=None):
        """Function that will take care of initializing the namespace
        kytos.storehouse.version within the storehouse and create a
        box object containing the version data that will be updated
        every time a change is detected in the topology."""
        log.info("########## create_update_topology ##########")
        if event_type == 1:
            self.storehouse.update_box()
        elif event_type == 2:
            self.storehouse.update_timestamp(event_timestamp)
        log.info("########## version ##########")
        version = self.storehouse.get_data()["version"]
        log.info("########## timestamp ##########")
        timestamp = self.storehouse.get_data()["time_stamp"]
        log.info("########## end timestamp ##########")
        log.info(timestamp)
        return ParseTopology(
            topology=self.get_kytos_topology(),
            version=version,
            timestamp=timestamp,
            model_version="1.0.0",
            oxp_name=self.oxp_name,
            oxp_url=self.oxp_url,
        ).get_sdx_topology()
