import requests
import json
import exceptions
from .encoder import JSONEncoder

class Backend(object):
    """
    Interface for backend to send HTTP messages to Intercom.io.
    """

    def send(self, creds, method, endpoint, json_data=None):
        raise NotImplementedError()

class SyncBackend(Backend):
    """
    Sends HTTP messages synchronously via python-requests.
    """

    def send(self, creds, method, endpoint, json_data=None):
        resp = requests.request(
            method=method,
            url=endpoint,
            data=json.dumps(json_data, cls=JSONEncoder) if json_data else None,
            auth=creds,
            headers={
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            }
        )

        if resp.status_code == 401:
            raise exceptions.AuthenticationError('', resp)

        if resp.status_code == 404:
            raise exceptions.ResourceNotFound('', resp)

        if resp.status_code >= 500:
            raise exceptions.ServerError('', resp)