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
        input = """fact : function integer (n : integer) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 602))

    def test_variable_program_3(self):
        """a, b, c, d: integer = 3, 4, 6;"""
        input = """a, b, c, d: integer = 3, 4, 6;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 603))

    def test_variable_program_4(self):
        """x: integer = foo(65);"""
        input = """delta: integer = fact(3);"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 604))

    def test_function_program_5(self):
        """main: function void () {}"""
        input = """main: function void () {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 605))

    def test_function_program_6(self):
        input ="""x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 606))
