import unittest
from httptrace.core import inspect

class Tests(unittest.TestCase):
    def test_validation(self):
        with self.assertRaises(ValueError): inspect("ftp://example.com")
        with self.assertRaises(ValueError): inspect("https://example.com",0)

if __name__ == "__main__": unittest.main()
