# Generated from c:\Users\84865\Documents\BK-CSE20\CSE-PPL\programing-code\src\main\bkool\parser\BKOOL1.g4 by ANTLR 4.9.2
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
        buf.write("K\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\6\2\26\n\2\r\2\16\2\27\3\2\3")
        buf.write("\2\3\3\3\3\5\3\36\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\60\n\5\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\5\78\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5")
        buf.write("\bA\n\b\3\t\3\t\3\t\3\t\5\tG\n\t\3\n\3\n\3\n\2\2\13\2")
        buf.write("\4\6\b\n\f\16\20\22\2\3\3\2\6\7\2G\2\25\3\2\2\2\4\35\3")
        buf.write("\2\2\2\6\37\3\2\2\2\b/\3\2\2\2\n\61\3\2\2\2\f\67\3\2\2")
        buf.write("\2\16@\3\2\2\2\20F\3\2\2\2\22H\3\2\2\2\24\26\5\4\3\2\25")
        buf.write("\24\3\2\2\2\26\27\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2")
        buf.write("\30\31\3\2\2\2\31\32\7\2\2\3\32\3\3\2\2\2\33\36\5\6\4")
        buf.write("\2\34\36\5\b\5\2\35\33\3\2\2\2\35\34\3\2\2\2\36\5\3\2")
        buf.write("\2\2\37 \t\2\2\2 !\5\20\t\2!\"\7\t\2\2\"\7\3\2\2\2#$\t")
        buf.write("\2\2\2$%\7\n\2\2%&\5\n\6\2&\'\5\22\n\2\'(\5\6\4\2(\60")
        buf.write("\3\2\2\2)*\t\2\2\2*+\7\n\2\2+,\5\n\6\2,-\5\22\n\2-.\5")
        buf.write("\b\5\2.\60\3\2\2\2/#\3\2\2\2/)\3\2\2\2\60\t\3\2\2\2\61")
        buf.write("\62\7\4\2\2\62\63\5\f\7\2\63\64\7\5\2\2\64\13\3\2\2\2")
        buf.write("\658\5\16\b\2\668\3\2\2\2\67\65\3\2\2\2\67\66\3\2\2\2")
        buf.write("8\r\3\2\2\29:\t\2\2\2:;\5\20\t\2;<\7\t\2\2<=\5\16\b\2")
        buf.write("=A\3\2\2\2>?\t\2\2\2?A\5\20\t\2@9\3\2\2\2@>\3\2\2\2A\17")
        buf.write("\3\2\2\2BC\7\n\2\2CD\7\b\2\2DG\5\20\t\2EG\7\n\2\2FB\3")
        buf.write("\2\2\2FE\3\2\2\2G\21\3\2\2\2HI\7\3\2\2I\23\3\2\2\2\b\27")
        buf.write("\35/\67@F")
        return buf.getvalue()


class BKOOL1Parser ( Parser ):

    grammarFileName = "BKOOL1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'body'", "'('", "')'", "'int'", "'float'", 
                     "','", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "LB", "RB", "INT", "FLOAT", 
                      "COMMA", "SEMI", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_vardecl = 2
    RULE_funcdecl = 3
    RULE_paradecl = 4
    RULE_paramlist = 5
    RULE_paramterm = 6
    RULE_idlist = 7
    RULE_body = 8

    ruleNames =  [ "program", "decl", "vardecl", "funcdecl", "paradecl", 
                   "paramlist", "paramterm", "idlist", "body" ]

    EOF = Token.EOF
    T__0=1
    LB=2
    RB=3
    INT=4
    FLOAT=5
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

        def EOF(self):
            return self.getToken(BKOOL1Parser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOL1Parser.DeclContext)
            else:
                return self.getTypedRuleContext(BKOOL1Parser.DeclContext,i)


        def getRuleIndex(self):
            return BKOOL1Parser.RULE_program




    def program(self):

        localctx = BKOOL1Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.decl()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOL1Parser.INT or _la==BKOOL1Parser.FLOAT):
                    break

            self.state = 23
            self.match(BKOOL1Parser.EOF)
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
            return self.getTypedRuleContext(BKOOL1Parser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(BKOOL1Parser.FuncdeclContext,0)


        def getRuleIndex(self):
            return BKOOL1Parser.RULE_decl




    def decl(self):

        localctx = BKOOL1Parser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
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

        def idlist(self):
            return self.getTypedRuleContext(BKOOL1Parser.IdlistContext,0)


        def SEMI(self):
            return self.getToken(BKOOL1Parser.SEMI, 0)

        def INT(self):
            return self.getToken(BKOOL1Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOL1Parser.FLOAT, 0)

        def getRuleIndex(self):
            return BKOOL1Parser.RULE_vardecl




    def vardecl(self):

        localctx = BKOOL1Parser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            _la = self._input.LA(1)
            if not(_la==BKOOL1Parser.INT or _la==BKOOL1Parser.FLOAT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 30
            self.idlist()
            self.state = 31
            self.match(BKOOL1Parser.SEMI)
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

        def ID(self):
            return self.getToken(BKOOL1Parser.ID, 0)

        def paradecl(self):
            return self.getTypedRuleContext(BKOOL1Parser.ParadeclContext,0)


        def body(self):
            return self.getTypedRuleContext(BKOOL1Parser.BodyContext,0)


        def INT(self):
            return self.getToken(BKOOL1Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOL1Parser.FLOAT, 0)

        def vardecl(self):
            return self.getTypedRuleContext(BKOOL1Parser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(BKOOL1Parser.FuncdeclContext,0)


        def getRuleIndex(self):
            return BKOOL1Parser.RULE_funcdecl




    def funcdecl(self):

        localctx = BKOOL1Parser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                _la = self._input.LA(1)
                if not(_la==BKOOL1Parser.INT or _la==BKOOL1Parser.FLOAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 34
                self.match(BKOOL1Parser.ID)
                self.state = 35
                self.paradecl()
                self.state = 36
                self.body()

                self.state = 37
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                _la = self._input.LA(1)
                if not(_la==BKOOL1Parser.INT or _la==BKOOL1Parser.FLOAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 40
                self.match(BKOOL1Parser.ID)
                self.state = 41
                self.paradecl()
                self.state = 42
                self.body()

                self.state = 43
                self.funcdecl()
                pass


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
            return self.getToken(BKOOL1Parser.LB, 0)

        def paramlist(self):
            return self.getTypedRuleContext(BKOOL1Parser.ParamlistContext,0)


        def RB(self):
            return self.getToken(BKOOL1Parser.RB, 0)

        def getRuleIndex(self):
            return BKOOL1Parser.RULE_paradecl




    def paradecl(self):

        localctx = BKOOL1Parser.ParadeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_paradecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(BKOOL1Parser.LB)
            self.state = 48
            self.paramlist()
            self.state = 49
            self.match(BKOOL1Parser.RB)
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
            return self.getTypedRuleContext(BKOOL1Parser.ParamtermContext,0)


        def getRuleIndex(self):
            return BKOOL1Parser.RULE_paramlist




    def paramlist(self):

        localctx = BKOOL1Parser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_paramlist)
        try:
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOL1Parser.INT, BKOOL1Parser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.paramterm()
                pass
            elif token in [BKOOL1Parser.RB]:
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

        def idlist(self):
            return self.getTypedRuleContext(BKOOL1Parser.IdlistContext,0)


        def SEMI(self):
            return self.getToken(BKOOL1Parser.SEMI, 0)

        def paramterm(self):
            return self.getTypedRuleContext(BKOOL1Parser.ParamtermContext,0)


        def INT(self):
            return self.getToken(BKOOL1Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOL1Parser.FLOAT, 0)

        def getRuleIndex(self):
            return BKOOL1Parser.RULE_paramterm




    def paramterm(self):

        localctx = BKOOL1Parser.ParamtermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_paramterm)
        self._la = 0 # Token type
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                _la = self._input.LA(1)
                if not(_la==BKOOL1Parser.INT or _la==BKOOL1Parser.FLOAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 56
                self.idlist()
                self.state = 57
                self.match(BKOOL1Parser.SEMI)
                self.state = 58
                self.paramterm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                _la = self._input.LA(1)
                if not(_la==BKOOL1Parser.INT or _la==BKOOL1Parser.FLOAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 61
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
            return self.getToken(BKOOL1Parser.ID, 0)

        def COMMA(self):
            return self.getToken(BKOOL1Parser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKOOL1Parser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOL1Parser.RULE_idlist




    def idlist(self):

        localctx = BKOOL1Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_idlist)
        try:
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.match(BKOOL1Parser.ID)
                self.state = 65
                self.match(BKOOL1Parser.COMMA)
                self.state = 66
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(BKOOL1Parser.ID)
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
            return BKOOL1Parser.RULE_body




    def body(self):

        localctx = BKOOL1Parser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(BKOOL1Parser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





