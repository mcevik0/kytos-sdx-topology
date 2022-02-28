"""
Module to handle the storehouse.
"""

import threading
from kytos.core import log
from kytos.core.events import KytosEvent
from napps.kytos.sdx_topology import utils  # pylint: disable=E0401


class StoreHouse:
    """Class to handle storehouse."""

    @classmethod
    def __new__(cls, *args, **kwargs):
        # pylint: disable=unused-argument
        """Make this class a Singleton."""
        instance = cls.__dict__.get("__instance__")

        if instance is not None:
            return instance
        cls.__instance__ = instance = object.__new__(cls)
        return instance

    def __init__(self, controller):
        """Create a storehouse instance."""
        self.controller = controller
        self.namespace = 'kytos.sdx.storehouse.version'
        self._lock = threading.Lock()

        self.counter = 0
        self.time_stamp = utils.get_timestamp()
        if 'box' not in self.__dict__:
            self.box = None
        self.list_stored_boxes()

    def get_data(self):
        """Return the box data."""
        log.info("########## get_data ##########")
        try:
            self.get_stored_box(self.box.box_id)
        except Exception:  # pylint: disable=W0703
            return {}
        log.info("########## self.box.data ##########")
        log.info(self.box.data)
        log.info("########## end get_data ##########")
        return self.box.data

    def create_box(self):
        """Create a new box with the napp version information"""
        log.info("########## create box ##########")
        content = {'namespace': 'kytos.sdx.storehouse.version',
                   'callback': self._create_box_callback,
                   'data': {"version": self.counter,
                            "time_stamp": self.time_stamp,
                            "oxp_name": "",
                            "oxp_url": ""
                            }
                   }
        log.info(content)

        event = KytosEvent(name='kytos.storehouse.create', content=content)

        self.controller.buffers.app.put(event)

    def _create_box_callback(self, _event, data, error):
        """Execute a callback to log the output of the create_box function."""
        log.info("########## _create box callback ##########")
        if error:
            log.error(f'Can\'t create box with namespace {self.namespace}')

        self.box = data
        log.info(self.box)
        log.info(f'Box {self.box.box_id} was created in {self.namespace}.')

    def update_box(self):
        """Update an existing box with a new version value after a topology
        change is detected."""
        self._lock.acquire()  # avoid race condition  # pylint: disable=R1732
        log.info(f'Lock {self._lock} acquired.')
        self.counter += 1
        content = {'namespace': self.namespace,
                   'box_id': self.box.box_id,
                   'data': {"version": self.counter},
                   'callback': self._update_box_callback}

        event = KytosEvent(name='kytos.storehouse.update', content=content)
        self.controller.buffers.app.put(event)

    def _update_box_callback(self, _event, data, error):
        """Record the updated_box function result in the log."""
        self._lock.release()
        log.info(f'Lock {self._lock} released.')
        if error:
            log.error(f'Can\'t update the {self.box.box_id}')

        log.info(f'Box {data.box_id} was updated.')

    def get_stored_box(self, box_id):
        """Retrieve box from storehouse."""
        log.info("######### get_stored_box ##########")
        content = {'namespace': self.namespace,
                   'callback': self._get_box_callback,
                   'box_id': box_id,
                   'data': {}}
        log.info(content)
        name = 'kytos.storehouse.retrieve'
        event = KytosEvent(name=name, content=content)
        self.controller.buffers.app.put(event)
        log.info(f'Retrieve box with {box_id} from {self.namespace}.')

    def _get_box_callback(self, _event, data, error):
        """Execute a callback to log the get_stored_box function output."""
        log.info("######### _get_box_callback ##########")

        self.box = data
        log.info(self.box)
        if error:
            log.error(f'Box {data.box_id} not found in {self.namespace}.')

        log.info(f'Box {self.box.box_id} was loaded from storehouse.')

    def list_stored_boxes(self):
        """List all boxes using the current namespace."""
        log.info("######### list stored boxes ##########")
        name = 'kytos.storehouse.list'
        content = {'namespace': self.namespace,
                   'callback': self._get_create_box}

        log.info("######### list stored boxes content  ##########")
        log.info(name)
        log.info(content)
        event = KytosEvent(name=name, content=content)
        self.controller.buffers.app.put(event)
        log.info(f'Bootstraping storehouse box for {self.namespace}.')

    def _get_create_box(self, _event, data, _error):
        """Create a new box or retrieve the stored box."""
        log.info("######### _get create box ##########")
        if data:
            log.info("######### data  ##########")
            log.info(data)
            self.get_stored_box(data[0])
        else:
            log.info("######### calling create box  ##########")
            self.create_box()

    def update_timestamp(self, time_stamp):
        """Update an existing box with a new timestamp value after a topology
        change is detected."""
        self._lock.acquire()  # avoid race condition  # pylint: disable=R1732
        log.info(f'Lock {self._lock} acquired.')
        self.time_stamp = utils.get_timestamp(time_stamp)
        self.box.data["time_stamp"] = self.time_stamp
        content = {'namespace': self.namespace,
                   'box_id': self.box.box_id,
                   'data': {"time_stamp": self.time_stamp},
                   'callback': self._update_box_callback}

        event = KytosEvent(name='kytos.storehouse.update', content=content)
        self.controller.buffers.app.put(event)

    def save_oxp_name(self, oxp_name):
        """Save the OXP NAME using the storehouse."""
        self._lock.acquire()  # avoid race condition  # pylint: disable=R1732
        log.info(f'Lock {self._lock} acquired.')
        self.box.data["oxp_name"] = oxp_name

        content = {'namespace': self.namespace,
                   'box_id': self.box.box_id,
                   'data': self.box.data,
                   'callback': self._save_oxp_callback}

        event = KytosEvent(name='kytos.storehouse.update', content=content)
        self.controller.buffers.app.put(event)

    def save_oxp_url(self, oxp_url):
        """Save the OXP URL using the storehouse."""
        self._lock.acquire()  # avoid race condition  # pylint: disable=R1732
        log.info(f'Lock {self._lock} acquired.')
        self.box.data["oxp_url"] = oxp_url

        content = {'namespace': self.namespace,
                   'box_id': self.box.box_id,
                   'data': self.box.data,
                   'callback': self._save_oxp_callback}

        event = KytosEvent(name='kytos.storehouse.update', content=content)
        self.controller.buffers.app.put(event)

    def _save_oxp_callback(self, _event, data, error):
        """Display the save EVC result in the log."""
        self._lock.release()
        log.info(f'Lock {self._lock} released.')
        if error:
            log.error("Can not update the self.box.box_id")

        log.info(f'Box {data.box_id} was updated.')
