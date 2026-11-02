import unittest
from greeting import greet

class GreetingTests(unittest.TestCase):
    def test_name(self):
        self.assertEqual(greet("GitHub"), "Hello, GitHub!")

if __name__ == "__main__":
    unittest.main()
