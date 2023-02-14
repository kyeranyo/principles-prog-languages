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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2%")
        buf.write("\u0209\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\5\2\u009c\n\2\3\3\3\3\3\3\3\3\7\3\u00a2\n\3")
        buf.write("\f\3\16\3\u00a5\13\3\3\4\3\4\3\4\3\4\7\4\u00ab\n\4\f\4")
        buf.write("\16\4\u00ae\13\4\3\4\3\4\3\4\3\5\6\5\u00b4\n\5\r\5\16")
        buf.write("\5\u00b5\3\5\7\5\u00b9\n\5\f\5\16\5\u00bc\13\5\3\6\6\6")
        buf.write("\u00bf\n\6\r\6\16\6\u00c0\3\7\3\7\3\7\7\7\u00c6\n\7\f")
        buf.write("\7\16\7\u00c9\13\7\3\7\3\7\6\7\u00cd\n\7\r\7\16\7\u00ce")
        buf.write("\7\7\u00d1\n\7\f\7\16\7\u00d4\13\7\3\7\5\7\u00d7\n\7\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\5\t\u00df\n\t\3\n\3\n\3\n\6\n\u00e4")
        buf.write("\n\n\r\n\16\n\u00e5\3\n\3\n\7\n\u00ea\n\n\f\n\16\n\u00ed")
        buf.write("\13\n\5\n\u00ef\n\n\3\13\6\13\u00f2\n\13\r\13\16\13\u00f3")
        buf.write("\3\13\3\13\3\13\6\13\u00f9\n\13\r\13\16\13\u00fa\3\f\3")
        buf.write("\f\5\f\u00ff\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\7\17\u010f\n\17\f\17\16\17\u0112")
        buf.write("\13\17\3\17\3\17\3\20\3\20\3\20\3\20\7\20\u011a\n\20\f")
        buf.write("\20\16\20\u011d\13\20\3\20\3\20\3\20\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\5\21\u0129\n\21\3\22\3\22\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\33\3\33\3\33\5\33\u0141\n\33\3")
        buf.write("\33\3\33\3\33\5\33\u0146\n\33\7\33\u0148\n\33\f\33\16")
        buf.write("\33\u014b\13\33\5\33\u014d\n\33\3\33\3\33\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3")
        buf.write("%\3%\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*")
        buf.write("\3+\3+\3+\3+\3+\3,\3,\3,\3-\3-\3-\3-\3-\3-\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67")
        buf.write("\3\67\38\38\38\39\39\3:\3:\3;\3;\3;\3<\3<\3<\3=\3=\3=")
        buf.write("\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3")
        buf.write("F\3G\3G\3H\3H\3I\6I\u01fd\nI\rI\16I\u01fe\3I\3I\3J\3J")
        buf.write("\3J\3K\3K\3L\3L\5\u00ac\u0110\u011b\2M\3\3\5\2\7\2\t\2")
        buf.write("\13\2\r\4\17\2\21\5\23\2\25\2\27\6\31\2\33\2\35\7\37\2")
        buf.write("!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63\2\65\b\67\t9\n;\13=")
        buf.write("\f?\rA\16C\17E\20G\21I\22K\23M\24O\25Q\26S\27U\30W\31")
        buf.write("Y\32[\33]\2_\2a\2c\2e\2g\2i\2k\2m\2o\2q\2s\2u\2w\2y\2")
        buf.write("{\34}\35\177\36\u0081\37\u0083 \u0085!\u0087\2\u0089\2")
        buf.write("\u008b\2\u008d\2\u008f\2\u0091\"\u0093#\u0095$\u0097%")
        buf.write("\3\2\21\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\62")
        buf.write(";\3\2\63;\4\2GGgg\4\2$$^^\3\2$$\3\2))\3\2\n\n\3\2\16\16")
        buf.write("\3\2\17\17\3\2\f\f\3\2^^\5\2\13\f\17\17\"\"\2\u01ff\2")
        buf.write("\3\3\2\2\2\2\r\3\2\2\2\2\21\3\2\2\2\2\27\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2")
        buf.write("\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\3\u009b\3\2\2\2\5\u009d\3\2\2\2\7\u00a6\3\2\2\2\t\u00b3")
        buf.write("\3\2\2\2\13\u00be\3\2\2\2\r\u00d6\3\2\2\2\17\u00d8\3\2")
        buf.write("\2\2\21\u00de\3\2\2\2\23\u00e0\3\2\2\2\25\u00f1\3\2\2")
        buf.write("\2\27\u00fe\3\2\2\2\31\u0100\3\2\2\2\33\u0106\3\2\2\2")
        buf.write("\35\u010b\3\2\2\2\37\u0115\3\2\2\2!\u0128\3\2\2\2#\u012a")
        buf.write("\3\2\2\2%\u012c\3\2\2\2\'\u012e\3\2\2\2)\u0130\3\2\2\2")
        buf.write("+\u0132\3\2\2\2-\u0134\3\2\2\2/\u0136\3\2\2\2\61\u0138")
        buf.write("\3\2\2\2\63\u013a\3\2\2\2\65\u013d\3\2\2\2\67\u0150\3")
        buf.write("\2\2\29\u0155\3\2\2\2;\u015b\3\2\2\2=\u0163\3\2\2\2?\u0168")
        buf.write("\3\2\2\2A\u016e\3\2\2\2C\u0174\3\2\2\2E\u017b\3\2\2\2")
        buf.write("G\u017f\3\2\2\2I\u0187\3\2\2\2K\u018b\3\2\2\2M\u0192\3")
        buf.write("\2\2\2O\u019b\3\2\2\2Q\u019e\3\2\2\2S\u01a7\3\2\2\2U\u01aa")
        buf.write("\3\2\2\2W\u01af\3\2\2\2Y\u01b2\3\2\2\2[\u01b8\3\2\2\2")
        buf.write("]\u01c0\3\2\2\2_\u01c2\3\2\2\2a\u01c4\3\2\2\2c\u01c6\3")
        buf.write("\2\2\2e\u01c8\3\2\2\2g\u01ca\3\2\2\2i\u01cc\3\2\2\2k\u01cf")
        buf.write("\3\2\2\2m\u01d2\3\2\2\2o\u01d5\3\2\2\2q\u01d8\3\2\2\2")
        buf.write("s\u01da\3\2\2\2u\u01dc\3\2\2\2w\u01df\3\2\2\2y\u01e2\3")
        buf.write("\2\2\2{\u01e5\3\2\2\2}\u01e7\3\2\2\2\177\u01e9\3\2\2\2")
        buf.write("\u0081\u01eb\3\2\2\2\u0083\u01ed\3\2\2\2\u0085\u01ef\3")
        buf.write("\2\2\2\u0087\u01f1\3\2\2\2\u0089\u01f3\3\2\2\2\u008b\u01f5")
        buf.write("\3\2\2\2\u008d\u01f7\3\2\2\2\u008f\u01f9\3\2\2\2\u0091")
        buf.write("\u01fc\3\2\2\2\u0093\u0202\3\2\2\2\u0095\u0205\3\2\2\2")
        buf.write("\u0097\u0207\3\2\2\2\u0099\u009c\5\5\3\2\u009a\u009c\5")
        buf.write("\7\4\2\u009b\u0099\3\2\2\2\u009b\u009a\3\2\2\2\u009c\4")
        buf.write("\3\2\2\2\u009d\u009e\7\61\2\2\u009e\u009f\7\61\2\2\u009f")
        buf.write("\u00a3\3\2\2\2\u00a0\u00a2\n\2\2\2\u00a1\u00a0\3\2\2\2")
        buf.write("\u00a2\u00a5\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3")
        buf.write("\2\2\2\u00a4\6\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a7")
        buf.write("\7\61\2\2\u00a7\u00a8\7,\2\2\u00a8\u00ac\3\2\2\2\u00a9")
        buf.write("\u00ab\13\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\u00ae\3\2\2")
        buf.write("\2\u00ac\u00ad\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ad\u00af")
        buf.write("\3\2\2\2\u00ae\u00ac\3\2\2\2\u00af\u00b0\7,\2\2\u00b0")
        buf.write("\u00b1\7\61\2\2\u00b1\b\3\2\2\2\u00b2\u00b4\t\3\2\2\u00b3")
        buf.write("\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b3\3\2\2\2")
        buf.write("\u00b5\u00b6\3\2\2\2\u00b6\u00ba\3\2\2\2\u00b7\u00b9\t")
        buf.write("\4\2\2\u00b8\u00b7\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8")
        buf.write("\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\n\3\2\2\2\u00bc\u00ba")
        buf.write("\3\2\2\2\u00bd\u00bf\t\5\2\2\u00be\u00bd\3\2\2\2\u00bf")
        buf.write("\u00c0\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2")
        buf.write("\u00c1\f\3\2\2\2\u00c2\u00d7\7\62\2\2\u00c3\u00c7\t\6")
        buf.write("\2\2\u00c4\u00c6\t\5\2\2\u00c5\u00c4\3\2\2\2\u00c6\u00c9")
        buf.write("\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8")
        buf.write("\u00d2\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca\u00cc\5\17\b")
        buf.write("\2\u00cb\u00cd\t\5\2\2\u00cc\u00cb\3\2\2\2\u00cd\u00ce")
        buf.write("\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf")
        buf.write("\u00d1\3\2\2\2\u00d0\u00ca\3\2\2\2\u00d1\u00d4\3\2\2\2")
        buf.write("\u00d2\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d5\3")
        buf.write("\2\2\2\u00d4\u00d2\3\2\2\2\u00d5\u00d7\b\7\2\2\u00d6\u00c2")
        buf.write("\3\2\2\2\u00d6\u00c3\3\2\2\2\u00d7\16\3\2\2\2\u00d8\u00d9")
        buf.write("\7a\2\2\u00d9\20\3\2\2\2\u00da\u00df\5\25\13\2\u00db\u00dc")
        buf.write("\5\23\n\2\u00dc\u00dd\b\t\3\2\u00dd\u00df\3\2\2\2\u00de")
        buf.write("\u00da\3\2\2\2\u00de\u00db\3\2\2\2\u00df\22\3\2\2\2\u00e0")
        buf.write("\u00e1\5\r\7\2\u00e1\u00e3\5\u0087D\2\u00e2\u00e4\t\5")
        buf.write("\2\2\u00e3\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e3")
        buf.write("\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00ee\3\2\2\2\u00e7")
        buf.write("\u00eb\t\7\2\2\u00e8\u00ea\t\5\2\2\u00e9\u00e8\3\2\2\2")
        buf.write("\u00ea\u00ed\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3")
        buf.write("\2\2\2\u00ec\u00ef\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00e7")
        buf.write("\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\24\3\2\2\2\u00f0\u00f2")
        buf.write("\t\5\2\2\u00f1\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3")
        buf.write("\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f5\3\2\2\2")
        buf.write("\u00f5\u00f6\t\7\2\2\u00f6\u00f8\5_\60\2\u00f7\u00f9\t")
        buf.write("\5\2\2\u00f8\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00f8")
        buf.write("\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\26\3\2\2\2\u00fc\u00ff")
        buf.write("\5\31\r\2\u00fd\u00ff\5\33\16\2\u00fe\u00fc\3\2\2\2\u00fe")
        buf.write("\u00fd\3\2\2\2\u00ff\30\3\2\2\2\u0100\u0101\7h\2\2\u0101")
        buf.write("\u0102\7c\2\2\u0102\u0103\7n\2\2\u0103\u0104\7u\2\2\u0104")
        buf.write("\u0105\7g\2\2\u0105\32\3\2\2\2\u0106\u0107\7v\2\2\u0107")
        buf.write("\u0108\7t\2\2\u0108\u0109\7w\2\2\u0109\u010a\7g\2\2\u010a")
        buf.write("\34\3\2\2\2\u010b\u0110\5#\22\2\u010c\u010f\n\b\2\2\u010d")
        buf.write("\u010f\5\37\20\2\u010e\u010c\3\2\2\2\u010e\u010d\3\2\2")
        buf.write("\2\u010f\u0112\3\2\2\2\u0110\u0111\3\2\2\2\u0110\u010e")
        buf.write("\3\2\2\2\u0111\u0113\3\2\2\2\u0112\u0110\3\2\2\2\u0113")
        buf.write("\u0114\5#\22\2\u0114\36\3\2\2\2\u0115\u0116\7^\2\2\u0116")
        buf.write("\u0117\7$\2\2\u0117\u011b\3\2\2\2\u0118\u011a\n\t\2\2")
        buf.write("\u0119\u0118\3\2\2\2\u011a\u011d\3\2\2\2\u011b\u011c\3")
        buf.write("\2\2\2\u011b\u0119\3\2\2\2\u011c\u011e\3\2\2\2\u011d\u011b")
        buf.write("\3\2\2\2\u011e\u011f\7^\2\2\u011f\u0120\7$\2\2\u0120 ")
        buf.write("\3\2\2\2\u0121\u0129\5\'\24\2\u0122\u0129\5)\25\2\u0123")
        buf.write("\u0129\5+\26\2\u0124\u0129\5-\27\2\u0125\u0129\5/\30\2")
        buf.write("\u0126\u0129\5\63\32\2\u0127\u0129\5\61\31\2\u0128\u0121")
        buf.write("\3\2\2\2\u0128\u0122\3\2\2\2\u0128\u0123\3\2\2\2\u0128")
        buf.write("\u0124\3\2\2\2\u0128\u0125\3\2\2\2\u0128\u0126\3\2\2\2")
        buf.write("\u0128\u0127\3\2\2\2\u0129\"\3\2\2\2\u012a\u012b\t\t\2")
        buf.write("\2\u012b$\3\2\2\2\u012c\u012d\t\n\2\2\u012d&\3\2\2\2\u012e")
        buf.write("\u012f\t\13\2\2\u012f(\3\2\2\2\u0130\u0131\t\f\2\2\u0131")
        buf.write("*\3\2\2\2\u0132\u0133\t\r\2\2\u0133,\3\2\2\2\u0134\u0135")
        buf.write("\t\16\2\2\u0135.\3\2\2\2\u0136\u0137\7)\2\2\u0137\60\3")
        buf.write("\2\2\2\u0138\u0139\t\17\2\2\u0139\62\3\2\2\2\u013a\u013b")
        buf.write("\7^\2\2\u013b\u013c\7$\2\2\u013c\64\3\2\2\2\u013d\u014c")
        buf.write("\5\u0083B\2\u013e\u0141\5\13\6\2\u013f\u0141\5\t\5\2\u0140")
        buf.write("\u013e\3\2\2\2\u0140\u013f\3\2\2\2\u0141\u0149\3\2\2\2")
        buf.write("\u0142\u0145\5\u0089E\2\u0143\u0146\5\13\6\2\u0144\u0146")
        buf.write("\5\t\5\2\u0145\u0143\3\2\2\2\u0145\u0144\3\2\2\2\u0146")
        buf.write("\u0148\3\2\2\2\u0147\u0142\3\2\2\2\u0148\u014b\3\2\2\2")
        buf.write("\u0149\u0147\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014d\3")
        buf.write("\2\2\2\u014b\u0149\3\2\2\2\u014c\u0140\3\2\2\2\u014c\u014d")
        buf.write("\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u014f\5\u0085C\2\u014f")
        buf.write("\66\3\2\2\2\u0150\u0151\7c\2\2\u0151\u0152\7w\2\2\u0152")
        buf.write("\u0153\7v\2\2\u0153\u0154\7q\2\2\u01548\3\2\2\2\u0155")
        buf.write("\u0156\7d\2\2\u0156\u0157\7t\2\2\u0157\u0158\7g\2\2\u0158")
        buf.write("\u0159\7c\2\2\u0159\u015a\7m\2\2\u015a:\3\2\2\2\u015b")
        buf.write("\u015c\7k\2\2\u015c\u015d\7p\2\2\u015d\u015e\7v\2\2\u015e")
        buf.write("\u015f\7g\2\2\u015f\u0160\7i\2\2\u0160\u0161\7g\2\2\u0161")
        buf.write("\u0162\7t\2\2\u0162<\3\2\2\2\u0163\u0164\7x\2\2\u0164")
        buf.write("\u0165\7q\2\2\u0165\u0166\7k\2\2\u0166\u0167\7f\2\2\u0167")
        buf.write(">\3\2\2\2\u0168\u0169\7c\2\2\u0169\u016a\7t\2\2\u016a")
        buf.write("\u016b\7t\2\2\u016b\u016c\7c\2\2\u016c\u016d\7{\2\2\u016d")
        buf.write("@\3\2\2\2\u016e\u016f\7h\2\2\u016f\u0170\7n\2\2\u0170")
        buf.write("\u0171\7q\2\2\u0171\u0172\7c\2\2\u0172\u0173\7v\2\2\u0173")
        buf.write("B\3\2\2\2\u0174\u0175\7t\2\2\u0175\u0176\7g\2\2\u0176")
        buf.write("\u0177\7v\2\2\u0177\u0178\7w\2\2\u0178\u0179\7t\2\2\u0179")
        buf.write("\u017a\7p\2\2\u017aD\3\2\2\2\u017b\u017c\7q\2\2\u017c")
        buf.write("\u017d\7w\2\2\u017d\u017e\7v\2\2\u017eF\3\2\2\2\u017f")
        buf.write("\u0180\7d\2\2\u0180\u0181\7q\2\2\u0181\u0182\7q\2\2\u0182")
        buf.write("\u0183\7n\2\2\u0183\u0184\7g\2\2\u0184\u0185\7c\2\2\u0185")
        buf.write("\u0186\7p\2\2\u0186H\3\2\2\2\u0187\u0188\7h\2\2\u0188")
        buf.write("\u0189\7q\2\2\u0189\u018a\7t\2\2\u018aJ\3\2\2\2\u018b")
        buf.write("\u018c\7u\2\2\u018c\u018d\7v\2\2\u018d\u018e\7t\2\2\u018e")
        buf.write("\u018f\7k\2\2\u018f\u0190\7p\2\2\u0190\u0191\7i\2\2\u0191")
        buf.write("L\3\2\2\2\u0192\u0193\7e\2\2\u0193\u0194\7q\2\2\u0194")
        buf.write("\u0195\7p\2\2\u0195\u0196\7v\2\2\u0196\u0197\7k\2\2\u0197")
        buf.write("\u0198\7p\2\2\u0198\u0199\7w\2\2\u0199\u019a\7g\2\2\u019a")
        buf.write("N\3\2\2\2\u019b\u019c\7f\2\2\u019c\u019d\7q\2\2\u019d")
        buf.write("P\3\2\2\2\u019e\u019f\7h\2\2\u019f\u01a0\7w\2\2\u01a0")
        buf.write("\u01a1\7p\2\2\u01a1\u01a2\7e\2\2\u01a2\u01a3\7v\2\2\u01a3")
        buf.write("\u01a4\7k\2\2\u01a4\u01a5\7q\2\2\u01a5\u01a6\7p\2\2\u01a6")
        buf.write("R\3\2\2\2\u01a7\u01a8\7q\2\2\u01a8\u01a9\7h\2\2\u01a9")
        buf.write("T\3\2\2\2\u01aa\u01ab\7g\2\2\u01ab\u01ac\7n\2\2\u01ac")
        buf.write("\u01ad\7u\2\2\u01ad\u01ae\7g\2\2\u01aeV\3\2\2\2\u01af")
        buf.write("\u01b0\7k\2\2\u01b0\u01b1\7h\2\2\u01b1X\3\2\2\2\u01b2")
        buf.write("\u01b3\7y\2\2\u01b3\u01b4\7j\2\2\u01b4\u01b5\7k\2\2\u01b5")
        buf.write("\u01b6\7n\2\2\u01b6\u01b7\7g\2\2\u01b7Z\3\2\2\2\u01b8")
        buf.write("\u01b9\7k\2\2\u01b9\u01ba\7p\2\2\u01ba\u01bb\7j\2\2\u01bb")
        buf.write("\u01bc\7g\2\2\u01bc\u01bd\7t\2\2\u01bd\u01be\7k\2\2\u01be")
        buf.write("\u01bf\7v\2\2\u01bf\\\3\2\2\2\u01c0\u01c1\7-\2\2\u01c1")
        buf.write("^\3\2\2\2\u01c2\u01c3\7/\2\2\u01c3`\3\2\2\2\u01c4\u01c5")
        buf.write("\7,\2\2\u01c5b\3\2\2\2\u01c6\u01c7\7\61\2\2\u01c7d\3\2")
        buf.write("\2\2\u01c8\u01c9\7\'\2\2\u01c9f\3\2\2\2\u01ca\u01cb\7")
        buf.write("#\2\2\u01cbh\3\2\2\2\u01cc\u01cd\7(\2\2\u01cd\u01ce\7")
        buf.write("(\2\2\u01cej\3\2\2\2\u01cf\u01d0\7~\2\2\u01d0\u01d1\7")
        buf.write("~\2\2\u01d1l\3\2\2\2\u01d2\u01d3\7?\2\2\u01d3\u01d4\7")
        buf.write("?\2\2\u01d4n\3\2\2\2\u01d5\u01d6\7#\2\2\u01d6\u01d7\7")
        buf.write("?\2\2\u01d7p\3\2\2\2\u01d8\u01d9\7>\2\2\u01d9r\3\2\2\2")
        buf.write("\u01da\u01db\7@\2\2\u01dbt\3\2\2\2\u01dc\u01dd\7>\2\2")
        buf.write("\u01dd\u01de\7?\2\2\u01dev\3\2\2\2\u01df\u01e0\7@\2\2")
        buf.write("\u01e0\u01e1\7?\2\2\u01e1x\3\2\2\2\u01e2\u01e3\7<\2\2")
        buf.write("\u01e3\u01e4\7<\2\2\u01e4z\3\2\2\2\u01e5\u01e6\7*\2\2")
        buf.write("\u01e6|\3\2\2\2\u01e7\u01e8\7+\2\2\u01e8~\3\2\2\2\u01e9")
        buf.write("\u01ea\7]\2\2\u01ea\u0080\3\2\2\2\u01eb\u01ec\7_\2\2\u01ec")
        buf.write("\u0082\3\2\2\2\u01ed\u01ee\7}\2\2\u01ee\u0084\3\2\2\2")
        buf.write("\u01ef\u01f0\7\177\2\2\u01f0\u0086\3\2\2\2\u01f1\u01f2")
        buf.write("\7\60\2\2\u01f2\u0088\3\2\2\2\u01f3\u01f4\7.\2\2\u01f4")
        buf.write("\u008a\3\2\2\2\u01f5\u01f6\7=\2\2\u01f6\u008c\3\2\2\2")
        buf.write("\u01f7\u01f8\7?\2\2\u01f8\u008e\3\2\2\2\u01f9\u01fa\7")
        buf.write("<\2\2\u01fa\u0090\3\2\2\2\u01fb\u01fd\t\20\2\2\u01fc\u01fb")
        buf.write("\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe")
        buf.write("\u01ff\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0201\bI\4\2")
        buf.write("\u0201\u0092\3\2\2\2\u0202\u0203\13\2\2\2\u0203\u0204")
        buf.write("\bJ\5\2\u0204\u0094\3\2\2\2\u0205\u0206\13\2\2\2\u0206")
        buf.write("\u0096\3\2\2\2\u0207\u0208\13\2\2\2\u0208\u0098\3\2\2")
        buf.write("\2\35\2\u009b\u00a3\u00ac\u00b5\u00ba\u00c0\u00c7\u00ce")
        buf.write("\u00d2\u00d6\u00de\u00e5\u00eb\u00ee\u00f3\u00fa\u00fe")
        buf.write("\u010e\u0110\u011b\u0128\u0140\u0145\u0149\u014c\u01fe")
        buf.write("\6\3\7\2\3\t\3\b\2\2\3J\4")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    INTEGER_LIT = 2
    FLOAT_LIT = 3
    BOOLEAN_LIT = 4
    STRING_LIT = 5
    ARRAY_LIT = 6
    AUTO = 7
    BREAK = 8
    INTEGER = 9
    VOID = 10
    ARRAY = 11
    FLOAT = 12
    RETURN = 13
    OUT = 14
    BOOLEAN = 15
    FOR = 16
    STRING = 17
    CONTINUE = 18
    DO = 19
    FUNCTION = 20
    OF = 21
    ELSE = 22
    IF = 23
    WHILE = 24
    INHERIT = 25
    LB = 26
    RB = 27
    LSB = 28
    RSB = 29
    LCB = 30
    RCB = 31
    WS = 32
    ERROR_CHAR = 33
    UNCLOSE_STRING = 34
    ILLEGAL_ESCAPE = 35

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'integer'", "'void'", "'array'", "'float'", 
            "'return'", "'out'", "'boolean'", "'for'", "'string'", "'continue'", 
            "'do'", "'function'", "'of'", "'else'", "'if'", "'while'", "'inherit'", 
            "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "INTEGER_LIT", "FLOAT_LIT", "BOOLEAN_LIT", "STRING_LIT", 
            "ARRAY_LIT", "AUTO", "BREAK", "INTEGER", "VOID", "ARRAY", "FLOAT", 
            "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", 
            "FUNCTION", "OF", "ELSE", "IF", "WHILE", "INHERIT", "LB", "RB", 
            "LSB", "RSB", "LCB", "RCB", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMMENT", "SingleLineComment", "MultiLineComment", "IDENTIFIER", 
                  "NUMBER", "INTEGER_LIT", "UNDERSCORE", "FLOAT_LIT", "DECPART", 
                  "EXPPART", "BOOLEAN_LIT", "FALSE", "TRUE", "STRING_LIT", 
                  "SubString", "Escape_Sequence", "DUO_QUOTE", "SINGLE_QUOTE", 
                  "BackSpace", "FormFeed", "CarriageReturn", "NewLine", 
                  "SingleQuote", "BackSlash", "Dou_quote", "ARRAY_LIT", 
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
            actions[5] = self.INTEGER_LIT_action 
            actions[7] = self.FLOAT_LIT_action 
            actions[72] = self.ERROR_CHAR_action 
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
     


