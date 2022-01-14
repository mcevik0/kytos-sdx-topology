"""
Module to handle the storehouse.
"""

import threading
from kytos.core import log
from kytos.core.events import KytosEvent


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

        if 'box' not in self.__dict__:
            self.box = None
        self.list_stored_boxes()
        self.counter = 0

    def get_data(self):
        """Return the box data."""
        if not self.box:
            return {}
        self.get_stored_box(self.box.box_id)
        return self.box.data

    def create_box(self):
        """Create a new box with the napp version information"""

        content = {'namespace': 'kytos.sdx.storehouse.version',
                   'callback': self._create_box_callback,
                   'data': {"version": self.counter,
                            "oxp_name": "",
                            "oxp_url": ""
                            }
                   }

        event = KytosEvent(name='kytos.storehouse.create', content=content)

        self.controller.buffers.app.put(event)

        log.info('Create box from storehouse')

    def _create_box_callback(self, _event, data, error):
        """Execute the callback to log the output of the create_box function."""
        if error:
            log.error(f'Can\'t create box with namespace {self.namespace}')

        self.box = data
        log.debug(f'Box {self.box.box_id} was created in {self.namespace}.')

    def update_box(self):
        """Update an existing box with a new version value after a topology change is detected."""
        self._lock.acquire()  # Lock to avoid race condition   # pylint: disable=R1732
        log.debug(f'Lock {self._lock} acquired.')
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
        log.debug(f'Lock {self._lock} released.')
        if error:
            log.error(f'Can\'t update the {self.box.box_id}')

        log.debug(f'Box {data.box_id} was updated.')

    def get_stored_box(self, box_id):
        """Retrieve box from storehouse."""

        content = {'namespace': self.namespace,
                   'callback': self._get_box_callback,
                   'box_id': box_id,
                   'data': {}}

        name = 'kytos.storehouse.retrieve'
        event = KytosEvent(name=name, content=content)
        self.controller.buffers.app.put(event)
        log.debug(f'Retrieve box with {box_id} from {self.namespace}.')

    def _get_box_callback(self, _event, data, error):
        """Execute the callback to log the output of the get_stored_box function."""
        self.box = data

        if error:
            log.error(f'Box {data.box_id} not found in {self.namespace}.')

        log.debug(f'Box {self.box.box_id} was loaded from storehouse.')

    def list_stored_boxes(self):
        """List all boxes using the current namespace."""
        name = 'kytos.storehouse.list'
        content = {'namespace': self.namespace,
                   'callback': self._get_or_create_a_box_from_list_of_boxes}

        event = KytosEvent(name=name, content=content)
        self.controller.buffers.app.put(event)
        log.debug(f'Bootstraping storehouse box for {self.namespace}.')

    def _get_or_create_a_box_from_list_of_boxes(self, _event, data, _error):
        """Create a new box or retrieve the stored box."""
        if data:
            self.get_stored_box(data[0])
        else:
            self.create_box()

    def save_oxp_name(self, oxp_name):
        """Save the OXP NAME using the storehouse."""
        self._lock.acquire()  # Lock to avoid race condition
        log.debug(f'Lock {self._lock} acquired.')
        self.box.data["oxp_name"] = oxp_name

        content = {'namespace': self.namespace,
                   'box_id': self.box.box_id,
                   'data': self.box.data,
                   'callback': self._save_oxp_callback}

        event = KytosEvent(name='kytos.storehouse.update', content=content)
        self.controller.buffers.app.put(event)

    def save_oxp_url(self, oxp_url):
        """Save the OXP URL using the storehouse."""
        self._lock.acquire()  # Lock to avoid race condition
        log.debug(f'Lock {self._lock} acquired.')
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
        log.debug(f'Lock {self._lock} released.')
        if error:
            log.error(f'Can\'t update the {self.box.box_id}')

        log.debug(f'Box {data.box_id} was updated.')
