import unittest
from app.main import greet, hello_world

class TestGreetFunction(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")
        self.assertEqual(greet("GitHub"), "Hello, GitHub!")
        self.assertEqual(greet(""), "Hello, !")
        self.assertEqual(greet("123"), "Hello, 123!")
        self.assertEqual(greet("John Doe"), "Hello, John Doe!")

class TestHelloWorldFunction(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()