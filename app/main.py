"""
Main module of amlight/sdx Kytos Network Application.
"""
import os
import shelve
import requests
from flask import request, jsonify
from werkzeug.exceptions import BadRequest
from napps.kytos.sdx_topology.topology_class import (ParseTopology) \
        # pylint: disable=E0401
from napps.kytos.sdx_topology import settings, utils, topology_mock \
        # pylint: disable=E0401

from kytos.core import KytosNApp, log, rest
from kytos.core.helpers import listen_to

HSH = "##########"
URN = "urn:sdx:"


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
        log.info(f"{HSH}{HSH}{HSH}")
        log.info(f"{HSH}sdx topology{HSH}")
        log.info(f"{HSH}{HSH}{HSH}")
        self.event_info = {}  # pylint: disable=W0201
        self.topology_loaded = False  # pylint: disable=W0201

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

    @listen_to("kytos/topology.unloaded")
    def unload_topology(self):  # pylint: disable=W0613
        """Function meant for validation, to make sure that the storehouse napp
        has been loaded before all the other functions that use it begins to
        call it."""
        self.topology_loaded = False  # pylint: disable=W0201

    def create_update_topology(self, event_type=0, event_timestamp=None):
        """Function that will take care of initializing the namespace
        kytos.storehouse.version within the storehouse and create a
        box object containing the version data that will be updated
        every time a change is detected in the topology."""
        # open a shelf file
        storehouse = shelve.open("storehouse")  # pylint: disable=W0201
        if event_type == 1:
            storehouse['version'] += 1
            storehouse['timestamp'] = utils.get_timestamp()
        elif event_type == 2:
            storehouse['timestamp'] = event_timestamp
        storehouse.sync()
        self.storehouse = dict(storehouse)  # pylint: disable=W0201
        return ParseTopology(
            topology=self.get_kytos_topology(),
            version=storehouse['version'],
            timestamp=storehouse['timestamp'],
            model_version=storehouse['model_version'],
            oxp_name=storehouse['oxp_name'],
            oxp_url=storehouse['oxp_url'],
        ).get_sdx_topology()

    def get_sdx_topology(self, event_type=0, event_timestamp=None):
        """ return the topology following the SDX data model"""
        if self.topology_loaded:
            try:
                if event_type != 0:
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
                else:
                    topology_dict = topology_mock.topology_mock()
                validate_topology = requests.post(
                        settings.SDX_TOPOLOGY_VALIDATE,
                        timeout=10,
                        json=topology_dict)
                if validate_topology.status_code == 200:
                    post_topology = requests.post(
                            settings.SDX_LC_TOPOLOGY,
                            timeout=10,
                            json=topology_dict)
                    if post_topology.status_code == 200:
                        return (topology_dict, 200)
                    return (post_topology.json(), 400)
                return (validate_topology.json(), 400)
            except Exception as err:  # pylint: disable=W0703
                log.info(err)
                return ("Validation Error", 400)
        return ("No SDX Topology loaded", 401)

    @rest("v1/topology")
    def get_sdx_topology_loaded(self):
        """ REST to return the sdx topology loaded"""
        response, status_code = self.get_sdx_topology()
        return jsonify(response), status_code

    @listen_to("kytos/topology.*")
    def listen_topology(self, event=None):
        """Function meant for listen topology"""
        f_name = " listen_topology "
        log.info(f"{HSH}{f_name}get kytos topology {HSH}")
        if event:
            if event.name in settings.ADMIN_EVENTS:
                event_type = 1
            elif event.name in settings.OPERATIONAL_EVENTS and \
                    event.timestamp is not None:
                event_type = 2
            else:
                return {"event": "not action event"}
            if self.storehouse:
                if 'id' in self.storehouse.keys() and \
                        'name' in self.storehouse.keys():
                    self.topology_loaded = True  # pylint: disable=W0201
                    return self.get_topology_version(
                            event_type, event.timestamp)
                return {"error": "not id or name in self.storehouse"}
            return {"error": "not self.storehouse"}
        return {"event": "None"}

    @rest("v1/listen_topology", methods=["GET"])
    def get_listen_topology(self):
        """consume call listen Topology"""
        f_name = " get_listen_topology "
        log.info(f"{HSH}{f_name}{HSH}")
        return self.listen_topology()

    def load_storehouse(self, event=None):  # pylint: disable=W0613
        """Function meant for validation, to make sure that the storehouse
        has been loaded before all the other functions that use it begins to
        call it."""
        if not self.topology_loaded:  # pylint: disable=E0203
            # open a shelf file
            storehouse = shelve.open("storehouse")  # pylint: disable=W0201
            if 'id' not in dict(storehouse.keys()) or \
                    'name' not in dict(storehouse.keys()):
                # initialize sdx topology
                storehouse['id'] = URN+"topology:"+os.environ.get("OXPO_URL")
                storehouse['name'] = os.environ.get("OXPO_NAME")
                storehouse['URL'] = os.environ.get("OXPO_URL")
                storehouse['version'] = 0
                storehouse['model_version'] = os.environ.get("MODEL_VERSION")
                storehouse['timestamp'] = utils.get_timestamp()
                storehouse['nodes'] = []
                storehouse['links'] = []
            self.storehouse = dict(storehouse)  # pylint: disable=W0201
            # now, we simply close the shelf file.
            storehouse.close()
