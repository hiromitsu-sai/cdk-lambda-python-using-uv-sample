from unittest import TestCase

from src.hello import handler, main


class TestHello(TestCase):
    def test_hello(self):
        expected = "Hello from test!"
        self.assertEqual(main(), expected)

    def test_handler(self):
        expected = "Hello from test!"
        self.assertEqual(handler({}, {}), expected)
