import requests
import json
from .encoder import JSONEncoder

class Pyntercom(requests.Session):
    """
    HTTP client for interacting with Intercom.io API.
    """

    base_url = 'https://api.intercom.io'

    def __init__(self, app_id, app_key):
        """
        Configures the requests session.

        More Info:
        http://doc.intercom.io/api/#authorization

        * ``app_id``: Application ID
        * ``app_key``: API key
        """

        super(Pyntercom, self).__init__()

        # authentication
        self.auth = (app_id, app_key)

        # headers
        self.headers['Content-Type'] = 'application/json'
        self.headers['Accept'] = 'application/json'

    def post(self, path, data):
        """
        POST request against the API

        * ``path``: URL path, prefixed with /
        * ``data``: Data to be json encoded and sent in body        
        """

        return super(Pyntercom, self).post(
            url=self.base_url + '/users',
            data=json.dumps(data, cls=JSONEncoder),
        )

    def save_user(self, **kwargs):
        """
        Create or Update User
        http://doc.intercom.io/api/#create-or-update-user
        """

        return self.post('/users', kwargs)