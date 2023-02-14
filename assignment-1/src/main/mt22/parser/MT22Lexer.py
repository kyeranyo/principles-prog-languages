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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2$")
        buf.write("\u01ed\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\5")
        buf.write("\2\u0098\n\2\3\3\3\3\3\3\3\3\7\3\u009e\n\3\f\3\16\3\u00a1")
        buf.write("\13\3\3\4\3\4\3\4\3\4\7\4\u00a7\n\4\f\4\16\4\u00aa\13")
        buf.write("\4\3\4\3\4\3\4\3\5\6\5\u00b0\n\5\r\5\16\5\u00b1\3\5\7")
        buf.write("\5\u00b5\n\5\f\5\16\5\u00b8\13\5\3\6\3\6\3\6\7\6\u00bd")
        buf.write("\n\6\f\6\16\6\u00c0\13\6\3\6\3\6\6\6\u00c4\n\6\r\6\16")
        buf.write("\6\u00c5\7\6\u00c8\n\6\f\6\16\6\u00cb\13\6\3\6\5\6\u00ce")
        buf.write("\n\6\3\7\3\7\3\b\3\b\3\b\3\b\5\b\u00d6\n\b\3\t\3\t\3\t")
        buf.write("\6\t\u00db\n\t\r\t\16\t\u00dc\3\t\3\t\7\t\u00e1\n\t\f")
        buf.write("\t\16\t\u00e4\13\t\5\t\u00e6\n\t\3\n\6\n\u00e9\n\n\r\n")
        buf.write("\16\n\u00ea\3\n\3\n\3\n\6\n\u00f0\n\n\r\n\16\n\u00f1\3")
        buf.write("\13\3\13\5\13\u00f6\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\16\3\16\3\16\7\16\u0106\n\16\f\16\16")
        buf.write("\16\u0109\13\16\3\16\3\16\3\17\3\17\3\17\3\17\7\17\u0111")
        buf.write("\n\17\f\17\16\17\u0114\13\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\5\20\u0120\n\20\3\21\3\21\3")
        buf.write("\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3+\3+")
        buf.write("\3,\3,\3,\3,\3,\3,\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3")
        buf.write("\61\3\61\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\67\3\67\38\38\39\39\39\3:")
        buf.write("\3:\3:\3;\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3")
        buf.write("B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\6G\u01e1\nG\rG\16G\u01e2")
        buf.write("\3G\3G\3H\3H\3H\3I\3I\3J\3J\5\u00a8\u0107\u0112\2K\3\3")
        buf.write("\5\2\7\2\t\2\13\4\r\2\17\5\21\2\23\2\25\6\27\2\31\2\33")
        buf.write("\7\35\2\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63\b\65\t\67")
        buf.write("\n9\13;\f=\r?\16A\17C\20E\21G\22I\23K\24M\25O\26Q\27S")
        buf.write("\30U\31W\32Y\2[\2]\2_\2a\2c\2e\2g\2i\2k\2m\2o\2q\2s\2")
        buf.write("u\2w\33y\34{\35}\36\177\37\u0081 \u0083\2\u0085\2\u0087")
        buf.write("\2\u0089\2\u008b\2\u008d!\u008f\"\u0091#\u0093$\3\2\21")
        buf.write("\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62")
        buf.write(";\4\2GGgg\4\2$$^^\3\2$$\3\2))\3\2\n\n\3\2\16\16\3\2\17")
        buf.write("\17\3\2\f\f\3\2^^\5\2\13\f\17\17\"\"\2\u01df\2\3\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\17\3\2\2\2\2\25\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;")
        buf.write("\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2")
        buf.write("E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2")
        buf.write("\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2")
        buf.write("\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write("\2\2\2\2\u0081\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2")
        buf.write("\2\u0091\3\2\2\2\2\u0093\3\2\2\2\3\u0097\3\2\2\2\5\u0099")
        buf.write("\3\2\2\2\7\u00a2\3\2\2\2\t\u00af\3\2\2\2\13\u00cd\3\2")
        buf.write("\2\2\r\u00cf\3\2\2\2\17\u00d5\3\2\2\2\21\u00d7\3\2\2\2")
        buf.write("\23\u00e8\3\2\2\2\25\u00f5\3\2\2\2\27\u00f7\3\2\2\2\31")
        buf.write("\u00fd\3\2\2\2\33\u0102\3\2\2\2\35\u010c\3\2\2\2\37\u011f")
        buf.write("\3\2\2\2!\u0121\3\2\2\2#\u0123\3\2\2\2%\u0125\3\2\2\2")
        buf.write("\'\u0127\3\2\2\2)\u0129\3\2\2\2+\u012b\3\2\2\2-\u012d")
        buf.write("\3\2\2\2/\u012f\3\2\2\2\61\u0131\3\2\2\2\63\u0134\3\2")
        buf.write("\2\2\65\u0139\3\2\2\2\67\u013f\3\2\2\29\u0147\3\2\2\2")
        buf.write(";\u014c\3\2\2\2=\u0152\3\2\2\2?\u0158\3\2\2\2A\u015f\3")
        buf.write("\2\2\2C\u0163\3\2\2\2E\u016b\3\2\2\2G\u016f\3\2\2\2I\u0176")
        buf.write("\3\2\2\2K\u017f\3\2\2\2M\u0182\3\2\2\2O\u018b\3\2\2\2")
        buf.write("Q\u018e\3\2\2\2S\u0193\3\2\2\2U\u0196\3\2\2\2W\u019c\3")
        buf.write("\2\2\2Y\u01a4\3\2\2\2[\u01a6\3\2\2\2]\u01a8\3\2\2\2_\u01aa")
        buf.write("\3\2\2\2a\u01ac\3\2\2\2c\u01ae\3\2\2\2e\u01b0\3\2\2\2")
        buf.write("g\u01b3\3\2\2\2i\u01b6\3\2\2\2k\u01b9\3\2\2\2m\u01bc\3")
        buf.write("\2\2\2o\u01be\3\2\2\2q\u01c0\3\2\2\2s\u01c3\3\2\2\2u\u01c6")
        buf.write("\3\2\2\2w\u01c9\3\2\2\2y\u01cb\3\2\2\2{\u01cd\3\2\2\2")
        buf.write("}\u01cf\3\2\2\2\177\u01d1\3\2\2\2\u0081\u01d3\3\2\2\2")
        buf.write("\u0083\u01d5\3\2\2\2\u0085\u01d7\3\2\2\2\u0087\u01d9\3")
        buf.write("\2\2\2\u0089\u01db\3\2\2\2\u008b\u01dd\3\2\2\2\u008d\u01e0")
        buf.write("\3\2\2\2\u008f\u01e6\3\2\2\2\u0091\u01e9\3\2\2\2\u0093")
        buf.write("\u01eb\3\2\2\2\u0095\u0098\5\5\3\2\u0096\u0098\5\7\4\2")
        buf.write("\u0097\u0095\3\2\2\2\u0097\u0096\3\2\2\2\u0098\4\3\2\2")
        buf.write("\2\u0099\u009a\7\61\2\2\u009a\u009b\7\61\2\2\u009b\u009f")
        buf.write("\3\2\2\2\u009c\u009e\n\2\2\2\u009d\u009c\3\2\2\2\u009e")
        buf.write("\u00a1\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2")
        buf.write("\u00a0\6\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u00a3\7\61")
        buf.write("\2\2\u00a3\u00a4\7,\2\2\u00a4\u00a8\3\2\2\2\u00a5\u00a7")
        buf.write("\13\2\2\2\u00a6\u00a5\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8")
        buf.write("\u00a9\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a9\u00ab\3\2\2\2")
        buf.write("\u00aa\u00a8\3\2\2\2\u00ab\u00ac\7,\2\2\u00ac\u00ad\7")
        buf.write("\61\2\2\u00ad\b\3\2\2\2\u00ae\u00b0\t\3\2\2\u00af\u00ae")
        buf.write("\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1")
        buf.write("\u00b2\3\2\2\2\u00b2\u00b6\3\2\2\2\u00b3\u00b5\t\4\2\2")
        buf.write("\u00b4\u00b3\3\2\2\2\u00b5\u00b8\3\2\2\2\u00b6\u00b4\3")
        buf.write("\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\n\3\2\2\2\u00b8\u00b6")
        buf.write("\3\2\2\2\u00b9\u00ce\7\62\2\2\u00ba\u00be\t\5\2\2\u00bb")
        buf.write("\u00bd\t\6\2\2\u00bc\u00bb\3\2\2\2\u00bd\u00c0\3\2\2\2")
        buf.write("\u00be\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c9\3")
        buf.write("\2\2\2\u00c0\u00be\3\2\2\2\u00c1\u00c3\5\r\7\2\u00c2\u00c4")
        buf.write("\t\6\2\2\u00c3\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5")
        buf.write("\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c8\3\2\2\2")
        buf.write("\u00c7\u00c1\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7\3")
        buf.write("\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cc\3\2\2\2\u00cb\u00c9")
        buf.write("\3\2\2\2\u00cc\u00ce\b\6\2\2\u00cd\u00b9\3\2\2\2\u00cd")
        buf.write("\u00ba\3\2\2\2\u00ce\f\3\2\2\2\u00cf\u00d0\7a\2\2\u00d0")
        buf.write("\16\3\2\2\2\u00d1\u00d6\5\23\n\2\u00d2\u00d3\5\21\t\2")
        buf.write("\u00d3\u00d4\b\b\3\2\u00d4\u00d6\3\2\2\2\u00d5\u00d1\3")
        buf.write("\2\2\2\u00d5\u00d2\3\2\2\2\u00d6\20\3\2\2\2\u00d7\u00d8")
        buf.write("\5\13\6\2\u00d8\u00da\5\u0083B\2\u00d9\u00db\t\6\2\2\u00da")
        buf.write("\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\u00da\3\2\2\2")
        buf.write("\u00dc\u00dd\3\2\2\2\u00dd\u00e5\3\2\2\2\u00de\u00e2\t")
        buf.write("\7\2\2\u00df\u00e1\t\6\2\2\u00e0\u00df\3\2\2\2\u00e1\u00e4")
        buf.write("\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3")
        buf.write("\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e5\u00de\3\2\2\2")
        buf.write("\u00e5\u00e6\3\2\2\2\u00e6\22\3\2\2\2\u00e7\u00e9\t\6")
        buf.write("\2\2\u00e8\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00e8")
        buf.write("\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec")
        buf.write("\u00ed\t\7\2\2\u00ed\u00ef\5[.\2\u00ee\u00f0\t\6\2\2\u00ef")
        buf.write("\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00ef\3\2\2\2")
        buf.write("\u00f1\u00f2\3\2\2\2\u00f2\24\3\2\2\2\u00f3\u00f6\5\27")
        buf.write("\f\2\u00f4\u00f6\5\31\r\2\u00f5\u00f3\3\2\2\2\u00f5\u00f4")
        buf.write("\3\2\2\2\u00f6\26\3\2\2\2\u00f7\u00f8\7h\2\2\u00f8\u00f9")
        buf.write("\7c\2\2\u00f9\u00fa\7n\2\2\u00fa\u00fb\7u\2\2\u00fb\u00fc")
        buf.write("\7g\2\2\u00fc\30\3\2\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff")
        buf.write("\7t\2\2\u00ff\u0100\7w\2\2\u0100\u0101\7g\2\2\u0101\32")
        buf.write("\3\2\2\2\u0102\u0107\5!\21\2\u0103\u0106\n\b\2\2\u0104")
        buf.write("\u0106\5\35\17\2\u0105\u0103\3\2\2\2\u0105\u0104\3\2\2")
        buf.write("\2\u0106\u0109\3\2\2\2\u0107\u0108\3\2\2\2\u0107\u0105")
        buf.write("\3\2\2\2\u0108\u010a\3\2\2\2\u0109\u0107\3\2\2\2\u010a")
        buf.write("\u010b\5!\21\2\u010b\34\3\2\2\2\u010c\u010d\7^\2\2\u010d")
        buf.write("\u010e\7$\2\2\u010e\u0112\3\2\2\2\u010f\u0111\n\t\2\2")
        buf.write("\u0110\u010f\3\2\2\2\u0111\u0114\3\2\2\2\u0112\u0113\3")
        buf.write("\2\2\2\u0112\u0110\3\2\2\2\u0113\u0115\3\2\2\2\u0114\u0112")
        buf.write("\3\2\2\2\u0115\u0116\7^\2\2\u0116\u0117\7$\2\2\u0117\36")
        buf.write("\3\2\2\2\u0118\u0120\5%\23\2\u0119\u0120\5\'\24\2\u011a")
        buf.write("\u0120\5)\25\2\u011b\u0120\5+\26\2\u011c\u0120\5-\27\2")
        buf.write("\u011d\u0120\5\61\31\2\u011e\u0120\5/\30\2\u011f\u0118")
        buf.write("\3\2\2\2\u011f\u0119\3\2\2\2\u011f\u011a\3\2\2\2\u011f")
        buf.write("\u011b\3\2\2\2\u011f\u011c\3\2\2\2\u011f\u011d\3\2\2\2")
        buf.write("\u011f\u011e\3\2\2\2\u0120 \3\2\2\2\u0121\u0122\t\t\2")
        buf.write("\2\u0122\"\3\2\2\2\u0123\u0124\t\n\2\2\u0124$\3\2\2\2")
        buf.write("\u0125\u0126\t\13\2\2\u0126&\3\2\2\2\u0127\u0128\t\f\2")
        buf.write("\2\u0128(\3\2\2\2\u0129\u012a\t\r\2\2\u012a*\3\2\2\2\u012b")
        buf.write("\u012c\t\16\2\2\u012c,\3\2\2\2\u012d\u012e\7)\2\2\u012e")
        buf.write(".\3\2\2\2\u012f\u0130\t\17\2\2\u0130\60\3\2\2\2\u0131")
        buf.write("\u0132\7^\2\2\u0132\u0133\7$\2\2\u0133\62\3\2\2\2\u0134")
        buf.write("\u0135\7c\2\2\u0135\u0136\7w\2\2\u0136\u0137\7v\2\2\u0137")
        buf.write("\u0138\7q\2\2\u0138\64\3\2\2\2\u0139\u013a\7d\2\2\u013a")
        buf.write("\u013b\7t\2\2\u013b\u013c\7g\2\2\u013c\u013d\7c\2\2\u013d")
        buf.write("\u013e\7m\2\2\u013e\66\3\2\2\2\u013f\u0140\7k\2\2\u0140")
        buf.write("\u0141\7p\2\2\u0141\u0142\7v\2\2\u0142\u0143\7g\2\2\u0143")
        buf.write("\u0144\7i\2\2\u0144\u0145\7g\2\2\u0145\u0146\7t\2\2\u0146")
        buf.write("8\3\2\2\2\u0147\u0148\7x\2\2\u0148\u0149\7q\2\2\u0149")
        buf.write("\u014a\7k\2\2\u014a\u014b\7f\2\2\u014b:\3\2\2\2\u014c")
        buf.write("\u014d\7c\2\2\u014d\u014e\7t\2\2\u014e\u014f\7t\2\2\u014f")
        buf.write("\u0150\7c\2\2\u0150\u0151\7{\2\2\u0151<\3\2\2\2\u0152")
        buf.write("\u0153\7h\2\2\u0153\u0154\7n\2\2\u0154\u0155\7q\2\2\u0155")
        buf.write("\u0156\7c\2\2\u0156\u0157\7v\2\2\u0157>\3\2\2\2\u0158")
        buf.write("\u0159\7t\2\2\u0159\u015a\7g\2\2\u015a\u015b\7v\2\2\u015b")
        buf.write("\u015c\7w\2\2\u015c\u015d\7t\2\2\u015d\u015e\7p\2\2\u015e")
        buf.write("@\3\2\2\2\u015f\u0160\7q\2\2\u0160\u0161\7w\2\2\u0161")
        buf.write("\u0162\7v\2\2\u0162B\3\2\2\2\u0163\u0164\7d\2\2\u0164")
        buf.write("\u0165\7q\2\2\u0165\u0166\7q\2\2\u0166\u0167\7n\2\2\u0167")
        buf.write("\u0168\7g\2\2\u0168\u0169\7c\2\2\u0169\u016a\7p\2\2\u016a")
        buf.write("D\3\2\2\2\u016b\u016c\7h\2\2\u016c\u016d\7q\2\2\u016d")
        buf.write("\u016e\7t\2\2\u016eF\3\2\2\2\u016f\u0170\7u\2\2\u0170")
        buf.write("\u0171\7v\2\2\u0171\u0172\7t\2\2\u0172\u0173\7k\2\2\u0173")
        buf.write("\u0174\7p\2\2\u0174\u0175\7i\2\2\u0175H\3\2\2\2\u0176")
        buf.write("\u0177\7e\2\2\u0177\u0178\7q\2\2\u0178\u0179\7p\2\2\u0179")
        buf.write("\u017a\7v\2\2\u017a\u017b\7k\2\2\u017b\u017c\7p\2\2\u017c")
        buf.write("\u017d\7w\2\2\u017d\u017e\7g\2\2\u017eJ\3\2\2\2\u017f")
        buf.write("\u0180\7f\2\2\u0180\u0181\7q\2\2\u0181L\3\2\2\2\u0182")
        buf.write("\u0183\7h\2\2\u0183\u0184\7w\2\2\u0184\u0185\7p\2\2\u0185")
        buf.write("\u0186\7e\2\2\u0186\u0187\7v\2\2\u0187\u0188\7k\2\2\u0188")
        buf.write("\u0189\7q\2\2\u0189\u018a\7p\2\2\u018aN\3\2\2\2\u018b")
        buf.write("\u018c\7q\2\2\u018c\u018d\7h\2\2\u018dP\3\2\2\2\u018e")
        buf.write("\u018f\7g\2\2\u018f\u0190\7n\2\2\u0190\u0191\7u\2\2\u0191")
        buf.write("\u0192\7g\2\2\u0192R\3\2\2\2\u0193\u0194\7k\2\2\u0194")
        buf.write("\u0195\7h\2\2\u0195T\3\2\2\2\u0196\u0197\7y\2\2\u0197")
        buf.write("\u0198\7j\2\2\u0198\u0199\7k\2\2\u0199\u019a\7n\2\2\u019a")
        buf.write("\u019b\7g\2\2\u019bV\3\2\2\2\u019c\u019d\7k\2\2\u019d")
        buf.write("\u019e\7p\2\2\u019e\u019f\7j\2\2\u019f\u01a0\7g\2\2\u01a0")
        buf.write("\u01a1\7t\2\2\u01a1\u01a2\7k\2\2\u01a2\u01a3\7v\2\2\u01a3")
        buf.write("X\3\2\2\2\u01a4\u01a5\7-\2\2\u01a5Z\3\2\2\2\u01a6\u01a7")
        buf.write("\7/\2\2\u01a7\\\3\2\2\2\u01a8\u01a9\7,\2\2\u01a9^\3\2")
        buf.write("\2\2\u01aa\u01ab\7\61\2\2\u01ab`\3\2\2\2\u01ac\u01ad\7")
        buf.write("\'\2\2\u01adb\3\2\2\2\u01ae\u01af\7#\2\2\u01afd\3\2\2")
        buf.write("\2\u01b0\u01b1\7(\2\2\u01b1\u01b2\7(\2\2\u01b2f\3\2\2")
        buf.write("\2\u01b3\u01b4\7~\2\2\u01b4\u01b5\7~\2\2\u01b5h\3\2\2")
        buf.write("\2\u01b6\u01b7\7?\2\2\u01b7\u01b8\7?\2\2\u01b8j\3\2\2")
        buf.write("\2\u01b9\u01ba\7#\2\2\u01ba\u01bb\7?\2\2\u01bbl\3\2\2")
        buf.write("\2\u01bc\u01bd\7>\2\2\u01bdn\3\2\2\2\u01be\u01bf\7@\2")
        buf.write("\2\u01bfp\3\2\2\2\u01c0\u01c1\7>\2\2\u01c1\u01c2\7?\2")
        buf.write("\2\u01c2r\3\2\2\2\u01c3\u01c4\7@\2\2\u01c4\u01c5\7?\2")
        buf.write("\2\u01c5t\3\2\2\2\u01c6\u01c7\7<\2\2\u01c7\u01c8\7<\2")
        buf.write("\2\u01c8v\3\2\2\2\u01c9\u01ca\7*\2\2\u01cax\3\2\2\2\u01cb")
        buf.write("\u01cc\7+\2\2\u01ccz\3\2\2\2\u01cd\u01ce\7]\2\2\u01ce")
        buf.write("|\3\2\2\2\u01cf\u01d0\7_\2\2\u01d0~\3\2\2\2\u01d1\u01d2")
        buf.write("\7}\2\2\u01d2\u0080\3\2\2\2\u01d3\u01d4\7\177\2\2\u01d4")
        buf.write("\u0082\3\2\2\2\u01d5\u01d6\7\60\2\2\u01d6\u0084\3\2\2")
        buf.write("\2\u01d7\u01d8\7.\2\2\u01d8\u0086\3\2\2\2\u01d9\u01da")
        buf.write("\7=\2\2\u01da\u0088\3\2\2\2\u01db\u01dc\7?\2\2\u01dc\u008a")
        buf.write("\3\2\2\2\u01dd\u01de\7<\2\2\u01de\u008c\3\2\2\2\u01df")
        buf.write("\u01e1\t\20\2\2\u01e0\u01df\3\2\2\2\u01e1\u01e2\3\2\2")
        buf.write("\2\u01e2\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3\u01e4")
        buf.write("\3\2\2\2\u01e4\u01e5\bG\4\2\u01e5\u008e\3\2\2\2\u01e6")
        buf.write("\u01e7\13\2\2\2\u01e7\u01e8\bH\5\2\u01e8\u0090\3\2\2\2")
        buf.write("\u01e9\u01ea\13\2\2\2\u01ea\u0092\3\2\2\2\u01eb\u01ec")
        buf.write("\13\2\2\2\u01ec\u0094\3\2\2\2\30\2\u0097\u009f\u00a8\u00b1")
        buf.write("\u00b6\u00be\u00c5\u00c9\u00cd\u00d5\u00dc\u00e2\u00e5")
        buf.write("\u00ea\u00f1\u00f5\u0105\u0107\u0112\u011f\u01e2\6\3\6")
        buf.write("\2\3\b\3\b\2\2\3H\4")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    INTEGER_LIT = 2
    FLOAT_LIT = 3
    BOOLEAN_LIT = 4
    STRING_LIT = 5
    AUTO = 6
    BREAK = 7
    INTEGER = 8
    VOID = 9
    ARRAY = 10
    FLOAT = 11
    RETURN = 12
    OUT = 13
    BOOLEAN = 14
    FOR = 15
    STRING = 16
    CONTINUE = 17
    DO = 18
    FUNCTION = 19
    OF = 20
    ELSE = 21
    IF = 22
    WHILE = 23
    INHERIT = 24
    LB = 25
    RB = 26
    LSB = 27
    RSB = 28
    LCB = 29
    RCB = 30
    WS = 31
    ERROR_CHAR = 32
    UNCLOSE_STRING = 33
    ILLEGAL_ESCAPE = 34

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'integer'", "'void'", "'array'", "'float'", 
            "'return'", "'out'", "'boolean'", "'for'", "'string'", "'continue'", 
            "'do'", "'function'", "'of'", "'else'", "'if'", "'while'", "'inherit'", 
            "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "INTEGER_LIT", "FLOAT_LIT", "BOOLEAN_LIT", "STRING_LIT", 
            "AUTO", "BREAK", "INTEGER", "VOID", "ARRAY", "FLOAT", "RETURN", 
            "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", "FUNCTION", 
            "OF", "ELSE", "IF", "WHILE", "INHERIT", "LB", "RB", "LSB", "RSB", 
            "LCB", "RCB", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMMENT", "SingleLineComment", "MultiLineComment", "IDENTIFIER", 
                  "INTEGER_LIT", "UNDERSCORE", "FLOAT_LIT", "DECPART", "EXPPART", 
                  "BOOLEAN_LIT", "FALSE", "TRUE", "STRING_LIT", "SubString", 
                  "Escape_Sequence", "DUO_QUOTE", "SINGLE_QUOTE", "BackSpace", 
                  "FormFeed", "CarriageReturn", "NewLine", "SingleQuote", 
                  "BackSlash", "Dou_quote", "AUTO", "BREAK", "INTEGER", 
                  "VOID", "ARRAY", "FLOAT", "RETURN", "OUT", "BOOLEAN", 
                  "FOR", "STRING", "CONTINUE", "DO", "FUNCTION", "OF", "ELSE", 
                  "IF", "WHILE", "INHERIT", "PLUS", "MINUS", "MUL", "DIV", 
                  "MOD", "NOT", "AND", "OR", "EQUAL_TO", "NOT_EQUAL", "LESS", 
                  "GREATER", "LESS_THAN_OR_EQUAL", "GREATER_THAN_OR_EQUAL", 
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
            actions[4] = self.INTEGER_LIT_action 
            actions[6] = self.FLOAT_LIT_action 
            actions[70] = self.ERROR_CHAR_action 
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
     


