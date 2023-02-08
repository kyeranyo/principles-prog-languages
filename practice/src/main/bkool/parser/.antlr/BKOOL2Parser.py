# Generated from c:\Users\84865\Documents\BK-CSE20\CSE-PPL\programing-code\src\main\bkool\parser\BKOOL2.g4 by ANTLR 4.9.2
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
        buf.write("F\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\3\3\3\3\3\3\5\3\33\n")
        buf.write("\3\3\4\3\4\5\4\37\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\7\6")
        buf.write("(\n\6\f\6\16\6+\13\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\5\b\64")
        buf.write("\n\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\7\t?\n\t\f\t")
        buf.write("\16\tB\13\t\3\n\3\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2")
        buf.write("\3\3\2\7\b\2A\2\24\3\2\2\2\4\32\3\2\2\2\6\36\3\2\2\2\b")
        buf.write(" \3\2\2\2\n$\3\2\2\2\f,\3\2\2\2\16\61\3\2\2\2\20\67\3")
        buf.write("\2\2\2\22C\3\2\2\2\24\25\5\4\3\2\25\3\3\2\2\2\26\27\5")
        buf.write("\6\4\2\27\30\5\4\3\2\30\33\3\2\2\2\31\33\5\6\4\2\32\26")
        buf.write("\3\2\2\2\32\31\3\2\2\2\33\5\3\2\2\2\34\37\5\b\5\2\35\37")
        buf.write("\5\f\7\2\36\34\3\2\2\2\36\35\3\2\2\2\37\7\3\2\2\2 !\5")
        buf.write("\22\n\2!\"\5\n\6\2\"#\7\t\2\2#\t\3\2\2\2$)\7\n\2\2%&\7")
        buf.write("\3\2\2&(\7\n\2\2\'%\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2")
        buf.write("\2\2*\13\3\2\2\2+)\3\2\2\2,-\5\22\n\2-.\7\n\2\2./\5\16")
        buf.write("\b\2/\60\7\4\2\2\60\r\3\2\2\2\61\63\7\5\2\2\62\64\5\20")
        buf.write("\t\2\63\62\3\2\2\2\63\64\3\2\2\2\64\65\3\2\2\2\65\66\7")
        buf.write("\6\2\2\66\17\3\2\2\2\678\5\22\n\289\5\n\6\29@\3\2\2\2")
        buf.write(":;\7\t\2\2;<\5\22\n\2<=\5\n\6\2=?\3\2\2\2>:\3\2\2\2?B")
        buf.write("\3\2\2\2@>\3\2\2\2@A\3\2\2\2A\21\3\2\2\2B@\3\2\2\2CD\t")
        buf.write("\2\2\2D\23\3\2\2\2\7\32\36)\63@")
        return buf.getvalue()


class BKOOL2Parser ( Parser ):

    grammarFileName = "BKOOL2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'body'", "'('", "')'", "'int'", 
                     "'float'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INT", "FLOAT", "SEMI", "ID", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_idlist = 4
    RULE_funcdecl = 5
    RULE_para_decl = 6
    RULE_parameters = 7
    RULE_typ = 8

    ruleNames =  [ "program", "decls", "decl", "vardecl", "idlist", "funcdecl", 
                   "para_decl", "parameters", "typ" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    INT=5
    FLOAT=6
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
            return self.getTypedRuleContext(BKOOL2Parser.DeclsContext,0)


        def getRuleIndex(self):
            return BKOOL2Parser.RULE_program




    def program(self):

        localctx = BKOOL2Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
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

        def decl(self):
            return self.getTypedRuleContext(BKOOL2Parser.DeclContext,0)


        def decls(self):
            return self.getTypedRuleContext(BKOOL2Parser.DeclsContext,0)


        def getRuleIndex(self):
            return BKOOL2Parser.RULE_decls




    def decls(self):

        localctx = BKOOL2Parser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.decl()
                self.state = 21
                self.decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
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
            return self.getTypedRuleContext(BKOOL2Parser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(BKOOL2Parser.FuncdeclContext,0)


        def getRuleIndex(self):
            return BKOOL2Parser.RULE_decl




    def decl(self):

        localctx = BKOOL2Parser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
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
            return self.getTypedRuleContext(BKOOL2Parser.TypContext,0)


        def idlist(self):
            return self.getTypedRuleContext(BKOOL2Parser.IdlistContext,0)


        def SEMI(self):
            return self.getToken(BKOOL2Parser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOL2Parser.RULE_vardecl




    def vardecl(self):

        localctx = BKOOL2Parser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.typ()
            self.state = 31
            self.idlist()
            self.state = 32
            self.match(BKOOL2Parser.SEMI)
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOL2Parser.ID)
            else:
                return self.getToken(BKOOL2Parser.ID, i)

        def getRuleIndex(self):
            return BKOOL2Parser.RULE_idlist




    def idlist(self):

        localctx = BKOOL2Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(BKOOL2Parser.ID)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOL2Parser.T__0:
                self.state = 35
                self.match(BKOOL2Parser.T__0)
                self.state = 36
                self.match(BKOOL2Parser.ID)
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            return self.getTypedRuleContext(BKOOL2Parser.TypContext,0)


        def ID(self):
            return self.getToken(BKOOL2Parser.ID, 0)

        def para_decl(self):
            return self.getTypedRuleContext(BKOOL2Parser.Para_declContext,0)


        def getRuleIndex(self):
            return BKOOL2Parser.RULE_funcdecl




    def funcdecl(self):

        localctx = BKOOL2Parser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.typ()
            self.state = 43
            self.match(BKOOL2Parser.ID)
            self.state = 44
            self.para_decl()
            self.state = 45
            self.match(BKOOL2Parser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameters(self):
            return self.getTypedRuleContext(BKOOL2Parser.ParametersContext,0)


        def getRuleIndex(self):
            return BKOOL2Parser.RULE_para_decl




    def para_decl(self):

        localctx = BKOOL2Parser.Para_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_para_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(BKOOL2Parser.T__2)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOL2Parser.INT or _la==BKOOL2Parser.FLOAT:
                self.state = 48
                self.parameters()


            self.state = 51
            self.match(BKOOL2Parser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOL2Parser.TypContext)
            else:
                return self.getTypedRuleContext(BKOOL2Parser.TypContext,i)


        def idlist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOL2Parser.IdlistContext)
            else:
                return self.getTypedRuleContext(BKOOL2Parser.IdlistContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOL2Parser.SEMI)
            else:
                return self.getToken(BKOOL2Parser.SEMI, i)

        def getRuleIndex(self):
            return BKOOL2Parser.RULE_parameters




    def parameters(self):

        localctx = BKOOL2Parser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.typ()
            self.state = 54
            self.idlist()
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOL2Parser.SEMI:
                self.state = 56
                self.match(BKOOL2Parser.SEMI)
                self.state = 57
                self.typ()
                self.state = 58
                self.idlist()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            return self.getToken(BKOOL2Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOL2Parser.FLOAT, 0)

        def getRuleIndex(self):
            return BKOOL2Parser.RULE_typ




    def typ(self):

        localctx = BKOOL2Parser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            _la = self._input.LA(1)
            if not(_la==BKOOL2Parser.INT or _la==BKOOL2Parser.FLOAT):
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





