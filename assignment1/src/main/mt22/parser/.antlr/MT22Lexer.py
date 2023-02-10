# Generated from c:\Users\84865\Documents\BK-CSE20\CSE-PPL\assignment1\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2,")
        buf.write("\u01a9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\3\2\3\2\3\2\7\2\u008b\n\2\f\2\16\2\u008e\13\2\3\2\3")
        buf.write("\2\6\2\u0092\n\2\r\2\16\2\u0093\7\2\u0096\n\2\f\2\16\2")
        buf.write("\u0099\13\2\3\2\5\2\u009c\n\2\3\3\3\3\3\4\3\4\3\4\3\4")
        buf.write("\5\4\u00a4\n\4\3\5\3\5\3\5\6\5\u00a9\n\5\r\5\16\5\u00aa")
        buf.write("\3\5\3\5\7\5\u00af\n\5\f\5\16\5\u00b2\13\5\5\5\u00b4\n")
        buf.write("\5\3\6\6\6\u00b7\n\6\r\6\16\6\u00b8\3\6\3\6\3\6\6\6\u00be")
        buf.write("\n\6\r\6\16\6\u00bf\3\7\3\7\5\7\u00c4\n\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\7\n\u00da\n\n\f\n\16\n\u00dd\13\n\3\n\3")
        buf.write("\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20")
        buf.write("\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3")
        buf.write("$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3")
        buf.write(")\3)\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3")
        buf.write(":\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\6@\u019d\n@\r@\16")
        buf.write("@\u019e\3@\3@\3A\3A\3A\3B\3B\3C\3C\2\2D\3\3\5\2\7\4\t")
        buf.write("\2\13\2\r\5\17\2\21\2\23\6\25\2\27\2\31\2\33\2\35\2\37")
        buf.write("\2!\2#\2%\7\'\b)\t+\n-\13/\f\61\r\63\16\65\17\67\209\21")
        buf.write(";\22=\23?\24A\25C\26E\27G\30I\31K\2M\2O\2Q\2S\2U\2W\32")
        buf.write("Y\33[\34]\35_\36a\37c e!g\"i#k$m%o&q\'s(u\2w\2y\2{\2}")
        buf.write("\2\177)\u0081*\u0083+\u0085,\3\2\r\3\2\63;\3\2\62;\4\2")
        buf.write("GGgg\3\2^^\3\2$$\3\2))\3\2\n\n\3\2\16\16\3\2\17\17\3\2")
        buf.write("\f\f\5\2\13\f\17\17\"\"\2\u01a3\2\3\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\23\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)")
        buf.write("\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2")
        buf.write("\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;")
        buf.write("\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2")
        buf.write("E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2")
        buf.write("\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2\177\3\2\2\2\2")
        buf.write("\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\3\u009b")
        buf.write("\3\2\2\2\5\u009d\3\2\2\2\7\u00a3\3\2\2\2\t\u00a5\3\2\2")
        buf.write("\2\13\u00b6\3\2\2\2\r\u00c3\3\2\2\2\17\u00c5\3\2\2\2\21")
        buf.write("\u00cb\3\2\2\2\23\u00d0\3\2\2\2\25\u00e0\3\2\2\2\27\u00e2")
        buf.write("\3\2\2\2\31\u00e4\3\2\2\2\33\u00e6\3\2\2\2\35\u00e8\3")
        buf.write("\2\2\2\37\u00ea\3\2\2\2!\u00ec\3\2\2\2#\u00ee\3\2\2\2")
        buf.write("%\u00f0\3\2\2\2\'\u00f5\3\2\2\2)\u00fb\3\2\2\2+\u0103")
        buf.write("\3\2\2\2-\u0108\3\2\2\2/\u010e\3\2\2\2\61\u0114\3\2\2")
        buf.write("\2\63\u011b\3\2\2\2\65\u011f\3\2\2\2\67\u0127\3\2\2\2")
        buf.write("9\u012b\3\2\2\2;\u0132\3\2\2\2=\u013b\3\2\2\2?\u013e\3")
        buf.write("\2\2\2A\u0147\3\2\2\2C\u014a\3\2\2\2E\u014f\3\2\2\2G\u0152")
        buf.write("\3\2\2\2I\u0158\3\2\2\2K\u0160\3\2\2\2M\u0162\3\2\2\2")
        buf.write("O\u0164\3\2\2\2Q\u0166\3\2\2\2S\u0168\3\2\2\2U\u016a\3")
        buf.write("\2\2\2W\u016c\3\2\2\2Y\u016f\3\2\2\2[\u0172\3\2\2\2]\u0175")
        buf.write("\3\2\2\2_\u0178\3\2\2\2a\u017a\3\2\2\2c\u017c\3\2\2\2")
        buf.write("e\u017f\3\2\2\2g\u0182\3\2\2\2i\u0185\3\2\2\2k\u0187\3")
        buf.write("\2\2\2m\u0189\3\2\2\2o\u018b\3\2\2\2q\u018d\3\2\2\2s\u018f")
        buf.write("\3\2\2\2u\u0191\3\2\2\2w\u0193\3\2\2\2y\u0195\3\2\2\2")
        buf.write("{\u0197\3\2\2\2}\u0199\3\2\2\2\177\u019c\3\2\2\2\u0081")
        buf.write("\u01a2\3\2\2\2\u0083\u01a5\3\2\2\2\u0085\u01a7\3\2\2\2")
        buf.write("\u0087\u009c\7\62\2\2\u0088\u008c\t\2\2\2\u0089\u008b")
        buf.write("\t\3\2\2\u008a\u0089\3\2\2\2\u008b\u008e\3\2\2\2\u008c")
        buf.write("\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u0097\3\2\2\2")
        buf.write("\u008e\u008c\3\2\2\2\u008f\u0091\5\5\3\2\u0090\u0092\t")
        buf.write("\3\2\2\u0091\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0091")
        buf.write("\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0096\3\2\2\2\u0095")
        buf.write("\u008f\3\2\2\2\u0096\u0099\3\2\2\2\u0097\u0095\3\2\2\2")
        buf.write("\u0097\u0098\3\2\2\2\u0098\u009a\3\2\2\2\u0099\u0097\3")
        buf.write("\2\2\2\u009a\u009c\b\2\2\2\u009b\u0087\3\2\2\2\u009b\u0088")
        buf.write("\3\2\2\2\u009c\4\3\2\2\2\u009d\u009e\7a\2\2\u009e\6\3")
        buf.write("\2\2\2\u009f\u00a4\5\13\6\2\u00a0\u00a1\5\t\5\2\u00a1")
        buf.write("\u00a2\b\4\3\2\u00a2\u00a4\3\2\2\2\u00a3\u009f\3\2\2\2")
        buf.write("\u00a3\u00a0\3\2\2\2\u00a4\b\3\2\2\2\u00a5\u00a6\5\3\2")
        buf.write("\2\u00a6\u00a8\5u;\2\u00a7\u00a9\t\3\2\2\u00a8\u00a7\3")
        buf.write("\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00ab")
        buf.write("\3\2\2\2\u00ab\u00b3\3\2\2\2\u00ac\u00b0\t\4\2\2\u00ad")
        buf.write("\u00af\t\3\2\2\u00ae\u00ad\3\2\2\2\u00af\u00b2\3\2\2\2")
        buf.write("\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b4\3")
        buf.write("\2\2\2\u00b2\u00b0\3\2\2\2\u00b3\u00ac\3\2\2\2\u00b3\u00b4")
        buf.write("\3\2\2\2\u00b4\n\3\2\2\2\u00b5\u00b7\t\3\2\2\u00b6\u00b5")
        buf.write("\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8")
        buf.write("\u00b9\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\t\4\2\2")
        buf.write("\u00bb\u00bd\5M\'\2\u00bc\u00be\t\3\2\2\u00bd\u00bc\3")
        buf.write("\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00bd\3\2\2\2\u00bf\u00c0")
        buf.write("\3\2\2\2\u00c0\f\3\2\2\2\u00c1\u00c4\5\17\b\2\u00c2\u00c4")
        buf.write("\5\21\t\2\u00c3\u00c1\3\2\2\2\u00c3\u00c2\3\2\2\2\u00c4")
        buf.write("\16\3\2\2\2\u00c5\u00c6\7h\2\2\u00c6\u00c7\7c\2\2\u00c7")
        buf.write("\u00c8\7n\2\2\u00c8\u00c9\7u\2\2\u00c9\u00ca\7g\2\2\u00ca")
        buf.write("\20\3\2\2\2\u00cb\u00cc\7v\2\2\u00cc\u00cd\7t\2\2\u00cd")
        buf.write("\u00ce\7w\2\2\u00ce\u00cf\7g\2\2\u00cf\22\3\2\2\2\u00d0")
        buf.write("\u00db\5\25\13\2\u00d1\u00d2\13\2\2\2\u00d2\u00da\n\5")
        buf.write("\2\2\u00d3\u00da\5\31\r\2\u00d4\u00da\5\33\16\2\u00d5")
        buf.write("\u00da\5\35\17\2\u00d6\u00da\5\37\20\2\u00d7\u00da\5!")
        buf.write("\21\2\u00d8\u00da\5#\22\2\u00d9\u00d1\3\2\2\2\u00d9\u00d3")
        buf.write("\3\2\2\2\u00d9\u00d4\3\2\2\2\u00d9\u00d5\3\2\2\2\u00d9")
        buf.write("\u00d6\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00d8\3\2\2\2")
        buf.write("\u00da\u00dd\3\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00dc\3")
        buf.write("\2\2\2\u00dc\u00de\3\2\2\2\u00dd\u00db\3\2\2\2\u00de\u00df")
        buf.write("\5\25\13\2\u00df\24\3\2\2\2\u00e0\u00e1\t\6\2\2\u00e1")
        buf.write("\26\3\2\2\2\u00e2\u00e3\t\7\2\2\u00e3\30\3\2\2\2\u00e4")
        buf.write("\u00e5\t\b\2\2\u00e5\32\3\2\2\2\u00e6\u00e7\t\t\2\2\u00e7")
        buf.write("\34\3\2\2\2\u00e8\u00e9\t\n\2\2\u00e9\36\3\2\2\2\u00ea")
        buf.write("\u00eb\t\13\2\2\u00eb \3\2\2\2\u00ec\u00ed\7)\2\2\u00ed")
        buf.write("\"\3\2\2\2\u00ee\u00ef\t\5\2\2\u00ef$\3\2\2\2\u00f0\u00f1")
        buf.write("\7c\2\2\u00f1\u00f2\7w\2\2\u00f2\u00f3\7v\2\2\u00f3\u00f4")
        buf.write("\7q\2\2\u00f4&\3\2\2\2\u00f5\u00f6\7d\2\2\u00f6\u00f7")
        buf.write("\7t\2\2\u00f7\u00f8\7g\2\2\u00f8\u00f9\7c\2\2\u00f9\u00fa")
        buf.write("\7m\2\2\u00fa(\3\2\2\2\u00fb\u00fc\7k\2\2\u00fc\u00fd")
        buf.write("\7p\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7g\2\2\u00ff\u0100")
        buf.write("\7i\2\2\u0100\u0101\7g\2\2\u0101\u0102\7t\2\2\u0102*\3")
        buf.write("\2\2\2\u0103\u0104\7x\2\2\u0104\u0105\7q\2\2\u0105\u0106")
        buf.write("\7k\2\2\u0106\u0107\7f\2\2\u0107,\3\2\2\2\u0108\u0109")
        buf.write("\7c\2\2\u0109\u010a\7t\2\2\u010a\u010b\7t\2\2\u010b\u010c")
        buf.write("\7c\2\2\u010c\u010d\7{\2\2\u010d.\3\2\2\2\u010e\u010f")
        buf.write("\7h\2\2\u010f\u0110\7n\2\2\u0110\u0111\7q\2\2\u0111\u0112")
        buf.write("\7c\2\2\u0112\u0113\7v\2\2\u0113\60\3\2\2\2\u0114\u0115")
        buf.write("\7t\2\2\u0115\u0116\7g\2\2\u0116\u0117\7v\2\2\u0117\u0118")
        buf.write("\7w\2\2\u0118\u0119\7t\2\2\u0119\u011a\7p\2\2\u011a\62")
        buf.write("\3\2\2\2\u011b\u011c\7q\2\2\u011c\u011d\7w\2\2\u011d\u011e")
        buf.write("\7v\2\2\u011e\64\3\2\2\2\u011f\u0120\7d\2\2\u0120\u0121")
        buf.write("\7q\2\2\u0121\u0122\7q\2\2\u0122\u0123\7n\2\2\u0123\u0124")
        buf.write("\7g\2\2\u0124\u0125\7c\2\2\u0125\u0126\7p\2\2\u0126\66")
        buf.write("\3\2\2\2\u0127\u0128\7h\2\2\u0128\u0129\7q\2\2\u0129\u012a")
        buf.write("\7t\2\2\u012a8\3\2\2\2\u012b\u012c\7u\2\2\u012c\u012d")
        buf.write("\7v\2\2\u012d\u012e\7t\2\2\u012e\u012f\7k\2\2\u012f\u0130")
        buf.write("\7p\2\2\u0130\u0131\7i\2\2\u0131:\3\2\2\2\u0132\u0133")
        buf.write("\7e\2\2\u0133\u0134\7q\2\2\u0134\u0135\7p\2\2\u0135\u0136")
        buf.write("\7v\2\2\u0136\u0137\7k\2\2\u0137\u0138\7p\2\2\u0138\u0139")
        buf.write("\7w\2\2\u0139\u013a\7g\2\2\u013a<\3\2\2\2\u013b\u013c")
        buf.write("\7f\2\2\u013c\u013d\7q\2\2\u013d>\3\2\2\2\u013e\u013f")
        buf.write("\7h\2\2\u013f\u0140\7w\2\2\u0140\u0141\7p\2\2\u0141\u0142")
        buf.write("\7e\2\2\u0142\u0143\7v\2\2\u0143\u0144\7k\2\2\u0144\u0145")
        buf.write("\7q\2\2\u0145\u0146\7p\2\2\u0146@\3\2\2\2\u0147\u0148")
        buf.write("\7q\2\2\u0148\u0149\7h\2\2\u0149B\3\2\2\2\u014a\u014b")
        buf.write("\7g\2\2\u014b\u014c\7n\2\2\u014c\u014d\7u\2\2\u014d\u014e")
        buf.write("\7g\2\2\u014eD\3\2\2\2\u014f\u0150\7k\2\2\u0150\u0151")
        buf.write("\7h\2\2\u0151F\3\2\2\2\u0152\u0153\7y\2\2\u0153\u0154")
        buf.write("\7j\2\2\u0154\u0155\7k\2\2\u0155\u0156\7n\2\2\u0156\u0157")
        buf.write("\7g\2\2\u0157H\3\2\2\2\u0158\u0159\7k\2\2\u0159\u015a")
        buf.write("\7p\2\2\u015a\u015b\7j\2\2\u015b\u015c\7g\2\2\u015c\u015d")
        buf.write("\7t\2\2\u015d\u015e\7k\2\2\u015e\u015f\7v\2\2\u015fJ\3")
        buf.write("\2\2\2\u0160\u0161\7-\2\2\u0161L\3\2\2\2\u0162\u0163\7")
        buf.write("/\2\2\u0163N\3\2\2\2\u0164\u0165\7,\2\2\u0165P\3\2\2\2")
        buf.write("\u0166\u0167\7\61\2\2\u0167R\3\2\2\2\u0168\u0169\7\'\2")
        buf.write("\2\u0169T\3\2\2\2\u016a\u016b\7#\2\2\u016bV\3\2\2\2\u016c")
        buf.write("\u016d\7(\2\2\u016d\u016e\7(\2\2\u016eX\3\2\2\2\u016f")
        buf.write("\u0170\7~\2\2\u0170\u0171\7~\2\2\u0171Z\3\2\2\2\u0172")
        buf.write("\u0173\7?\2\2\u0173\u0174\7?\2\2\u0174\\\3\2\2\2\u0175")
        buf.write("\u0176\7#\2\2\u0176\u0177\7?\2\2\u0177^\3\2\2\2\u0178")
        buf.write("\u0179\7>\2\2\u0179`\3\2\2\2\u017a\u017b\7@\2\2\u017b")
        buf.write("b\3\2\2\2\u017c\u017d\7>\2\2\u017d\u017e\7?\2\2\u017e")
        buf.write("d\3\2\2\2\u017f\u0180\7@\2\2\u0180\u0181\7?\2\2\u0181")
        buf.write("f\3\2\2\2\u0182\u0183\7<\2\2\u0183\u0184\7<\2\2\u0184")
        buf.write("h\3\2\2\2\u0185\u0186\7*\2\2\u0186j\3\2\2\2\u0187\u0188")
        buf.write("\7+\2\2\u0188l\3\2\2\2\u0189\u018a\7]\2\2\u018an\3\2\2")
        buf.write("\2\u018b\u018c\7_\2\2\u018cp\3\2\2\2\u018d\u018e\7}\2")
        buf.write("\2\u018er\3\2\2\2\u018f\u0190\7\177\2\2\u0190t\3\2\2\2")
        buf.write("\u0191\u0192\7\60\2\2\u0192v\3\2\2\2\u0193\u0194\7.\2")
        buf.write("\2\u0194x\3\2\2\2\u0195\u0196\7=\2\2\u0196z\3\2\2\2\u0197")
        buf.write("\u0198\7?\2\2\u0198|\3\2\2\2\u0199\u019a\7<\2\2\u019a")
        buf.write("~\3\2\2\2\u019b\u019d\t\f\2\2\u019c\u019b\3\2\2\2\u019d")
        buf.write("\u019e\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019f\3\2\2\2")
        buf.write("\u019f\u01a0\3\2\2\2\u01a0\u01a1\b@\4\2\u01a1\u0080\3")
        buf.write("\2\2\2\u01a2\u01a3\13\2\2\2\u01a3\u01a4\bA\5\2\u01a4\u0082")
        buf.write("\3\2\2\2\u01a5\u01a6\13\2\2\2\u01a6\u0084\3\2\2\2\u01a7")
        buf.write("\u01a8\13\2\2\2\u01a8\u0086\3\2\2\2\21\2\u008c\u0093\u0097")
        buf.write("\u009b\u00a3\u00aa\u00b0\u00b3\u00b8\u00bf\u00c3\u00d9")
        buf.write("\u00db\u019e\6\3\2\2\3\4\3\b\2\2\3A\4")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTEGER_LIT = 1
    FLOAT_LIT = 2
    BOOLEAN_LIT = 3
    STRING_LIT = 4
    AUTO = 5
    BREAK = 6
    INTEGER = 7
    VOID = 8
    ARRAY = 9
    FLOAT = 10
    RETURN = 11
    OUT = 12
    BOOLEAN = 13
    FOR = 14
    STRING = 15
    CONTINUE = 16
    DO = 17
    FUNCTION = 18
    OF = 19
    ELSE = 20
    IF = 21
    WHILE = 22
    INHERIT = 23
    AND = 24
    OR = 25
    EQUAL_TO = 26
    NOT_EQUAL = 27
    LESS = 28
    GREATER = 29
    LESS_THAN_OR_EQUAL = 30
    GREATER_THAN_OR_EQUAL = 31
    SCOPE_RES = 32
    LB = 33
    RB = 34
    LSB = 35
    RSB = 36
    LCB = 37
    RCB = 38
    WS = 39
    ERROR_CHAR = 40
    UNCLOSE_STRING = 41
    ILLEGAL_ESCAPE = 42

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'integer'", "'void'", "'array'", "'float'", 
            "'return'", "'out'", "'boolean'", "'for'", "'string'", "'continue'", 
            "'do'", "'function'", "'of'", "'else'", "'if'", "'while'", "'inherit'", 
            "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
            "'::'", "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "INTEGER_LIT", "FLOAT_LIT", "BOOLEAN_LIT", "STRING_LIT", "AUTO", 
            "BREAK", "INTEGER", "VOID", "ARRAY", "FLOAT", "RETURN", "OUT", 
            "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", "FUNCTION", "OF", 
            "ELSE", "IF", "WHILE", "INHERIT", "AND", "OR", "EQUAL_TO", "NOT_EQUAL", 
            "LESS", "GREATER", "LESS_THAN_OR_EQUAL", "GREATER_THAN_OR_EQUAL", 
            "SCOPE_RES", "LB", "RB", "LSB", "RSB", "LCB", "RCB", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INTEGER_LIT", "UNDERSCORE", "FLOAT_LIT", "DECPART", "EXPPART", 
                  "BOOLEAN_LIT", "FALSE", "TRUE", "STRING_LIT", "DUO_QUOTE", 
                  "SINGLE_QUOTE", "BackSpace", "FormFeed", "CarriageReturn", 
                  "NewLine", "SingleQuote", "BackSlash", "AUTO", "BREAK", 
                  "INTEGER", "VOID", "ARRAY", "FLOAT", "RETURN", "OUT", 
                  "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", "FUNCTION", 
                  "OF", "ELSE", "IF", "WHILE", "INHERIT", "PLUS", "MINUS", 
                  "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL_TO", "NOT_EQUAL", 
                  "LESS", "GREATER", "LESS_THAN_OR_EQUAL", "GREATER_THAN_OR_EQUAL", 
                  "SCOPE_RES", "LB", "RB", "LSB", "RSB", "LCB", "RCB", "PERIOD", 
                  "COMMA", "SEMI", "EQUAL", "COLON", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[0] = self.INTEGER_LIT_action 
            actions[2] = self.FLOAT_LIT_action 
            actions[63] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTEGER_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_","")
     

    def FLOAT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_","")
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     


