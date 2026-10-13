import unittest

from main import greeting


class GreetingTests(unittest.TestCase):
    def test_default_greeting(self):
        self.assertEqual(greeting(), "Hello, world!")

    def test_named_greeting(self):
        self.assertEqual(greeting("Python"), "Hello, Python!")


if __name__ == "__main__":
    unittest.main()
