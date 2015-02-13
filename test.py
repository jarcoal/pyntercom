from unittest import main, TestCase
from datetime import datetime
from pyntercom import Pyntercom
from pyntercom.encoder import JSONEncoder, datetime_to_unix_timestamp
import httmock
import json

now = datetime.utcnow()

class PyntercomClientTest(TestCase):
    """
    Test the HTTP client.
    """

    def setUp(self):
        super(PyntercomClientTest, self).setUp()
        self.client = Pyntercom(app_id='abc', app_key='def')

    def test_track_event(self):
        """Tests the Pyntercom.trackEvent method."""

        created_at = datetime.now()

        mock_payload = {
            'user_id': 1,
            'event_name': 'Event',
            'metadata': {
                'hello': 'world',
            },
            'created_at': datetime_to_unix_timestamp(created_at)
        }

        @httmock.urlmatch(method='POST', netloc='api.intercom.io', path='/events')
        def mock_track_event(url, request):
            result = json.loads(request.body)
            expected = json.loads(json.dumps(mock_payload, cls=JSONEncoder))

            self.assertEqual(result, expected)
            return request.body

        with httmock.HTTMock(mock_track_event):
            self.client.track_event(
                user_id=1,
                event_name='Event',
                metadata={
                    'hello': 'world',
                },
                created_at=created_at,
            )

    def test_save_user(self):
        """POST /users"""

        payload = {
            'user_id': 1,
            'email': 'john@gmail.com',
            'name': 'John Smith',
            'remote_created_at': now,
            'last_seen_ip': '1.2.3.4',
            'user_agent_data': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9',
            'custom_attributes': {
                'hello': 'world'
            },
            'companies': [
                {
                    'company_id': 1,
                    'name': 'Company'
                }
            ]
        }

        @httmock.urlmatch(method='POST', netloc='api.intercom.io', path='/users')
        def mock_save_user(url, request):
            """
            Mock responder for creating/updating users.
            """

            result = json.loads(request.body)
            expected = json.loads(json.dumps(payload, cls=JSONEncoder))

            self.assertEqual(result, expected)

            return request.body

        with httmock.HTTMock(mock_save_user):
            self.client.save_user(**payload)

if __name__ == '__main__':
    main()
