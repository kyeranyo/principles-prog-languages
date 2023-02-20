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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2:")
        buf.write("\u022a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\3\2\3\2\5\2\u00a2\n\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\7\3\u00aa\n\3\f\3\16\3\u00ad\13\3\3\4\3\4")
        buf.write("\3\4\3\4\7\4\u00b3\n\4\f\4\16\4\u00b6\13\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\7\5\u00be\n\5\f\5\16\5\u00c1\13\5\3\5\3\5")
        buf.write("\6\5\u00c5\n\5\r\5\16\5\u00c6\7\5\u00c9\n\5\f\5\16\5\u00cc")
        buf.write("\13\5\3\5\5\5\u00cf\n\5\3\6\3\6\3\7\3\7\3\7\3\7\5\7\u00d7")
        buf.write("\n\7\3\b\3\b\3\b\6\b\u00dc\n\b\r\b\16\b\u00dd\3\b\3\b")
        buf.write("\7\b\u00e2\n\b\f\b\16\b\u00e5\13\b\5\b\u00e7\n\b\3\t\6")
        buf.write("\t\u00ea\n\t\r\t\16\t\u00eb\3\t\3\t\3\t\6\t\u00f1\n\t")
        buf.write("\r\t\16\t\u00f2\3\n\3\n\5\n\u00f7\n\n\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\7\r\u0107")
        buf.write("\n\r\f\r\16\r\u010a\13\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\7\16\u0113\n\16\f\16\16\16\u0116\13\16\3\16\3\16\3")
        buf.write("\16\3\17\3\17\5\17\u011d\n\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\5\20\u0124\n\20\3\21\3\21\3\21\3\21\3\21\5\21\u012b\n")
        buf.write("\21\3\22\3\22\3\22\3\22\3\22\5\22\u0132\n\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\5\23\u0139\n\23\3\24\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\5\24\u0142\n\24\3\25\3\25\3\26\3\26\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)")
        buf.write("\3)\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3-\3")
        buf.write("-\3-\3-\3-\3.\3.\3.\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\38\39\3")
        buf.write("9\39\3:\3:\3;\3;\3;\3<\3<\3<\3=\3=\3=\3>\3>\3>\3?\3?\3")
        buf.write("?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3")
        buf.write("H\3I\3I\3J\3J\3K\6K\u0203\nK\rK\16K\u0204\3K\7K\u0208")
        buf.write("\nK\fK\16K\u020b\13K\3L\6L\u020e\nL\rL\16L\u020f\3L\3")
        buf.write("L\3M\3M\3M\7M\u0217\nM\fM\16M\u021a\13M\3M\3M\3N\3N\7")
        buf.write("N\u0220\nN\fN\16N\u0223\13N\3N\3N\3N\3O\3O\3O\7\u00b4")
        buf.write("\u0108\u0114\u0218\u0221\2P\3\3\5\2\7\2\t\4\13\2\r\5\17")
        buf.write("\2\21\2\23\6\25\2\27\2\31\7\33\2\35\b\37\2!\2#\2%\2\'")
        buf.write("\2)\2+\2-\2/\2\61\2\63\2\65\2\67\29\2;\t=\n?\13A\fC\r")
        buf.write("E\16G\17I\20K\21M\22O\23Q\24S\25U\26W\27Y\30[\31]\32_")
        buf.write("\33a\34c\35e\36g\37i k!m\"o#q$s%u&w\'y({)}*\177+\u0081")
        buf.write(",\u0083-\u0085.\u0087/\u0089\60\u008b\61\u008d\62\u008f")
        buf.write("\63\u0091\64\u0093\65\u0095\66\u0097\67\u00998\u009b9")
        buf.write("\u009d:\3\2\21\4\2\f\f\17\17\3\2\63;\3\2\62;\4\2GGgg\4")
        buf.write("\2$$^^\3\2$$\3\2))\3\2\n\n\3\2\16\16\3\2\17\17\3\2\f\f")
        buf.write("\3\2^^\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2")
        buf.write("\u0237\2\3\3\2\2\2\2\t\3\2\2\2\2\r\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\35\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?")
        buf.write("\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2")
        buf.write("I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2")
        buf.write("\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2")
        buf.write("\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2")
        buf.write("\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3")
        buf.write("\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y")
        buf.write("\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3")
        buf.write("\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2")
        buf.write("\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\3\u00a1\3\2\2\2\5\u00a5\3\2\2\2\7\u00ae\3\2\2")
        buf.write("\2\t\u00ce\3\2\2\2\13\u00d0\3\2\2\2\r\u00d6\3\2\2\2\17")
        buf.write("\u00d8\3\2\2\2\21\u00e9\3\2\2\2\23\u00f6\3\2\2\2\25\u00f8")
        buf.write("\3\2\2\2\27\u00fe\3\2\2\2\31\u0103\3\2\2\2\33\u010e\3")
        buf.write("\2\2\2\35\u011a\3\2\2\2\37\u0123\3\2\2\2!\u012a\3\2\2")
        buf.write("\2#\u0131\3\2\2\2%\u0138\3\2\2\2\'\u0141\3\2\2\2)\u0143")
        buf.write("\3\2\2\2+\u0145\3\2\2\2-\u0147\3\2\2\2/\u0149\3\2\2\2")
        buf.write("\61\u014b\3\2\2\2\63\u014d\3\2\2\2\65\u014f\3\2\2\2\67")
        buf.write("\u0151\3\2\2\29\u0153\3\2\2\2;\u0156\3\2\2\2=\u015b\3")
        buf.write("\2\2\2?\u0161\3\2\2\2A\u0169\3\2\2\2C\u016e\3\2\2\2E\u0174")
        buf.write("\3\2\2\2G\u017a\3\2\2\2I\u0181\3\2\2\2K\u0185\3\2\2\2")
        buf.write("M\u018d\3\2\2\2O\u0191\3\2\2\2Q\u0198\3\2\2\2S\u01a1\3")
        buf.write("\2\2\2U\u01a4\3\2\2\2W\u01ad\3\2\2\2Y\u01b0\3\2\2\2[\u01b5")
        buf.write("\3\2\2\2]\u01b8\3\2\2\2_\u01be\3\2\2\2a\u01c6\3\2\2\2")
        buf.write("c\u01c8\3\2\2\2e\u01ca\3\2\2\2g\u01cc\3\2\2\2i\u01ce\3")
        buf.write("\2\2\2k\u01d0\3\2\2\2m\u01d2\3\2\2\2o\u01d4\3\2\2\2q\u01d7")
        buf.write("\3\2\2\2s\u01da\3\2\2\2u\u01dc\3\2\2\2w\u01df\3\2\2\2")
        buf.write("y\u01e2\3\2\2\2{\u01e5\3\2\2\2}\u01e8\3\2\2\2\177\u01eb")
        buf.write("\3\2\2\2\u0081\u01ed\3\2\2\2\u0083\u01ef\3\2\2\2\u0085")
        buf.write("\u01f1\3\2\2\2\u0087\u01f3\3\2\2\2\u0089\u01f5\3\2\2\2")
        buf.write("\u008b\u01f7\3\2\2\2\u008d\u01f9\3\2\2\2\u008f\u01fb\3")
        buf.write("\2\2\2\u0091\u01fd\3\2\2\2\u0093\u01ff\3\2\2\2\u0095\u0202")
        buf.write("\3\2\2\2\u0097\u020d\3\2\2\2\u0099\u0213\3\2\2\2\u009b")
        buf.write("\u0221\3\2\2\2\u009d\u0227\3\2\2\2\u009f\u00a2\5\5\3\2")
        buf.write("\u00a0\u00a2\5\7\4\2\u00a1\u009f\3\2\2\2\u00a1\u00a0\3")
        buf.write("\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\b\2\2\2\u00a4\4")
        buf.write("\3\2\2\2\u00a5\u00a6\7\61\2\2\u00a6\u00a7\7\61\2\2\u00a7")
        buf.write("\u00ab\3\2\2\2\u00a8\u00aa\n\2\2\2\u00a9\u00a8\3\2\2\2")
        buf.write("\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac\3")
        buf.write("\2\2\2\u00ac\6\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00af")
        buf.write("\7\61\2\2\u00af\u00b0\7,\2\2\u00b0\u00b4\3\2\2\2\u00b1")
        buf.write("\u00b3\13\2\2\2\u00b2\u00b1\3\2\2\2\u00b3\u00b6\3\2\2")
        buf.write("\2\u00b4\u00b5\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b5\u00b7")
        buf.write("\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b7\u00b8\7,\2\2\u00b8")
        buf.write("\u00b9\7\61\2\2\u00b9\b\3\2\2\2\u00ba\u00cf\7\62\2\2\u00bb")
        buf.write("\u00bf\t\3\2\2\u00bc\u00be\t\4\2\2\u00bd\u00bc\3\2\2\2")
        buf.write("\u00be\u00c1\3\2\2\2\u00bf\u00bd\3\2\2\2\u00bf\u00c0\3")
        buf.write("\2\2\2\u00c0\u00ca\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c2\u00c4")
        buf.write("\5\13\6\2\u00c3\u00c5\t\4\2\2\u00c4\u00c3\3\2\2\2\u00c5")
        buf.write("\u00c6\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2")
        buf.write("\u00c7\u00c9\3\2\2\2\u00c8\u00c2\3\2\2\2\u00c9\u00cc\3")
        buf.write("\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cd")
        buf.write("\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00cf\b\5\3\2\u00ce")
        buf.write("\u00ba\3\2\2\2\u00ce\u00bb\3\2\2\2\u00cf\n\3\2\2\2\u00d0")
        buf.write("\u00d1\7a\2\2\u00d1\f\3\2\2\2\u00d2\u00d7\5\21\t\2\u00d3")
        buf.write("\u00d4\5\17\b\2\u00d4\u00d5\b\7\4\2\u00d5\u00d7\3\2\2")
        buf.write("\2\u00d6\u00d2\3\2\2\2\u00d6\u00d3\3\2\2\2\u00d7\16\3")
        buf.write("\2\2\2\u00d8\u00d9\5\t\5\2\u00d9\u00db\5\177@\2\u00da")
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
        buf.write("\u0102\7g\2\2\u0102\30\3\2\2\2\u0103\u0108\5)\25\2\u0104")
        buf.write("\u0107\n\6\2\2\u0105\u0107\5\33\16\2\u0106\u0104\3\2\2")
        buf.write("\2\u0106\u0105\3\2\2\2\u0107\u010a\3\2\2\2\u0108\u0109")
        buf.write("\3\2\2\2\u0108\u0106\3\2\2\2\u0109\u010b\3\2\2\2\u010a")
        buf.write("\u0108\3\2\2\2\u010b\u010c\5)\25\2\u010c\u010d\b\r\5\2")
        buf.write("\u010d\32\3\2\2\2\u010e\u010f\7^\2\2\u010f\u0110\7$\2")
        buf.write("\2\u0110\u0114\3\2\2\2\u0111\u0113\13\2\2\2\u0112\u0111")
        buf.write("\3\2\2\2\u0113\u0116\3\2\2\2\u0114\u0115\3\2\2\2\u0114")
        buf.write("\u0112\3\2\2\2\u0115\u0117\3\2\2\2\u0116\u0114\3\2\2\2")
        buf.write("\u0117\u0118\7^\2\2\u0118\u0119\7$\2\2\u0119\34\3\2\2")
        buf.write("\2\u011a\u011c\5\u0091I\2\u011b\u011d\5\37\20\2\u011c")
        buf.write("\u011b\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011e\3\2\2\2")
        buf.write("\u011e\u011f\5\u0093J\2\u011f\36\3\2\2\2\u0120\u0124\5")
        buf.write("!\21\2\u0121\u0124\5#\22\2\u0122\u0124\5%\23\2\u0123\u0120")
        buf.write("\3\2\2\2\u0123\u0121\3\2\2\2\u0123\u0122\3\2\2\2\u0124")
        buf.write(" \3\2\2\2\u0125\u0126\5\t\5\2\u0126\u0127\5\u0081A\2\u0127")
        buf.write("\u0128\5!\21\2\u0128\u012b\3\2\2\2\u0129\u012b\5\t\5\2")
        buf.write("\u012a\u0125\3\2\2\2\u012a\u0129\3\2\2\2\u012b\"\3\2\2")
        buf.write("\2\u012c\u012d\5\r\7\2\u012d\u012e\5\u0081A\2\u012e\u012f")
        buf.write("\5#\22\2\u012f\u0132\3\2\2\2\u0130\u0132\5\r\7\2\u0131")
        buf.write("\u012c\3\2\2\2\u0131\u0130\3\2\2\2\u0132$\3\2\2\2\u0133")
        buf.write("\u0134\5\31\r\2\u0134\u0135\5\u0081A\2\u0135\u0136\5%")
        buf.write("\23\2\u0136\u0139\3\2\2\2\u0137\u0139\5\31\r\2\u0138\u0133")
        buf.write("\3\2\2\2\u0138\u0137\3\2\2\2\u0139&\3\2\2\2\u013a\u0142")
        buf.write("\5-\27\2\u013b\u0142\5/\30\2\u013c\u0142\5\61\31\2\u013d")
        buf.write("\u0142\5\63\32\2\u013e\u0142\5\65\33\2\u013f\u0142\59")
        buf.write("\35\2\u0140\u0142\5\67\34\2\u0141\u013a\3\2\2\2\u0141")
        buf.write("\u013b\3\2\2\2\u0141\u013c\3\2\2\2\u0141\u013d\3\2\2\2")
        buf.write("\u0141\u013e\3\2\2\2\u0141\u013f\3\2\2\2\u0141\u0140\3")
        buf.write("\2\2\2\u0142(\3\2\2\2\u0143\u0144\t\7\2\2\u0144*\3\2\2")
        buf.write("\2\u0145\u0146\t\b\2\2\u0146,\3\2\2\2\u0147\u0148\t\t")
        buf.write("\2\2\u0148.\3\2\2\2\u0149\u014a\t\n\2\2\u014a\60\3\2\2")
        buf.write("\2\u014b\u014c\t\13\2\2\u014c\62\3\2\2\2\u014d\u014e\t")
        buf.write("\f\2\2\u014e\64\3\2\2\2\u014f\u0150\7)\2\2\u0150\66\3")
        buf.write("\2\2\2\u0151\u0152\t\r\2\2\u01528\3\2\2\2\u0153\u0154")
        buf.write("\7^\2\2\u0154\u0155\7$\2\2\u0155:\3\2\2\2\u0156\u0157")
        buf.write("\7c\2\2\u0157\u0158\7w\2\2\u0158\u0159\7v\2\2\u0159\u015a")
        buf.write("\7q\2\2\u015a<\3\2\2\2\u015b\u015c\7d\2\2\u015c\u015d")
        buf.write("\7t\2\2\u015d\u015e\7g\2\2\u015e\u015f\7c\2\2\u015f\u0160")
        buf.write("\7m\2\2\u0160>\3\2\2\2\u0161\u0162\7k\2\2\u0162\u0163")
        buf.write("\7p\2\2\u0163\u0164\7v\2\2\u0164\u0165\7g\2\2\u0165\u0166")
        buf.write("\7i\2\2\u0166\u0167\7g\2\2\u0167\u0168\7t\2\2\u0168@\3")
        buf.write("\2\2\2\u0169\u016a\7x\2\2\u016a\u016b\7q\2\2\u016b\u016c")
        buf.write("\7k\2\2\u016c\u016d\7f\2\2\u016dB\3\2\2\2\u016e\u016f")
        buf.write("\7c\2\2\u016f\u0170\7t\2\2\u0170\u0171\7t\2\2\u0171\u0172")
        buf.write("\7c\2\2\u0172\u0173\7{\2\2\u0173D\3\2\2\2\u0174\u0175")
        buf.write("\7h\2\2\u0175\u0176\7n\2\2\u0176\u0177\7q\2\2\u0177\u0178")
        buf.write("\7c\2\2\u0178\u0179\7v\2\2\u0179F\3\2\2\2\u017a\u017b")
        buf.write("\7t\2\2\u017b\u017c\7g\2\2\u017c\u017d\7v\2\2\u017d\u017e")
        buf.write("\7w\2\2\u017e\u017f\7t\2\2\u017f\u0180\7p\2\2\u0180H\3")
        buf.write("\2\2\2\u0181\u0182\7q\2\2\u0182\u0183\7w\2\2\u0183\u0184")
        buf.write("\7v\2\2\u0184J\3\2\2\2\u0185\u0186\7d\2\2\u0186\u0187")
        buf.write("\7q\2\2\u0187\u0188\7q\2\2\u0188\u0189\7n\2\2\u0189\u018a")
        buf.write("\7g\2\2\u018a\u018b\7c\2\2\u018b\u018c\7p\2\2\u018cL\3")
        buf.write("\2\2\2\u018d\u018e\7h\2\2\u018e\u018f\7q\2\2\u018f\u0190")
        buf.write("\7t\2\2\u0190N\3\2\2\2\u0191\u0192\7u\2\2\u0192\u0193")
        buf.write("\7v\2\2\u0193\u0194\7t\2\2\u0194\u0195\7k\2\2\u0195\u0196")
        buf.write("\7p\2\2\u0196\u0197\7i\2\2\u0197P\3\2\2\2\u0198\u0199")
        buf.write("\7e\2\2\u0199\u019a\7q\2\2\u019a\u019b\7p\2\2\u019b\u019c")
        buf.write("\7v\2\2\u019c\u019d\7k\2\2\u019d\u019e\7p\2\2\u019e\u019f")
        buf.write("\7w\2\2\u019f\u01a0\7g\2\2\u01a0R\3\2\2\2\u01a1\u01a2")
        buf.write("\7f\2\2\u01a2\u01a3\7q\2\2\u01a3T\3\2\2\2\u01a4\u01a5")
        buf.write("\7h\2\2\u01a5\u01a6\7w\2\2\u01a6\u01a7\7p\2\2\u01a7\u01a8")
        buf.write("\7e\2\2\u01a8\u01a9\7v\2\2\u01a9\u01aa\7k\2\2\u01aa\u01ab")
        buf.write("\7q\2\2\u01ab\u01ac\7p\2\2\u01acV\3\2\2\2\u01ad\u01ae")
        buf.write("\7q\2\2\u01ae\u01af\7h\2\2\u01afX\3\2\2\2\u01b0\u01b1")
        buf.write("\7g\2\2\u01b1\u01b2\7n\2\2\u01b2\u01b3\7u\2\2\u01b3\u01b4")
        buf.write("\7g\2\2\u01b4Z\3\2\2\2\u01b5\u01b6\7k\2\2\u01b6\u01b7")
        buf.write("\7h\2\2\u01b7\\\3\2\2\2\u01b8\u01b9\7y\2\2\u01b9\u01ba")
        buf.write("\7j\2\2\u01ba\u01bb\7k\2\2\u01bb\u01bc\7n\2\2\u01bc\u01bd")
        buf.write("\7g\2\2\u01bd^\3\2\2\2\u01be\u01bf\7k\2\2\u01bf\u01c0")
        buf.write("\7p\2\2\u01c0\u01c1\7j\2\2\u01c1\u01c2\7g\2\2\u01c2\u01c3")
        buf.write("\7t\2\2\u01c3\u01c4\7k\2\2\u01c4\u01c5\7v\2\2\u01c5`\3")
        buf.write("\2\2\2\u01c6\u01c7\7-\2\2\u01c7b\3\2\2\2\u01c8\u01c9\7")
        buf.write("/\2\2\u01c9d\3\2\2\2\u01ca\u01cb\7,\2\2\u01cbf\3\2\2\2")
        buf.write("\u01cc\u01cd\7\61\2\2\u01cdh\3\2\2\2\u01ce\u01cf\7\'\2")
        buf.write("\2\u01cfj\3\2\2\2\u01d0\u01d1\7>\2\2\u01d1l\3\2\2\2\u01d2")
        buf.write("\u01d3\7@\2\2\u01d3n\3\2\2\2\u01d4\u01d5\7>\2\2\u01d5")
        buf.write("\u01d6\7?\2\2\u01d6p\3\2\2\2\u01d7\u01d8\7@\2\2\u01d8")
        buf.write("\u01d9\7?\2\2\u01d9r\3\2\2\2\u01da\u01db\7#\2\2\u01db")
        buf.write("t\3\2\2\2\u01dc\u01dd\7(\2\2\u01dd\u01de\7(\2\2\u01de")
        buf.write("v\3\2\2\2\u01df\u01e0\7~\2\2\u01e0\u01e1\7~\2\2\u01e1")
        buf.write("x\3\2\2\2\u01e2\u01e3\7?\2\2\u01e3\u01e4\7?\2\2\u01e4")
        buf.write("z\3\2\2\2\u01e5\u01e6\7#\2\2\u01e6\u01e7\7?\2\2\u01e7")
        buf.write("|\3\2\2\2\u01e8\u01e9\7<\2\2\u01e9\u01ea\7<\2\2\u01ea")
        buf.write("~\3\2\2\2\u01eb\u01ec\7\60\2\2\u01ec\u0080\3\2\2\2\u01ed")
        buf.write("\u01ee\7.\2\2\u01ee\u0082\3\2\2\2\u01ef\u01f0\7=\2\2\u01f0")
        buf.write("\u0084\3\2\2\2\u01f1\u01f2\7?\2\2\u01f2\u0086\3\2\2\2")
        buf.write("\u01f3\u01f4\7<\2\2\u01f4\u0088\3\2\2\2\u01f5\u01f6\7")
        buf.write("*\2\2\u01f6\u008a\3\2\2\2\u01f7\u01f8\7+\2\2\u01f8\u008c")
        buf.write("\3\2\2\2\u01f9\u01fa\7]\2\2\u01fa\u008e\3\2\2\2\u01fb")
        buf.write("\u01fc\7_\2\2\u01fc\u0090\3\2\2\2\u01fd\u01fe\7}\2\2\u01fe")
        buf.write("\u0092\3\2\2\2\u01ff\u0200\7\177\2\2\u0200\u0094\3\2\2")
        buf.write("\2\u0201\u0203\t\16\2\2\u0202\u0201\3\2\2\2\u0203\u0204")
        buf.write("\3\2\2\2\u0204\u0202\3\2\2\2\u0204\u0205\3\2\2\2\u0205")
        buf.write("\u0209\3\2\2\2\u0206\u0208\t\17\2\2\u0207\u0206\3\2\2")
        buf.write("\2\u0208\u020b\3\2\2\2\u0209\u0207\3\2\2\2\u0209\u020a")
        buf.write("\3\2\2\2\u020a\u0096\3\2\2\2\u020b\u0209\3\2\2\2\u020c")
        buf.write("\u020e\t\20\2\2\u020d\u020c\3\2\2\2\u020e\u020f\3\2\2")
        buf.write("\2\u020f\u020d\3\2\2\2\u020f\u0210\3\2\2\2\u0210\u0211")
        buf.write("\3\2\2\2\u0211\u0212\bL\2\2\u0212\u0098\3\2\2\2\u0213")
        buf.write("\u0218\7$\2\2\u0214\u0217\n\6\2\2\u0215\u0217\5\33\16")
        buf.write("\2\u0216\u0214\3\2\2\2\u0216\u0215\3\2\2\2\u0217\u021a")
        buf.write("\3\2\2\2\u0218\u0219\3\2\2\2\u0218\u0216\3\2\2\2\u0219")
        buf.write("\u021b\3\2\2\2\u021a\u0218\3\2\2\2\u021b\u021c\bM\6\2")
        buf.write("\u021c\u009a\3\2\2\2\u021d\u0220\n\6\2\2\u021e\u0220\5")
        buf.write("\33\16\2\u021f\u021d\3\2\2\2\u021f\u021e\3\2\2\2\u0220")
        buf.write("\u0223\3\2\2\2\u0221\u0222\3\2\2\2\u0221\u021f\3\2\2\2")
        buf.write("\u0222\u0224\3\2\2\2\u0223\u0221\3\2\2\2\u0224\u0225\7")
        buf.write("$\2\2\u0225\u0226\bN\7\2\u0226\u009c\3\2\2\2\u0227\u0228")
        buf.write("\13\2\2\2\u0228\u0229\bO\b\2\u0229\u009e\3\2\2\2!\2\u00a1")
        buf.write("\u00ab\u00b4\u00bf\u00c6\u00ca\u00ce\u00d6\u00dd\u00e3")
        buf.write("\u00e6\u00eb\u00f2\u00f6\u0106\u0108\u0114\u011c\u0123")
        buf.write("\u012a\u0131\u0138\u0141\u0204\u0209\u020f\u0216\u0218")
        buf.write("\u021f\u0221\t\b\2\2\3\5\2\3\7\3\3\r\4\3M\5\3N\6\3O\7")
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
    PLUS = 26
    MINUS = 27
    MUL = 28
    DIV = 29
    MOD = 30
    LESS = 31
    GREATER = 32
    LTE = 33
    GTE = 34
    NOT = 35
    AND = 36
    OR = 37
    EQUAL_TO = 38
    NOT_EQUAL = 39
    CONCAT = 40
    PERIOD = 41
    COMMA = 42
    SEMI = 43
    EQUAL = 44
    COLON = 45
    LB = 46
    RB = 47
    LSB = 48
    RSB = 49
    LCB = 50
    RCB = 51
    IDENTIFIER = 52
    WS = 53
    UNCLOSE_STRING = 54
    ILLEGAL_ESCAPE = 55
    ERROR_CHAR = 56

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
            "COMMENT", "INTEGER_LIT", "FLOAT_LIT", "BOOLEAN_LIT", "STRING_LIT", 
            "ARRAY_LIT", "AUTO", "BREAK", "INTEGER", "VOID", "ARRAY", "FLOAT", 
            "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", 
            "FUNCTION", "OF", "ELSE", "IF", "WHILE", "INHERIT", "PLUS", 
            "MINUS", "MUL", "DIV", "MOD", "LESS", "GREATER", "LTE", "GTE", 
            "NOT", "AND", "OR", "EQUAL_TO", "NOT_EQUAL", "CONCAT", "PERIOD", 
            "COMMA", "SEMI", "EQUAL", "COLON", "LB", "RB", "LSB", "RSB", 
            "LCB", "RCB", "IDENTIFIER", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "COMMENT", "SingleLineComment", "MultiLineComment", "INTEGER_LIT", 
                  "UNDERSCORE", "FLOAT_LIT", "DECPART", "EXPPART", "BOOLEAN_LIT", 
                  "FALSE", "TRUE", "STRING_LIT", "SUBSTRING", "ARRAY_LIT", 
                  "EXPS", "INT_TYPE", "FLOAT_TYPE", "STRINGLIST", "Escape_Sequence", 
                  "DUO_QUOTE", "SINGLE_QUOTE", "BackSpace", "FormFeed", 
                  "CarriageReturn", "NewLine", "SingleQuote", "BackSlash", 
                  "Dou_quote", "AUTO", "BREAK", "INTEGER", "VOID", "ARRAY", 
                  "FLOAT", "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", 
                  "CONTINUE", "DO", "FUNCTION", "OF", "ELSE", "IF", "WHILE", 
                  "INHERIT", "PLUS", "MINUS", "MUL", "DIV", "MOD", "LESS", 
                  "GREATER", "LTE", "GTE", "NOT", "AND", "OR", "EQUAL_TO", 
                  "NOT_EQUAL", "CONCAT", "PERIOD", "COMMA", "SEMI", "EQUAL", 
                  "COLON", "LB", "RB", "LSB", "RSB", "LCB", "RCB", "IDENTIFIER", 
                  "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[11] = self.STRING_LIT_action 
            actions[75] = self.UNCLOSE_STRING_action 
            actions[76] = self.ILLEGAL_ESCAPE_action 
            actions[77] = self.ERROR_CHAR_action 
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
     


