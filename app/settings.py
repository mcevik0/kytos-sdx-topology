"""Module with the Constants used in the kytos/sdx_topology."""

KYTOS_TOPOLOGY_URL = "http://localhost:8181/api/kytos/topology/v3/"
AMLIGHT_TOPOLOGY = "http://3.218.56.104:8181/api/kytos/topology/v3"
TENET_TOPOLOGY_API = "http://23.20.21.212:8181/api/kytos/topology/v3"
SDX_TOPOLOGY_API = "http://0.0.0.0:8181/api/kytos/sdx_topology/v1"
GET_SDX_TOPOLOGY = \
        "http://0.0.0.0:8181/api/kytos/sdx_topology/v1/topology"
VALIDATE_TOPOLOGY = \
        "http://0.0.0.0:8181/api/kytos/sdx_topology/v1/validate"
SDX_LC = "http://0.0.0.0:8080/SDX-LC/1.0.0/topology"
SDX_PROVISIONING = "http://0.0.0.0:8088/SDX-LC/1.0.0/provision"
HEADERS = {"Content-type": "application/json"}
ADMIN_EVENTS = [
        "kytos/topology.switch.enabled",
        "kytos/topology.switch.disabled"]
OPERATIONAL_EVENTS = [
        "kytos/topology.link_up",
        "kytos/topology.link_down"]
