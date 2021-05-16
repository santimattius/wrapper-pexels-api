import json
import unittest

from tests.base import BaseTestCase


def health_check(self):
    return self.client.get(
        '/test/healthcheck',
        content_type='application/json'
    )


class TestHealthcheckBlueprint(BaseTestCase):

    def test_health_check(self):

        with self.client:
            # health check
            response = health_check(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()
