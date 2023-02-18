# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\31")
        buf.write("\u01d6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\f")
        buf.write("\3\f\3\r\3\r\5\r\u00c2\n\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\7\16\u00ca\n\16\f\16\16\16\u00cd\13\16\3\17\3\17\3\17")
        buf.write("\3\17\7\17\u00d3\n\17\f\17\16\17\u00d6\13\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\7\20\u00de\n\20\f\20\16\20\u00e1")
        buf.write("\13\20\3\20\3\20\6\20\u00e5\n\20\r\20\16\20\u00e6\7\20")
        buf.write("\u00e9\n\20\f\20\16\20\u00ec\13\20\3\20\5\20\u00ef\n\20")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\5\22\u00f7\n\22\3\23\3")
        buf.write("\23\3\23\6\23\u00fc\n\23\r\23\16\23\u00fd\3\23\3\23\7")
        buf.write("\23\u0102\n\23\f\23\16\23\u0105\13\23\5\23\u0107\n\23")
        buf.write("\3\24\6\24\u010a\n\24\r\24\16\24\u010b\3\24\3\24\3\24")
        buf.write("\6\24\u0111\n\24\r\24\16\24\u0112\3\25\3\25\5\25\u0117")
        buf.write("\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\7\30\u0127\n\30\f\30\16\30\u012a")
        buf.write("\13\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\7\31\u0133\n")
        buf.write("\31\f\31\16\31\u0136\13\31\3\31\3\31\3\31\3\32\3\32\5")
        buf.write("\32\u013d\n\32\3\32\3\32\3\33\3\33\5\33\u0143\n\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\5\34\u014a\n\34\3\35\3\35\3\35\3")
        buf.write("\35\3\35\5\35\u0151\n\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\5\36\u015a\n\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3")
        buf.write("#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3")
        buf.write("+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3")
        buf.write("\61\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:")
        buf.write("\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\6B\u01ab")
        buf.write("\nB\rB\16B\u01ac\3B\7B\u01b0\nB\fB\16B\u01b3\13B\3C\3")
        buf.write("C\5C\u01b7\nC\3D\6D\u01ba\nD\rD\16D\u01bb\3D\3D\3E\3E")
        buf.write("\3E\7E\u01c3\nE\fE\16E\u01c6\13E\3E\3E\3F\3F\7F\u01cc")
        buf.write("\nF\fF\16F\u01cf\13F\3F\3F\3F\3G\3G\3G\7\u00d4\u0128\u0134")
        buf.write("\u01c4\u01cd\2H\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\2\35\2\37\17!\2#\20%\2\'\2)\21")
        buf.write("+\2-\2/\22\61\2\63\23\65\2\67\29\2;\2=\2?\2A\2C\2E\2G")
        buf.write("\2I\2K\2M\2O\2Q\2S\2U\2W\2Y\2[\2]\2_\2a\2c\2e\2g\2i\2")
        buf.write("k\2m\2o\2q\2s\2u\2w\2y\2{\2}\2\177\2\u0081\2\u0083\24")
        buf.write("\u0085\25\u0087\26\u0089\27\u008b\30\u008d\31\3\2\21\4")
        buf.write("\2\f\f\17\17\3\2\63;\3\2\62;\4\2GGgg\4\2$$^^\3\2$$\3\2")
        buf.write("))\3\2\n\n\3\2\16\16\3\2\17\17\3\2\f\f\3\2^^\5\2C\\aa")
        buf.write("c|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2\u01c9\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\37\3\2\2\2\2#\3\2")
        buf.write("\2\2\2)\3\2\2\2\2/\3\2\2\2\2\63\3\2\2\2\2\u0083\3\2\2")
        buf.write("\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\3\u008f\3\2\2\2\5\u0091\3\2\2")
        buf.write("\2\7\u0097\3\2\2\2\t\u0099\3\2\2\2\13\u009b\3\2\2\2\r")
        buf.write("\u009e\3\2\2\2\17\u00a6\3\2\2\2\21\u00ac\3\2\2\2\23\u00b4")
        buf.write("\3\2\2\2\25\u00bb\3\2\2\2\27\u00bd\3\2\2\2\31\u00c1\3")
        buf.write("\2\2\2\33\u00c5\3\2\2\2\35\u00ce\3\2\2\2\37\u00ee\3\2")
        buf.write("\2\2!\u00f0\3\2\2\2#\u00f6\3\2\2\2%\u00f8\3\2\2\2\'\u0109")
        buf.write("\3\2\2\2)\u0116\3\2\2\2+\u0118\3\2\2\2-\u011e\3\2\2\2")
        buf.write("/\u0123\3\2\2\2\61\u012e\3\2\2\2\63\u013a\3\2\2\2\65\u0142")
        buf.write("\3\2\2\2\67\u0149\3\2\2\29\u0150\3\2\2\2;\u0159\3\2\2")
        buf.write("\2=\u015b\3\2\2\2?\u015d\3\2\2\2A\u015f\3\2\2\2C\u0161")
        buf.write("\3\2\2\2E\u0163\3\2\2\2G\u0165\3\2\2\2I\u0167\3\2\2\2")
        buf.write("K\u0169\3\2\2\2M\u016b\3\2\2\2O\u016e\3\2\2\2Q\u0170\3")
        buf.write("\2\2\2S\u0172\3\2\2\2U\u0174\3\2\2\2W\u0176\3\2\2\2Y\u0178")
        buf.write("\3\2\2\2[\u017a\3\2\2\2]\u017c\3\2\2\2_\u017f\3\2\2\2")
        buf.write("a\u0182\3\2\2\2c\u0184\3\2\2\2e\u0187\3\2\2\2g\u018a\3")
        buf.write("\2\2\2i\u018d\3\2\2\2k\u0190\3\2\2\2m\u0193\3\2\2\2o\u0195")
        buf.write("\3\2\2\2q\u0197\3\2\2\2s\u0199\3\2\2\2u\u019b\3\2\2\2")
        buf.write("w\u019d\3\2\2\2y\u019f\3\2\2\2{\u01a1\3\2\2\2}\u01a3\3")
        buf.write("\2\2\2\177\u01a5\3\2\2\2\u0081\u01a7\3\2\2\2\u0083\u01aa")
        buf.write("\3\2\2\2\u0085\u01b6\3\2\2\2\u0087\u01b9\3\2\2\2\u0089")
        buf.write("\u01bf\3\2\2\2\u008b\u01cd\3\2\2\2\u008d\u01d3\3\2\2\2")
        buf.write("\u008f\u0090\7.\2\2\u0090\4\3\2\2\2\u0091\u0092\7c\2\2")
        buf.write("\u0092\u0093\7t\2\2\u0093\u0094\7t\2\2\u0094\u0095\7c")
        buf.write("\2\2\u0095\u0096\7{\2\2\u0096\6\3\2\2\2\u0097\u0098\7")
        buf.write("]\2\2\u0098\b\3\2\2\2\u0099\u009a\7_\2\2\u009a\n\3\2\2")
        buf.write("\2\u009b\u009c\7q\2\2\u009c\u009d\7h\2\2\u009d\f\3\2\2")
        buf.write("\2\u009e\u009f\7k\2\2\u009f\u00a0\7p\2\2\u00a0\u00a1\7")
        buf.write("v\2\2\u00a1\u00a2\7g\2\2\u00a2\u00a3\7i\2\2\u00a3\u00a4")
        buf.write("\7g\2\2\u00a4\u00a5\7t\2\2\u00a5\16\3\2\2\2\u00a6\u00a7")
        buf.write("\7h\2\2\u00a7\u00a8\7n\2\2\u00a8\u00a9\7q\2\2\u00a9\u00aa")
        buf.write("\7c\2\2\u00aa\u00ab\7v\2\2\u00ab\20\3\2\2\2\u00ac\u00ad")
        buf.write("\7d\2\2\u00ad\u00ae\7q\2\2\u00ae\u00af\7q\2\2\u00af\u00b0")
        buf.write("\7n\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2\7c\2\2\u00b2\u00b3")
        buf.write("\7p\2\2\u00b3\22\3\2\2\2\u00b4\u00b5\7u\2\2\u00b5\u00b6")
        buf.write("\7v\2\2\u00b6\u00b7\7t\2\2\u00b7\u00b8\7k\2\2\u00b8\u00b9")
        buf.write("\7p\2\2\u00b9\u00ba\7i\2\2\u00ba\24\3\2\2\2\u00bb\u00bc")
        buf.write("\7=\2\2\u00bc\26\3\2\2\2\u00bd\u00be\7?\2\2\u00be\30\3")
        buf.write("\2\2\2\u00bf\u00c2\5\33\16\2\u00c0\u00c2\5\35\17\2\u00c1")
        buf.write("\u00bf\3\2\2\2\u00c1\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2")
        buf.write("\u00c3\u00c4\b\r\2\2\u00c4\32\3\2\2\2\u00c5\u00c6\7\61")
        buf.write("\2\2\u00c6\u00c7\7\61\2\2\u00c7\u00cb\3\2\2\2\u00c8\u00ca")
        buf.write("\n\2\2\2\u00c9\u00c8\3\2\2\2\u00ca\u00cd\3\2\2\2\u00cb")
        buf.write("\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\34\3\2\2\2\u00cd")
        buf.write("\u00cb\3\2\2\2\u00ce\u00cf\7\61\2\2\u00cf\u00d0\7,\2\2")
        buf.write("\u00d0\u00d4\3\2\2\2\u00d1\u00d3\13\2\2\2\u00d2\u00d1")
        buf.write("\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d4")
        buf.write("\u00d2\3\2\2\2\u00d5\u00d7\3\2\2\2\u00d6\u00d4\3\2\2\2")
        buf.write("\u00d7\u00d8\7,\2\2\u00d8\u00d9\7\61\2\2\u00d9\36\3\2")
        buf.write("\2\2\u00da\u00ef\7\62\2\2\u00db\u00df\t\3\2\2\u00dc\u00de")
        buf.write("\t\4\2\2\u00dd\u00dc\3\2\2\2\u00de\u00e1\3\2\2\2\u00df")
        buf.write("\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00ea\3\2\2\2")
        buf.write("\u00e1\u00df\3\2\2\2\u00e2\u00e4\5!\21\2\u00e3\u00e5\t")
        buf.write("\4\2\2\u00e4\u00e3\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e4")
        buf.write("\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e9\3\2\2\2\u00e8")
        buf.write("\u00e2\3\2\2\2\u00e9\u00ec\3\2\2\2\u00ea\u00e8\3\2\2\2")
        buf.write("\u00ea\u00eb\3\2\2\2\u00eb\u00ed\3\2\2\2\u00ec\u00ea\3")
        buf.write("\2\2\2\u00ed\u00ef\b\20\3\2\u00ee\u00da\3\2\2\2\u00ee")
        buf.write("\u00db\3\2\2\2\u00ef \3\2\2\2\u00f0\u00f1\7a\2\2\u00f1")
        buf.write("\"\3\2\2\2\u00f2\u00f7\5\'\24\2\u00f3\u00f4\5%\23\2\u00f4")
        buf.write("\u00f5\b\22\4\2\u00f5\u00f7\3\2\2\2\u00f6\u00f2\3\2\2")
        buf.write("\2\u00f6\u00f3\3\2\2\2\u00f7$\3\2\2\2\u00f8\u00f9\5\37")
        buf.write("\20\2\u00f9\u00fb\5m\67\2\u00fa\u00fc\t\4\2\2\u00fb\u00fa")
        buf.write("\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd")
        buf.write("\u00fe\3\2\2\2\u00fe\u0106\3\2\2\2\u00ff\u0103\t\5\2\2")
        buf.write("\u0100\u0102\t\4\2\2\u0101\u0100\3\2\2\2\u0102\u0105\3")
        buf.write("\2\2\2\u0103\u0101\3\2\2\2\u0103\u0104\3\2\2\2\u0104\u0107")
        buf.write("\3\2\2\2\u0105\u0103\3\2\2\2\u0106\u00ff\3\2\2\2\u0106")
        buf.write("\u0107\3\2\2\2\u0107&\3\2\2\2\u0108\u010a\t\4\2\2\u0109")
        buf.write("\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u0109\3\2\2\2")
        buf.write("\u010b\u010c\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u010e\t")
        buf.write("\5\2\2\u010e\u0110\5Q)\2\u010f\u0111\t\4\2\2\u0110\u010f")
        buf.write("\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0110\3\2\2\2\u0112")
        buf.write("\u0113\3\2\2\2\u0113(\3\2\2\2\u0114\u0117\5+\26\2\u0115")
        buf.write("\u0117\5-\27\2\u0116\u0114\3\2\2\2\u0116\u0115\3\2\2\2")
        buf.write("\u0117*\3\2\2\2\u0118\u0119\7h\2\2\u0119\u011a\7c\2\2")
        buf.write("\u011a\u011b\7n\2\2\u011b\u011c\7u\2\2\u011c\u011d\7g")
        buf.write("\2\2\u011d,\3\2\2\2\u011e\u011f\7v\2\2\u011f\u0120\7t")
        buf.write("\2\2\u0120\u0121\7w\2\2\u0121\u0122\7g\2\2\u0122.\3\2")
        buf.write("\2\2\u0123\u0128\5=\37\2\u0124\u0127\n\6\2\2\u0125\u0127")
        buf.write("\5\61\31\2\u0126\u0124\3\2\2\2\u0126\u0125\3\2\2\2\u0127")
        buf.write("\u012a\3\2\2\2\u0128\u0129\3\2\2\2\u0128\u0126\3\2\2\2")
        buf.write("\u0129\u012b\3\2\2\2\u012a\u0128\3\2\2\2\u012b\u012c\5")
        buf.write("=\37\2\u012c\u012d\b\30\5\2\u012d\60\3\2\2\2\u012e\u012f")
        buf.write("\7^\2\2\u012f\u0130\7$\2\2\u0130\u0134\3\2\2\2\u0131\u0133")
        buf.write("\13\2\2\2\u0132\u0131\3\2\2\2\u0133\u0136\3\2\2\2\u0134")
        buf.write("\u0135\3\2\2\2\u0134\u0132\3\2\2\2\u0135\u0137\3\2\2\2")
        buf.write("\u0136\u0134\3\2\2\2\u0137\u0138\7^\2\2\u0138\u0139\7")
        buf.write("$\2\2\u0139\62\3\2\2\2\u013a\u013c\5\177@\2\u013b\u013d")
        buf.write("\5\65\33\2\u013c\u013b\3\2\2\2\u013c\u013d\3\2\2\2\u013d")
        buf.write("\u013e\3\2\2\2\u013e\u013f\5\u0081A\2\u013f\64\3\2\2\2")
        buf.write("\u0140\u0143\5\67\34\2\u0141\u0143\59\35\2\u0142\u0140")
        buf.write("\3\2\2\2\u0142\u0141\3\2\2\2\u0143\66\3\2\2\2\u0144\u0145")
        buf.write("\5\u0085C\2\u0145\u0146\5o8\2\u0146\u0147\5\67\34\2\u0147")
        buf.write("\u014a\3\2\2\2\u0148\u014a\5\u0085C\2\u0149\u0144\3\2")
        buf.write("\2\2\u0149\u0148\3\2\2\2\u014a8\3\2\2\2\u014b\u014c\5")
        buf.write("/\30\2\u014c\u014d\5o8\2\u014d\u014e\59\35\2\u014e\u0151")
        buf.write("\3\2\2\2\u014f\u0151\5/\30\2\u0150\u014b\3\2\2\2\u0150")
        buf.write("\u014f\3\2\2\2\u0151:\3\2\2\2\u0152\u015a\5A!\2\u0153")
        buf.write("\u015a\5C\"\2\u0154\u015a\5E#\2\u0155\u015a\5G$\2\u0156")
        buf.write("\u015a\5I%\2\u0157\u015a\5M\'\2\u0158\u015a\5K&\2\u0159")
        buf.write("\u0152\3\2\2\2\u0159\u0153\3\2\2\2\u0159\u0154\3\2\2\2")
        buf.write("\u0159\u0155\3\2\2\2\u0159\u0156\3\2\2\2\u0159\u0157\3")
        buf.write("\2\2\2\u0159\u0158\3\2\2\2\u015a<\3\2\2\2\u015b\u015c")
        buf.write("\t\7\2\2\u015c>\3\2\2\2\u015d\u015e\t\b\2\2\u015e@\3\2")
        buf.write("\2\2\u015f\u0160\t\t\2\2\u0160B\3\2\2\2\u0161\u0162\t")
        buf.write("\n\2\2\u0162D\3\2\2\2\u0163\u0164\t\13\2\2\u0164F\3\2")
        buf.write("\2\2\u0165\u0166\t\f\2\2\u0166H\3\2\2\2\u0167\u0168\7")
        buf.write(")\2\2\u0168J\3\2\2\2\u0169\u016a\t\r\2\2\u016aL\3\2\2")
        buf.write("\2\u016b\u016c\7^\2\2\u016c\u016d\7$\2\2\u016dN\3\2\2")
        buf.write("\2\u016e\u016f\7-\2\2\u016fP\3\2\2\2\u0170\u0171\7/\2")
        buf.write("\2\u0171R\3\2\2\2\u0172\u0173\7,\2\2\u0173T\3\2\2\2\u0174")
        buf.write("\u0175\7\61\2\2\u0175V\3\2\2\2\u0176\u0177\7\'\2\2\u0177")
        buf.write("X\3\2\2\2\u0178\u0179\7>\2\2\u0179Z\3\2\2\2\u017a\u017b")
        buf.write("\7@\2\2\u017b\\\3\2\2\2\u017c\u017d\7>\2\2\u017d\u017e")
        buf.write("\7?\2\2\u017e^\3\2\2\2\u017f\u0180\7@\2\2\u0180\u0181")
        buf.write("\7?\2\2\u0181`\3\2\2\2\u0182\u0183\7#\2\2\u0183b\3\2\2")
        buf.write("\2\u0184\u0185\7(\2\2\u0185\u0186\7(\2\2\u0186d\3\2\2")
        buf.write("\2\u0187\u0188\7~\2\2\u0188\u0189\7~\2\2\u0189f\3\2\2")
        buf.write("\2\u018a\u018b\7?\2\2\u018b\u018c\7?\2\2\u018ch\3\2\2")
        buf.write("\2\u018d\u018e\7#\2\2\u018e\u018f\7?\2\2\u018fj\3\2\2")
        buf.write("\2\u0190\u0191\7<\2\2\u0191\u0192\7<\2\2\u0192l\3\2\2")
        buf.write("\2\u0193\u0194\7\60\2\2\u0194n\3\2\2\2\u0195\u0196\7.")
        buf.write("\2\2\u0196p\3\2\2\2\u0197\u0198\7=\2\2\u0198r\3\2\2\2")
        buf.write("\u0199\u019a\7?\2\2\u019at\3\2\2\2\u019b\u019c\7<\2\2")
        buf.write("\u019cv\3\2\2\2\u019d\u019e\7*\2\2\u019ex\3\2\2\2\u019f")
        buf.write("\u01a0\7+\2\2\u01a0z\3\2\2\2\u01a1\u01a2\7]\2\2\u01a2")
        buf.write("|\3\2\2\2\u01a3\u01a4\7_\2\2\u01a4~\3\2\2\2\u01a5\u01a6")
        buf.write("\7}\2\2\u01a6\u0080\3\2\2\2\u01a7\u01a8\7\177\2\2\u01a8")
        buf.write("\u0082\3\2\2\2\u01a9\u01ab\t\16\2\2\u01aa\u01a9\3\2\2")
        buf.write("\2\u01ab\u01ac\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad")
        buf.write("\3\2\2\2\u01ad\u01b1\3\2\2\2\u01ae\u01b0\t\17\2\2\u01af")
        buf.write("\u01ae\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2")
        buf.write("\u01b1\u01b2\3\2\2\2\u01b2\u0084\3\2\2\2\u01b3\u01b1\3")
        buf.write("\2\2\2\u01b4\u01b7\5\37\20\2\u01b5\u01b7\5#\22\2\u01b6")
        buf.write("\u01b4\3\2\2\2\u01b6\u01b5\3\2\2\2\u01b7\u0086\3\2\2\2")
        buf.write("\u01b8\u01ba\t\20\2\2\u01b9\u01b8\3\2\2\2\u01ba\u01bb")
        buf.write("\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc")
        buf.write("\u01bd\3\2\2\2\u01bd\u01be\bD\2\2\u01be\u0088\3\2\2\2")
        buf.write("\u01bf\u01c4\7$\2\2\u01c0\u01c3\n\6\2\2\u01c1\u01c3\5")
        buf.write("\61\31\2\u01c2\u01c0\3\2\2\2\u01c2\u01c1\3\2\2\2\u01c3")
        buf.write("\u01c6\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c4\u01c2\3\2\2\2")
        buf.write("\u01c5\u01c7\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c7\u01c8\b")
        buf.write("E\6\2\u01c8\u008a\3\2\2\2\u01c9\u01cc\n\6\2\2\u01ca\u01cc")
        buf.write("\5\61\31\2\u01cb\u01c9\3\2\2\2\u01cb\u01ca\3\2\2\2\u01cc")
        buf.write("\u01cf\3\2\2\2\u01cd\u01ce\3\2\2\2\u01cd\u01cb\3\2\2\2")
        buf.write("\u01ce\u01d0\3\2\2\2\u01cf\u01cd\3\2\2\2\u01d0\u01d1\7")
        buf.write("$\2\2\u01d1\u01d2\bF\7\2\u01d2\u008c\3\2\2\2\u01d3\u01d4")
        buf.write("\13\2\2\2\u01d4\u01d5\bG\b\2\u01d5\u008e\3\2\2\2!\2\u00c1")
        buf.write("\u00cb\u00d4\u00df\u00e6\u00ea\u00ee\u00f6\u00fd\u0103")
        buf.write("\u0106\u010b\u0112\u0116\u0126\u0128\u0134\u013c\u0142")
        buf.write("\u0149\u0150\u0159\u01ac\u01b1\u01b6\u01bb\u01c2\u01c4")
        buf.write("\u01cb\u01cd\t\b\2\2\3\20\2\3\22\3\3\30\4\3E\5\3F\6\3")
        buf.write("G\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

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
    T__9 = 10
    T__10 = 11
    COMMENT = 12
    INTEGER_LIT = 13
    FLOAT_LIT = 14
    BOOLEAN_LIT = 15
    STRING_LIT = 16
    ARRAY_LIT = 17
    IDENTIFIER = 18
    NUMBER = 19
    WS = 20
    UNCLOSE_STRING = 21
    ILLEGAL_ESCAPE = 22
    ERROR_CHAR = 23

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "'array'", "'['", "']'", "'of'", "'integer'", "'float'", 
            "'boolean'", "'string'", "';'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "INTEGER_LIT", "FLOAT_LIT", "BOOLEAN_LIT", "STRING_LIT", 
            "ARRAY_LIT", "IDENTIFIER", "NUMBER", "WS", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "COMMENT", "SingleLineComment", 
                  "MultiLineComment", "INTEGER_LIT", "UNDERSCORE", "FLOAT_LIT", 
                  "DECPART", "EXPPART", "BOOLEAN_LIT", "FALSE", "TRUE", 
                  "STRING_LIT", "SUBSTRING", "ARRAY_LIT", "EXPS", "NUMLIST", 
                  "STRINGLIST", "Escape_Sequence", "DUO_QUOTE", "SINGLE_QUOTE", 
                  "BackSpace", "FormFeed", "CarriageReturn", "NewLine", 
                  "SingleQuote", "BackSlash", "Dou_quote", "PLUS", "MINUS", 
                  "MUL", "DIV", "MOD", "LESS", "GREATER", "LESS_THAN_OR_EQUAL", 
                  "GREATER_THAN_OR_EQUAL", "NOT", "AND", "OR", "EQUAL_TO", 
                  "NOT_EQUAL", "SCOPE_RES", "PERIOD", "COMMA", "SEMI", "EQUAL", 
                  "COLON", "LB", "RB", "LSB", "RSB", "LCB", "RCB", "IDENTIFIER", 
                  "NUMBER", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[14] = self.INTEGER_LIT_action 
            actions[16] = self.FLOAT_LIT_action 
            actions[22] = self.STRING_LIT_action 
            actions[67] = self.UNCLOSE_STRING_action 
            actions[68] = self.ILLEGAL_ESCAPE_action 
            actions[69] = self.ERROR_CHAR_action 
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
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text=self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise UncloseString(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise IllegalEscape(self.text)
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


