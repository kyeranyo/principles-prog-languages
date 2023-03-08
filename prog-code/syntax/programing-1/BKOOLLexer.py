# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write(".\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\4\6\4\"\n\4\r\4\16\4#\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\2\2\b\3\3\5\4\7\5\t\6\13\7\r\b\3")
        buf.write("\2\3\5\2\13\f\17\17\"\"\2.\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\3\17\3\2")
        buf.write("\2\2\5\30\3\2\2\2\7!\3\2\2\2\t\'\3\2\2\2\13*\3\2\2\2\r")
        buf.write(",\3\2\2\2\17\20\7h\2\2\20\21\7w\2\2\21\22\7p\2\2\22\23")
        buf.write("\7e\2\2\23\24\7f\2\2\24\25\7g\2\2\25\26\7e\2\2\26\27\7")
        buf.write("n\2\2\27\4\3\2\2\2\30\31\7x\2\2\31\32\7c\2\2\32\33\7t")
        buf.write("\2\2\33\34\7f\2\2\34\35\7g\2\2\35\36\7e\2\2\36\37\7n\2")
        buf.write("\2\37\6\3\2\2\2 \"\t\2\2\2! \3\2\2\2\"#\3\2\2\2#!\3\2")
        buf.write("\2\2#$\3\2\2\2$%\3\2\2\2%&\b\4\2\2&\b\3\2\2\2\'(\13\2")
        buf.write("\2\2()\b\5\3\2)\n\3\2\2\2*+\13\2\2\2+\f\3\2\2\2,-\13\2")
        buf.write("\2\2-\16\3\2\2\2\4\2#\4\b\2\2\3\5\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    WS = 3
    ERROR_CHAR = 4
    UNCLOSE_STRING = 5
    ILLEGAL_ESCAPE = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'funcdecl'", "'vardecl'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
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
            actions[3] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


