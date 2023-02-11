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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\27")
        buf.write("t\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3")
        buf.write("\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\6\20V\n\20\r\20\16")
        buf.write("\20W\3\21\6\21[\n\21\r\21\16\21\\\3\21\3\21\6\21a\n\21")
        buf.write("\r\21\16\21b\3\22\6\22f\n\22\r\22\16\22g\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\25\3\25\3\26\3\26\2\2\27\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22#\23%\24\'\25)\26+\27\3\2\5\3\2\62")
        buf.write(";\4\2C\\c|\5\2\13\f\17\17\"\"\2w\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\3-\3\2\2\2\5/\3\2\2\2\7\61\3\2\2")
        buf.write("\2\t\63\3\2\2\2\13\65\3\2\2\2\r\67\3\2\2\2\17>\3\2\2\2")
        buf.write("\21B\3\2\2\2\23H\3\2\2\2\25J\3\2\2\2\27L\3\2\2\2\31N\3")
        buf.write("\2\2\2\33P\3\2\2\2\35R\3\2\2\2\37U\3\2\2\2!Z\3\2\2\2#")
        buf.write("e\3\2\2\2%i\3\2\2\2\'m\3\2\2\2)p\3\2\2\2+r\3\2\2\2-.\7")
        buf.write("-\2\2.\4\3\2\2\2/\60\7/\2\2\60\6\3\2\2\2\61\62\7,\2\2")
        buf.write("\62\b\3\2\2\2\63\64\7\61\2\2\64\n\3\2\2\2\65\66\7?\2\2")
        buf.write("\66\f\3\2\2\2\678\7t\2\289\7g\2\29:\7v\2\2:;\7w\2\2;<")
        buf.write("\7t\2\2<=\7p\2\2=\16\3\2\2\2>?\7k\2\2?@\7p\2\2@A\7v\2")
        buf.write("\2A\20\3\2\2\2BC\7h\2\2CD\7n\2\2DE\7q\2\2EF\7c\2\2FG\7")
        buf.write("v\2\2G\22\3\2\2\2HI\7.\2\2I\24\3\2\2\2JK\7=\2\2K\26\3")
        buf.write("\2\2\2LM\7*\2\2M\30\3\2\2\2NO\7+\2\2O\32\3\2\2\2PQ\7}")
        buf.write("\2\2Q\34\3\2\2\2RS\7\177\2\2S\36\3\2\2\2TV\t\2\2\2UT\3")
        buf.write("\2\2\2VW\3\2\2\2WU\3\2\2\2WX\3\2\2\2X \3\2\2\2Y[\t\2\2")
        buf.write("\2ZY\3\2\2\2[\\\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]^\3\2\2")
        buf.write("\2^`\7\60\2\2_a\t\2\2\2`_\3\2\2\2ab\3\2\2\2b`\3\2\2\2")
        buf.write("bc\3\2\2\2c\"\3\2\2\2df\t\3\2\2ed\3\2\2\2fg\3\2\2\2ge")
        buf.write("\3\2\2\2gh\3\2\2\2h$\3\2\2\2ij\t\4\2\2jk\3\2\2\2kl\b\23")
        buf.write("\2\2l&\3\2\2\2mn\13\2\2\2no\b\24\3\2o(\3\2\2\2pq\13\2")
        buf.write("\2\2q*\3\2\2\2rs\13\2\2\2s,\3\2\2\2\7\2W\\bg\4\b\2\2\3")
        buf.write("\24\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    INT = 7
    FLOAT = 8
    COMMA = 9
    SEMI = 10
    LB = 11
    RB = 12
    LCB = 13
    RCB = 14
    INTEGER = 15
    REAL = 16
    ID = 17
    WS = 18
    ERROR_CHAR = 19
    UNCLOSE_STRING = 20
    ILLEGAL_ESCAPE = 21

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'='", "'return'", "'int'", "'float'", 
            "','", "';'", "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "COMMA", "SEMI", "LB", "RB", "LCB", "RCB", "INTEGER", 
            "REAL", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "INT", 
                  "FLOAT", "COMMA", "SEMI", "LB", "RB", "LCB", "RCB", "INTEGER", 
                  "REAL", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[18] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


