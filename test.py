from unittest import main, TestCase
from datetime import datetime
from pyntercom import Pyntercom
from pyntercom.encoder import JSONEncoder
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
