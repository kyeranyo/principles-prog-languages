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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26")
        buf.write("\u010f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\13\3\13\5\13p\n")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\7\fx\n\f\f\f\16\f{\13\f")
        buf.write("\3\r\3\r\3\r\3\r\7\r\u0081\n\r\f\r\16\r\u0084\13\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\5\16\u008b\n\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\7\21")
        buf.write("\u009b\n\21\f\21\16\21\u009e\13\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\7\22\u00a7\n\22\f\22\16\22\u00aa\13\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\5\23\u00b1\n\23\3\23\3\23\3")
        buf.write("\24\3\24\5\24\u00b7\n\24\3\25\3\25\3\25\3\25\3\25\5\25")
        buf.write("\u00be\n\25\3\26\3\26\3\26\3\26\3\26\5\26\u00c5\n\26\3")
        buf.write("\27\3\27\5\27\u00c9\n\27\3\30\3\30\3\30\7\30\u00ce\n\30")
        buf.write("\f\30\16\30\u00d1\13\30\3\30\3\30\6\30\u00d5\n\30\r\30")
        buf.write("\16\30\u00d6\7\30\u00d9\n\30\f\30\16\30\u00dc\13\30\3")
        buf.write("\30\5\30\u00df\n\30\3\31\3\31\3\32\3\32\3\32\3\32\5\32")
        buf.write("\u00e7\n\32\3\33\3\33\3\33\6\33\u00ec\n\33\r\33\16\33")
        buf.write("\u00ed\3\33\3\33\7\33\u00f2\n\33\f\33\16\33\u00f5\13\33")
        buf.write("\5\33\u00f7\n\33\3\34\6\34\u00fa\n\34\r\34\16\34\u00fb")
        buf.write("\3\34\3\34\3\34\6\34\u0101\n\34\r\34\16\34\u0102\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \5\u0082")
        buf.write("\u009c\u00a8\2!\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\2\31\2\33\r\35\2\37\2!\16#\2%\17\'\2)\2+\2")
        buf.write("-\20/\21\61\2\63\22\65\2\67\29\23;\24=\25?\26\3\2\b\4")
        buf.write("\2\f\f\17\17\4\2$$^^\3\2\63;\3\2\62;\4\2GGgg\5\2\13\f")
        buf.write("\17\17\"\"\2\u0119\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\33\3\2\2\2\2!\3\2")
        buf.write("\2\2\2%\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\63\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\3A\3\2\2\2\5")
        buf.write("G\3\2\2\2\7I\3\2\2\2\tK\3\2\2\2\13N\3\2\2\2\rV\3\2\2\2")
        buf.write("\17\\\3\2\2\2\21d\3\2\2\2\23k\3\2\2\2\25o\3\2\2\2\27s")
        buf.write("\3\2\2\2\31|\3\2\2\2\33\u008a\3\2\2\2\35\u008c\3\2\2\2")
        buf.write("\37\u0092\3\2\2\2!\u0097\3\2\2\2#\u00a2\3\2\2\2%\u00ae")
        buf.write("\3\2\2\2\'\u00b6\3\2\2\2)\u00bd\3\2\2\2+\u00c4\3\2\2\2")
        buf.write("-\u00c8\3\2\2\2/\u00de\3\2\2\2\61\u00e0\3\2\2\2\63\u00e6")
        buf.write("\3\2\2\2\65\u00e8\3\2\2\2\67\u00f9\3\2\2\29\u0104\3\2")
        buf.write("\2\2;\u0108\3\2\2\2=\u010b\3\2\2\2?\u010d\3\2\2\2AB\7")
        buf.write("c\2\2BC\7t\2\2CD\7t\2\2DE\7c\2\2EF\7{\2\2F\4\3\2\2\2G")
        buf.write("H\7]\2\2H\6\3\2\2\2IJ\7_\2\2J\b\3\2\2\2KL\7q\2\2LM\7h")
        buf.write("\2\2M\n\3\2\2\2NO\7k\2\2OP\7p\2\2PQ\7v\2\2QR\7g\2\2RS")
        buf.write("\7i\2\2ST\7g\2\2TU\7t\2\2U\f\3\2\2\2VW\7h\2\2WX\7n\2\2")
        buf.write("XY\7q\2\2YZ\7c\2\2Z[\7v\2\2[\16\3\2\2\2\\]\7d\2\2]^\7")
        buf.write("q\2\2^_\7q\2\2_`\7n\2\2`a\7g\2\2ab\7c\2\2bc\7p\2\2c\20")
        buf.write("\3\2\2\2de\7u\2\2ef\7v\2\2fg\7t\2\2gh\7k\2\2hi\7p\2\2")
        buf.write("ij\7i\2\2j\22\3\2\2\2kl\7.\2\2l\24\3\2\2\2mp\5\27\f\2")
        buf.write("np\5\31\r\2om\3\2\2\2on\3\2\2\2pq\3\2\2\2qr\b\13\2\2r")
        buf.write("\26\3\2\2\2st\7\61\2\2tu\7\61\2\2uy\3\2\2\2vx\n\2\2\2")
        buf.write("wv\3\2\2\2x{\3\2\2\2yw\3\2\2\2yz\3\2\2\2z\30\3\2\2\2{")
        buf.write("y\3\2\2\2|}\7\61\2\2}~\7,\2\2~\u0082\3\2\2\2\177\u0081")
        buf.write("\13\2\2\2\u0080\177\3\2\2\2\u0081\u0084\3\2\2\2\u0082")
        buf.write("\u0083\3\2\2\2\u0082\u0080\3\2\2\2\u0083\u0085\3\2\2\2")
        buf.write("\u0084\u0082\3\2\2\2\u0085\u0086\7,\2\2\u0086\u0087\7")
        buf.write("\61\2\2\u0087\32\3\2\2\2\u0088\u008b\5\35\17\2\u0089\u008b")
        buf.write("\5\37\20\2\u008a\u0088\3\2\2\2\u008a\u0089\3\2\2\2\u008b")
        buf.write("\34\3\2\2\2\u008c\u008d\7h\2\2\u008d\u008e\7c\2\2\u008e")
        buf.write("\u008f\7n\2\2\u008f\u0090\7u\2\2\u0090\u0091\7g\2\2\u0091")
        buf.write("\36\3\2\2\2\u0092\u0093\7v\2\2\u0093\u0094\7t\2\2\u0094")
        buf.write("\u0095\7w\2\2\u0095\u0096\7g\2\2\u0096 \3\2\2\2\u0097")
        buf.write("\u009c\7$\2\2\u0098\u009b\n\3\2\2\u0099\u009b\5#\22\2")
        buf.write("\u009a\u0098\3\2\2\2\u009a\u0099\3\2\2\2\u009b\u009e\3")
        buf.write("\2\2\2\u009c\u009d\3\2\2\2\u009c\u009a\3\2\2\2\u009d\u009f")
        buf.write("\3\2\2\2\u009e\u009c\3\2\2\2\u009f\u00a0\7$\2\2\u00a0")
        buf.write("\u00a1\b\21\3\2\u00a1\"\3\2\2\2\u00a2\u00a3\7^\2\2\u00a3")
        buf.write("\u00a4\7$\2\2\u00a4\u00a8\3\2\2\2\u00a5\u00a7\13\2\2\2")
        buf.write("\u00a6\u00a5\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8\u00a9\3")
        buf.write("\2\2\2\u00a8\u00a6\3\2\2\2\u00a9\u00ab\3\2\2\2\u00aa\u00a8")
        buf.write("\3\2\2\2\u00ab\u00ac\7^\2\2\u00ac\u00ad\7$\2\2\u00ad$")
        buf.write("\3\2\2\2\u00ae\u00b0\7}\2\2\u00af\u00b1\5\'\24\2\u00b0")
        buf.write("\u00af\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\3\2\2\2")
        buf.write("\u00b2\u00b3\7\177\2\2\u00b3&\3\2\2\2\u00b4\u00b7\5)\25")
        buf.write("\2\u00b5\u00b7\5+\26\2\u00b6\u00b4\3\2\2\2\u00b6\u00b5")
        buf.write("\3\2\2\2\u00b7(\3\2\2\2\u00b8\u00b9\5-\27\2\u00b9\u00ba")
        buf.write("\7.\2\2\u00ba\u00bb\5)\25\2\u00bb\u00be\3\2\2\2\u00bc")
        buf.write("\u00be\5-\27\2\u00bd\u00b8\3\2\2\2\u00bd\u00bc\3\2\2\2")
        buf.write("\u00be*\3\2\2\2\u00bf\u00c0\5!\21\2\u00c0\u00c1\7.\2\2")
        buf.write("\u00c1\u00c2\5+\26\2\u00c2\u00c5\3\2\2\2\u00c3\u00c5\5")
        buf.write("!\21\2\u00c4\u00bf\3\2\2\2\u00c4\u00c3\3\2\2\2\u00c5,")
        buf.write("\3\2\2\2\u00c6\u00c9\5/\30\2\u00c7\u00c9\5\63\32\2\u00c8")
        buf.write("\u00c6\3\2\2\2\u00c8\u00c7\3\2\2\2\u00c9.\3\2\2\2\u00ca")
        buf.write("\u00df\7\62\2\2\u00cb\u00cf\t\4\2\2\u00cc\u00ce\t\5\2")
        buf.write("\2\u00cd\u00cc\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf\u00cd")
        buf.write("\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00da\3\2\2\2\u00d1")
        buf.write("\u00cf\3\2\2\2\u00d2\u00d4\5\61\31\2\u00d3\u00d5\t\5\2")
        buf.write("\2\u00d4\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d4")
        buf.write("\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00d9\3\2\2\2\u00d8")
        buf.write("\u00d2\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da\u00d8\3\2\2\2")
        buf.write("\u00da\u00db\3\2\2\2\u00db\u00dd\3\2\2\2\u00dc\u00da\3")
        buf.write("\2\2\2\u00dd\u00df\b\30\4\2\u00de\u00ca\3\2\2\2\u00de")
        buf.write("\u00cb\3\2\2\2\u00df\60\3\2\2\2\u00e0\u00e1\7a\2\2\u00e1")
        buf.write("\62\3\2\2\2\u00e2\u00e7\5\67\34\2\u00e3\u00e4\5\65\33")
        buf.write("\2\u00e4\u00e5\b\32\5\2\u00e5\u00e7\3\2\2\2\u00e6\u00e2")
        buf.write("\3\2\2\2\u00e6\u00e3\3\2\2\2\u00e7\64\3\2\2\2\u00e8\u00e9")
        buf.write("\5/\30\2\u00e9\u00eb\7\60\2\2\u00ea\u00ec\t\5\2\2\u00eb")
        buf.write("\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00eb\3\2\2\2")
        buf.write("\u00ed\u00ee\3\2\2\2\u00ee\u00f6\3\2\2\2\u00ef\u00f3\t")
        buf.write("\6\2\2\u00f0\u00f2\t\5\2\2\u00f1\u00f0\3\2\2\2\u00f2\u00f5")
        buf.write("\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4")
        buf.write("\u00f7\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f6\u00ef\3\2\2\2")
        buf.write("\u00f6\u00f7\3\2\2\2\u00f7\66\3\2\2\2\u00f8\u00fa\t\5")
        buf.write("\2\2\u00f9\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00f9")
        buf.write("\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd")
        buf.write("\u00fe\t\6\2\2\u00fe\u0100\7/\2\2\u00ff\u0101\t\5\2\2")
        buf.write("\u0100\u00ff\3\2\2\2\u0101\u0102\3\2\2\2\u0102\u0100\3")
        buf.write("\2\2\2\u0102\u0103\3\2\2\2\u01038\3\2\2\2\u0104\u0105")
        buf.write("\t\7\2\2\u0105\u0106\3\2\2\2\u0106\u0107\b\35\2\2\u0107")
        buf.write(":\3\2\2\2\u0108\u0109\13\2\2\2\u0109\u010a\b\36\6\2\u010a")
        buf.write("<\3\2\2\2\u010b\u010c\13\2\2\2\u010c>\3\2\2\2\u010d\u010e")
        buf.write("\13\2\2\2\u010e@\3\2\2\2\31\2oy\u0082\u008a\u009a\u009c")
        buf.write("\u00a8\u00b0\u00b6\u00bd\u00c4\u00c8\u00cf\u00d6\u00da")
        buf.write("\u00de\u00e6\u00ed\u00f3\u00f6\u00fb\u0102\7\b\2\2\3\21")
        buf.write("\2\3\30\3\3\32\4\3\36\5")
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
    T__6 = 7
    T__7 = 8
    T__8 = 9
    COMMENT = 10
    BOOLEAN_LIT = 11
    STRING_LIT = 12
    ARRAY_LIT = 13
    NUMBER = 14
    INTEGER_LIT = 15
    FLOAT_LIT = 16
    WS = 17
    ERROR_CHAR = 18
    UNCLOSE_STRING = 19
    ILLEGAL_ESCAPE = 20

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'array'", "'['", "']'", "'of'", "'integer'", "'float'", "'boolean'", 
            "'string'", "','" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "BOOLEAN_LIT", "STRING_LIT", "ARRAY_LIT", "NUMBER", 
            "INTEGER_LIT", "FLOAT_LIT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "COMMENT", "SingleLineComment", "MultiLineComment", 
                  "BOOLEAN_LIT", "FALSE", "TRUE", "STRING_LIT", "SUBSTRING", 
                  "ARRAY_LIT", "EXPS", "NUMLIST", "STRINGLIST", "NUMBER", 
                  "INTEGER_LIT", "UNDERSCORE", "FLOAT_LIT", "DECPART", "EXPPART", 
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
            actions[15] = self.STRING_LIT_action 
            actions[22] = self.INTEGER_LIT_action 
            actions[24] = self.FLOAT_LIT_action 
            actions[28] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text=self.text[1:-1]
     

    def INTEGER_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_","")
     

    def FLOAT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text.replace("_","")
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


