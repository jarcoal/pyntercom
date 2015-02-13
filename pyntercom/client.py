from .backend import SyncBackend
from datetime import datetime

class Pyntercom(object):
    """
    HTTP client for interacting with Intercom.io API.
    """

    base_url = 'https://api.intercom.io'

    def __init__(self, app_id, app_key, backend=None):
        """
        Configures the requests session.

        More Info:
        http://doc.intercom.io/api/#authorization

        * ``app_id``: Application ID
        * ``app_key``: API key
        * ``backend``: optional - Backend implementation for fulfilling requests
        """

        self.auth = (app_id, app_key)
        self.backend = backend or SyncBackend()

    def save_user(self, **kwargs):
        """
        Create or Update User
        http://doc.intercom.io/api/#create-or-update-user
        """

        self.backend.send(self.auth, 'POST', self.base_url + '/users', kwargs)

    def track_event(self,
                    user_id=None,
                    email=None,
                    event_name=None,
                    metadata=None,
                    created_at=None):

        """
        Track Event
        http://doc.intercom.io/api/#event-model

        * ``user_id``: Your user-assigned identifier.  Required unless email is present.
        * ``email``: User email.  Required unless user_id is present.
        * ``event_name``: Name of event
        * ``metadata``: Additional data to associate with the event (optional)
        * ``created_at``: Datetime for when this event occured.  Defaults to datetime.now().
        """

        assert user_id or email

        params = {
            'event_name': event_name,
            'metadata': metadata,
            'created_at': created_at or datetime.now(),
        }

        if user_id:
            params['user_id'] = user_id

        if email:
            params['email'] = email

        self.backend.send(self.auth, 'POST', self.base_url + '/events', params)
