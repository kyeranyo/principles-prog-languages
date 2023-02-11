import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def testcase_1(self):
        """TEST SIMPLE CASE"""
        input = """float goo (float a, b) {
    foo(expr, expr, expr);
    return expr;
}

c = expr;"""
        expect = "Error on line 6 col 0: c"
        self.assertTrue(TestParser.test(input, expect, 201))

#     def testcase_2(self):
#         """int a, b,;"""
#         input = """int a, b,;"""
#         expect = "Error on line 1 col 9: ;"
#         self.assertTrue(TestParser.test(input, expect, 202))

#     def testcase_3(self):
#         """float foo(int a, float c, d) body"""
#         input = """float foo(int a, float c, d) body"""
#         expect = "Error on line 1 col 17: float"
#         self.assertTrue(TestParser.test(input, expect, 203))

#     def testcase_4(self):
#         """float foo(int a; float c, d;) body"""
#         input = """float foo(int a; float c, d;) body"""
#         expect = "Error on line 1 col 28: )"
#         self.assertTrue(TestParser.test(input, expect, 204))

#     def testcase_5(self):
#         """int c;
#         float A()"""
#         input = """int c;
# float A()"""
#         expect = "Error on line 2 col 9: <EOF>"
#         self.assertTrue(TestParser.test(input, expect, 205))

#     def testcase_6(self):
#         """int c
#         float A() body"""
#         input = """int c
# float A() body"""
#         expect = "Error on line 2 col 0: float"
#         self.assertTrue(TestParser.test(input, expect, 206))

#     def testcase_7(self):
#         """int a, b,c;
#         float foo(int a; float c, d) body
#         int c,d;
#         float goo (float a, b) body
#         int"""
#         input = """int a, b,c;
#                 float foo(int a; float c, d) body
#                 int c,d;
#                 float goo (float a, b) body
#                 int"""
#         expect = "Error on line 5 col 3: <EOF>"
#         self.assertTrue(TestParser.test(input, expect, 207))

#     def testcase_8(self):
#         """float foo() body
#         int foo() body
#         float foo(int a) body"""
#         input = """float foo() body
#                 int foo() body
#                 float foo(int a) body"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 208))

#     def testcase_9(self):
#         """int a;
#         float b,c;
#         int a;"""
#         input = """int a;
# float b,c;
# int a;"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 209))

#     def testcase_10(self):
#         """int a,b,c;"""
#         input = "int a,b,c;"
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 210))
