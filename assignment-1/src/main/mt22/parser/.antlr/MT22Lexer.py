# Generated from c:\Users\84865\Documents\BK-CSE20\CSE-PPL\assignment-1\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
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
        buf.write("\u01ad\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\3\2\3\2\7\2\u008d\n\2\f\2\16\2\u0090\13\2")
        buf.write("\3\2\3\2\6\2\u0094\n\2\r\2\16\2\u0095\7\2\u0098\n\2\f")
        buf.write("\2\16\2\u009b\13\2\3\2\5\2\u009e\n\2\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\5\4\u00a6\n\4\3\5\3\5\3\5\6\5\u00ab\n\5\r\5\16")
        buf.write("\5\u00ac\3\5\3\5\7\5\u00b1\n\5\f\5\16\5\u00b4\13\5\5\5")
        buf.write("\u00b6\n\5\3\6\6\6\u00b9\n\6\r\6\16\6\u00ba\3\6\3\6\3")
        buf.write("\6\6\6\u00c0\n\6\r\6\16\6\u00c1\3\7\3\7\5\7\u00c6\n\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\7\n\u00d7\n\n\f\n\16\n\u00da\13\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\5\13\u00e3\n\13\3\f\3\f\3\r\3\r\3")
        buf.write("\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3")
        buf.write("#\3#\3#\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3-\3")
        buf.write(".\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3\62\3")
        buf.write("\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66")
        buf.write("\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3")
        buf.write("?\3?\3@\3@\3A\6A\u01a1\nA\rA\16A\u01a2\3A\3A\3B\3B\3B")
        buf.write("\3C\3C\3D\3D\3\u00d8\2E\3\3\5\2\7\4\t\2\13\2\r\5\17\2")
        buf.write("\21\2\23\6\25\2\27\2\31\2\33\2\35\2\37\2!\2#\2%\2\'\7")
        buf.write(")\b+\t-\n/\13\61\f\63\r\65\16\67\179\20;\21=\22?\23A\24")
        buf.write("C\25E\26G\27I\30K\31M\2O\2Q\2S\2U\2W\2Y\32[\33]\34_\35")
        buf.write("a\36c\37e g!i\"k#m$o%q&s\'u(w\2y\2{\2}\2\177\2\u0081)")
        buf.write("\u0083*\u0085+\u0087,\3\2\r\3\2\63;\3\2\62;\4\2GGgg\3")
        buf.write("\2^^\3\2$$\3\2))\3\2\n\n\3\2\16\16\3\2\17\17\3\2\f\f\5")
        buf.write("\2\13\f\17\17\"\"\2\u01a5\2\3\3\2\2\2\2\7\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2")
        buf.write("\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\3\u009d\3\2\2")
        buf.write("\2\5\u009f\3\2\2\2\7\u00a5\3\2\2\2\t\u00a7\3\2\2\2\13")
        buf.write("\u00b8\3\2\2\2\r\u00c5\3\2\2\2\17\u00c7\3\2\2\2\21\u00cd")
        buf.write("\3\2\2\2\23\u00d2\3\2\2\2\25\u00e2\3\2\2\2\27\u00e4\3")
        buf.write("\2\2\2\31\u00e6\3\2\2\2\33\u00e8\3\2\2\2\35\u00ea\3\2")
        buf.write("\2\2\37\u00ec\3\2\2\2!\u00ee\3\2\2\2#\u00f0\3\2\2\2%\u00f2")
        buf.write("\3\2\2\2\'\u00f4\3\2\2\2)\u00f9\3\2\2\2+\u00ff\3\2\2\2")
        buf.write("-\u0107\3\2\2\2/\u010c\3\2\2\2\61\u0112\3\2\2\2\63\u0118")
        buf.write("\3\2\2\2\65\u011f\3\2\2\2\67\u0123\3\2\2\29\u012b\3\2")
        buf.write("\2\2;\u012f\3\2\2\2=\u0136\3\2\2\2?\u013f\3\2\2\2A\u0142")
        buf.write("\3\2\2\2C\u014b\3\2\2\2E\u014e\3\2\2\2G\u0153\3\2\2\2")
        buf.write("I\u0156\3\2\2\2K\u015c\3\2\2\2M\u0164\3\2\2\2O\u0166\3")
        buf.write("\2\2\2Q\u0168\3\2\2\2S\u016a\3\2\2\2U\u016c\3\2\2\2W\u016e")
        buf.write("\3\2\2\2Y\u0170\3\2\2\2[\u0173\3\2\2\2]\u0176\3\2\2\2")
        buf.write("_\u0179\3\2\2\2a\u017c\3\2\2\2c\u017e\3\2\2\2e\u0180\3")
        buf.write("\2\2\2g\u0183\3\2\2\2i\u0186\3\2\2\2k\u0189\3\2\2\2m\u018b")
        buf.write("\3\2\2\2o\u018d\3\2\2\2q\u018f\3\2\2\2s\u0191\3\2\2\2")
        buf.write("u\u0193\3\2\2\2w\u0195\3\2\2\2y\u0197\3\2\2\2{\u0199\3")
        buf.write("\2\2\2}\u019b\3\2\2\2\177\u019d\3\2\2\2\u0081\u01a0\3")
        buf.write("\2\2\2\u0083\u01a6\3\2\2\2\u0085\u01a9\3\2\2\2\u0087\u01ab")
        buf.write("\3\2\2\2\u0089\u009e\7\62\2\2\u008a\u008e\t\2\2\2\u008b")
        buf.write("\u008d\t\3\2\2\u008c\u008b\3\2\2\2\u008d\u0090\3\2\2\2")
        buf.write("\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0099\3")
        buf.write("\2\2\2\u0090\u008e\3\2\2\2\u0091\u0093\5\5\3\2\u0092\u0094")
        buf.write("\t\3\2\2\u0093\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095")
        buf.write("\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0098\3\2\2\2")
        buf.write("\u0097\u0091\3\2\2\2\u0098\u009b\3\2\2\2\u0099\u0097\3")
        buf.write("\2\2\2\u0099\u009a\3\2\2\2\u009a\u009c\3\2\2\2\u009b\u0099")
        buf.write("\3\2\2\2\u009c\u009e\b\2\2\2\u009d\u0089\3\2\2\2\u009d")
        buf.write("\u008a\3\2\2\2\u009e\4\3\2\2\2\u009f\u00a0\7a\2\2\u00a0")
        buf.write("\6\3\2\2\2\u00a1\u00a6\5\13\6\2\u00a2\u00a3\5\t\5\2\u00a3")
        buf.write("\u00a4\b\4\3\2\u00a4\u00a6\3\2\2\2\u00a5\u00a1\3\2\2\2")
        buf.write("\u00a5\u00a2\3\2\2\2\u00a6\b\3\2\2\2\u00a7\u00a8\5\3\2")
        buf.write("\2\u00a8\u00aa\5w<\2\u00a9\u00ab\t\3\2\2\u00aa\u00a9\3")
        buf.write("\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad")
        buf.write("\3\2\2\2\u00ad\u00b5\3\2\2\2\u00ae\u00b2\t\4\2\2\u00af")
        buf.write("\u00b1\t\3\2\2\u00b0\u00af\3\2\2\2\u00b1\u00b4\3\2\2\2")
        buf.write("\u00b2\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b6\3")
        buf.write("\2\2\2\u00b4\u00b2\3\2\2\2\u00b5\u00ae\3\2\2\2\u00b5\u00b6")
        buf.write("\3\2\2\2\u00b6\n\3\2\2\2\u00b7\u00b9\t\3\2\2\u00b8\u00b7")
        buf.write("\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba")
        buf.write("\u00bb\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd\t\4\2\2")
        buf.write("\u00bd\u00bf\5O(\2\u00be\u00c0\t\3\2\2\u00bf\u00be\3\2")
        buf.write("\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2")
        buf.write("\3\2\2\2\u00c2\f\3\2\2\2\u00c3\u00c6\5\17\b\2\u00c4\u00c6")
        buf.write("\5\21\t\2\u00c5\u00c3\3\2\2\2\u00c5\u00c4\3\2\2\2\u00c6")
        buf.write("\16\3\2\2\2\u00c7\u00c8\7h\2\2\u00c8\u00c9\7c\2\2\u00c9")
        buf.write("\u00ca\7n\2\2\u00ca\u00cb\7u\2\2\u00cb\u00cc\7g\2\2\u00cc")
        buf.write("\20\3\2\2\2\u00cd\u00ce\7v\2\2\u00ce\u00cf\7t\2\2\u00cf")
        buf.write("\u00d0\7w\2\2\u00d0\u00d1\7g\2\2\u00d1\22\3\2\2\2\u00d2")
        buf.write("\u00d8\5\27\f\2\u00d3\u00d4\13\2\2\2\u00d4\u00d7\n\5\2")
        buf.write("\2\u00d5\u00d7\3\2\2\2\u00d6\u00d3\3\2\2\2\u00d6\u00d5")
        buf.write("\3\2\2\2\u00d7\u00da\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d8")
        buf.write("\u00d6\3\2\2\2\u00d9\u00db\3\2\2\2\u00da\u00d8\3\2\2\2")
        buf.write("\u00db\u00dc\5\27\f\2\u00dc\24\3\2\2\2\u00dd\u00e3\5\33")
        buf.write("\16\2\u00de\u00e3\5\35\17\2\u00df\u00e3\5\37\20\2\u00e0")
        buf.write("\u00e3\5!\21\2\u00e1\u00e3\5#\22\2\u00e2\u00dd\3\2\2\2")
        buf.write("\u00e2\u00de\3\2\2\2\u00e2\u00df\3\2\2\2\u00e2\u00e0\3")
        buf.write("\2\2\2\u00e2\u00e1\3\2\2\2\u00e3\26\3\2\2\2\u00e4\u00e5")
        buf.write("\t\6\2\2\u00e5\30\3\2\2\2\u00e6\u00e7\t\7\2\2\u00e7\32")
        buf.write("\3\2\2\2\u00e8\u00e9\t\b\2\2\u00e9\34\3\2\2\2\u00ea\u00eb")
        buf.write("\t\t\2\2\u00eb\36\3\2\2\2\u00ec\u00ed\t\n\2\2\u00ed \3")
        buf.write("\2\2\2\u00ee\u00ef\t\13\2\2\u00ef\"\3\2\2\2\u00f0\u00f1")
        buf.write("\7)\2\2\u00f1$\3\2\2\2\u00f2\u00f3\t\5\2\2\u00f3&\3\2")
        buf.write("\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6\7w\2\2\u00f6\u00f7")
        buf.write("\7v\2\2\u00f7\u00f8\7q\2\2\u00f8(\3\2\2\2\u00f9\u00fa")
        buf.write("\7d\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc\7g\2\2\u00fc\u00fd")
        buf.write("\7c\2\2\u00fd\u00fe\7m\2\2\u00fe*\3\2\2\2\u00ff\u0100")
        buf.write("\7k\2\2\u0100\u0101\7p\2\2\u0101\u0102\7v\2\2\u0102\u0103")
        buf.write("\7g\2\2\u0103\u0104\7i\2\2\u0104\u0105\7g\2\2\u0105\u0106")
        buf.write("\7t\2\2\u0106,\3\2\2\2\u0107\u0108\7x\2\2\u0108\u0109")
        buf.write("\7q\2\2\u0109\u010a\7k\2\2\u010a\u010b\7f\2\2\u010b.\3")
        buf.write("\2\2\2\u010c\u010d\7c\2\2\u010d\u010e\7t\2\2\u010e\u010f")
        buf.write("\7t\2\2\u010f\u0110\7c\2\2\u0110\u0111\7{\2\2\u0111\60")
        buf.write("\3\2\2\2\u0112\u0113\7h\2\2\u0113\u0114\7n\2\2\u0114\u0115")
        buf.write("\7q\2\2\u0115\u0116\7c\2\2\u0116\u0117\7v\2\2\u0117\62")
        buf.write("\3\2\2\2\u0118\u0119\7t\2\2\u0119\u011a\7g\2\2\u011a\u011b")
        buf.write("\7v\2\2\u011b\u011c\7w\2\2\u011c\u011d\7t\2\2\u011d\u011e")
        buf.write("\7p\2\2\u011e\64\3\2\2\2\u011f\u0120\7q\2\2\u0120\u0121")
        buf.write("\7w\2\2\u0121\u0122\7v\2\2\u0122\66\3\2\2\2\u0123\u0124")
        buf.write("\7d\2\2\u0124\u0125\7q\2\2\u0125\u0126\7q\2\2\u0126\u0127")
        buf.write("\7n\2\2\u0127\u0128\7g\2\2\u0128\u0129\7c\2\2\u0129\u012a")
        buf.write("\7p\2\2\u012a8\3\2\2\2\u012b\u012c\7h\2\2\u012c\u012d")
        buf.write("\7q\2\2\u012d\u012e\7t\2\2\u012e:\3\2\2\2\u012f\u0130")
        buf.write("\7u\2\2\u0130\u0131\7v\2\2\u0131\u0132\7t\2\2\u0132\u0133")
        buf.write("\7k\2\2\u0133\u0134\7p\2\2\u0134\u0135\7i\2\2\u0135<\3")
        buf.write("\2\2\2\u0136\u0137\7e\2\2\u0137\u0138\7q\2\2\u0138\u0139")
        buf.write("\7p\2\2\u0139\u013a\7v\2\2\u013a\u013b\7k\2\2\u013b\u013c")
        buf.write("\7p\2\2\u013c\u013d\7w\2\2\u013d\u013e\7g\2\2\u013e>\3")
        buf.write("\2\2\2\u013f\u0140\7f\2\2\u0140\u0141\7q\2\2\u0141@\3")
        buf.write("\2\2\2\u0142\u0143\7h\2\2\u0143\u0144\7w\2\2\u0144\u0145")
        buf.write("\7p\2\2\u0145\u0146\7e\2\2\u0146\u0147\7v\2\2\u0147\u0148")
        buf.write("\7k\2\2\u0148\u0149\7q\2\2\u0149\u014a\7p\2\2\u014aB\3")
        buf.write("\2\2\2\u014b\u014c\7q\2\2\u014c\u014d\7h\2\2\u014dD\3")
        buf.write("\2\2\2\u014e\u014f\7g\2\2\u014f\u0150\7n\2\2\u0150\u0151")
        buf.write("\7u\2\2\u0151\u0152\7g\2\2\u0152F\3\2\2\2\u0153\u0154")
        buf.write("\7k\2\2\u0154\u0155\7h\2\2\u0155H\3\2\2\2\u0156\u0157")
        buf.write("\7y\2\2\u0157\u0158\7j\2\2\u0158\u0159\7k\2\2\u0159\u015a")
        buf.write("\7n\2\2\u015a\u015b\7g\2\2\u015bJ\3\2\2\2\u015c\u015d")
        buf.write("\7k\2\2\u015d\u015e\7p\2\2\u015e\u015f\7j\2\2\u015f\u0160")
        buf.write("\7g\2\2\u0160\u0161\7t\2\2\u0161\u0162\7k\2\2\u0162\u0163")
        buf.write("\7v\2\2\u0163L\3\2\2\2\u0164\u0165\7-\2\2\u0165N\3\2\2")
        buf.write("\2\u0166\u0167\7/\2\2\u0167P\3\2\2\2\u0168\u0169\7,\2")
        buf.write("\2\u0169R\3\2\2\2\u016a\u016b\7\61\2\2\u016bT\3\2\2\2")
        buf.write("\u016c\u016d\7\'\2\2\u016dV\3\2\2\2\u016e\u016f\7#\2\2")
        buf.write("\u016fX\3\2\2\2\u0170\u0171\7(\2\2\u0171\u0172\7(\2\2")
        buf.write("\u0172Z\3\2\2\2\u0173\u0174\7~\2\2\u0174\u0175\7~\2\2")
        buf.write("\u0175\\\3\2\2\2\u0176\u0177\7?\2\2\u0177\u0178\7?\2\2")
        buf.write("\u0178^\3\2\2\2\u0179\u017a\7#\2\2\u017a\u017b\7?\2\2")
        buf.write("\u017b`\3\2\2\2\u017c\u017d\7>\2\2\u017db\3\2\2\2\u017e")
        buf.write("\u017f\7@\2\2\u017fd\3\2\2\2\u0180\u0181\7>\2\2\u0181")
        buf.write("\u0182\7?\2\2\u0182f\3\2\2\2\u0183\u0184\7@\2\2\u0184")
        buf.write("\u0185\7?\2\2\u0185h\3\2\2\2\u0186\u0187\7<\2\2\u0187")
        buf.write("\u0188\7<\2\2\u0188j\3\2\2\2\u0189\u018a\7*\2\2\u018a")
        buf.write("l\3\2\2\2\u018b\u018c\7+\2\2\u018cn\3\2\2\2\u018d\u018e")
        buf.write("\7]\2\2\u018ep\3\2\2\2\u018f\u0190\7_\2\2\u0190r\3\2\2")
        buf.write("\2\u0191\u0192\7}\2\2\u0192t\3\2\2\2\u0193\u0194\7\177")
        buf.write("\2\2\u0194v\3\2\2\2\u0195\u0196\7\60\2\2\u0196x\3\2\2")
        buf.write("\2\u0197\u0198\7.\2\2\u0198z\3\2\2\2\u0199\u019a\7=\2")
        buf.write("\2\u019a|\3\2\2\2\u019b\u019c\7?\2\2\u019c~\3\2\2\2\u019d")
        buf.write("\u019e\7<\2\2\u019e\u0080\3\2\2\2\u019f\u01a1\t\f\2\2")
        buf.write("\u01a0\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a0\3")
        buf.write("\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a5")
        buf.write("\bA\4\2\u01a5\u0082\3\2\2\2\u01a6\u01a7\13\2\2\2\u01a7")
        buf.write("\u01a8\bB\5\2\u01a8\u0084\3\2\2\2\u01a9\u01aa\13\2\2\2")
        buf.write("\u01aa\u0086\3\2\2\2\u01ab\u01ac\13\2\2\2\u01ac\u0088")
        buf.write("\3\2\2\2\22\2\u008e\u0095\u0099\u009d\u00a5\u00ac\u00b2")
        buf.write("\u00b5\u00ba\u00c1\u00c5\u00d6\u00d8\u00e2\u01a2\6\3\2")
        buf.write("\2\3\4\3\b\2\2\3B\4")
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
                  "BOOLEAN_LIT", "FALSE", "TRUE", "STRING_LIT", "Escape_Sequence", 
                  "DUO_QUOTE", "SINGLE_QUOTE", "BackSpace", "FormFeed", 
                  "CarriageReturn", "NewLine", "SingleQuote", "BackSlash", 
                  "AUTO", "BREAK", "INTEGER", "VOID", "ARRAY", "FLOAT", 
                  "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", 
                  "DO", "FUNCTION", "OF", "ELSE", "IF", "WHILE", "INHERIT", 
                  "PLUS", "MINUS", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                  "EQUAL_TO", "NOT_EQUAL", "LESS", "GREATER", "LESS_THAN_OR_EQUAL", 
                  "GREATER_THAN_OR_EQUAL", "SCOPE_RES", "LB", "RB", "LSB", 
                  "RSB", "LCB", "RCB", "PERIOD", "COMMA", "SEMI", "EQUAL", 
                  "COLON", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[64] = self.ERROR_CHAR_action 
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
     


