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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2,")
        buf.write("\u01b4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\n\7\n\u00d6\n\n\f\n\16\n\u00d9\13\n\3\n\7\n\u00dc\n\n")
        buf.write("\f\n\16\n\u00df\13\n\5\n\u00e1\n\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\5\13\u00ea\n\13\3\f\3\f\3\r\3\r\3\16\3\16")
        buf.write("\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3")
        buf.write("!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3")
        buf.write("$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'")
        buf.write("\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3-\3.\3.\3.\3/\3")
        buf.write("/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\67\3\67\38")
        buf.write("\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3")
        buf.write("A\6A\u01a8\nA\rA\16A\u01a9\3A\3A\3B\3B\3B\3C\3C\3D\3D")
        buf.write("\4\u00d7\u00dd\2E\3\3\5\2\7\4\t\2\13\2\r\5\17\2\21\2\23")
        buf.write("\6\25\2\27\2\31\2\33\2\35\2\37\2!\2#\2%\2\'\7)\b+\t-\n")
        buf.write("/\13\61\f\63\r\65\16\67\179\20;\21=\22?\23A\24C\25E\26")
        buf.write("G\27I\30K\31M\2O\2Q\2S\2U\2W\2Y\32[\33]\34_\35a\36c\37")
        buf.write("e g!i\"k#m$o%q&s\'u(w\2y\2{\2}\2\177\2\u0081)\u0083*\u0085")
        buf.write("+\u0087,\3\2\r\3\2\63;\3\2\62;\4\2GGgg\3\2^^\3\2$$\3\2")
        buf.write("))\3\2\n\n\3\2\16\16\3\2\17\17\3\2\f\f\5\2\13\f\17\17")
        buf.write("\"\"\2\u01ad\2\3\3\2\2\2\2\7\3\2\2\2\2\r\3\2\2\2\2\23")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2")
        buf.write("\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2")
        buf.write("\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3")
        buf.write("\2\2\2\2u\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\3\u009d\3\2\2\2\5\u009f\3\2\2")
        buf.write("\2\7\u00a5\3\2\2\2\t\u00a7\3\2\2\2\13\u00b8\3\2\2\2\r")
        buf.write("\u00c5\3\2\2\2\17\u00c7\3\2\2\2\21\u00cd\3\2\2\2\23\u00d2")
        buf.write("\3\2\2\2\25\u00e9\3\2\2\2\27\u00eb\3\2\2\2\31\u00ed\3")
        buf.write("\2\2\2\33\u00ef\3\2\2\2\35\u00f1\3\2\2\2\37\u00f3\3\2")
        buf.write("\2\2!\u00f5\3\2\2\2#\u00f7\3\2\2\2%\u00f9\3\2\2\2\'\u00fb")
        buf.write("\3\2\2\2)\u0100\3\2\2\2+\u0106\3\2\2\2-\u010e\3\2\2\2")
        buf.write("/\u0113\3\2\2\2\61\u0119\3\2\2\2\63\u011f\3\2\2\2\65\u0126")
        buf.write("\3\2\2\2\67\u012a\3\2\2\29\u0132\3\2\2\2;\u0136\3\2\2")
        buf.write("\2=\u013d\3\2\2\2?\u0146\3\2\2\2A\u0149\3\2\2\2C\u0152")
        buf.write("\3\2\2\2E\u0155\3\2\2\2G\u015a\3\2\2\2I\u015d\3\2\2\2")
        buf.write("K\u0163\3\2\2\2M\u016b\3\2\2\2O\u016d\3\2\2\2Q\u016f\3")
        buf.write("\2\2\2S\u0171\3\2\2\2U\u0173\3\2\2\2W\u0175\3\2\2\2Y\u0177")
        buf.write("\3\2\2\2[\u017a\3\2\2\2]\u017d\3\2\2\2_\u0180\3\2\2\2")
        buf.write("a\u0183\3\2\2\2c\u0185\3\2\2\2e\u0187\3\2\2\2g\u018a\3")
        buf.write("\2\2\2i\u018d\3\2\2\2k\u0190\3\2\2\2m\u0192\3\2\2\2o\u0194")
        buf.write("\3\2\2\2q\u0196\3\2\2\2s\u0198\3\2\2\2u\u019a\3\2\2\2")
        buf.write("w\u019c\3\2\2\2y\u019e\3\2\2\2{\u01a0\3\2\2\2}\u01a2\3")
        buf.write("\2\2\2\177\u01a4\3\2\2\2\u0081\u01a7\3\2\2\2\u0083\u01ad")
        buf.write("\3\2\2\2\u0085\u01b0\3\2\2\2\u0087\u01b2\3\2\2\2\u0089")
        buf.write("\u009e\7\62\2\2\u008a\u008e\t\2\2\2\u008b\u008d\t\3\2")
        buf.write("\2\u008c\u008b\3\2\2\2\u008d\u0090\3\2\2\2\u008e\u008c")
        buf.write("\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0099\3\2\2\2\u0090")
        buf.write("\u008e\3\2\2\2\u0091\u0093\5\5\3\2\u0092\u0094\t\3\2\2")
        buf.write("\u0093\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0093\3")
        buf.write("\2\2\2\u0095\u0096\3\2\2\2\u0096\u0098\3\2\2\2\u0097\u0091")
        buf.write("\3\2\2\2\u0098\u009b\3\2\2\2\u0099\u0097\3\2\2\2\u0099")
        buf.write("\u009a\3\2\2\2\u009a\u009c\3\2\2\2\u009b\u0099\3\2\2\2")
        buf.write("\u009c\u009e\b\2\2\2\u009d\u0089\3\2\2\2\u009d\u008a\3")
        buf.write("\2\2\2\u009e\4\3\2\2\2\u009f\u00a0\7a\2\2\u00a0\6\3\2")
        buf.write("\2\2\u00a1\u00a6\5\13\6\2\u00a2\u00a3\5\t\5\2\u00a3\u00a4")
        buf.write("\b\4\3\2\u00a4\u00a6\3\2\2\2\u00a5\u00a1\3\2\2\2\u00a5")
        buf.write("\u00a2\3\2\2\2\u00a6\b\3\2\2\2\u00a7\u00a8\5\3\2\2\u00a8")
        buf.write("\u00aa\5w<\2\u00a9\u00ab\t\3\2\2\u00aa\u00a9\3\2\2\2\u00ab")
        buf.write("\u00ac\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2")
        buf.write("\u00ad\u00b5\3\2\2\2\u00ae\u00b2\t\4\2\2\u00af\u00b1\t")
        buf.write("\3\2\2\u00b0\u00af\3\2\2\2\u00b1\u00b4\3\2\2\2\u00b2\u00b0")
        buf.write("\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b6\3\2\2\2\u00b4")
        buf.write("\u00b2\3\2\2\2\u00b5\u00ae\3\2\2\2\u00b5\u00b6\3\2\2\2")
        buf.write("\u00b6\n\3\2\2\2\u00b7\u00b9\t\3\2\2\u00b8\u00b7\3\2\2")
        buf.write("\2\u00b9\u00ba\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb")
        buf.write("\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd\t\4\2\2\u00bd")
        buf.write("\u00bf\5O(\2\u00be\u00c0\t\3\2\2\u00bf\u00be\3\2\2\2\u00c0")
        buf.write("\u00c1\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2")
        buf.write("\u00c2\f\3\2\2\2\u00c3\u00c6\5\17\b\2\u00c4\u00c6\5\21")
        buf.write("\t\2\u00c5\u00c3\3\2\2\2\u00c5\u00c4\3\2\2\2\u00c6\16")
        buf.write("\3\2\2\2\u00c7\u00c8\7h\2\2\u00c8\u00c9\7c\2\2\u00c9\u00ca")
        buf.write("\7n\2\2\u00ca\u00cb\7u\2\2\u00cb\u00cc\7g\2\2\u00cc\20")
        buf.write("\3\2\2\2\u00cd\u00ce\7v\2\2\u00ce\u00cf\7t\2\2\u00cf\u00d0")
        buf.write("\7w\2\2\u00d0\u00d1\7g\2\2\u00d1\22\3\2\2\2\u00d2\u00e0")
        buf.write("\5\27\f\2\u00d3\u00d7\13\2\2\2\u00d4\u00d6\n\5\2\2\u00d5")
        buf.write("\u00d4\3\2\2\2\u00d6\u00d9\3\2\2\2\u00d7\u00d8\3\2\2\2")
        buf.write("\u00d7\u00d5\3\2\2\2\u00d8\u00dd\3\2\2\2\u00d9\u00d7\3")
        buf.write("\2\2\2\u00da\u00dc\5\25\13\2\u00db\u00da\3\2\2\2\u00dc")
        buf.write("\u00df\3\2\2\2\u00dd\u00de\3\2\2\2\u00dd\u00db\3\2\2\2")
        buf.write("\u00de\u00e1\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0\u00d3\3")
        buf.write("\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e3")
        buf.write("\5\27\f\2\u00e3\24\3\2\2\2\u00e4\u00ea\5\33\16\2\u00e5")
        buf.write("\u00ea\5\35\17\2\u00e6\u00ea\5\37\20\2\u00e7\u00ea\5!")
        buf.write("\21\2\u00e8\u00ea\5#\22\2\u00e9\u00e4\3\2\2\2\u00e9\u00e5")
        buf.write("\3\2\2\2\u00e9\u00e6\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9")
        buf.write("\u00e8\3\2\2\2\u00ea\26\3\2\2\2\u00eb\u00ec\t\6\2\2\u00ec")
        buf.write("\30\3\2\2\2\u00ed\u00ee\t\7\2\2\u00ee\32\3\2\2\2\u00ef")
        buf.write("\u00f0\t\b\2\2\u00f0\34\3\2\2\2\u00f1\u00f2\t\t\2\2\u00f2")
        buf.write("\36\3\2\2\2\u00f3\u00f4\t\n\2\2\u00f4 \3\2\2\2\u00f5\u00f6")
        buf.write("\t\13\2\2\u00f6\"\3\2\2\2\u00f7\u00f8\7)\2\2\u00f8$\3")
        buf.write("\2\2\2\u00f9\u00fa\t\5\2\2\u00fa&\3\2\2\2\u00fb\u00fc")
        buf.write("\7c\2\2\u00fc\u00fd\7w\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff")
        buf.write("\7q\2\2\u00ff(\3\2\2\2\u0100\u0101\7d\2\2\u0101\u0102")
        buf.write("\7t\2\2\u0102\u0103\7g\2\2\u0103\u0104\7c\2\2\u0104\u0105")
        buf.write("\7m\2\2\u0105*\3\2\2\2\u0106\u0107\7k\2\2\u0107\u0108")
        buf.write("\7p\2\2\u0108\u0109\7v\2\2\u0109\u010a\7g\2\2\u010a\u010b")
        buf.write("\7i\2\2\u010b\u010c\7g\2\2\u010c\u010d\7t\2\2\u010d,\3")
        buf.write("\2\2\2\u010e\u010f\7x\2\2\u010f\u0110\7q\2\2\u0110\u0111")
        buf.write("\7k\2\2\u0111\u0112\7f\2\2\u0112.\3\2\2\2\u0113\u0114")
        buf.write("\7c\2\2\u0114\u0115\7t\2\2\u0115\u0116\7t\2\2\u0116\u0117")
        buf.write("\7c\2\2\u0117\u0118\7{\2\2\u0118\60\3\2\2\2\u0119\u011a")
        buf.write("\7h\2\2\u011a\u011b\7n\2\2\u011b\u011c\7q\2\2\u011c\u011d")
        buf.write("\7c\2\2\u011d\u011e\7v\2\2\u011e\62\3\2\2\2\u011f\u0120")
        buf.write("\7t\2\2\u0120\u0121\7g\2\2\u0121\u0122\7v\2\2\u0122\u0123")
        buf.write("\7w\2\2\u0123\u0124\7t\2\2\u0124\u0125\7p\2\2\u0125\64")
        buf.write("\3\2\2\2\u0126\u0127\7q\2\2\u0127\u0128\7w\2\2\u0128\u0129")
        buf.write("\7v\2\2\u0129\66\3\2\2\2\u012a\u012b\7d\2\2\u012b\u012c")
        buf.write("\7q\2\2\u012c\u012d\7q\2\2\u012d\u012e\7n\2\2\u012e\u012f")
        buf.write("\7g\2\2\u012f\u0130\7c\2\2\u0130\u0131\7p\2\2\u01318\3")
        buf.write("\2\2\2\u0132\u0133\7h\2\2\u0133\u0134\7q\2\2\u0134\u0135")
        buf.write("\7t\2\2\u0135:\3\2\2\2\u0136\u0137\7u\2\2\u0137\u0138")
        buf.write("\7v\2\2\u0138\u0139\7t\2\2\u0139\u013a\7k\2\2\u013a\u013b")
        buf.write("\7p\2\2\u013b\u013c\7i\2\2\u013c<\3\2\2\2\u013d\u013e")
        buf.write("\7e\2\2\u013e\u013f\7q\2\2\u013f\u0140\7p\2\2\u0140\u0141")
        buf.write("\7v\2\2\u0141\u0142\7k\2\2\u0142\u0143\7p\2\2\u0143\u0144")
        buf.write("\7w\2\2\u0144\u0145\7g\2\2\u0145>\3\2\2\2\u0146\u0147")
        buf.write("\7f\2\2\u0147\u0148\7q\2\2\u0148@\3\2\2\2\u0149\u014a")
        buf.write("\7h\2\2\u014a\u014b\7w\2\2\u014b\u014c\7p\2\2\u014c\u014d")
        buf.write("\7e\2\2\u014d\u014e\7v\2\2\u014e\u014f\7k\2\2\u014f\u0150")
        buf.write("\7q\2\2\u0150\u0151\7p\2\2\u0151B\3\2\2\2\u0152\u0153")
        buf.write("\7q\2\2\u0153\u0154\7h\2\2\u0154D\3\2\2\2\u0155\u0156")
        buf.write("\7g\2\2\u0156\u0157\7n\2\2\u0157\u0158\7u\2\2\u0158\u0159")
        buf.write("\7g\2\2\u0159F\3\2\2\2\u015a\u015b\7k\2\2\u015b\u015c")
        buf.write("\7h\2\2\u015cH\3\2\2\2\u015d\u015e\7y\2\2\u015e\u015f")
        buf.write("\7j\2\2\u015f\u0160\7k\2\2\u0160\u0161\7n\2\2\u0161\u0162")
        buf.write("\7g\2\2\u0162J\3\2\2\2\u0163\u0164\7k\2\2\u0164\u0165")
        buf.write("\7p\2\2\u0165\u0166\7j\2\2\u0166\u0167\7g\2\2\u0167\u0168")
        buf.write("\7t\2\2\u0168\u0169\7k\2\2\u0169\u016a\7v\2\2\u016aL\3")
        buf.write("\2\2\2\u016b\u016c\7-\2\2\u016cN\3\2\2\2\u016d\u016e\7")
        buf.write("/\2\2\u016eP\3\2\2\2\u016f\u0170\7,\2\2\u0170R\3\2\2\2")
        buf.write("\u0171\u0172\7\61\2\2\u0172T\3\2\2\2\u0173\u0174\7\'\2")
        buf.write("\2\u0174V\3\2\2\2\u0175\u0176\7#\2\2\u0176X\3\2\2\2\u0177")
        buf.write("\u0178\7(\2\2\u0178\u0179\7(\2\2\u0179Z\3\2\2\2\u017a")
        buf.write("\u017b\7~\2\2\u017b\u017c\7~\2\2\u017c\\\3\2\2\2\u017d")
        buf.write("\u017e\7?\2\2\u017e\u017f\7?\2\2\u017f^\3\2\2\2\u0180")
        buf.write("\u0181\7#\2\2\u0181\u0182\7?\2\2\u0182`\3\2\2\2\u0183")
        buf.write("\u0184\7>\2\2\u0184b\3\2\2\2\u0185\u0186\7@\2\2\u0186")
        buf.write("d\3\2\2\2\u0187\u0188\7>\2\2\u0188\u0189\7?\2\2\u0189")
        buf.write("f\3\2\2\2\u018a\u018b\7@\2\2\u018b\u018c\7?\2\2\u018c")
        buf.write("h\3\2\2\2\u018d\u018e\7<\2\2\u018e\u018f\7<\2\2\u018f")
        buf.write("j\3\2\2\2\u0190\u0191\7*\2\2\u0191l\3\2\2\2\u0192\u0193")
        buf.write("\7+\2\2\u0193n\3\2\2\2\u0194\u0195\7]\2\2\u0195p\3\2\2")
        buf.write("\2\u0196\u0197\7_\2\2\u0197r\3\2\2\2\u0198\u0199\7}\2")
        buf.write("\2\u0199t\3\2\2\2\u019a\u019b\7\177\2\2\u019bv\3\2\2\2")
        buf.write("\u019c\u019d\7\60\2\2\u019dx\3\2\2\2\u019e\u019f\7.\2")
        buf.write("\2\u019fz\3\2\2\2\u01a0\u01a1\7=\2\2\u01a1|\3\2\2\2\u01a2")
        buf.write("\u01a3\7?\2\2\u01a3~\3\2\2\2\u01a4\u01a5\7<\2\2\u01a5")
        buf.write("\u0080\3\2\2\2\u01a6\u01a8\t\f\2\2\u01a7\u01a6\3\2\2\2")
        buf.write("\u01a8\u01a9\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01aa\3")
        buf.write("\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ac\bA\4\2\u01ac\u0082")
        buf.write("\3\2\2\2\u01ad\u01ae\13\2\2\2\u01ae\u01af\bB\5\2\u01af")
        buf.write("\u0084\3\2\2\2\u01b0\u01b1\13\2\2\2\u01b1\u0086\3\2\2")
        buf.write("\2\u01b2\u01b3\13\2\2\2\u01b3\u0088\3\2\2\2\23\2\u008e")
        buf.write("\u0095\u0099\u009d\u00a5\u00ac\u00b2\u00b5\u00ba\u00c1")
        buf.write("\u00c5\u00d7\u00dd\u00e0\u00e9\u01a9\6\3\2\2\3\4\3\b\2")
        buf.write("\2\3B\4")
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
     


