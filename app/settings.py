"""Module with the Constants used in the kytos/sdx_topology."""

KYTOS_TOPOLOGY = "http://0.0.0.0:8181/api/kytos/topology/v3/"
KYTOS_SDX_TOPOLOGY_API = \
        "http://0.0.0.0:8181/api/kytos/sdx_topology/v1"
KYTOS_SDX_TOPOLOGY = \
        "http://0.0.0.0:8181/api/kytos/sdx_topology/v1/topology"
KYTOS_SDX_TOPOLOGY_VERSION_CONTROL = \
        "http://0.0.0.0:8181/api/kytos/sdx_topology/v1/version/control"
SDX_TOPOLOGY_VALIDATE = \
        "http://192.168.0.14:8000/validator/v1/validate"
SDX_LC_TOPOLOGY = "http://192.168.0.15:8080/sdx-lc/v2/topology"
HEADERS = {"Content-type": "application/json"}
ADMIN_EVENTS = [
        "version/control.initialize",
        "kytos/topology.switch.enabled",
        "kytos/topology.switch.disabled",
        "kytos/topology.switch.metadata.added",
        "kytos/topology.interface.metadata.added",
        "kytos/topology.link.metadata.added",
        "kytos/topology.switch.metadata.removed",
        "kytos/topology.interface.metadata.removed",
        "kytos/topology.link.metadata.removed",
        # 'kytos/topology.notify_link_up_if_status',
        # 'kytos/core.shutdown',
        # 'kytos/core.shutdown.kytos/topology',
        # '.*.topo_controller.upsert_switch',
        # '.*.of_lldp.network_status.updated',
        # '.*.switch.interfaces.created',
        # '.*.topology.switch.interface.created',
        # '.*.switch.interface.deleted',
        # '.*.switch.port.created',
        # 'topology.interruption.start',
        # 'topology.interruption.end',
        ]
OPERATIONAL_EVENTS = [
        "topology_loaded",
        "kytos/topology.link_up",
        "kytos/topology.link_down",
        # '.*.connection.lost',
        # '.*.switch.interface.link_down',
        # '.*.switch.interface.link_up',
        # '.*.switch.(new|reconnected)'
        ]
