# Generated from c:\Users\84865\Documents\BK-CSE20\CSE-PPL\practice\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("\u00a3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\6\2(\n\2\r\2\16\2)\3\2\3\2\3\3\3\3\3\3\3\3\5\3\62")
        buf.write("\n\3\3\4\3\4\5\4\66\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\7\6E\n\6\f\6\16\6H\13\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\7\bU\n\b\f\b\16\b")
        buf.write("X\13\b\3\t\3\t\3\t\3\t\3\t\3\t\7\t`\n\t\f\t\16\tc\13\t")
        buf.write("\3\n\3\n\3\n\3\n\5\ni\n\n\3\n\3\n\3\n\3\n\5\no\n\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\5")
        buf.write("\r~\n\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\5\16\u0087\n")
        buf.write("\16\3\17\3\17\3\17\3\17\3\20\3\20\5\20\u008f\n\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u0099\n\21\3")
        buf.write("\22\3\22\3\22\3\22\5\22\u009f\n\22\3\23\3\23\3\23\2\4")
        buf.write("\16\20\24\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$\2")
        buf.write("\6\3\2\21\23\3\2\3\4\3\2\5\6\3\2\t\n\2\u00a1\2\'\3\2\2")
        buf.write("\2\4\61\3\2\2\2\6\65\3\2\2\2\b\67\3\2\2\2\n;\3\2\2\2\f")
        buf.write("L\3\2\2\2\16N\3\2\2\2\20Y\3\2\2\2\22n\3\2\2\2\24p\3\2")
        buf.write("\2\2\26u\3\2\2\2\30y\3\2\2\2\32\u0086\3\2\2\2\34\u0088")
        buf.write("\3\2\2\2\36\u008e\3\2\2\2 \u0098\3\2\2\2\"\u009e\3\2\2")
        buf.write("\2$\u00a0\3\2\2\2&(\5\4\3\2\'&\3\2\2\2()\3\2\2\2)\'\3")
        buf.write("\2\2\2)*\3\2\2\2*+\3\2\2\2+,\7\2\2\3,\3\3\2\2\2-.\5\6")
        buf.write("\4\2./\5\6\4\2/\62\3\2\2\2\60\62\5\6\4\2\61-\3\2\2\2\61")
        buf.write("\60\3\2\2\2\62\5\3\2\2\2\63\66\5\n\6\2\64\66\5\b\5\2\65")
        buf.write("\63\3\2\2\2\65\64\3\2\2\2\66\7\3\2\2\2\678\5$\23\289\5")
        buf.write("\"\22\29:\7\f\2\2:\t\3\2\2\2;<\5$\23\2<=\7\23\2\2=>\5")
        buf.write("\34\17\2>F\7\17\2\2?E\5\b\5\2@E\5\24\13\2AB\5\30\r\2B")
        buf.write("C\7\f\2\2CE\3\2\2\2D?\3\2\2\2D@\3\2\2\2DA\3\2\2\2EH\3")
        buf.write("\2\2\2FD\3\2\2\2FG\3\2\2\2GI\3\2\2\2HF\3\2\2\2IJ\5\26")
        buf.write("\f\2JK\7\20\2\2K\13\3\2\2\2LM\t\2\2\2M\r\3\2\2\2NO\b\b")
        buf.write("\1\2OP\5\20\t\2PV\3\2\2\2QR\f\4\2\2RS\t\3\2\2SU\5\20\t")
        buf.write("\2TQ\3\2\2\2UX\3\2\2\2VT\3\2\2\2VW\3\2\2\2W\17\3\2\2\2")
        buf.write("XV\3\2\2\2YZ\b\t\1\2Z[\5\22\n\2[a\3\2\2\2\\]\f\4\2\2]")
        buf.write("^\t\4\2\2^`\5\22\n\2_\\\3\2\2\2`c\3\2\2\2a_\3\2\2\2ab")
        buf.write("\3\2\2\2b\21\3\2\2\2ca\3\2\2\2di\7\21\2\2ei\7\22\2\2f")
        buf.write("i\7\23\2\2gi\5\30\r\2hd\3\2\2\2he\3\2\2\2hf\3\2\2\2hg")
        buf.write("\3\2\2\2io\3\2\2\2jk\7\r\2\2kl\5\16\b\2lm\7\16\2\2mo\3")
        buf.write("\2\2\2nh\3\2\2\2nj\3\2\2\2o\23\3\2\2\2pq\7\23\2\2qr\7")
        buf.write("\7\2\2rs\5\16\b\2st\7\f\2\2t\25\3\2\2\2uv\7\b\2\2vw\5")
        buf.write("\16\b\2wx\7\f\2\2x\27\3\2\2\2yz\7\23\2\2z}\7\r\2\2{~\5")
        buf.write("\32\16\2|~\3\2\2\2}{\3\2\2\2}|\3\2\2\2~\177\3\2\2\2\177")
        buf.write("\u0080\7\16\2\2\u0080\31\3\2\2\2\u0081\u0082\5\f\7\2\u0082")
        buf.write("\u0083\7\13\2\2\u0083\u0084\5\32\16\2\u0084\u0087\3\2")
        buf.write("\2\2\u0085\u0087\5\f\7\2\u0086\u0081\3\2\2\2\u0086\u0085")
        buf.write("\3\2\2\2\u0087\33\3\2\2\2\u0088\u0089\7\r\2\2\u0089\u008a")
        buf.write("\5\36\20\2\u008a\u008b\7\16\2\2\u008b\35\3\2\2\2\u008c")
        buf.write("\u008f\5 \21\2\u008d\u008f\3\2\2\2\u008e\u008c\3\2\2\2")
        buf.write("\u008e\u008d\3\2\2\2\u008f\37\3\2\2\2\u0090\u0091\5$\23")
        buf.write("\2\u0091\u0092\5\"\22\2\u0092\u0093\7\f\2\2\u0093\u0094")
        buf.write("\5 \21\2\u0094\u0099\3\2\2\2\u0095\u0096\5$\23\2\u0096")
        buf.write("\u0097\5\"\22\2\u0097\u0099\3\2\2\2\u0098\u0090\3\2\2")
        buf.write("\2\u0098\u0095\3\2\2\2\u0099!\3\2\2\2\u009a\u009b\7\23")
        buf.write("\2\2\u009b\u009c\7\13\2\2\u009c\u009f\5\"\22\2\u009d\u009f")
        buf.write("\7\23\2\2\u009e\u009a\3\2\2\2\u009e\u009d\3\2\2\2\u009f")
        buf.write("#\3\2\2\2\u00a0\u00a1\t\5\2\2\u00a1%\3\2\2\2\20)\61\65")
        buf.write("DFVahn}\u0086\u008e\u0098\u009e")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'='", "'return'", 
                     "'int'", "'float'", "','", "';'", "'('", "')'", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INT", "FLOAT", 
                      "COMMA", "SEMI", "LB", "RB", "LCB", "RCB", "INTEGER", 
                      "REAL", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_funcdecl = 4
    RULE_expr = 5
    RULE_exp = 6
    RULE_term = 7
    RULE_factor = 8
    RULE_assign_stmt = 9
    RULE_return_stmt = 10
    RULE_call_stmt = 11
    RULE_param_call_stmt = 12
    RULE_paramdecl = 13
    RULE_paramterm = 14
    RULE_param = 15
    RULE_idlist = 16
    RULE_typ = 17

    ruleNames =  [ "program", "decls", "decl", "vardecl", "funcdecl", "expr", 
                   "exp", "term", "factor", "assign_stmt", "return_stmt", 
                   "call_stmt", "param_call_stmt", "paramdecl", "paramterm", 
                   "param", "idlist", "typ" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    INT=7
    FLOAT=8
    COMMA=9
    SEMI=10
    LB=11
    RB=12
    LCB=13
    RCB=14
    INTEGER=15
    REAL=16
    ID=17
    WS=18
    ERROR_CHAR=19
    UNCLOSE_STRING=20
    ILLEGAL_ESCAPE=21

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
            return self.getToken(BKOOLParser.EOF, 0)

        def decls(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.DeclsContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.DeclsContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.decls()
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.INT or _la==BKOOLParser.FLOAT):
                    break

            self.state = 41
            self.match(BKOOLParser.EOF)
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
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.decl()
                self.state = 44
                self.decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
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

        def funcdecl(self):
            return self.getTypedRuleContext(BKOOLParser.FuncdeclContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_decl




    def decl(self):

        localctx = BKOOLParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.funcdecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.vardecl()
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
            self.state = 53
            self.typ()
            self.state = 54
            self.idlist()
            self.state = 55
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

        def paramdecl(self):
            return self.getTypedRuleContext(BKOOLParser.ParamdeclContext,0)


        def LCB(self):
            return self.getToken(BKOOLParser.LCB, 0)

        def return_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Return_stmtContext,0)


        def RCB(self):
            return self.getToken(BKOOLParser.RCB, 0)

        def vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.VardeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.VardeclContext,i)


        def assign_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Assign_stmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Assign_stmtContext,i)


        def call_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Call_stmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Call_stmtContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.SEMI)
            else:
                return self.getToken(BKOOLParser.SEMI, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_funcdecl




    def funcdecl(self):

        localctx = BKOOLParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.typ()
            self.state = 58
            self.match(BKOOLParser.ID)
            self.state = 59
            self.paramdecl()
            self.state = 60
            self.match(BKOOLParser.LCB)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 66
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 61
                    self.vardecl()
                    pass

                elif la_ == 2:
                    self.state = 62
                    self.assign_stmt()
                    pass

                elif la_ == 3:
                    self.state = 63
                    self.call_stmt()
                    self.state = 64
                    self.match(BKOOLParser.SEMI)
                    pass


                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
            self.return_stmt()
            self.state = 72
            self.match(BKOOLParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def INTEGER(self):
            return self.getToken(BKOOLParser.INTEGER, 0)

        def REAL(self):
            return self.getToken(BKOOLParser.REAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INTEGER) | (1 << BKOOLParser.REAL) | (1 << BKOOLParser.ID))) != 0)):
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


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(BKOOLParser.TermContext,0)


        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 84
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.ExpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                    self.state = 79
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 80
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.T__0 or _la==BKOOLParser.T__1):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 81
                    self.term(0) 
                self.state = 86
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(BKOOLParser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(BKOOLParser.TermContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_term



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_term, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 95
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.TermContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 90
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 91
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.T__2 or _la==BKOOLParser.T__3):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 92
                    self.factor() 
                self.state = 97
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(BKOOLParser.INTEGER, 0)

        def REAL(self):
            return self.getToken(BKOOLParser.REAL, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def call_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Call_stmtContext,0)


        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_factor




    def factor(self):

        localctx = BKOOLParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_factor)
        try:
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTEGER, BKOOLParser.REAL, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 98
                    self.match(BKOOLParser.INTEGER)
                    pass

                elif la_ == 2:
                    self.state = 99
                    self.match(BKOOLParser.REAL)
                    pass

                elif la_ == 3:
                    self.state = 100
                    self.match(BKOOLParser.ID)
                    pass

                elif la_ == 4:
                    self.state = 101
                    self.call_stmt()
                    pass


                pass
            elif token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.match(BKOOLParser.LB)
                self.state = 105
                self.exp(0)
                self.state = 106
                self.match(BKOOLParser.RB)
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


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = BKOOLParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(BKOOLParser.ID)
            self.state = 111
            self.match(BKOOLParser.T__4)
            self.state = 112
            self.exp(0)
            self.state = 113
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_return_stmt




    def return_stmt(self):

        localctx = BKOOLParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(BKOOLParser.T__5)

            self.state = 116
            self.exp(0)
            self.state = 117
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def param_call_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Param_call_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_call_stmt




    def call_stmt(self):

        localctx = BKOOLParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(BKOOLParser.ID)
            self.state = 120
            self.match(BKOOLParser.LB)
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTEGER, BKOOLParser.REAL, BKOOLParser.ID]:
                self.state = 121
                self.param_call_stmt()
                pass
            elif token in [BKOOLParser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 125
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def param_call_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Param_call_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param_call_stmt




    def param_call_stmt(self):

        localctx = BKOOLParser.Param_call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param_call_stmt)
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.expr()
                self.state = 128
                self.match(BKOOLParser.COMMA)
                self.state = 129
                self.param_call_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def paramterm(self):
            return self.getTypedRuleContext(BKOOLParser.ParamtermContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_paramdecl




    def paramdecl(self):

        localctx = BKOOLParser.ParamdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_paramdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(BKOOLParser.LB)
            self.state = 135
            self.paramterm()
            self.state = 136
            self.match(BKOOLParser.RB)
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

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramterm




    def paramterm(self):

        localctx = BKOOLParser.ParamtermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_paramterm)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT, BKOOLParser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.param()
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


    class ParamContext(ParserRuleContext):
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

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_param)
        try:
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.typ()
                self.state = 143
                self.idlist()
                self.state = 144
                self.match(BKOOLParser.SEMI)
                self.state = 145
                self.param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.typ()
                self.state = 148
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
        self.enterRule(localctx, 32, self.RULE_idlist)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.match(BKOOLParser.ID)
                self.state = 153
                self.match(BKOOLParser.COMMA)
                self.state = 154
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.match(BKOOLParser.ID)
                pass


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
        self.enterRule(localctx, 34, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.exp_sempred
        self._predicates[7] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




