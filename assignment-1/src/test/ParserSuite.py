import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_variable_program_2(self):
        """fact : function integer (n : integer)"""
        input = """fact : function integer (n : integer) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 602))

    def test_variable_program_3(self):
        """a, b, c, d: integer = 3, 4, 6;"""
        input = """a, b, c, d: integer = 3, 4, 6;"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 603))

    def test_variable_program_4(self):
        """testcase: 604.txt"""
        input = """delta: array [2] of integer = {};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 604))

    def test_function_program_5(self):
        """main: function void () {}"""
        input = """main: function void () {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 605))

    def test_function_program_6(self):
        input ="""
        x: integer = 65;
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
            r,s : integer;
            r = 2.0;
            a,b : array [5] of integer;
            s = r * r * myPi;
            a[0] = s;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 606))
