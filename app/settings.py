"""Module with the Constants used in the kytos/sdx_topology."""

KYTOS_TOPOLOGY = "http://0.0.0.0:8181/api/kytos/topology/v3/"
KYTOS_SDX_TOPOLOGY_API = \
        "http://0.0.0.0:8181/api/kytos/sdx_topology/v1"
KYTOS_SDX_TOPOLOGY = \
        "http://0.0.0.0:8181/api/kytos/sdx_topology/v1/topology"
KYTOS_SDX_VALIDATE = \
        "http://0.0.0.0:8181/api/kytos/sdx_topology/v1/validate"
SDX_LC_TOPOLOGY = "http://0.0.0.0:8080/sdx-lc/v2/topology"
HEADERS = {"Content-type": "application/json"}
ADMIN_EVENTS = [
        "kytos/topology.switch.enabled",
        "kytos/topology.switch.disabled",
        "kytos/topology.switch.metadata.added",
        "kytos/topology.interface.metadata.added",
        "kytos/topology.link.metadata.added",
        "kytos/topology.switch.metadata.removed",
        "kytos/topology.interface.metadata.removed",
        "kytos/topology.link.metadata.removed",
        ]
OPERATIONAL_EVENTS = [
        "kytos.topology.updated",
        "kytos/topology.link_up",
        "kytos/topology.link_down"]
