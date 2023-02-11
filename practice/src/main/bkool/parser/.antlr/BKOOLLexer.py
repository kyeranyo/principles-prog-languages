# Generated from c:\Users\84865\Documents\BK-CSE20\CSE-PPL\practice\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("W\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3")
        buf.write("\n\3\13\3\13\3\f\3\f\3\r\6\rI\n\r\r\r\16\rJ\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\21\3\21\2\2\22\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22\3\2\4\4\2C\\c|\5\2\13\f\17\17\"")
        buf.write("\"\2W\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\3#\3\2\2")
        buf.write("\2\5%\3\2\2\2\7,\3\2\2\2\t\61\3\2\2\2\13\65\3\2\2\2\r")
        buf.write(";\3\2\2\2\17=\3\2\2\2\21?\3\2\2\2\23A\3\2\2\2\25C\3\2")
        buf.write("\2\2\27E\3\2\2\2\31H\3\2\2\2\33L\3\2\2\2\35P\3\2\2\2\37")
        buf.write("S\3\2\2\2!U\3\2\2\2#$\7?\2\2$\4\3\2\2\2%&\7t\2\2&\'\7")
        buf.write("g\2\2\'(\7v\2\2()\7w\2\2)*\7t\2\2*+\7p\2\2+\6\3\2\2\2")
        buf.write(",-\7g\2\2-.\7z\2\2./\7r\2\2/\60\7t\2\2\60\b\3\2\2\2\61")
        buf.write("\62\7k\2\2\62\63\7p\2\2\63\64\7v\2\2\64\n\3\2\2\2\65\66")
        buf.write("\7h\2\2\66\67\7n\2\2\678\7q\2\289\7c\2\29:\7v\2\2:\f\3")
        buf.write("\2\2\2;<\7.\2\2<\16\3\2\2\2=>\7=\2\2>\20\3\2\2\2?@\7*")
        buf.write("\2\2@\22\3\2\2\2AB\7+\2\2B\24\3\2\2\2CD\7}\2\2D\26\3\2")
        buf.write("\2\2EF\7\177\2\2F\30\3\2\2\2GI\t\2\2\2HG\3\2\2\2IJ\3\2")
        buf.write("\2\2JH\3\2\2\2JK\3\2\2\2K\32\3\2\2\2LM\t\3\2\2MN\3\2\2")
        buf.write("\2NO\b\16\2\2O\34\3\2\2\2PQ\13\2\2\2QR\b\17\3\2R\36\3")
        buf.write("\2\2\2ST\13\2\2\2T \3\2\2\2UV\13\2\2\2V\"\3\2\2\2\4\2")
        buf.write("J\4\b\2\2\3\17\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    INT = 4
    FLOAT = 5
    COMMA = 6
    SEMI = 7
    LB = 8
    RB = 9
    LCB = 10
    RCB = 11
    ID = 12
    WS = 13
    ERROR_CHAR = 14
    UNCLOSE_STRING = 15
    ILLEGAL_ESCAPE = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'return'", "'expr'", "'int'", "'float'", "','", "';'", 
            "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "COMMA", "SEMI", "LB", "RB", "LCB", "RCB", "ID", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "INT", "FLOAT", "COMMA", "SEMI", 
                  "LB", "RB", "LCB", "RCB", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[13] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


