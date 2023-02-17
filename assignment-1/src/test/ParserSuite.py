import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_array_program_2(self):
        """Simple program: array [2,3] of integer """
        input = """array [2,3] of integer"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 601))

    # def test_variable_program_2(self):
    #     """x,y: integer = 65,66;"""
    #     input = """x,y: integer = 65,66;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 602))

