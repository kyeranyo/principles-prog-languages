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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3=")
        buf.write(";\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3\2\3\2\3")
        buf.write("\3\3\3\5\3\35\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\5\5+\n\5\3\5\3\5\3\6\3\6\3\6\3\6\5\6\63\n")
        buf.write("\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\2\2\n\2\4\6\b\n\f\16\20")
        buf.write("\2\3\6\2\13\13\16\16\21\21\23\23\2\66\2\25\3\2\2\2\4\34")
        buf.write("\3\2\2\2\6\36\3\2\2\2\b%\3\2\2\2\n\62\3\2\2\2\f\64\3\2")
        buf.write("\2\2\16\66\3\2\2\2\208\3\2\2\2\22\24\5\4\3\2\23\22\3\2")
        buf.write("\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\30\3")
        buf.write("\2\2\2\27\25\3\2\2\2\30\31\7\2\2\3\31\3\3\2\2\2\32\35")
        buf.write("\5\6\4\2\33\35\5\b\5\2\34\32\3\2\2\2\34\33\3\2\2\2\35")
        buf.write("\5\3\2\2\2\36\37\7\r\2\2\37 \7\64\2\2 !\5\20\t\2!\"\7")
        buf.write("\65\2\2\"#\7\27\2\2#$\5\16\b\2$\7\3\2\2\2%&\5\n\6\2&\'")
        buf.write("\7\61\2\2\'*\5\16\b\2()\7\60\2\2)+\5\f\7\2*(\3\2\2\2*")
        buf.write("+\3\2\2\2+,\3\2\2\2,-\7/\2\2-\t\3\2\2\2./\7*\2\2/\60\7")
        buf.write(".\2\2\60\63\5\n\6\2\61\63\7*\2\2\62.\3\2\2\2\62\61\3\2")
        buf.write("\2\2\63\13\3\2\2\2\64\65\5\20\t\2\65\r\3\2\2\2\66\67\t")
        buf.write("\2\2\2\67\17\3\2\2\289\78\2\29\21\3\2\2\2\6\25\34*\62")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'auto'", "'break'", 
                     "'integer'", "'void'", "'array'", "'float'", "'return'", 
                     "'out'", "'boolean'", "'for'", "'string'", "'continue'", 
                     "'do'", "'function'", "'of'", "'else'", "'if'", "'while'", 
                     "'inherit'", "'+'", "'-'", "'*'", "'/'", "'%'", "'<'", 
                     "'>'", "'<='", "'>='", "'!'", "'&&'", "'||'", "'=='", 
                     "'!='", "<INVALID>", "<INVALID>", "'::'", "'.'", "','", 
                     "';'", "'='", "':'", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "INTEGER_LIT", "FLOAT_LIT", 
                      "BOOLEAN_LIT", "STRING_LIT", "ARRAY_LIT", "AUTO", 
                      "BREAK", "INTEGER", "VOID", "ARRAY", "FLOAT", "RETURN", 
                      "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", 
                      "FUNCTION", "OF", "ELSE", "IF", "WHILE", "INHERIT", 
                      "PLUS", "MINUS", "MUL", "DIV", "MOD", "LESS", "GREATER", 
                      "LESS_THAN_OR_EQUAL", "GREATER_THAN_OR_EQUAL", "NOT", 
                      "AND", "OR", "EQUAL_TO", "NOT_EQUAL", "IDENTIFIER", 
                      "NUMBER", "SCOPE_RES", "PERIOD", "COMMA", "SEMI", 
                      "EQUAL", "COLON", "LB", "RB", "LSB", "RSB", "LCB", 
                      "RCB", "NUMLIST", "STRINGLIST", "WS", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_array_type = 2
    RULE_variable_decl = 3
    RULE_identifier_list = 4
    RULE_expression_list = 5
    RULE_element_type = 6
    RULE_dimesion = 7

    ruleNames =  [ "program", "decls", "array_type", "variable_decl", "identifier_list", 
                   "expression_list", "element_type", "dimesion" ]

    EOF = Token.EOF
    COMMENT=1
    INTEGER_LIT=2
    FLOAT_LIT=3
    BOOLEAN_LIT=4
    STRING_LIT=5
    ARRAY_LIT=6
    AUTO=7
    BREAK=8
    INTEGER=9
    VOID=10
    ARRAY=11
    FLOAT=12
    RETURN=13
    OUT=14
    BOOLEAN=15
    FOR=16
    STRING=17
    CONTINUE=18
    DO=19
    FUNCTION=20
    OF=21
    ELSE=22
    IF=23
    WHILE=24
    INHERIT=25
    PLUS=26
    MINUS=27
    MUL=28
    DIV=29
    MOD=30
    LESS=31
    GREATER=32
    LESS_THAN_OR_EQUAL=33
    GREATER_THAN_OR_EQUAL=34
    NOT=35
    AND=36
    OR=37
    EQUAL_TO=38
    NOT_EQUAL=39
    IDENTIFIER=40
    NUMBER=41
    SCOPE_RES=42
    PERIOD=43
    COMMA=44
    SEMI=45
    EQUAL=46
    COLON=47
    LB=48
    RB=49
    LSB=50
    RSB=51
    LCB=52
    RCB=53
    NUMLIST=54
    STRINGLIST=55
    WS=56
    UNCLOSE_STRING=57
    ILLEGAL_ESCAPE=58
    ERROR_CHAR=59

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
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MT22Parser.ARRAY or _la==MT22Parser.IDENTIFIER:
                self.state = 16
                self.decls()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
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

        def array_type(self):
            return self.getTypedRuleContext(MT22Parser.Array_typeContext,0)


        def variable_decl(self):
            return self.getTypedRuleContext(MT22Parser.Variable_declContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decls




    def decls(self):

        localctx = MT22Parser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.array_type()
                pass
            elif token in [MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.variable_decl()
                pass
            else:
                raise NoViableAltException(self)

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

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def dimesion(self):
            return self.getTypedRuleContext(MT22Parser.DimesionContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def OF(self):
            return self.getToken(MT22Parser.OF, 0)

        def element_type(self):
            return self.getTypedRuleContext(MT22Parser.Element_typeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_array_type




    def array_type(self):

        localctx = MT22Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(MT22Parser.ARRAY)
            self.state = 29
            self.match(MT22Parser.LSB)
            self.state = 30
            self.dimesion()
            self.state = 31
            self.match(MT22Parser.RSB)
            self.state = 32
            self.match(MT22Parser.OF)
            self.state = 33
            self.element_type()
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


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def element_type(self):
            return self.getTypedRuleContext(MT22Parser.Element_typeContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def EQUAL(self):
            return self.getToken(MT22Parser.EQUAL, 0)

        def expression_list(self):
            return self.getTypedRuleContext(MT22Parser.Expression_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_variable_decl




    def variable_decl(self):

        localctx = MT22Parser.Variable_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.identifier_list()
            self.state = 36
            self.match(MT22Parser.COLON)
            self.state = 37
            self.element_type()
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.EQUAL:
                self.state = 38
                self.match(MT22Parser.EQUAL)
                self.state = 39
                self.expression_list()


            self.state = 42
            self.match(MT22Parser.SEMI)
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

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def identifier_list(self):
            return self.getTypedRuleContext(MT22Parser.Identifier_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_identifier_list




    def identifier_list(self):

        localctx = MT22Parser.Identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_identifier_list)
        try:
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.match(MT22Parser.IDENTIFIER)
                self.state = 45
                self.match(MT22Parser.COMMA)
                self.state = 46
                self.identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
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
        self.enterRule(localctx, 10, self.RULE_expression_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.dimesion()
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

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_element_type




    def element_type(self):

        localctx = MT22Parser.Element_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_element_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTEGER) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.STRING))) != 0)):
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


    class DimesionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMLIST(self):
            return self.getToken(MT22Parser.NUMLIST, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_dimesion




    def dimesion(self):

        localctx = MT22Parser.DimesionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_dimesion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(MT22Parser.NUMLIST)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





