# Generated from c:\Users\84865\Documents\BK-CSE20\CSE-PPL\practice\src\test\gui\BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\60\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\3\2\3\2\5\2\22\n\2\3\3\3\3\7\3\26\n\3\f\3\16\3\31\13")
        buf.write("\3\3\3\3\3\3\4\6\4\36\n\4\r\4\16\4\37\3\4\7\4#\n\4\f\4")
        buf.write("\16\4&\13\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\2\2\b")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\3\2\7\3\2\63;\3\2\62;\6\2\64")
        buf.write("\64\66\6688::\4\2C\\c|\b\2CCEEGGcceegg\2\63\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\3\21\3\2\2\2\5\23\3\2\2\2\7\35\3\2\2\2\t)\3")
        buf.write("\2\2\2\13,\3\2\2\2\r.\3\2\2\2\17\22\5\5\3\2\20\22\5\7")
        buf.write("\4\2\21\17\3\2\2\2\21\20\3\2\2\2\22\4\3\2\2\2\23\27\t")
        buf.write("\2\2\2\24\26\t\3\2\2\25\24\3\2\2\2\26\31\3\2\2\2\27\25")
        buf.write("\3\2\2\2\27\30\3\2\2\2\30\32\3\2\2\2\31\27\3\2\2\2\32")
        buf.write("\33\t\4\2\2\33\6\3\2\2\2\34\36\t\2\2\2\35\34\3\2\2\2\36")
        buf.write("\37\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 $\3\2\2\2!#\t\5")
        buf.write("\2\2\"!\3\2\2\2#&\3\2\2\2$\"\3\2\2\2$%\3\2\2\2%\'\3\2")
        buf.write("\2\2&$\3\2\2\2\'(\t\6\2\2(\b\3\2\2\2)*\13\2\2\2*+\b\5")
        buf.write("\2\2+\n\3\2\2\2,-\13\2\2\2-\f\3\2\2\2./\13\2\2\2/\16\3")
        buf.write("\2\2\2\7\2\21\27\37$\3\3\5\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SHEXA = 1
    EVEN = 2
    DIGITNUM = 3
    ERROR_CHAR = 4
    UNCLOSE_STRING = 5
    ILLEGAL_ESCAPE = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "SHEXA", "EVEN", "DIGITNUM", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "SHEXA", "EVEN", "DIGITNUM", "ERROR_CHAR", "UNCLOSE_STRING", 
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
     


