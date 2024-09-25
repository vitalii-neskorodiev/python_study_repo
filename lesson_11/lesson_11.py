import unittest
import logging
from io import StringIO

from lesson_11.homework_10 import log_event


class TestLoginEvents(unittest.TestCase):

    def setUp(self):
        self.log_stream = StringIO()
        logging.basicConfig(stream=self.log_stream, level=logging.INFO)
        logging.getLogger("log_event").handlers = []

    def test_log_event_success(self):
        log_event("testuser", "success")
        self.log_stream.seek(0)
        log_output = self.log_stream.getvalue()
        self.assertIn("INFO", log_output)
        self.assertIn("Login event - Username: testuser, Status: success", log_output)

    def test_log_event_expired(self):
        log_event("testuser", "expired")
        self.log_stream.seek(0)
        log_output = self.log_stream.getvalue()
        self.assertIn("WARNING", log_output)
        self.assertIn("Login event - Username: testuser, Status: expired", log_output)

    def test_log_event_failed(self):
        log_event("testuser", "failed")
        self.log_stream.seek(0)
        log_output = self.log_stream.getvalue()
        self.assertIn("ERROR", log_output)
        self.assertIn("Login event - Username: testuser, Status: failed", log_output)


if __name__ == '__main__':
    unittest.main()
