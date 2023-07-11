"""
Main module of amlight/sdx Kytos Network Application.
"""
import requests
from napps.kytos.sdx_topology import settings  # pylint: disable=E0401
from werkzeug.exceptions import BadRequest

from kytos.core import KytosNApp, log, rest
from kytos.core.helpers import listen_to


HSH = "##########"


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

    @listen_to("kytos/topology.*")
    def listen_topology(self, event=None):
        """Function meant for listen topology"""
        f_name = " listen_topology "
        log.info(f"{HSH}{f_name}get kytos topology {HSH}")
        event_info = {}  # pylint: disable=W0201
        if event:
            allowed_events = [
                "kytos/topology.switch.enabled",
                "kytos/topology.switch.disabled",
                "kytos/topology.link_up",
                "kytos/topology.link_down",
            ]
            if event.name in allowed_events:
                try:
                    topology = requests.get(settings.KYTOS_TOPOLOGY_URL).json()
                    log.info(
                        f"{HSH}{f_name}constructor post request {HSH}"
                    )
                    event_info = {
                        "event": event,
                        "kytostopology": topology,
                    }  # pylint: disable=W0201
                    try:
                        requests.post(settings.SDX_CONSTRUCTOR).json(event_info)
                    except Exception as err:  # pylint: disable=W0703
                        log.info(f"{HSH}{f_name}constructor post error {HSH}")
                        log.info(err, event_info)
                except Exception as err:  # pylint: disable=W0703
                    log.info(
                            f"{HSH}{f_name}get kytos topology error {HSH}"
                    )
                    log.info(err)
        return event_info

    @rest("v2/listen_topology", methods=["GET"])
    def get_listen_topology(self):
        """consume call listen Topology"""
        f_name = " get_listen_topology "
        log.info(f"{HSH}{f_name}{HSH}")
        return self.listen_topology()
