"""
Main module of amlight/sdx Kytos Network Application.
"""
import requests
from flask import request, jsonify
from werkzeug.exceptions import BadRequest, UnsupportedMediaType

from kytos.core import KytosNApp, rest, log
from kytos.core.helpers import listen_to
from napps.kytos.sdx_topology import settings  # pylint: disable=E0401
from napps.kytos.sdx_topology import storehouse  # pylint: disable=E0401
from napps.kytos.sdx_topology.topology_class import (ParseTopology) \
        # pylint: disable=E0401
from napps.kytos.sdx_topology import utils  # pylint: disable=E0401

spec = utils.load_spec()


class Main(KytosNApp):  # pylint: disable=R0904
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
        """ Property for OXP_URL """
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

    @property
    def storehouse(self):
        """ Property for storehouse """
        try:
            my_storehouse = storehouse.StoreHouse(self.controller)  \
                    # pylint: disable=W0201
        except Exception:  # pylint: disable=W0703
            return storehouse.get_store_house()
        return my_storehouse

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
        admin_events = [
                "kytos/topology.switch.enabled",
                "kytos/topology.switch.disabled"]
        operational_events = [
                "kytos/topology.link_up",
                "kytos/topology.link_down"]
        if event.name in admin_events:
            event_type = 1
        elif event.name in operational_events and event.timestamp is not None:
            event_type = 2
        else:
            return {"error": "None"}

        if self.storehouse:
            if self.storehouse.box is not None:
                self.topology_loaded = True  # pylint: disable=W0201
                return self.get_topology_version(event_type, event.timestamp)
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
            raise BadRequest(result) from BadRequest

        if not isinstance(oxp_name, str):
            return jsonify("Incorrect Type submitted"), 401
        self.oxp_name = oxp_name
        return jsonify(oxp_name), 200

    @rest("v1/validate", methods=["POST"])
    def validate_sdx_topology(self):
        """ REST to validate the topology following the SDX data model"""
        response, status_code = self.get_validate()
        return jsonify(response), status_code

    def get_validate(self):
        """ REST to validate the topology following the SDX data model"""
        if self.topology_loaded or self.test_kytos_topology():
            try:
                data = request  # pylint: disable=W0201
            except BadRequest:
                result = "The request body is not a well-formed JSON."
                raise BadRequest(result) from BadRequest
            if data is None:
                result = "The request body mimetype is not application/json."
                raise UnsupportedMediaType(result)
            response, status_code = utils.validate_request(spec, data)
            return (response, status_code)
        response = ("Topology napp has not loaded", 401)
        return response

    @rest("v1/topology")
    def validate_sdx_topology_loaded(self):
        """ REST to return the sdx topology loaded"""
        response, status_code = self.get_topology_version()
        return jsonify(response), status_code

    def get_topology_version(self, event_type=0, event_timestamp=None):
        """ return the topology following the SDX data model"""
        if not self.oxp_url:
            return ("Submit oxp_url previous to request topology schema", 401)
        if not self.oxp_name:
            return ("Submit oxp_name previous to request topology schema", 401)
        if self.topology_loaded or self.test_kytos_topology():
            try:
                topology_update = self.create_update_topology(
                        event_type, event_timestamp)
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
                    requests.post(
                            settings.SDX_LC, json=topology_update)
                    return (topology_update, 200)
                return (validate_topology.json(), 400)
            except Exception as err:  # pylint: disable=W0703
                log.info(err)
                return ("Validation Error", 400)
        return ("Topology napp has not loaded", 401)

    @rest("v1/eval_kytos_topology", methods=["POST"])
    def get_df_diff(self):
        """ REST to return the kytos topology with pandas df """
        eval_param = request.get_json()
        current_params = self.current_kytos_topology()[eval_param]
        initial_params = self.initial_kytos_topology()[eval_param]
        params_diff = {}
        if current_params and initial_params:
            params_diff = utils.diff_pd(current_params, initial_params)
        return params_diff

    @rest("v1/get_sdx_topology", methods=["GET"])
    def get_sdx_topology(self):
        """ REST to return the SDX Topology """
        return self.create_update_topology()

    def create_update_topology(self, event_type=0, event_timestamp=None):
        """Function that will take care of initializing the namespace
        kytos.storehouse.version within the storehouse and create a
        box object containing the version data that will be updated
        every time a change is detected in the topology."""
        if event_type == 1:
            self.storehouse.update_box()
        elif event_type == 2:
            self.storehouse.update_timestamp(event_timestamp)
        try:
            version = self.storehouse.get_data()['version']
            timestamp = self.storehouse.get_data()["time_stamp"]
        except Exception as err:  # pylint: disable=W0703:
            log.info(err)
            version = 1
            timestamp = utils.get_timestamp()
        return ParseTopology(
            topology=self.get_kytos_topology(),
            version=version,
            timestamp=timestamp,
            model_version="1.0.0",
            oxp_name=self.oxp_name,
            oxp_url=self.oxp_url,
        ).get_sdx_topology()
