import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_simple_string(self):
        """test simple string 1"""
        input = "1B"
        expect = "Error Token 1"
        self.assertTrue(TestLexer.test(input, expect, 101))

# def test_simple_string2(self):
#     """test simple string 2"""
#     input = "192.168.01.1"
#     expect = "Error Token 1"
#     self.assertTrue(TestLexer.test(input, expect, 102))

# def test_simple_string3(self):
#     """test simple string 3"""
#     input = "152.101.227.0"
#     expect = "152.101.227.0,<EOF>"
#     self.assertTrue(TestLexer.test(input, expect, 103))

# def test_simple_string4(self):
#     """test simple string 4"""
#     input = "1168.93.28.1"
#     expect = "Error Token 1"
#     self.assertTrue(TestLexer.test(input, expect, 104))

# def test_simple_string5(self):
#     """test simple string 5"""
#     input = "2.1687.0.2"
#     expect = "Error Token 2"
#     self.assertTrue(TestLexer.test(input, expect, 105))

# def test_complex_string(self):
#     """test complex string"""
#     self.assertTrue(TestLexer.test("'isn''t'","'isn''t',<EOF>",102))
