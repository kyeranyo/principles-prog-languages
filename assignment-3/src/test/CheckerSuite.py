import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_undeclared_function(self):
        """Simple program: int main() {} """
        input = """f : integer ;"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,400))