# Generated from c:\Users\84865\Documents\BK-CSE20\CSE-PPL\assignment-1\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("<\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\6\2\24\n\2\r\2\16\2\25\3\2\3\2\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\5\4 \n\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\5\7\60\n\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\5\b8\n\b\3\t\3\t\3\t\2\2\n\2\4\6\b\n\f\16")
        buf.write("\20\2\3\3\2\b\13\2\67\2\23\3\2\2\2\4\31\3\2\2\2\6\37\3")
        buf.write("\2\2\2\b!\3\2\2\2\n(\3\2\2\2\f*\3\2\2\2\16\67\3\2\2\2")
        buf.write("\209\3\2\2\2\22\24\5\4\3\2\23\22\3\2\2\2\24\25\3\2\2\2")
        buf.write("\25\23\3\2\2\2\25\26\3\2\2\2\26\27\3\2\2\2\27\30\7\2\2")
        buf.write("\3\30\3\3\2\2\2\31\32\5\6\4\2\32\5\3\2\2\2\33\34\7\25")
        buf.write("\2\2\34\35\7\3\2\2\35 \5\6\4\2\36 \7\25\2\2\37\33\3\2")
        buf.write("\2\2\37\36\3\2\2\2 \7\3\2\2\2!\"\7\4\2\2\"#\7\5\2\2#$")
        buf.write("\5\6\4\2$%\7\6\2\2%&\7\7\2\2&\'\5\n\6\2\'\t\3\2\2\2()")
        buf.write("\t\2\2\2)\13\3\2\2\2*+\5\16\b\2+,\7\f\2\2,/\5\n\6\2-.")
        buf.write("\7\r\2\2.\60\5\20\t\2/-\3\2\2\2/\60\3\2\2\2\60\61\3\2")
        buf.write("\2\2\61\62\7\f\2\2\62\r\3\2\2\2\63\64\7\24\2\2\64\65\7")
        buf.write("\3\2\2\658\5\16\b\2\668\7\24\2\2\67\63\3\2\2\2\67\66\3")
        buf.write("\2\2\28\17\3\2\2\29:\5\6\4\2:\21\3\2\2\2\6\25\37/\67")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'array'", "'['", "']'", "'of'", 
                     "'integer'", "'float'", "'boolean'", "'string'", "';'", 
                     "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "COMMENT", "INTEGER_LIT", "FLOAT_LIT", "BOOLEAN_LIT", 
                      "STRING_LIT", "ARRAY_LIT", "IDENTIFIER", "NUMBER", 
                      "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_dimesion = 2
    RULE_array_type = 3
    RULE_element_type = 4
    RULE_variable_decl = 5
    RULE_identifier_list = 6
    RULE_expression_list = 7

    ruleNames =  [ "program", "decls", "dimesion", "array_type", "element_type", 
                   "variable_decl", "identifier_list", "expression_list" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    COMMENT=12
    INTEGER_LIT=13
    FLOAT_LIT=14
    BOOLEAN_LIT=15
    STRING_LIT=16
    ARRAY_LIT=17
    IDENTIFIER=18
    NUMBER=19
    WS=20
    UNCLOSE_STRING=21
    ILLEGAL_ESCAPE=22
    ERROR_CHAR=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def decls(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.DeclsContext)
            else:
                return self.getTypedRuleContext(MT22Parser.DeclsContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_program




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.decls()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MT22Parser.NUMBER):
                    break

            self.state = 21
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimesion(self):
            return self.getTypedRuleContext(MT22Parser.DimesionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decls




    def decls(self):

        localctx = MT22Parser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.dimesion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimesionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(MT22Parser.NUMBER, 0)

        def dimesion(self):
            return self.getTypedRuleContext(MT22Parser.DimesionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_dimesion




    def dimesion(self):

        localctx = MT22Parser.DimesionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_dimesion)
        try:
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.match(MT22Parser.NUMBER)
                self.state = 26
                self.match(MT22Parser.T__0)
                self.state = 27
                self.dimesion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.match(MT22Parser.NUMBER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimesion(self):
            return self.getTypedRuleContext(MT22Parser.DimesionContext,0)


        def element_type(self):
            return self.getTypedRuleContext(MT22Parser.Element_typeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_array_type




    def array_type(self):

        localctx = MT22Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(MT22Parser.T__1)
            self.state = 32
            self.match(MT22Parser.T__2)
            self.state = 33
            self.dimesion()
            self.state = 34
            self.match(MT22Parser.T__3)
            self.state = 35
            self.match(MT22Parser.T__4)
            self.state = 36
            self.element_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MT22Parser.RULE_element_type




    def element_type(self):

        localctx = MT22Parser.Element_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_element_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.T__5) | (1 << MT22Parser.T__6) | (1 << MT22Parser.T__7) | (1 << MT22Parser.T__8))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier_list(self):
            return self.getTypedRuleContext(MT22Parser.Identifier_listContext,0)


        def element_type(self):
            return self.getTypedRuleContext(MT22Parser.Element_typeContext,0)


        def expression_list(self):
            return self.getTypedRuleContext(MT22Parser.Expression_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_variable_decl




    def variable_decl(self):

        localctx = MT22Parser.Variable_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variable_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.identifier_list()
            self.state = 41
            self.match(MT22Parser.T__9)
            self.state = 42
            self.element_type()
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.T__10:
                self.state = 43
                self.match(MT22Parser.T__10)
                self.state = 44
                self.expression_list()


            self.state = 47
            self.match(MT22Parser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Identifier_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def identifier_list(self):
            return self.getTypedRuleContext(MT22Parser.Identifier_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_identifier_list




    def identifier_list(self):

        localctx = MT22Parser.Identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_identifier_list)
        try:
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.match(MT22Parser.IDENTIFIER)
                self.state = 50
                self.match(MT22Parser.T__0)
                self.state = 51
                self.identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.match(MT22Parser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimesion(self):
            return self.getTypedRuleContext(MT22Parser.DimesionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expression_list




    def expression_list(self):

        localctx = MT22Parser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expression_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.dimesion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





