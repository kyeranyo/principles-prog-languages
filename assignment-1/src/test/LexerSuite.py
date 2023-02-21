import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_comment_1(self):
        """COMMENT TEST #1 CASE #1"""
        input = "/* A C-style comment */"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 301))

    def test_comment_2(self):
        """COMMENT TEST #2 CASE #1"""
        input = "// A C++ style comment"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 302))

    def test_comment_3(self):
        """COMMENT TEST #3 CASE #1"""
        input = "/*/**/"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 303))

    def test_comment_4(self):
        """COMMENT TEST #4 CASE #1"""
        input = "/*//*/"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 304))

    def test_comment_5(self):
        """COMMENT TEST #5 CASE #1"""
        input = "/**/*/"
        expect = "*,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 305))

    def test_comment_6(self):
        """COMMENT TEST #6 CASE #1"""
        input = "// abc \n xyz"
        expect = "xyz,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 306))

    def test_comment_7(self):
        """COMMENT TEST #7 CASE #1"""
        input = "/*aabbcsda\taaw*/"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 307))

    def test_literals_integer_1(self):
        """INTEGER LITERALS #1 CASE#2"""
        input = "1_72"
        expect = "172,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 101))

    def test_literals_integer_2(self):
        """INTEGER LITERALS #2 CASE#2"""
        input = "1_234_567"
        expect = "1234567,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 102))

    def test_literals_integer_3(self):
        """INTEGER LITERALS #3 CASE#3"""
        input = "1_123"
        expect = "1123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 103))

    def test_literals_integer_4(self):
        """INTEGER LITERALS #4 CASE#4"""
        input = "201"
        expect = "201,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 104))

    def test_literals_integer_5(self):
        """INTEGER LITERALS #5 CASE#5"""
        input = "123_92_213_21"
        expect = "1239221321,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 105))

    def test_literals_float_1(self):
        """FLOAT LITERALS #1 CASE#6"""
        input = "2.01"
        expect = "2.01,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 201))

    def test_literals_float_2(self):
        """FLOAT LITERALS #2 CASE#7"""
        input = "1.234"
        expect = "1.234,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 202))

    def test_literals_float_3(self):
        """FLOAT LITERALS #3 CASE#8"""
        input = "1_234.567"
        expect = "1234.567,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 203))

    def test_literals_float_4(self):
        """FLOAT LITERALS #4 CASE#9"""
        input = "7E-10"
        expect = "7E-10,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 204))

    def test_literals_float_5(self):
        """FLOAT LITERALS #5 CASE#10"""
        input = "0.123e3"
        expect = "0.123e3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 205))

    def test_literals_float_6(self):
        """FLOAT LITERALS #6 CASE#11"""
        input = "0.023e321"
        expect = "0.023e321,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 206))

    def test_literals_float_7(self):
        """FLOAT LITERALS #7 CASE#12"""
        input = "0.00203e301"
        expect = "0.00203e301,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 207))

    def test_literals_string_1(self):
        """STRING LITERALS #1 CASE#13"""
        input = "\"duchunghbo@$%^*7@()mail.com\""
        expect = "duchunghbo@$%^*7@()mail.com,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 401))

    def test_literals_string_2(self):
        """STRING LITERALS #2 CASE#14"""
        input = "\"Hanoi\""
        expect = "Hanoi,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 402))

    def test_literals_string_3(self):
        """STRING LITERALS #3 CASE#15"""
        input = "\"duchungh\to@$%^*7@()mail.com\b\""
        expect = "duchungh\to@$%^*7@()mail.com\b,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 403))

    def test_literals_string_4(self):
        """STRING LITERALS #4 CASE#16"""
        input = "duchungho@$%^*7@()mail.com\""
        expect = "Illegal Escape In String: duchungho@$%^*7@()mail.com\""
        self.assertTrue(TestLexer.test(input, expect, 404))

    def test_literals_string_5(self):
        """STRING LITERALS #5 CASE#17"""
        input = "\"duchungho\b@$%^*7@()ma\til.com\""
        expect = "duchungho\b@$%^*7@()ma\til.com,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 405))

    def test_literals_string_6(self):
        """STRING LITERALS #6 CASE#18"""
        input = "\"duchungh\\o@$%^*7@()mail.com"
        expect = "Unclosed String: \""
        self.assertTrue(TestLexer.test(input, expect, 406))

    def test_literals_string_7(self):
        """STRING LITERALS #7 CASE#19"""
        input = "\"This is string containing tab \t \""
        expect = "This is string containing tab \t ,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 407))

    def test_literals_string_8(self):
        """STRING LITERALS #8 CASE#20"""
        input = """ "He asked me: \\"Where is John?\\"" """
        expect = """He asked me: \\"Where is john\\",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 408))

    def test_literals_string_9(self):
        """STRING LITERALS #9 CASE#21"""
        input = "\"duchungho\r@$%^*7@()%^#$@mail.com\""
        expect = "\"duchungho\r@$%^*7@()%^#$@mail.com\",<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 409))

    def test_literals_string_9(self):
        """STRING LITERALS #10 CASE#22"""
        input = "\"\""
        expect = ",<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 410))

    def test_literals_array_1(self):
        """Simple program: {1,2,3,4,5} """
        input = """{1}"""
        expect = "{1},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 501))

    def test_literals_array_2(self):
        """Simple program: {"Hanoi","Tokyo","London"} """
        input = """{"Hanoi","Tokyo","London"}"""
        expect = "{\"Hanoi\",\"Tokyo\",\"London\"},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 502))
