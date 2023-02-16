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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2 ")
        buf.write("\u0217\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\3\2\3\2\5\2\u00a4\n\2\3\3\3")
        buf.write("\3\3\3\3\3\7\3\u00aa\n\3\f\3\16\3\u00ad\13\3\3\4\3\4\3")
        buf.write("\4\3\4\7\4\u00b3\n\4\f\4\16\4\u00b6\13\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\7\5\u00be\n\5\f\5\16\5\u00c1\13\5\3\5\3\5\6")
        buf.write("\5\u00c5\n\5\r\5\16\5\u00c6\7\5\u00c9\n\5\f\5\16\5\u00cc")
        buf.write("\13\5\3\5\5\5\u00cf\n\5\3\6\3\6\3\7\3\7\3\7\3\7\5\7\u00d7")
        buf.write("\n\7\3\b\3\b\3\b\6\b\u00dc\n\b\r\b\16\b\u00dd\3\b\3\b")
        buf.write("\7\b\u00e2\n\b\f\b\16\b\u00e5\13\b\5\b\u00e7\n\b\3\t\6")
        buf.write("\t\u00ea\n\t\r\t\16\t\u00eb\3\t\3\t\3\t\6\t\u00f1\n\t")
        buf.write("\r\t\16\t\u00f2\3\n\3\n\5\n\u00f7\n\n\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\7\r\u0107")
        buf.write("\n\r\f\r\16\r\u010a\13\r\3\r\3\r\3\16\3\16\3\16\3\16\7")
        buf.write("\16\u0112\n\16\f\16\16\16\u0115\13\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u0121\n\17\3\20")
        buf.write("\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\5\32\u013a\n\32\3\33\3\33\3\33\3\33\3\33\5\33\u0141\n")
        buf.write("\33\3\34\3\34\5\34\u0145\n\34\3\35\3\35\3\35\7\35\u014a")
        buf.write("\n\35\f\35\16\35\u014d\13\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3")
        buf.write("#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)")
        buf.write("\3)\3)\3)\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write("+\3,\3,\3,\3-\3-\3-\3-\3-\3.\3.\3.\3/\3/\3/\3/\3/\3/\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\62")
        buf.write("\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67")
        buf.write("\3\67\38\38\38\39\39\39\3:\3:\3:\3;\3;\3<\3<\3=\3=\3=")
        buf.write("\3>\3>\3>\3?\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3")
        buf.write("E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3K\6K\u01fb\nK\rK\16K")
        buf.write("\u01fc\3K\7K\u0200\nK\fK\16K\u0203\13K\3L\6L\u0206\nL")
        buf.write("\rL\16L\u0207\3M\6M\u020b\nM\rM\16M\u020c\3M\3M\3N\3N")
        buf.write("\3N\3O\3O\3P\3P\6\u00b4\u0108\u0113\u014b\2Q\3\3\5\2\7")
        buf.write("\2\t\4\13\2\r\5\17\2\21\2\23\6\25\2\27\2\31\7\33\2\35")
        buf.write("\2\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61\b\63\2\65\2\67\29")
        buf.write("\t;\n=\13?\fA\rC\16E\17G\20I\21K\22M\23O\24Q\25S\26U\27")
        buf.write("W\30Y\31[\32]\33_\34a\2c\2e\2g\2i\2k\2m\2o\2q\2s\2u\2")
        buf.write("w\2y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089")
        buf.write("\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093\2\u0095\2\u0097")
        buf.write("\2\u0099\35\u009b\36\u009d\37\u009f \3\2\21\4\2\f\f\17")
        buf.write("\17\3\2\63;\3\2\62;\4\2GGgg\4\2$$^^\3\2$$\3\2))\3\2\n")
        buf.write("\n\3\2\16\16\3\2\17\17\3\2\f\f\3\2^^\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\5\2\13\f\17\17\"\"\2\u0204\2\3\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\23\3\2\2\2\2\31\3\2\2\2\2\61\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2")
        buf.write("U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2")
        buf.write("\2_\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3")
        buf.write("\2\2\2\2\u009f\3\2\2\2\3\u00a3\3\2\2\2\5\u00a5\3\2\2\2")
        buf.write("\7\u00ae\3\2\2\2\t\u00ce\3\2\2\2\13\u00d0\3\2\2\2\r\u00d6")
        buf.write("\3\2\2\2\17\u00d8\3\2\2\2\21\u00e9\3\2\2\2\23\u00f6\3")
        buf.write("\2\2\2\25\u00f8\3\2\2\2\27\u00fe\3\2\2\2\31\u0103\3\2")
        buf.write("\2\2\33\u010d\3\2\2\2\35\u0120\3\2\2\2\37\u0122\3\2\2")
        buf.write("\2!\u0124\3\2\2\2#\u0126\3\2\2\2%\u0128\3\2\2\2\'\u012a")
        buf.write("\3\2\2\2)\u012c\3\2\2\2+\u012e\3\2\2\2-\u0130\3\2\2\2")
        buf.write("/\u0132\3\2\2\2\61\u0135\3\2\2\2\63\u0139\3\2\2\2\65\u0140")
        buf.write("\3\2\2\2\67\u0144\3\2\2\29\u0146\3\2\2\2;\u014e\3\2\2")
        buf.write("\2=\u0153\3\2\2\2?\u0159\3\2\2\2A\u0161\3\2\2\2C\u0166")
        buf.write("\3\2\2\2E\u016c\3\2\2\2G\u0172\3\2\2\2I\u0179\3\2\2\2")
        buf.write("K\u017d\3\2\2\2M\u0185\3\2\2\2O\u0189\3\2\2\2Q\u0190\3")
        buf.write("\2\2\2S\u0199\3\2\2\2U\u019c\3\2\2\2W\u01a5\3\2\2\2Y\u01a8")
        buf.write("\3\2\2\2[\u01ad\3\2\2\2]\u01b0\3\2\2\2_\u01b6\3\2\2\2")
        buf.write("a\u01be\3\2\2\2c\u01c0\3\2\2\2e\u01c2\3\2\2\2g\u01c4\3")
        buf.write("\2\2\2i\u01c6\3\2\2\2k\u01c8\3\2\2\2m\u01ca\3\2\2\2o\u01cd")
        buf.write("\3\2\2\2q\u01d0\3\2\2\2s\u01d3\3\2\2\2u\u01d6\3\2\2\2")
        buf.write("w\u01d8\3\2\2\2y\u01da\3\2\2\2{\u01dd\3\2\2\2}\u01e0\3")
        buf.write("\2\2\2\177\u01e3\3\2\2\2\u0081\u01e5\3\2\2\2\u0083\u01e7")
        buf.write("\3\2\2\2\u0085\u01e9\3\2\2\2\u0087\u01eb\3\2\2\2\u0089")
        buf.write("\u01ed\3\2\2\2\u008b\u01ef\3\2\2\2\u008d\u01f1\3\2\2\2")
        buf.write("\u008f\u01f3\3\2\2\2\u0091\u01f5\3\2\2\2\u0093\u01f7\3")
        buf.write("\2\2\2\u0095\u01fa\3\2\2\2\u0097\u0205\3\2\2\2\u0099\u020a")
        buf.write("\3\2\2\2\u009b\u0210\3\2\2\2\u009d\u0213\3\2\2\2\u009f")
        buf.write("\u0215\3\2\2\2\u00a1\u00a4\5\5\3\2\u00a2\u00a4\5\7\4\2")
        buf.write("\u00a3\u00a1\3\2\2\2\u00a3\u00a2\3\2\2\2\u00a4\4\3\2\2")
        buf.write("\2\u00a5\u00a6\7\61\2\2\u00a6\u00a7\7\61\2\2\u00a7\u00ab")
        buf.write("\3\2\2\2\u00a8\u00aa\n\2\2\2\u00a9\u00a8\3\2\2\2\u00aa")
        buf.write("\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2")
        buf.write("\u00ac\6\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00af\7\61")
        buf.write("\2\2\u00af\u00b0\7,\2\2\u00b0\u00b4\3\2\2\2\u00b1\u00b3")
        buf.write("\13\2\2\2\u00b2\u00b1\3\2\2\2\u00b3\u00b6\3\2\2\2\u00b4")
        buf.write("\u00b5\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b5\u00b7\3\2\2\2")
        buf.write("\u00b6\u00b4\3\2\2\2\u00b7\u00b8\7,\2\2\u00b8\u00b9\7")
        buf.write("\61\2\2\u00b9\b\3\2\2\2\u00ba\u00cf\7\62\2\2\u00bb\u00bf")
        buf.write("\t\3\2\2\u00bc\u00be\t\4\2\2\u00bd\u00bc\3\2\2\2\u00be")
        buf.write("\u00c1\3\2\2\2\u00bf\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2")
        buf.write("\u00c0\u00ca\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c2\u00c4\5")
        buf.write("\13\6\2\u00c3\u00c5\t\4\2\2\u00c4\u00c3\3\2\2\2\u00c5")
        buf.write("\u00c6\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2")
        buf.write("\u00c7\u00c9\3\2\2\2\u00c8\u00c2\3\2\2\2\u00c9\u00cc\3")
        buf.write("\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cd")
        buf.write("\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00cf\b\5\2\2\u00ce")
        buf.write("\u00ba\3\2\2\2\u00ce\u00bb\3\2\2\2\u00cf\n\3\2\2\2\u00d0")
        buf.write("\u00d1\7a\2\2\u00d1\f\3\2\2\2\u00d2\u00d7\5\21\t\2\u00d3")
        buf.write("\u00d4\5\17\b\2\u00d4\u00d5\b\7\3\2\u00d5\u00d7\3\2\2")
        buf.write("\2\u00d6\u00d2\3\2\2\2\u00d6\u00d3\3\2\2\2\u00d7\16\3")
        buf.write("\2\2\2\u00d8\u00d9\5\t\5\2\u00d9\u00db\5\u008bF\2\u00da")
        buf.write("\u00dc\t\4\2\2\u00db\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2")
        buf.write("\u00dd\u00db\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00e6\3")
        buf.write("\2\2\2\u00df\u00e3\t\5\2\2\u00e0\u00e2\t\4\2\2\u00e1\u00e0")
        buf.write("\3\2\2\2\u00e2\u00e5\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3")
        buf.write("\u00e4\3\2\2\2\u00e4\u00e7\3\2\2\2\u00e5\u00e3\3\2\2\2")
        buf.write("\u00e6\u00df\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\20\3\2")
        buf.write("\2\2\u00e8\u00ea\t\4\2\2\u00e9\u00e8\3\2\2\2\u00ea\u00eb")
        buf.write("\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec")
        buf.write("\u00ed\3\2\2\2\u00ed\u00ee\t\5\2\2\u00ee\u00f0\5c\62\2")
        buf.write("\u00ef\u00f1\t\4\2\2\u00f0\u00ef\3\2\2\2\u00f1\u00f2\3")
        buf.write("\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\22")
        buf.write("\3\2\2\2\u00f4\u00f7\5\25\13\2\u00f5\u00f7\5\27\f\2\u00f6")
        buf.write("\u00f4\3\2\2\2\u00f6\u00f5\3\2\2\2\u00f7\24\3\2\2\2\u00f8")
        buf.write("\u00f9\7h\2\2\u00f9\u00fa\7c\2\2\u00fa\u00fb\7n\2\2\u00fb")
        buf.write("\u00fc\7u\2\2\u00fc\u00fd\7g\2\2\u00fd\26\3\2\2\2\u00fe")
        buf.write("\u00ff\7v\2\2\u00ff\u0100\7t\2\2\u0100\u0101\7w\2\2\u0101")
        buf.write("\u0102\7g\2\2\u0102\30\3\2\2\2\u0103\u0108\5\37\20\2\u0104")
        buf.write("\u0107\n\6\2\2\u0105\u0107\5\33\16\2\u0106\u0104\3\2\2")
        buf.write("\2\u0106\u0105\3\2\2\2\u0107\u010a\3\2\2\2\u0108\u0109")
        buf.write("\3\2\2\2\u0108\u0106\3\2\2\2\u0109\u010b\3\2\2\2\u010a")
        buf.write("\u0108\3\2\2\2\u010b\u010c\5\37\20\2\u010c\32\3\2\2\2")
        buf.write("\u010d\u010e\7^\2\2\u010e\u010f\7$\2\2\u010f\u0113\3\2")
        buf.write("\2\2\u0110\u0112\n\7\2\2\u0111\u0110\3\2\2\2\u0112\u0115")
        buf.write("\3\2\2\2\u0113\u0114\3\2\2\2\u0113\u0111\3\2\2\2\u0114")
        buf.write("\u0116\3\2\2\2\u0115\u0113\3\2\2\2\u0116\u0117\7^\2\2")
        buf.write("\u0117\u0118\7$\2\2\u0118\34\3\2\2\2\u0119\u0121\5#\22")
        buf.write("\2\u011a\u0121\5%\23\2\u011b\u0121\5\'\24\2\u011c\u0121")
        buf.write("\5)\25\2\u011d\u0121\5+\26\2\u011e\u0121\5/\30\2\u011f")
        buf.write("\u0121\5-\27\2\u0120\u0119\3\2\2\2\u0120\u011a\3\2\2\2")
        buf.write("\u0120\u011b\3\2\2\2\u0120\u011c\3\2\2\2\u0120\u011d\3")
        buf.write("\2\2\2\u0120\u011e\3\2\2\2\u0120\u011f\3\2\2\2\u0121\36")
        buf.write("\3\2\2\2\u0122\u0123\t\7\2\2\u0123 \3\2\2\2\u0124\u0125")
        buf.write("\t\b\2\2\u0125\"\3\2\2\2\u0126\u0127\t\t\2\2\u0127$\3")
        buf.write("\2\2\2\u0128\u0129\t\n\2\2\u0129&\3\2\2\2\u012a\u012b")
        buf.write("\t\13\2\2\u012b(\3\2\2\2\u012c\u012d\t\f\2\2\u012d*\3")
        buf.write("\2\2\2\u012e\u012f\7)\2\2\u012f,\3\2\2\2\u0130\u0131\t")
        buf.write("\r\2\2\u0131.\3\2\2\2\u0132\u0133\7^\2\2\u0133\u0134\7")
        buf.write("$\2\2\u0134\60\3\2\2\2\u0135\u0136\59\35\2\u0136\62\3")
        buf.write("\2\2\2\u0137\u013a\5\65\33\2\u0138\u013a\3\2\2\2\u0139")
        buf.write("\u0137\3\2\2\2\u0139\u0138\3\2\2\2\u013a\64\3\2\2\2\u013b")
        buf.write("\u013c\5\67\34\2\u013c\u013d\5\u008dG\2\u013d\u013e\5")
        buf.write("\65\33\2\u013e\u0141\3\2\2\2\u013f\u0141\5\67\34\2\u0140")
        buf.write("\u013b\3\2\2\2\u0140\u013f\3\2\2\2\u0141\66\3\2\2\2\u0142")
        buf.write("\u0145\5\u0097L\2\u0143\u0145\5\31\r\2\u0144\u0142\3\2")
        buf.write("\2\2\u0144\u0143\3\2\2\2\u01458\3\2\2\2\u0146\u014b\5")
        buf.write("\31\r\2\u0147\u0148\7.\2\2\u0148\u014a\5\31\r\2\u0149")
        buf.write("\u0147\3\2\2\2\u014a\u014d\3\2\2\2\u014b\u014c\3\2\2\2")
        buf.write("\u014b\u0149\3\2\2\2\u014c:\3\2\2\2\u014d\u014b\3\2\2")
        buf.write("\2\u014e\u014f\7c\2\2\u014f\u0150\7w\2\2\u0150\u0151\7")
        buf.write("v\2\2\u0151\u0152\7q\2\2\u0152<\3\2\2\2\u0153\u0154\7")
        buf.write("d\2\2\u0154\u0155\7t\2\2\u0155\u0156\7g\2\2\u0156\u0157")
        buf.write("\7c\2\2\u0157\u0158\7m\2\2\u0158>\3\2\2\2\u0159\u015a")
        buf.write("\7k\2\2\u015a\u015b\7p\2\2\u015b\u015c\7v\2\2\u015c\u015d")
        buf.write("\7g\2\2\u015d\u015e\7i\2\2\u015e\u015f\7g\2\2\u015f\u0160")
        buf.write("\7t\2\2\u0160@\3\2\2\2\u0161\u0162\7x\2\2\u0162\u0163")
        buf.write("\7q\2\2\u0163\u0164\7k\2\2\u0164\u0165\7f\2\2\u0165B\3")
        buf.write("\2\2\2\u0166\u0167\7c\2\2\u0167\u0168\7t\2\2\u0168\u0169")
        buf.write("\7t\2\2\u0169\u016a\7c\2\2\u016a\u016b\7{\2\2\u016bD\3")
        buf.write("\2\2\2\u016c\u016d\7h\2\2\u016d\u016e\7n\2\2\u016e\u016f")
        buf.write("\7q\2\2\u016f\u0170\7c\2\2\u0170\u0171\7v\2\2\u0171F\3")
        buf.write("\2\2\2\u0172\u0173\7t\2\2\u0173\u0174\7g\2\2\u0174\u0175")
        buf.write("\7v\2\2\u0175\u0176\7w\2\2\u0176\u0177\7t\2\2\u0177\u0178")
        buf.write("\7p\2\2\u0178H\3\2\2\2\u0179\u017a\7q\2\2\u017a\u017b")
        buf.write("\7w\2\2\u017b\u017c\7v\2\2\u017cJ\3\2\2\2\u017d\u017e")
        buf.write("\7d\2\2\u017e\u017f\7q\2\2\u017f\u0180\7q\2\2\u0180\u0181")
        buf.write("\7n\2\2\u0181\u0182\7g\2\2\u0182\u0183\7c\2\2\u0183\u0184")
        buf.write("\7p\2\2\u0184L\3\2\2\2\u0185\u0186\7h\2\2\u0186\u0187")
        buf.write("\7q\2\2\u0187\u0188\7t\2\2\u0188N\3\2\2\2\u0189\u018a")
        buf.write("\7u\2\2\u018a\u018b\7v\2\2\u018b\u018c\7t\2\2\u018c\u018d")
        buf.write("\7k\2\2\u018d\u018e\7p\2\2\u018e\u018f\7i\2\2\u018fP\3")
        buf.write("\2\2\2\u0190\u0191\7e\2\2\u0191\u0192\7q\2\2\u0192\u0193")
        buf.write("\7p\2\2\u0193\u0194\7v\2\2\u0194\u0195\7k\2\2\u0195\u0196")
        buf.write("\7p\2\2\u0196\u0197\7w\2\2\u0197\u0198\7g\2\2\u0198R\3")
        buf.write("\2\2\2\u0199\u019a\7f\2\2\u019a\u019b\7q\2\2\u019bT\3")
        buf.write("\2\2\2\u019c\u019d\7h\2\2\u019d\u019e\7w\2\2\u019e\u019f")
        buf.write("\7p\2\2\u019f\u01a0\7e\2\2\u01a0\u01a1\7v\2\2\u01a1\u01a2")
        buf.write("\7k\2\2\u01a2\u01a3\7q\2\2\u01a3\u01a4\7p\2\2\u01a4V\3")
        buf.write("\2\2\2\u01a5\u01a6\7q\2\2\u01a6\u01a7\7h\2\2\u01a7X\3")
        buf.write("\2\2\2\u01a8\u01a9\7g\2\2\u01a9\u01aa\7n\2\2\u01aa\u01ab")
        buf.write("\7u\2\2\u01ab\u01ac\7g\2\2\u01acZ\3\2\2\2\u01ad\u01ae")
        buf.write("\7k\2\2\u01ae\u01af\7h\2\2\u01af\\\3\2\2\2\u01b0\u01b1")
        buf.write("\7y\2\2\u01b1\u01b2\7j\2\2\u01b2\u01b3\7k\2\2\u01b3\u01b4")
        buf.write("\7n\2\2\u01b4\u01b5\7g\2\2\u01b5^\3\2\2\2\u01b6\u01b7")
        buf.write("\7k\2\2\u01b7\u01b8\7p\2\2\u01b8\u01b9\7j\2\2\u01b9\u01ba")
        buf.write("\7g\2\2\u01ba\u01bb\7t\2\2\u01bb\u01bc\7k\2\2\u01bc\u01bd")
        buf.write("\7v\2\2\u01bd`\3\2\2\2\u01be\u01bf\7-\2\2\u01bfb\3\2\2")
        buf.write("\2\u01c0\u01c1\7/\2\2\u01c1d\3\2\2\2\u01c2\u01c3\7,\2")
        buf.write("\2\u01c3f\3\2\2\2\u01c4\u01c5\7\61\2\2\u01c5h\3\2\2\2")
        buf.write("\u01c6\u01c7\7\'\2\2\u01c7j\3\2\2\2\u01c8\u01c9\7#\2\2")
        buf.write("\u01c9l\3\2\2\2\u01ca\u01cb\7(\2\2\u01cb\u01cc\7(\2\2")
        buf.write("\u01ccn\3\2\2\2\u01cd\u01ce\7~\2\2\u01ce\u01cf\7~\2\2")
        buf.write("\u01cfp\3\2\2\2\u01d0\u01d1\7?\2\2\u01d1\u01d2\7?\2\2")
        buf.write("\u01d2r\3\2\2\2\u01d3\u01d4\7#\2\2\u01d4\u01d5\7?\2\2")
        buf.write("\u01d5t\3\2\2\2\u01d6\u01d7\7>\2\2\u01d7v\3\2\2\2\u01d8")
        buf.write("\u01d9\7@\2\2\u01d9x\3\2\2\2\u01da\u01db\7>\2\2\u01db")
        buf.write("\u01dc\7?\2\2\u01dcz\3\2\2\2\u01dd\u01de\7@\2\2\u01de")
        buf.write("\u01df\7?\2\2\u01df|\3\2\2\2\u01e0\u01e1\7<\2\2\u01e1")
        buf.write("\u01e2\7<\2\2\u01e2~\3\2\2\2\u01e3\u01e4\7*\2\2\u01e4")
        buf.write("\u0080\3\2\2\2\u01e5\u01e6\7+\2\2\u01e6\u0082\3\2\2\2")
        buf.write("\u01e7\u01e8\7]\2\2\u01e8\u0084\3\2\2\2\u01e9\u01ea\7")
        buf.write("_\2\2\u01ea\u0086\3\2\2\2\u01eb\u01ec\7}\2\2\u01ec\u0088")
        buf.write("\3\2\2\2\u01ed\u01ee\7\177\2\2\u01ee\u008a\3\2\2\2\u01ef")
        buf.write("\u01f0\7\60\2\2\u01f0\u008c\3\2\2\2\u01f1\u01f2\7.\2\2")
        buf.write("\u01f2\u008e\3\2\2\2\u01f3\u01f4\7=\2\2\u01f4\u0090\3")
        buf.write("\2\2\2\u01f5\u01f6\7?\2\2\u01f6\u0092\3\2\2\2\u01f7\u01f8")
        buf.write("\7<\2\2\u01f8\u0094\3\2\2\2\u01f9\u01fb\t\16\2\2\u01fa")
        buf.write("\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fa\3\2\2\2")
        buf.write("\u01fc\u01fd\3\2\2\2\u01fd\u0201\3\2\2\2\u01fe\u0200\t")
        buf.write("\17\2\2\u01ff\u01fe\3\2\2\2\u0200\u0203\3\2\2\2\u0201")
        buf.write("\u01ff\3\2\2\2\u0201\u0202\3\2\2\2\u0202\u0096\3\2\2\2")
        buf.write("\u0203\u0201\3\2\2\2\u0204\u0206\t\4\2\2\u0205\u0204\3")
        buf.write("\2\2\2\u0206\u0207\3\2\2\2\u0207\u0205\3\2\2\2\u0207\u0208")
        buf.write("\3\2\2\2\u0208\u0098\3\2\2\2\u0209\u020b\t\20\2\2\u020a")
        buf.write("\u0209\3\2\2\2\u020b\u020c\3\2\2\2\u020c\u020a\3\2\2\2")
        buf.write("\u020c\u020d\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u020f\b")
        buf.write("M\4\2\u020f\u009a\3\2\2\2\u0210\u0211\13\2\2\2\u0211\u0212")
        buf.write("\bN\5\2\u0212\u009c\3\2\2\2\u0213\u0214\13\2\2\2\u0214")
        buf.write("\u009e\3\2\2\2\u0215\u0216\13\2\2\2\u0216\u00a0\3\2\2")
        buf.write("\2\35\2\u00a3\u00ab\u00b4\u00bf\u00c6\u00ca\u00ce\u00d6")
        buf.write("\u00dd\u00e3\u00e6\u00eb\u00f2\u00f6\u0106\u0108\u0113")
        buf.write("\u0120\u0139\u0140\u0144\u014b\u01fc\u0201\u0207\u020c")
        buf.write("\6\3\5\2\3\7\3\b\2\2\3N\4")
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
    StringList = 7
    AUTO = 8
    BREAK = 9
    INTEGER = 10
    VOID = 11
    ARRAY = 12
    FLOAT = 13
    RETURN = 14
    OUT = 15
    BOOLEAN = 16
    FOR = 17
    STRING = 18
    CONTINUE = 19
    DO = 20
    FUNCTION = 21
    OF = 22
    ELSE = 23
    IF = 24
    WHILE = 25
    INHERIT = 26
    WS = 27
    ERROR_CHAR = 28
    UNCLOSE_STRING = 29
    ILLEGAL_ESCAPE = 30

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'integer'", "'void'", "'array'", "'float'", 
            "'return'", "'out'", "'boolean'", "'for'", "'string'", "'continue'", 
            "'do'", "'function'", "'of'", "'else'", "'if'", "'while'", "'inherit'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "INTEGER_LIT", "FLOAT_LIT", "BOOLEAN_LIT", "STRING_LIT", 
            "ARRAY_LIT", "StringList", "AUTO", "BREAK", "INTEGER", "VOID", 
            "ARRAY", "FLOAT", "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", 
            "CONTINUE", "DO", "FUNCTION", "OF", "ELSE", "IF", "WHILE", "INHERIT", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMMENT", "SingleLineComment", "MultiLineComment", "INTEGER_LIT", 
                  "UNDERSCORE", "FLOAT_LIT", "DECPART", "EXPPART", "BOOLEAN_LIT", 
                  "FALSE", "TRUE", "STRING_LIT", "SubString", "Escape_Sequence", 
                  "DUO_QUOTE", "SINGLE_QUOTE", "BackSpace", "FormFeed", 
                  "CarriageReturn", "NewLine", "SingleQuote", "BackSlash", 
                  "Dou_quote", "ARRAY_LIT", "EXPS", "EXP", "ELEMENT", "StringList", 
                  "AUTO", "BREAK", "INTEGER", "VOID", "ARRAY", "FLOAT", 
                  "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", 
                  "DO", "FUNCTION", "OF", "ELSE", "IF", "WHILE", "INHERIT", 
                  "PLUS", "MINUS", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                  "EQUAL_TO", "NOT_EQUAL", "LESS", "GREATER", "LESS_THAN_OR_EQUAL", 
                  "GREATER_THAN_OR_EQUAL", "SCOPE_RES", "LB", "RB", "LSB", 
                  "RSB", "LCB", "RCB", "PERIOD", "COMMA", "SEMI", "EQUAL", 
                  "COLON", "IDENTIFIER", "NUMBER", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

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
            actions[3] = self.INTEGER_LIT_action 
            actions[5] = self.FLOAT_LIT_action 
            actions[76] = self.ERROR_CHAR_action 
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
     


