import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    # ----- String literal -------
    def test_string_1(self):
        input = """ "He asked me: \\\"Where is John?\\\"" """
        expect = """He asked me: \\\"Where is John?\\\",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 101))

    def test_string_2(self):
        input = """ "Nguoi co don cho doi em\n" """
        expect = """Unclosed String: Nguoi co don cho doi em"""
        self.assertTrue(TestLexer.test(input, expect, 102))

    def test_string_3(self):
        input = """ "nguyen ly ngon ngu l@p tr1nh \\b \\t" """
        expect = """nguyen ly ngon ngu l@p tr1nh \\b \\t,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 103))

    def test_string_4(self):
        input = """ "duchungh0 \\n \\r \\f" """
        expect = """duchungh0 \\n \\r \\f,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 104))

    def test_string_5(self):
        input = """ "This is Hung\'s PC" """
        expect = """This is Hung\'s PC,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 105))

    def test_string_6(self):
        input = """ "Chuoi \\"cua\\" ban la: \\"12345\\"" """
        expect = """Chuoi \\"cua\\" ban la: \\"12345\\",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 106))

    def test_string_7(self):
        input = """ "Chuoi cua ban la: \\"12345\\"" """
        expect = """Chuoi cua ban la: \\"12345\\",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 107))

    def test_string_8(self):
        input = """ "@#$&^@$(@(ahs\\"ash\\"%%@&@\\"dsad\\"123&^@@" """
        expect = """@#$&^@$(@(ahs\\"ash\\"%%@&@\\"dsad\\"123&^@@,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 108))

    def test_string_9(self):
        input = """ "@#$&\t^@$(@(ahs\\"ash\\"%%@&@\\"dsad\\"123&^@@" """
        expect = """@#$&\t^@$(@(ahs\\"ash\\"%%@&@\\"dsad\\"123&^@@,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 109))

    def test_string_10(self):
        input = """ "@#$\b&^@$(@(ahs\\"ash\\"%%@&@\\"dsad\\"123&^@@" """
        expect = """@#$\b&^@$(@(ahs\\"ash\\"%%@&@\\"dsad\\"123&^@@,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 110))

    #  ---------- Unclose String -------------
    def test_string_unclose_1(self):
        input = """ "Sang mai hoc ppl luc 8h """
        expect = """Unclosed String: Sang mai hoc ppl luc 8h """
        self.assertTrue(TestLexer.test(input, expect, 201))

    def test_string_unclose_2(self):
        input = """ "Cac ki tu dac biet \\b \\t \\r \\n """
        expect = """Unclosed String: Cac ki tu dac biet \\b \\t \\r \\n """
        self.assertTrue(TestLexer.test(input, expect, 202))

    def test_string_unclose_3(self):
        input = """ "chuoi nay chua dong \\\\ abc'"hello" """
        expect = """chuoi nay chua dong \\\\ abc',hello,Unclosed String:  """
        self.assertTrue(TestLexer.test(input, expect, 203))

    def test_string_unclose_4(self):
        input = """ "chuoi nay" chua dong \\\\ abc'"hello" """
        expect = """chuoi nay,chua,dong,Error Token \\"""
        self.assertTrue(TestLexer.test(input, expect, 204))

    def test_string_unclose_5(self):
        input = """ abcyxhhcmut"bchw """
        expect = """abcyxhhcmut,Unclosed String: bchw """
        self.assertTrue(TestLexer.test(input, expect, 205))

    def test_string_unclose_6(self):
        input = """ "Ho Duc\n Hung" """
        expect = """Unclosed String: Ho Duc"""""
        self.assertTrue(TestLexer.test(input, expect, 206))

    def test_string_unclose_7(self):
        input = """ "Ho Duc Hung \n" """
        expect ="""Unclosed String: Ho Duc Hung """
        self.assertTrue(TestLexer.test(input, expect, 207))

    def test_string_unclose_8(self):
        input = """ "Ho Duc Hung \n abc"""
        expect = """Unclosed String: Ho Duc Hung """
        self.assertTrue(TestLexer.test(input, expect, 208))

    def test_string_unclose_9(self):
        input = """ "Ho Duc Hung \n hungdeptraivippro" """
        expect = """Unclosed String: Ho Duc Hung """
        self.assertTrue(TestLexer.test(input, expect, 209))
    #  ---------- Illegal Escape In String -------------

    def test_string_Illegal_1(self):
        input = """ "Day la chuoi chu \\@ ki tu dac biet \\@" """
        expect = """Illegal Escape In String: Day la chuoi chu \\@"""
        self.assertTrue(TestLexer.test(input, expect, 301))

    def test_string_Illegal_2(self):
        input = """ "product by \\t yes \\i 1c4n hcmut" """
        expect = """Illegal Escape In String: product by \\t yes \\i"""
        self.assertTrue(TestLexer.test(input, expect, 302))

    def test_string_Illegal_3(self):
        input = """ "IEls fo my acb\\\\ the dst \\q \\\\ se rat dep do\\> " """
        expect = """Illegal Escape In String: IEls fo my acb\\\\ the dst \\q"""
        self.assertTrue(TestLexer.test(input, expect, 303))

    def test_string_Illegal_4(self):
        input = """ "IEls fo my acb\t the dst \\q \\\\ se rat dep do\\> " """
        expect = """Illegal Escape In String: IEls fo my acb\t the dst \\q"""
        self.assertTrue(TestLexer.test(input, expect, 304))

    def test_string_Illegal_5(self):
        input = """ "IEls fo my acb\\t the dst \\q \\\\ se rat dep do\\> " """
        expect = """Illegal Escape In String: IEls fo my acb\\t the dst \\q"""
        self.assertTrue(TestLexer.test(input, expect, 305))

    def test_string_Illegal_6(self):
        input = """ "IEls fo\\b my acb\\t the dst \\' \\\\ se rat dep do\\> " """
        expect = """Illegal Escape In String: IEls fo\\b my acb\\t the dst \\' \\\\ se rat dep do\\>"""
        self.assertTrue(TestLexer.test(input, expect, 306))

    def test_string_Illegal_7(self):
        input = """ "IEls fo\\" my acb\\t the dst \\' \\\\ se rat dep do\\> " """
        expect = """Illegal Escape In String: IEls fo\\" my acb\\t the dst \\' \\\\ se rat dep do\\>"""
        self.assertTrue(TestLexer.test(input, expect, 307))

    def test_string_Illegal_8(self):
        input = """ "IEls fo\\q my acb\\t the dst \\' \\\\ se rat dep do\\> " """
        expect = """Illegal Escape In String: IEls fo\\q"""
        self.assertTrue(TestLexer.test(input, expect, 308))

    def test_string_Illegal_9(self):
        input = """ "IEls fo\\y my acb\\y the dst \\' \\\\ se rat dep do\\> " """
        expect = """Illegal Escape In String: IEls fo\\y"""
        self.assertTrue(TestLexer.test(input, expect, 309))

    def test_string_Illegal_10(self):
        input = """ "dem het thu 6 qua \\s ang thu hai" """
        expect = "Illegal Escape In String: dem het thu 6 qua \\s"
        self.assertTrue(TestLexer.test(input, expect, 310))

    def test_string_Illegal_11(self):
        input = """ "dem het thu 6 qua \\q ang thu hai" """
        expect = "Illegal Escape In String: dem het thu 6 qua \\q"
        self.assertTrue(TestLexer.test(input, expect, 311))

    def test_string_Illegal_12(self):
        input = """ "dem het thu 6 qua \\e ang thu hai" """
        expect = "Illegal Escape In String: dem het thu 6 qua \\e"
        self.assertTrue(TestLexer.test(input, expect, 312))

    def test_string_Illegal_13(self):
        input = """ "dem het thu 6 qua \\o ang thu hai" """
        expect = "Illegal Escape In String: dem het thu 6 qua \\o"
        self.assertTrue(TestLexer.test(input, expect, 313))

    def test_string_Illegal_14(self):
        input = """ "dem het thu 6 qua \\p ang thu hai" """
        expect = "Illegal Escape In String: dem het thu 6 qua \\p"
        self.assertTrue(TestLexer.test(input, expect, 314))

    def test_string_Illegal_15(self):
        input = """ "dem het thu 6 qua \\k ang thu hai" """
        expect = "Illegal Escape In String: dem het thu 6 qua \\k"
        self.assertTrue(TestLexer.test(input, expect, 315))

    def test_string_Illegal_16(self):
        input = """ "dem het thu 6 qua \\z ang thu hai" """
        expect = "Illegal Escape In String: dem het thu 6 qua \\z"
        self.assertTrue(TestLexer.test(input, expect, 316))

    def test_string_Illegal_17(self):
        input = """ "dem het thu 6 qua \\l ang thu hai" """
        expect = "Illegal Escape In String: dem het thu 6 qua \\l"
        self.assertTrue(TestLexer.test(input, expect, 317))

    def test_string_Illegal_18(self):
        input = """ "dem het thu 6 qua \\g ang thu hai" """
        expect = "Illegal Escape In String: dem het thu 6 qua \\g"
        self.assertTrue(TestLexer.test(input, expect, 318))

    def test_string_Illegal_19(self):
        input = """ "dem het thu 6 qua \\hang thu hai" """
        expect = "Illegal Escape In String: dem het thu 6 qua \\h"
        self.assertTrue(TestLexer.test(input, expect, 319))
    #  ---------- Keyword -------------

    def test_keyword_1(self):
        input = """ for do while{}factor true false """
        expect = """for,do,while,{,},factor,true,false,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 401))

    def test_keyword_2(self):
        input = """ continue for break{}; true false """
        expect = """continue,for,break,{,},;,true,false,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 402))

    # ------------ INTLIT ---------------

    def test_intlit_1(self):
        input = """ 1_23_1414_214 """
        expect = """1231414214,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 501))

    def test_intlit_2(self):
        input = """ 0_23_1414_214 """
        expect = """0,_23_1414_214,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 502))

    def test_intlit_3(self):
        input = """ 1_23_1414_214 """
        expect = """1231414214,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 503))

    def test_intlit_4(self):
        input = """ 3200_21000_123_000 """
        expect = """320021000123000,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 504))

    def test_intlit_5(self):
        input = """ 100000000_12 """
        expect = """10000000012,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 505))

    # ------------- FLOATLIT --------------

    def test_floatlit_1(self):
        input = """ 1_23.4_56 """
        expect = """123.4,_56,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 601))

    def test_floatlit_2(self):
        input = """ 0.4_5_6 """
        expect = """0.4,_5_6,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 602))

    def test_floatlit_3(self):
        input = """ 1_23.456e-10 """
        expect = """123.456e-10,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 603))

    def test_floatlit_4(self):
        input = """ 1_23e+4_56 """
        expect = """123e+4,_56,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 604))

    def test_floatlit_5(self):
        input = """ 1_23E-456 """
        expect = """123E-456,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 605))

    def test_floatlit_6(self):
        input = """ 1_23.4E+56 """
        expect = """123.4E+56,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 606))

    def test_floatlit_7(self):
        input = """ 1_23.000456E-10 """
        expect = """123.000456E-10,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 607))

    def test_floatlit_8(self):
        input = """ 1_23.04E-56 """
        expect = """123.04E-56,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 608))

    def test_floatlit_9(self):
        input = """ 1_2.0e-34_56 """
        expect = """12.0e-34,_56,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 609))

    def test_floatlit_10(self):
        input = """ 1_23.40E+156 """
        expect = """123.40E+156,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 610))

    # -------------- IDENTIFIER --------------

    def test_identifier_1(self):
        input = "___duchungho@abc"
        expect = "___duchungho,Error Token @"
        self.assertTrue(TestLexer.test(input, expect, 611))

    def test_identifier_2(self):
        input = "duchungprovip123"
        expect = "duchungprovip123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 612))

    def test_identifier_3(self):
        input = "3nguoicodonchodoiem"
        expect = "3,nguoicodonchodoiem,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 613))

    def test_identifier_4(self):
        input = "k_123_hcmut_edu_vn"
        expect = "k_123_hcmut_edu_vn,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 614))

    def test_identifier_5(self):
        input = "_123_hcmut_edu_vn"
        expect = "_123_hcmut_edu_vn,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 615))

    def test_identifier_6(self):
        input = "_123_hc__mut_edu_vn"
        expect = "_123_hc__mut_edu_vn,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 616))

    def test_identifier_7(self):
        input = "_123_hcmut@_edu_vn"
        expect = "_123_hcmut,Error Token @"
        self.assertTrue(TestLexer.test(input, expect, 617))

    def test_identifier_8(self):
        input = "~_123_hcmut@_edu_vn"
        expect = "Error Token ~"
        self.assertTrue(TestLexer.test(input, expect, 617))

    #: COMMENT STYLE
    def test_comment_1(self):
        input = "// abc xuz anc \n abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect, 621))

    def test_comment_2(self):
        input = "// abc 123124!$@!$%!@%!@$\t\b\fxuz anc \n abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect, 622))

    def test_comment_3(self):
        input = "// ab_____\tc xuz anc \r abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect, 623))

    def test_comment_4(self):
        input = "// abc x//uz anc \n abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect, 624))

    def test_comment_5(self):
        input = "// abc \bxuz anc \n abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect, 625))

    def test_comment_6(self):
        input = "// ab~?/][8134270014c xuz anc \n abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect, 626))

    def test_comment_7(self):
        input = "// abc x....1412481481246235$!$@^uz anc \n abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect, 627))

    def test_comment_8(self):
        input = "// /*abc x....1412481481246235$!$@^uz*/ anc \n abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect, 628))

    def test_comment_9(self):
        input = "// bac xyz \n /*neu nhu anh lo yeu em tu dau*/ \n abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect, 629))

    def test_comment_10(self):
        input = "// neu nhu anh lo yeu em dam sau \n /*neu nhu anh lo yeu em dai lau*/ \n abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect, 630))

    def test_comment_11(self):
        input = "// ngay troi qua voi \n // anh chang mong chung minh thanh doi \n /*nguoi buoc di qua doi toi*/ \n abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input,expect, 631))

    def test_comment_12(self):
        input = "/*qua hai gio sang sao */ em khong ve chung voi anh*/"
        expect = "em,khong,ve,chung,voi,anh,*,/,<EOF>"
        self.assertTrue(TestLexer.test(input,expect, 632))

    def test_comment_13(self):
        input = "/*tran khac chan nam qua xa, */ \n //ve day voi nhau hai dua dap chung men*/ abcxyz"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input,expect, 633))

    def test_comment_14(self):
        input = "/* ba ma em dang di choi vung tau, het hon hai ngay, ve nha di anh nau com*/"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 634))

    def test_comment_15(self):
        input = "/* anh lay xe wave alpha dua em di toi da lat ... thang ba */ abc */  "
        expect = "abc,*,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 635))

    def test_comment_16(self):
        input = "/* anh muon ta ve cung mot nha, an sang va cung hat ca */ // nhung biet sao gio  "
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 635))

    def test_comment_17(self):
        input = "/* anh muon ta ve cung\t \n \r \b mot nha, an sang va cung hat ca */ // nhung biet sao gio  "
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 636))

    #: OTHER

    def testOther_0(self):
        input = """x == y != z > w >= v < u <= t"""
        expect = """x,==,y,!=,z,>,w,>=,v,<,u,<=,t,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 700))

    def testOther_1(self):
        input = """(a + b) * (c - d)"""
        expect = """(,a,+,b,),*,(,c,-,d,),<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 701))

    def testOther_2(self):
        input = """if x > y then x = x - y else x = x + y"""
        expect = """if,x,>,y,then,x,=,x,-,y,else,x,=,x,+,y,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 702))

    def testOther_3(self):
        input = """for i = 1 to 10 do print(i)"""
        expect = """for,i,=,1,to,10,do,print,(,i,),<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 703))

    def testOther_4(self):
        input = """x = 5 // This is a comment"""
        expect = """x,=,5,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect,704))

    def testOther_6(self):
        input = """/* This is a\nmulti-line comment\n*/ x = 5"""
        expect = """x,=,5,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 705))

    def testOther_7(self):
        input = """"/* This is a /* nested */ comment */"""
        expect = """Unclosed String: /* This is a /* nested */ comment */"""
        self.assertTrue(TestLexer.test(input, expect, 706))

    def testOther_8(self):
        input = """a(ssddd) _ass1234546ee "*&(*@^@)()*/-122@*@" """
        expect = """a,(,ssddd,),_ass1234546ee,*&(*@^@)()*/-122@*@,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 707))

    def testOther_9(self):
        input = """{ "name": "John", "age": 30 }"""
        expect = """{,name,:,John,,,age,:,30,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 708))

    def testOther_10(self):
        input = """Helllo haalooo 123 123123 01213 .eas2184 "aaaabbbc &&*(((@)))" """
        expect = """Helllo,haalooo,123,123123,0,1213,.,eas2184,aaaabbbc &&*(((@))),<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 709))

    def testOther_11(self):
        input = """+ - * / %"""
        expect = """+,-,*,/,%,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 710))
    # --- Boolean Operators -----

    def testOther_12(self):
        input = """! && ||"""
        expect = """!,&&,||,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 711))
    # --- Relational Operators -----

    def testOther_13(self):
        input = """== != < > <= >="""
        expect = """==,!=,<,>,<=,>=,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 712))
    # --- String Operators -----

    def testOther_14(self):
        input = """::"""
        expect = """::,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 713))
    # --------------- Separators ------------

    def testOther_15(self):
        input = """{ }"""
        expect = """{,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 714))

    def testOther_16(self):
        input = """[ ]"""
        expect = """[,],<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 715))

    def testOther_17(self):
        input = """( )"""
        expect = """(,),<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 716))

    def testOther_18(self):
        input = """."""
        expect = """.,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 717))

    def testOther_19(self):
        input = ""","""
        expect = """,,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 718))

    def testOther_20(self):
        input = """ "Hello, World" """
        expect = """Hello, World,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 719))