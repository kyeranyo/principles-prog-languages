import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_array_program_2(self):
        """Simple program: array [2,3] of integer """
        input = """array [2] of integer"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 601))

    def test_variable_program_2(self):
        """fact : function integer (n : integer)"""
        input = """fact : function integer (n : integer)"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 602))

    def test_variable_program_3(self):
        """x,y: string = "abc","xyz";"""
        input = """x,y: integer = 65,66;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 603))

