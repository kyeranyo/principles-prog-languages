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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\29")
        buf.write("\u01e9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\5\2\u008e\n\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\7\3\u0096\n\3\f\3\16\3\u0099\13\3\3\4\3\4\3\4\3")
        buf.write("\4\7\4\u009f\n\4\f\4\16\4\u00a2\13\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\7\5\u00ab\n\5\f\5\16\5\u00ae\13\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\7\6\u00b5\n\6\f\6\16\6\u00b8\13\6\3\6\3\6\6")
        buf.write("\6\u00bc\n\6\r\6\16\6\u00bd\7\6\u00c0\n\6\f\6\16\6\u00c3")
        buf.write("\13\6\3\6\5\6\u00c6\n\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00d7\n\b\3\b\3\b\3")
        buf.write("\t\3\t\7\t\u00dd\n\t\f\t\16\t\u00e0\13\t\3\n\3\n\5\n\u00e4")
        buf.write("\n\n\3\n\6\n\u00e7\n\n\r\n\16\n\u00e8\3\13\3\13\5\13\u00ed")
        buf.write("\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\7\16\u00fd\n\16\f\16\16\16\u0100\13\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3")
        buf.write(",\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=")
        buf.write("\3=\3>\3>\3?\3?\3@\3@\3A\6A\u01be\nA\rA\16A\u01bf\3A\7")
        buf.write("A\u01c3\nA\fA\16A\u01c6\13A\3B\6B\u01c9\nB\rB\16B\u01ca")
        buf.write("\3B\3B\3C\3C\3C\7C\u01d2\nC\fC\16C\u01d5\13C\3C\5C\u01d8")
        buf.write("\nC\3C\3C\3D\3D\3D\7D\u01df\nD\fD\16D\u01e2\13D\3D\3D")
        buf.write("\3D\3E\3E\3E\5\u00a0\u00ac\u01d3\2F\3\3\5\2\7\2\t\2\13")
        buf.write("\4\r\2\17\5\21\2\23\2\25\6\27\2\31\2\33\7\35\2\37\2!\2")
        buf.write("#\2%\2\'\b)\t+\n-\13/\f\61\r\63\16\65\17\67\209\21;\22")
        buf.write("=\23?\24A\25C\26E\27G\30I\31K\32M\33O\34Q\35S\36U\37W")
        buf.write(" Y![\"]#_$a%c&e\'g(i)k*m+o,q-s.u/w\60y\61{\62}\63\177")
        buf.write("\64\u0081\65\u0083\66\u0085\67\u00878\u00899\3\2\20\4")
        buf.write("\2\f\f\17\17\3\2\63;\3\2\62;\4\2GGgg\4\2--//\6\2\f\f\17")
        buf.write("\17$$^^\n\2$$))^^ddhhppttvv\3\2$$\3\2))\5\2C\\aac|\6\2")
        buf.write("\62;C\\aac|\5\2\13\f\17\17\"\"\4\3\f\f\17\17\4\2$$^^\2")
        buf.write("\u01f3\2\3\3\2\2\2\2\13\3\2\2\2\2\17\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o")
        buf.write("\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2")
        buf.write("y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\3\u008d\3\2\2\2\5\u0091\3\2\2\2\7\u009a")
        buf.write("\3\2\2\2\t\u00a6\3\2\2\2\13\u00c5\3\2\2\2\r\u00c7\3\2")
        buf.write("\2\2\17\u00d6\3\2\2\2\21\u00da\3\2\2\2\23\u00e1\3\2\2")
        buf.write("\2\25\u00ec\3\2\2\2\27\u00ee\3\2\2\2\31\u00f4\3\2\2\2")
        buf.write("\33\u00f9\3\2\2\2\35\u0104\3\2\2\2\37\u0107\3\2\2\2!\u010a")
        buf.write("\3\2\2\2#\u010d\3\2\2\2%\u010f\3\2\2\2\'\u0111\3\2\2\2")
        buf.write(")\u0116\3\2\2\2+\u011c\3\2\2\2-\u0124\3\2\2\2/\u0129\3")
        buf.write("\2\2\2\61\u012f\3\2\2\2\63\u0135\3\2\2\2\65\u013c\3\2")
        buf.write("\2\2\67\u0140\3\2\2\29\u0148\3\2\2\2;\u014c\3\2\2\2=\u0153")
        buf.write("\3\2\2\2?\u015c\3\2\2\2A\u015f\3\2\2\2C\u0168\3\2\2\2")
        buf.write("E\u016b\3\2\2\2G\u0170\3\2\2\2I\u0173\3\2\2\2K\u0179\3")
        buf.write("\2\2\2M\u0181\3\2\2\2O\u0183\3\2\2\2Q\u0185\3\2\2\2S\u0187")
        buf.write("\3\2\2\2U\u0189\3\2\2\2W\u018b\3\2\2\2Y\u018d\3\2\2\2")
        buf.write("[\u018f\3\2\2\2]\u0192\3\2\2\2_\u0195\3\2\2\2a\u0197\3")
        buf.write("\2\2\2c\u019a\3\2\2\2e\u019d\3\2\2\2g\u01a0\3\2\2\2i\u01a3")
        buf.write("\3\2\2\2k\u01a6\3\2\2\2m\u01a8\3\2\2\2o\u01aa\3\2\2\2")
        buf.write("q\u01ac\3\2\2\2s\u01ae\3\2\2\2u\u01b0\3\2\2\2w\u01b2\3")
        buf.write("\2\2\2y\u01b4\3\2\2\2{\u01b6\3\2\2\2}\u01b8\3\2\2\2\177")
        buf.write("\u01ba\3\2\2\2\u0081\u01bd\3\2\2\2\u0083\u01c8\3\2\2\2")
        buf.write("\u0085\u01ce\3\2\2\2\u0087\u01db\3\2\2\2\u0089\u01e6\3")
        buf.write("\2\2\2\u008b\u008e\5\5\3\2\u008c\u008e\5\7\4\2\u008d\u008b")
        buf.write("\3\2\2\2\u008d\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f")
        buf.write("\u0090\b\2\2\2\u0090\4\3\2\2\2\u0091\u0092\7\61\2\2\u0092")
        buf.write("\u0093\7\61\2\2\u0093\u0097\3\2\2\2\u0094\u0096\n\2\2")
        buf.write("\2\u0095\u0094\3\2\2\2\u0096\u0099\3\2\2\2\u0097\u0095")
        buf.write("\3\2\2\2\u0097\u0098\3\2\2\2\u0098\6\3\2\2\2\u0099\u0097")
        buf.write("\3\2\2\2\u009a\u009b\7\61\2\2\u009b\u009c\7,\2\2\u009c")
        buf.write("\u00a0\3\2\2\2\u009d\u009f\13\2\2\2\u009e\u009d\3\2\2")
        buf.write("\2\u009f\u00a2\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a0\u009e")
        buf.write("\3\2\2\2\u00a1\u00a3\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a3")
        buf.write("\u00a4\7,\2\2\u00a4\u00a5\7\61\2\2\u00a5\b\3\2\2\2\u00a6")
        buf.write("\u00a7\7\61\2\2\u00a7\u00a8\7,\2\2\u00a8\u00ac\3\2\2\2")
        buf.write("\u00a9\u00ab\13\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\u00ae")
        buf.write("\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ad")
        buf.write("\u00af\3\2\2\2\u00ae\u00ac\3\2\2\2\u00af\u00b0\7\2\2\3")
        buf.write("\u00b0\n\3\2\2\2\u00b1\u00c6\7\62\2\2\u00b2\u00b6\t\3")
        buf.write("\2\2\u00b3\u00b5\t\4\2\2\u00b4\u00b3\3\2\2\2\u00b5\u00b8")
        buf.write("\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7")
        buf.write("\u00c1\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b9\u00bb\5\r\7\2")
        buf.write("\u00ba\u00bc\t\4\2\2\u00bb\u00ba\3\2\2\2\u00bc\u00bd\3")
        buf.write("\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00c0")
        buf.write("\3\2\2\2\u00bf\u00b9\3\2\2\2\u00c0\u00c3\3\2\2\2\u00c1")
        buf.write("\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c4\3\2\2\2")
        buf.write("\u00c3\u00c1\3\2\2\2\u00c4\u00c6\b\6\3\2\u00c5\u00b1\3")
        buf.write("\2\2\2\u00c5\u00b2\3\2\2\2\u00c6\f\3\2\2\2\u00c7\u00c8")
        buf.write("\7a\2\2\u00c8\16\3\2\2\2\u00c9\u00ca\5\13\6\2\u00ca\u00cb")
        buf.write("\5\21\t\2\u00cb\u00cc\5\23\n\2\u00cc\u00d7\3\2\2\2\u00cd")
        buf.write("\u00ce\5\13\6\2\u00ce\u00cf\5\21\t\2\u00cf\u00d7\3\2\2")
        buf.write("\2\u00d0\u00d1\5\13\6\2\u00d1\u00d2\5\23\n\2\u00d2\u00d7")
        buf.write("\3\2\2\2\u00d3\u00d4\5\21\t\2\u00d4\u00d5\5\23\n\2\u00d5")
        buf.write("\u00d7\3\2\2\2\u00d6\u00c9\3\2\2\2\u00d6\u00cd\3\2\2\2")
        buf.write("\u00d6\u00d0\3\2\2\2\u00d6\u00d3\3\2\2\2\u00d7\u00d8\3")
        buf.write("\2\2\2\u00d8\u00d9\b\b\4\2\u00d9\20\3\2\2\2\u00da\u00de")
        buf.write("\5k\66\2\u00db\u00dd\t\4\2\2\u00dc\u00db\3\2\2\2\u00dd")
        buf.write("\u00e0\3\2\2\2\u00de\u00dc\3\2\2\2\u00de\u00df\3\2\2\2")
        buf.write("\u00df\22\3\2\2\2\u00e0\u00de\3\2\2\2\u00e1\u00e3\t\5")
        buf.write("\2\2\u00e2\u00e4\t\6\2\2\u00e3\u00e2\3\2\2\2\u00e3\u00e4")
        buf.write("\3\2\2\2\u00e4\u00e6\3\2\2\2\u00e5\u00e7\t\4\2\2\u00e6")
        buf.write("\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00e6\3\2\2\2")
        buf.write("\u00e8\u00e9\3\2\2\2\u00e9\24\3\2\2\2\u00ea\u00ed\5\27")
        buf.write("\f\2\u00eb\u00ed\5\31\r\2\u00ec\u00ea\3\2\2\2\u00ec\u00eb")
        buf.write("\3\2\2\2\u00ed\26\3\2\2\2\u00ee\u00ef\7h\2\2\u00ef\u00f0")
        buf.write("\7c\2\2\u00f0\u00f1\7n\2\2\u00f1\u00f2\7u\2\2\u00f2\u00f3")
        buf.write("\7g\2\2\u00f3\30\3\2\2\2\u00f4\u00f5\7v\2\2\u00f5\u00f6")
        buf.write("\7t\2\2\u00f6\u00f7\7w\2\2\u00f7\u00f8\7g\2\2\u00f8\32")
        buf.write("\3\2\2\2\u00f9\u00fe\5#\22\2\u00fa\u00fd\n\7\2\2\u00fb")
        buf.write("\u00fd\5\37\20\2\u00fc\u00fa\3\2\2\2\u00fc\u00fb\3\2\2")
        buf.write("\2\u00fd\u0100\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00ff")
        buf.write("\3\2\2\2\u00ff\u0101\3\2\2\2\u0100\u00fe\3\2\2\2\u0101")
        buf.write("\u0102\5#\22\2\u0102\u0103\b\16\5\2\u0103\34\3\2\2\2\u0104")
        buf.write("\u0105\7^\2\2\u0105\u0106\n\b\2\2\u0106\36\3\2\2\2\u0107")
        buf.write("\u0108\7^\2\2\u0108\u0109\t\b\2\2\u0109 \3\2\2\2\u010a")
        buf.write("\u010b\7^\2\2\u010b\u010c\n\t\2\2\u010c\"\3\2\2\2\u010d")
        buf.write("\u010e\t\t\2\2\u010e$\3\2\2\2\u010f\u0110\t\n\2\2\u0110")
        buf.write("&\3\2\2\2\u0111\u0112\7c\2\2\u0112\u0113\7w\2\2\u0113")
        buf.write("\u0114\7v\2\2\u0114\u0115\7q\2\2\u0115(\3\2\2\2\u0116")
        buf.write("\u0117\7d\2\2\u0117\u0118\7t\2\2\u0118\u0119\7g\2\2\u0119")
        buf.write("\u011a\7c\2\2\u011a\u011b\7m\2\2\u011b*\3\2\2\2\u011c")
        buf.write("\u011d\7k\2\2\u011d\u011e\7p\2\2\u011e\u011f\7v\2\2\u011f")
        buf.write("\u0120\7g\2\2\u0120\u0121\7i\2\2\u0121\u0122\7g\2\2\u0122")
        buf.write("\u0123\7t\2\2\u0123,\3\2\2\2\u0124\u0125\7x\2\2\u0125")
        buf.write("\u0126\7q\2\2\u0126\u0127\7k\2\2\u0127\u0128\7f\2\2\u0128")
        buf.write(".\3\2\2\2\u0129\u012a\7c\2\2\u012a\u012b\7t\2\2\u012b")
        buf.write("\u012c\7t\2\2\u012c\u012d\7c\2\2\u012d\u012e\7{\2\2\u012e")
        buf.write("\60\3\2\2\2\u012f\u0130\7h\2\2\u0130\u0131\7n\2\2\u0131")
        buf.write("\u0132\7q\2\2\u0132\u0133\7c\2\2\u0133\u0134\7v\2\2\u0134")
        buf.write("\62\3\2\2\2\u0135\u0136\7t\2\2\u0136\u0137\7g\2\2\u0137")
        buf.write("\u0138\7v\2\2\u0138\u0139\7w\2\2\u0139\u013a\7t\2\2\u013a")
        buf.write("\u013b\7p\2\2\u013b\64\3\2\2\2\u013c\u013d\7q\2\2\u013d")
        buf.write("\u013e\7w\2\2\u013e\u013f\7v\2\2\u013f\66\3\2\2\2\u0140")
        buf.write("\u0141\7d\2\2\u0141\u0142\7q\2\2\u0142\u0143\7q\2\2\u0143")
        buf.write("\u0144\7n\2\2\u0144\u0145\7g\2\2\u0145\u0146\7c\2\2\u0146")
        buf.write("\u0147\7p\2\2\u01478\3\2\2\2\u0148\u0149\7h\2\2\u0149")
        buf.write("\u014a\7q\2\2\u014a\u014b\7t\2\2\u014b:\3\2\2\2\u014c")
        buf.write("\u014d\7u\2\2\u014d\u014e\7v\2\2\u014e\u014f\7t\2\2\u014f")
        buf.write("\u0150\7k\2\2\u0150\u0151\7p\2\2\u0151\u0152\7i\2\2\u0152")
        buf.write("<\3\2\2\2\u0153\u0154\7e\2\2\u0154\u0155\7q\2\2\u0155")
        buf.write("\u0156\7p\2\2\u0156\u0157\7v\2\2\u0157\u0158\7k\2\2\u0158")
        buf.write("\u0159\7p\2\2\u0159\u015a\7w\2\2\u015a\u015b\7g\2\2\u015b")
        buf.write(">\3\2\2\2\u015c\u015d\7f\2\2\u015d\u015e\7q\2\2\u015e")
        buf.write("@\3\2\2\2\u015f\u0160\7h\2\2\u0160\u0161\7w\2\2\u0161")
        buf.write("\u0162\7p\2\2\u0162\u0163\7e\2\2\u0163\u0164\7v\2\2\u0164")
        buf.write("\u0165\7k\2\2\u0165\u0166\7q\2\2\u0166\u0167\7p\2\2\u0167")
        buf.write("B\3\2\2\2\u0168\u0169\7q\2\2\u0169\u016a\7h\2\2\u016a")
        buf.write("D\3\2\2\2\u016b\u016c\7g\2\2\u016c\u016d\7n\2\2\u016d")
        buf.write("\u016e\7u\2\2\u016e\u016f\7g\2\2\u016fF\3\2\2\2\u0170")
        buf.write("\u0171\7k\2\2\u0171\u0172\7h\2\2\u0172H\3\2\2\2\u0173")
        buf.write("\u0174\7y\2\2\u0174\u0175\7j\2\2\u0175\u0176\7k\2\2\u0176")
        buf.write("\u0177\7n\2\2\u0177\u0178\7g\2\2\u0178J\3\2\2\2\u0179")
        buf.write("\u017a\7k\2\2\u017a\u017b\7p\2\2\u017b\u017c\7j\2\2\u017c")
        buf.write("\u017d\7g\2\2\u017d\u017e\7t\2\2\u017e\u017f\7k\2\2\u017f")
        buf.write("\u0180\7v\2\2\u0180L\3\2\2\2\u0181\u0182\7-\2\2\u0182")
        buf.write("N\3\2\2\2\u0183\u0184\7/\2\2\u0184P\3\2\2\2\u0185\u0186")
        buf.write("\7,\2\2\u0186R\3\2\2\2\u0187\u0188\7\61\2\2\u0188T\3\2")
        buf.write("\2\2\u0189\u018a\7\'\2\2\u018aV\3\2\2\2\u018b\u018c\7")
        buf.write(">\2\2\u018cX\3\2\2\2\u018d\u018e\7@\2\2\u018eZ\3\2\2\2")
        buf.write("\u018f\u0190\7>\2\2\u0190\u0191\7?\2\2\u0191\\\3\2\2\2")
        buf.write("\u0192\u0193\7@\2\2\u0193\u0194\7?\2\2\u0194^\3\2\2\2")
        buf.write("\u0195\u0196\7#\2\2\u0196`\3\2\2\2\u0197\u0198\7(\2\2")
        buf.write("\u0198\u0199\7(\2\2\u0199b\3\2\2\2\u019a\u019b\7~\2\2")
        buf.write("\u019b\u019c\7~\2\2\u019cd\3\2\2\2\u019d\u019e\7?\2\2")
        buf.write("\u019e\u019f\7?\2\2\u019ff\3\2\2\2\u01a0\u01a1\7#\2\2")
        buf.write("\u01a1\u01a2\7?\2\2\u01a2h\3\2\2\2\u01a3\u01a4\7<\2\2")
        buf.write("\u01a4\u01a5\7<\2\2\u01a5j\3\2\2\2\u01a6\u01a7\7\60\2")
        buf.write("\2\u01a7l\3\2\2\2\u01a8\u01a9\7.\2\2\u01a9n\3\2\2\2\u01aa")
        buf.write("\u01ab\7=\2\2\u01abp\3\2\2\2\u01ac\u01ad\7?\2\2\u01ad")
        buf.write("r\3\2\2\2\u01ae\u01af\7<\2\2\u01aft\3\2\2\2\u01b0\u01b1")
        buf.write("\7*\2\2\u01b1v\3\2\2\2\u01b2\u01b3\7+\2\2\u01b3x\3\2\2")
        buf.write("\2\u01b4\u01b5\7]\2\2\u01b5z\3\2\2\2\u01b6\u01b7\7_\2")
        buf.write("\2\u01b7|\3\2\2\2\u01b8\u01b9\7}\2\2\u01b9~\3\2\2\2\u01ba")
        buf.write("\u01bb\7\177\2\2\u01bb\u0080\3\2\2\2\u01bc\u01be\t\13")
        buf.write("\2\2\u01bd\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01bd")
        buf.write("\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c4\3\2\2\2\u01c1")
        buf.write("\u01c3\t\f\2\2\u01c2\u01c1\3\2\2\2\u01c3\u01c6\3\2\2\2")
        buf.write("\u01c4\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u0082\3")
        buf.write("\2\2\2\u01c6\u01c4\3\2\2\2\u01c7\u01c9\t\r\2\2\u01c8\u01c7")
        buf.write("\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01c8\3\2\2\2\u01ca")
        buf.write("\u01cb\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01cd\bB\2\2")
        buf.write("\u01cd\u0084\3\2\2\2\u01ce\u01d3\5#\22\2\u01cf\u01d2\n")
        buf.write("\t\2\2\u01d0\u01d2\5\37\20\2\u01d1\u01cf\3\2\2\2\u01d1")
        buf.write("\u01d0\3\2\2\2\u01d2\u01d5\3\2\2\2\u01d3\u01d4\3\2\2\2")
        buf.write("\u01d3\u01d1\3\2\2\2\u01d4\u01d7\3\2\2\2\u01d5\u01d3\3")
        buf.write("\2\2\2\u01d6\u01d8\t\16\2\2\u01d7\u01d6\3\2\2\2\u01d8")
        buf.write("\u01d9\3\2\2\2\u01d9\u01da\bC\6\2\u01da\u0086\3\2\2\2")
        buf.write("\u01db\u01e0\5#\22\2\u01dc\u01df\n\17\2\2\u01dd\u01df")
        buf.write("\5\37\20\2\u01de\u01dc\3\2\2\2\u01de\u01dd\3\2\2\2\u01df")
        buf.write("\u01e2\3\2\2\2\u01e0\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2")
        buf.write("\u01e1\u01e3\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e3\u01e4\5")
        buf.write("\35\17\2\u01e4\u01e5\bD\7\2\u01e5\u0088\3\2\2\2\u01e6")
        buf.write("\u01e7\13\2\2\2\u01e7\u01e8\bE\b\2\u01e8\u008a\3\2\2\2")
        buf.write("\32\2\u008d\u0097\u00a0\u00ac\u00b6\u00bd\u00c1\u00c5")
        buf.write("\u00d6\u00de\u00e3\u00e8\u00ec\u00fc\u00fe\u01bf\u01c4")
        buf.write("\u01ca\u01d1\u01d3\u01d7\u01de\u01e0\t\b\2\2\3\6\2\3\b")
        buf.write("\3\3\16\4\3C\5\3D\6\3E\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    INTLIT = 2
    FLOATLIT = 3
    BOOLEANLIT = 4
    STRINGLIT = 5
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
    PLUS = 25
    MINUS = 26
    MUL = 27
    DIV = 28
    MOD = 29
    LESS = 30
    GREATER = 31
    LTE = 32
    GTE = 33
    NOT = 34
    AND = 35
    OR = 36
    EQUAL_TO = 37
    NOT_EQUAL = 38
    CONCAT = 39
    PERIOD = 40
    COMMA = 41
    SEMI = 42
    EQUAL = 43
    COLON = 44
    LB = 45
    RB = 46
    LSB = 47
    RSB = 48
    LCB = 49
    RCB = 50
    IDENTIFIER = 51
    WS = 52
    UNCLOSE_STRING = 53
    ILLEGAL_ESCAPE = 54
    ERROR_CHAR = 55

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'integer'", "'void'", "'array'", "'float'", 
            "'return'", "'out'", "'boolean'", "'for'", "'string'", "'continue'", 
            "'do'", "'function'", "'of'", "'else'", "'if'", "'while'", "'inherit'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'<'", "'>'", "'<='", "'>='", 
            "'!'", "'&&'", "'||'", "'=='", "'!='", "'::'", "'.'", "','", 
            "';'", "'='", "':'", "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "INTLIT", "FLOATLIT", "BOOLEANLIT", "STRINGLIT", 
            "AUTO", "BREAK", "INTEGER", "VOID", "ARRAY", "FLOAT", "RETURN", 
            "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", "FUNCTION", 
            "OF", "ELSE", "IF", "WHILE", "INHERIT", "PLUS", "MINUS", "MUL", 
            "DIV", "MOD", "LESS", "GREATER", "LTE", "GTE", "NOT", "AND", 
            "OR", "EQUAL_TO", "NOT_EQUAL", "CONCAT", "PERIOD", "COMMA", 
            "SEMI", "EQUAL", "COLON", "LB", "RB", "LSB", "RSB", "LCB", "RCB", 
            "IDENTIFIER", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "COMMENT", "SingleLineComment", "MultiLineComment", "CommentAll", 
                  "INTLIT", "UNDERSCORE", "FLOATLIT", "DECPART", "EXPPART", 
                  "BOOLEANLIT", "FALSE", "TRUE", "STRINGLIT", "NOTESC", 
                  "ESC", "AllEscSeq", "DUO_QUOTE", "SINGLE_QUOTE", "AUTO", 
                  "BREAK", "INTEGER", "VOID", "ARRAY", "FLOAT", "RETURN", 
                  "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", "FUNCTION", 
                  "OF", "ELSE", "IF", "WHILE", "INHERIT", "PLUS", "MINUS", 
                  "MUL", "DIV", "MOD", "LESS", "GREATER", "LTE", "GTE", 
                  "NOT", "AND", "OR", "EQUAL_TO", "NOT_EQUAL", "CONCAT", 
                  "PERIOD", "COMMA", "SEMI", "EQUAL", "COLON", "LB", "RB", 
                  "LSB", "RSB", "LCB", "RCB", "IDENTIFIER", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[4] = self.INTLIT_action 
            actions[6] = self.FLOATLIT_action 
            actions[12] = self.STRINGLIT_action 
            actions[65] = self.UNCLOSE_STRING_action 
            actions[66] = self.ILLEGAL_ESCAPE_action 
            actions[67] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_","")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_","")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text=str(self.text[1:-1])
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            s = self.text
            if s[len(s) - 1] == '\n' or s[len(s) - 1] == '\r':
                raise UncloseString(self.text[1:-1])
            raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise IllegalEscape(self.text[1:])
            		
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


