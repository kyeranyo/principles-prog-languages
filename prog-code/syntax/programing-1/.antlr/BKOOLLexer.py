# Generated from c:\Users\84865\Documents\BK-CSE20\CSE-PPL\programing-code\syntax\programing-1\BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("E\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\6\t\64\n\t\r\t")
        buf.write("\16\t\65\3\n\6\n9\n\n\r\n\16\n:\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\3\2\4\4\2C\\c|\5\2\13\f\17")
        buf.write("\17\"\"\2F\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\3\33\3\2\2\2\5 \3\2\2\2\7$\3\2\2\2\t*\3\2\2\2\13,\3\2")
        buf.write("\2\2\r.\3\2\2\2\17\60\3\2\2\2\21\63\3\2\2\2\238\3\2\2")
        buf.write("\2\25>\3\2\2\2\27A\3\2\2\2\31C\3\2\2\2\33\34\7d\2\2\34")
        buf.write("\35\7q\2\2\35\36\7f\2\2\36\37\7{\2\2\37\4\3\2\2\2 !\7")
        buf.write("k\2\2!\"\7p\2\2\"#\7v\2\2#\6\3\2\2\2$%\7h\2\2%&\7n\2\2")
        buf.write("&\'\7q\2\2\'(\7c\2\2()\7v\2\2)\b\3\2\2\2*+\7*\2\2+\n\3")
        buf.write("\2\2\2,-\7+\2\2-\f\3\2\2\2./\7.\2\2/\16\3\2\2\2\60\61")
        buf.write("\7=\2\2\61\20\3\2\2\2\62\64\t\2\2\2\63\62\3\2\2\2\64\65")
        buf.write("\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\66\22\3\2\2\2\67")
        buf.write("9\t\3\2\28\67\3\2\2\29:\3\2\2\2:8\3\2\2\2:;\3\2\2\2;<")
        buf.write("\3\2\2\2<=\b\n\2\2=\24\3\2\2\2>?\13\2\2\2?@\b\13\3\2@")
        buf.write("\26\3\2\2\2AB\13\2\2\2B\30\3\2\2\2CD\13\2\2\2D\32\3\2")
        buf.write("\2\2\5\2\65:\4\b\2\2\3\13\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INT = 2
    FLOAT = 3
    LB = 4
    RB = 5
    COMMA = 6
    SEMI = 7
    ID = 8
    WS = 9
    ERROR_CHAR = 10
    UNCLOSE_STRING = 11
    ILLEGAL_ESCAPE = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'body'", "'int'", "'float'", "'('", "')'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "LB", "RB", "COMMA", "SEMI", "ID", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INT", "FLOAT", "LB", "RB", "COMMA", "SEMI", "ID", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[9] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


