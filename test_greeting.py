import unittest
from greeting import greet

class GreetingTests(unittest.TestCase):
    def test_name(self):
        self.assertEqual(greet("GitHub"), "Hello, GitHub!")

    def test_whitespace(self):
        self.assertEqual(greet("  GitHub  "), "Hello, GitHub!")

    def test_empty_name(self):
        for name in ("", "   "):
            with self.subTest(name=name):
                with self.assertRaises(ValueError):
                    greet(name)

if __name__ == "__main__":
    unittest.main()
