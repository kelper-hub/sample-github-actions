import unittest
from app.main import greet


class TestGreetFunction(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")
        self.assertEqual(greet("GitHub"), "Hello, GitHub!")


if __name__ == "__main__":
    unittest.main()
