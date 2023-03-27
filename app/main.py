"""
Main module of amlight/sdx Kytos Network Application.
"""
import requests
from werkzeug.exceptions import BadRequest

from kytos.core import KytosNApp, rest, log
from kytos.core.helpers import listen_to
from napps.kytos.sdx_topology import settings  # pylint: disable=E0401
# pylint: disable=E0401


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

    def execute(self):
        """Run after the setup method execution.

        You can also use this method in loop mode if you add to the above setup
        method a line like the following example:

            self.execute_as_loop(30)  # 30-second interval.
        """

    def shutdown(self):
        """Run when your NApp is unloaded.

        If you have some cleanup procedure, insert it here.
        """

    @staticmethod
    def get_kytos_topology():
        """retrieve topology from API"""
        kytos_topology = requests.get(settings.KYTOS_TOPOLOGY_URL).json()
        log.info("######### get_kytos_topology #########")
        # log.info(kytos_topology)
        return kytos_topology["topology"]

    @listen_to("kytos/topology.*")
    def load_topology(self, event=None):  # pylint: disable=W0613
        """ Function meant for listen topology """
        log.info("######### load_topology #########")
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
        try:
            topology = self.get_kytos_topology()
            topology_info = {
                    "event": event,
                    "event_type": event_type,
                    "event_name": event.name,
                    "timestamp": event.timestamp,
                    "topology": topology}
            # log.info(topology_info["event"])
            log.info("######### Topology_info event_type #########")
            log.info(topology_info["event_type"])
            log.info("######### Topology_info event_name #########")
            log.info(topology_info["event_name"])
            log.info("######### Topology_info timestamp #########")
            log.info(topology_info["timestamp"])
            # log.info(topology_info[topology])
            if event_type != 0:
                pass
        except Exception as err:  # pylint: disable=W0703
            log.info("######### load_topology error #########")
            log.info(err)

    @rest("v1/get_sdx_topology", methods=["GET"])
    def get_sdx_topology(self):
        """ REST to return the SDX Topology """
        log.info("######### get_sdx_topology #########")
        sdx_topology = self.load_topology()
        log.info("######### sdx_topology #########")
        log.info(sdx_topology)
        if sdx_topology:
            return sdx_topology
        return {}
