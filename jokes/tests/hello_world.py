import unittest
from jokes.core import parser

class HelloWorldTests(unittest.TestCase):
    
    def test_parsing(self):
        self.assertEqual(parser.read_sentence("output('Hello World')"), 'Hello World')