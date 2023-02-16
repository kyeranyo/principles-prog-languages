import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_array_program(self):
        """Simple program: {1,2,3,4,5} """
        input = """{1,2,3,4,5}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 501))

    def test_array_program_3(self):
        """Simple program: {} """
        input = """{}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 503))
