import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_literals_integer_1(self):
        """INTEGER LITERALS #1 CASE#1"""
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
        input = "0_123"
        expect = "0,Error Token _"
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

    # def test_literals_string_1(self):
    #     """STRING LITERALS #1 CASE#13"""
    #     input = "\"duchungh\bo@$%^*7@()mail.com\""
    #     expect = "\"duchungh\bo@$%^*7@()mail.com\",<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 401))

    # def test_literals_string_2(self):
    #     """STRING LITERALS #2 CASE#14"""
    #     input = "\"duchungh\fo@$%^*7@()mail.com\""
    #     expect = "\"duchungh\fo@$%^*7@()mail.com\",<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 402))

    # def test_literals_string_3(self):
    #     """STRING LITERALS #3 CASE#15"""
    #     input = "\"duchungh\ro@$%^*7@()mail.com\""
    #     expect = "\"duchungh\ro@$%^*7@()mail.com\",<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 403))

    # def test_literals_string_4(self):
    #     """STRING LITERALS #4 CASE#16"""
    #     input = "\"duchungh\no@$%^*7@()mail.com\""
    #     expect = "\"duchungh\no@$%^*7@()mail.com\",<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 404))

    # def test_literals_string_5(self):
    #     """STRING LITERALS #5 CASE#17"""
    #     input = "\"duchungh\'o@$%^*7@()mail.com\""
    #     expect = "\"duchungh\'o@$%^*7@()mail.com\",<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 405))

    # def test_literals_string_6(self):
    #     """STRING LITERALS #6 CASE#18"""
    #     input = "\"duchungh\\o@$%^*7@()mail.com\""
    #     expect = "\"duchungh\\o@$%^*7@()mail.com\",<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 406))

    def test_literals_string_7(self):
        """STRING LITERALS #7 CASE#19"""
        input = "\"This is string containing tab \t \""
        expect = "\"This is string containing tab \t \",<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 407))

    def test_literals_string_8(self):
        """STRING LITERALS #8 CASE#20"""
        input = "\"He asked me \"Where is John\"\""
        expect = "\"He asked me \"Where is John\"\",<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 408))
