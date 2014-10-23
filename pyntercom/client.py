from .backend import SyncBackend

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

        return self._send('POST', '/users', kwargs)

    def _send(self, method, url, data=None):
        """
        Passes request data to the backend to be fulfilled.

        * ``method``: HTTP verb
        * ``url``: Endpoint URL
        * ``data``: optional - data to be JSON encoded and sent in HTTP body
        """

        self.backend.send(self.auth, method, self.base_url + url, data)