# Generated from c:\Users\84865\Documents\BK-CSE20\CSE-PPL\programing-code\syntax\programing-1\BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("J\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\5\3\37\n\3\3\4\3\4\5\4#\n\4\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\5\b\64\n\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t>\n\t\3\n\3\n\3\n")
        buf.write("\3\n\5\nD\n\n\3\13\3\13\3\f\3\f\3\f\2\2\r\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\2\3\3\2\4\5\2C\2\30\3\2\2\2\4\36\3\2\2")
        buf.write("\2\6\"\3\2\2\2\b$\3\2\2\2\n(\3\2\2\2\f-\3\2\2\2\16\63")
        buf.write("\3\2\2\2\20=\3\2\2\2\22C\3\2\2\2\24E\3\2\2\2\26G\3\2\2")
        buf.write("\2\30\31\5\4\3\2\31\3\3\2\2\2\32\33\5\6\4\2\33\34\5\6")
        buf.write("\4\2\34\37\3\2\2\2\35\37\5\6\4\2\36\32\3\2\2\2\36\35\3")
        buf.write("\2\2\2\37\5\3\2\2\2 #\5\b\5\2!#\5\n\6\2\" \3\2\2\2\"!")
        buf.write("\3\2\2\2#\7\3\2\2\2$%\5\26\f\2%&\5\22\n\2&\'\7\t\2\2\'")
        buf.write("\t\3\2\2\2()\5\26\f\2)*\7\n\2\2*+\5\f\7\2+,\5\24\13\2")
        buf.write(",\13\3\2\2\2-.\7\6\2\2./\5\16\b\2/\60\7\7\2\2\60\r\3\2")
        buf.write("\2\2\61\64\5\20\t\2\62\64\3\2\2\2\63\61\3\2\2\2\63\62")
        buf.write("\3\2\2\2\64\17\3\2\2\2\65\66\5\26\f\2\66\67\5\22\n\2\67")
        buf.write("8\7\t\2\289\5\20\t\29>\3\2\2\2:;\5\26\f\2;<\5\22\n\2<")
        buf.write(">\3\2\2\2=\65\3\2\2\2=:\3\2\2\2>\21\3\2\2\2?@\7\n\2\2")
        buf.write("@A\7\b\2\2AD\5\22\n\2BD\7\n\2\2C?\3\2\2\2CB\3\2\2\2D\23")
        buf.write("\3\2\2\2EF\7\3\2\2F\25\3\2\2\2GH\t\2\2\2H\27\3\2\2\2\7")
        buf.write("\36\"\63=C")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'body'", "'int'", "'float'", "'('", "')'", 
                     "','", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "INT", "FLOAT", "LB", "RB", 
                      "COMMA", "SEMI", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_funcdecl = 4
    RULE_paradecl = 5
    RULE_paramlist = 6
    RULE_paramterm = 7
    RULE_idlist = 8
    RULE_body = 9
    RULE_typ = 10

    ruleNames =  [ "program", "decls", "decl", "vardecl", "funcdecl", "paradecl", 
                   "paramlist", "paramterm", "idlist", "body", "typ" ]

    EOF = Token.EOF
    T__0=1
    INT=2
    FLOAT=3
    LB=4
    RB=5
    COMMA=6
    SEMI=7
    ID=8
    WS=9
    ERROR_CHAR=10
    UNCLOSE_STRING=11
    ILLEGAL_ESCAPE=12

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

        def decls(self):
            return self.getTypedRuleContext(BKOOLParser.DeclsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.decls()
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

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.DeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.DeclContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_decls




    def decls(self):

        localctx = BKOOLParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.decl()
                self.state = 25
                self.decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(BKOOLParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_decl




    def decl(self):

        localctx = BKOOLParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.funcdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecl




    def vardecl(self):

        localctx = BKOOLParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.typ()
            self.state = 35
            self.idlist()
            self.state = 36
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def paradecl(self):
            return self.getTypedRuleContext(BKOOLParser.ParadeclContext,0)


        def body(self):
            return self.getTypedRuleContext(BKOOLParser.BodyContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_funcdecl




    def funcdecl(self):

        localctx = BKOOLParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.typ()
            self.state = 39
            self.match(BKOOLParser.ID)
            self.state = 40
            self.paradecl()
            self.state = 41
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParadeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_paradecl




    def paradecl(self):

        localctx = BKOOLParser.ParadeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_paradecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(BKOOLParser.LB)
            self.state = 44
            self.paramlist()
            self.state = 45
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramterm(self):
            return self.getTypedRuleContext(BKOOLParser.ParamtermContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramlist




    def paramlist(self):

        localctx = BKOOLParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_paramlist)
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT, BKOOLParser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.paramterm()
                pass
            elif token in [BKOOLParser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class ParamtermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def paramterm(self):
            return self.getTypedRuleContext(BKOOLParser.ParamtermContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramterm




    def paramterm(self):

        localctx = BKOOLParser.ParamtermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_paramterm)
        try:
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.typ()
                self.state = 52
                self.idlist()
                self.state = 53
                self.match(BKOOLParser.SEMI)
                self.state = 54
                self.paramterm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.typ()
                self.state = 57
                self.idlist()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_idlist




    def idlist(self):

        localctx = BKOOLParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_idlist)
        try:
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.match(BKOOLParser.ID)
                self.state = 62
                self.match(BKOOLParser.COMMA)
                self.state = 63
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKOOLParser.RULE_body




    def body(self):

        localctx = BKOOLParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(BKOOLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_typ




    def typ(self):

        localctx = BKOOLParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.INT or _la==BKOOLParser.FLOAT):
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





