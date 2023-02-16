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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2!")
        buf.write("\u021f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\3\2\3\2\5\2\u00a2\n\2\3\3\3\3\3\3")
        buf.write("\3\3\7\3\u00a8\n\3\f\3\16\3\u00ab\13\3\3\4\3\4\3\4\3\4")
        buf.write("\7\4\u00b1\n\4\f\4\16\4\u00b4\13\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\7\5\u00bc\n\5\f\5\16\5\u00bf\13\5\3\5\3\5\6\5\u00c3")
        buf.write("\n\5\r\5\16\5\u00c4\7\5\u00c7\n\5\f\5\16\5\u00ca\13\5")
        buf.write("\3\5\5\5\u00cd\n\5\3\6\3\6\3\7\3\7\3\7\3\7\5\7\u00d5\n")
        buf.write("\7\3\b\3\b\3\b\6\b\u00da\n\b\r\b\16\b\u00db\3\b\3\b\7")
        buf.write("\b\u00e0\n\b\f\b\16\b\u00e3\13\b\5\b\u00e5\n\b\3\t\6\t")
        buf.write("\u00e8\n\t\r\t\16\t\u00e9\3\t\3\t\3\t\6\t\u00ef\n\t\r")
        buf.write("\t\16\t\u00f0\3\n\3\n\5\n\u00f5\n\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\7\r\u0105\n")
        buf.write("\r\f\r\16\r\u0108\13\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\7\16\u0111\n\16\f\16\16\16\u0114\13\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\5\17\u011b\n\17\3\17\3\17\3\20\3\20\5\20\u0121")
        buf.write("\n\20\3\21\3\21\3\21\3\21\7\21\u0127\n\21\f\21\16\21\u012a")
        buf.write("\13\21\3\21\5\21\u012d\n\21\3\22\3\22\3\22\3\22\7\22\u0133")
        buf.write("\n\22\f\22\16\22\u0136\13\22\3\22\5\22\u0139\n\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0142\n\23\3\24\3")
        buf.write("\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3$\3$\3")
        buf.write("$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3*")
        buf.write("\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3,\3,\3,\3,\3,\3-\3")
        buf.write("-\3-\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3/\3\60\3")
        buf.write("\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\67\3\67\3\67\38\38\38\39\39\39\3:\3")
        buf.write(":\3;\3;\3<\3<\3<\3=\3=\3=\3>\3>\3>\3?\3?\3@\3@\3A\3A\3")
        buf.write("B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\6J\u0203")
        buf.write("\nJ\rJ\16J\u0204\3J\7J\u0208\nJ\fJ\16J\u020b\13J\3K\6")
        buf.write("K\u020e\nK\rK\16K\u020f\3L\6L\u0213\nL\rL\16L\u0214\3")
        buf.write("L\3L\3M\3M\3M\3N\3N\3O\3O\5\u00b2\u0106\u0112\2P\3\3\5")
        buf.write("\2\7\2\t\4\13\2\r\5\17\2\21\2\23\6\25\2\27\2\31\7\33\2")
        buf.write("\35\b\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63\2\65\2\67")
        buf.write("\29\t;\n=\13?\fA\rC\16E\17G\20I\21K\22M\23O\24Q\25S\26")
        buf.write("U\27W\30Y\31[\32]\33_\2a\2c\2e\2g\2i\2k\2m\2o\2q\2s\2")
        buf.write("u\2w\2y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087\2")
        buf.write("\u0089\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093\34\u0095")
        buf.write("\35\u0097\36\u0099\37\u009b \u009d!\3\2\21\4\2\f\f\17")
        buf.write("\17\3\2\63;\3\2\62;\4\2GGgg\4\2$$^^\3\2$$\3\2))\3\2\n")
        buf.write("\n\3\2\16\16\3\2\17\17\3\2\f\f\3\2^^\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\5\2\13\f\17\17\"\"\2\u0210\2\3\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\23\3\2\2\2\2\31\3\2\2\2\2\35\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2")
        buf.write("U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2")
        buf.write("\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099")
        buf.write("\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\3\u00a1\3\2\2")
        buf.write("\2\5\u00a3\3\2\2\2\7\u00ac\3\2\2\2\t\u00cc\3\2\2\2\13")
        buf.write("\u00ce\3\2\2\2\r\u00d4\3\2\2\2\17\u00d6\3\2\2\2\21\u00e7")
        buf.write("\3\2\2\2\23\u00f4\3\2\2\2\25\u00f6\3\2\2\2\27\u00fc\3")
        buf.write("\2\2\2\31\u0101\3\2\2\2\33\u010c\3\2\2\2\35\u0118\3\2")
        buf.write("\2\2\37\u0120\3\2\2\2!\u012c\3\2\2\2#\u0138\3\2\2\2%\u0141")
        buf.write("\3\2\2\2\'\u0143\3\2\2\2)\u0145\3\2\2\2+\u0147\3\2\2\2")
        buf.write("-\u0149\3\2\2\2/\u014b\3\2\2\2\61\u014d\3\2\2\2\63\u014f")
        buf.write("\3\2\2\2\65\u0151\3\2\2\2\67\u0153\3\2\2\29\u0156\3\2")
        buf.write("\2\2;\u015b\3\2\2\2=\u0161\3\2\2\2?\u0169\3\2\2\2A\u016e")
        buf.write("\3\2\2\2C\u0174\3\2\2\2E\u017a\3\2\2\2G\u0181\3\2\2\2")
        buf.write("I\u0185\3\2\2\2K\u018d\3\2\2\2M\u0191\3\2\2\2O\u0198\3")
        buf.write("\2\2\2Q\u01a1\3\2\2\2S\u01a4\3\2\2\2U\u01ad\3\2\2\2W\u01b0")
        buf.write("\3\2\2\2Y\u01b5\3\2\2\2[\u01b8\3\2\2\2]\u01be\3\2\2\2")
        buf.write("_\u01c6\3\2\2\2a\u01c8\3\2\2\2c\u01ca\3\2\2\2e\u01cc\3")
        buf.write("\2\2\2g\u01ce\3\2\2\2i\u01d0\3\2\2\2k\u01d2\3\2\2\2m\u01d5")
        buf.write("\3\2\2\2o\u01d8\3\2\2\2q\u01db\3\2\2\2s\u01de\3\2\2\2")
        buf.write("u\u01e0\3\2\2\2w\u01e2\3\2\2\2y\u01e5\3\2\2\2{\u01e8\3")
        buf.write("\2\2\2}\u01eb\3\2\2\2\177\u01ed\3\2\2\2\u0081\u01ef\3")
        buf.write("\2\2\2\u0083\u01f1\3\2\2\2\u0085\u01f3\3\2\2\2\u0087\u01f5")
        buf.write("\3\2\2\2\u0089\u01f7\3\2\2\2\u008b\u01f9\3\2\2\2\u008d")
        buf.write("\u01fb\3\2\2\2\u008f\u01fd\3\2\2\2\u0091\u01ff\3\2\2\2")
        buf.write("\u0093\u0202\3\2\2\2\u0095\u020d\3\2\2\2\u0097\u0212\3")
        buf.write("\2\2\2\u0099\u0218\3\2\2\2\u009b\u021b\3\2\2\2\u009d\u021d")
        buf.write("\3\2\2\2\u009f\u00a2\5\5\3\2\u00a0\u00a2\5\7\4\2\u00a1")
        buf.write("\u009f\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2\4\3\2\2\2\u00a3")
        buf.write("\u00a4\7\61\2\2\u00a4\u00a5\7\61\2\2\u00a5\u00a9\3\2\2")
        buf.write("\2\u00a6\u00a8\n\2\2\2\u00a7\u00a6\3\2\2\2\u00a8\u00ab")
        buf.write("\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa")
        buf.write("\6\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00ad\7\61\2\2\u00ad")
        buf.write("\u00ae\7,\2\2\u00ae\u00b2\3\2\2\2\u00af\u00b1\13\2\2\2")
        buf.write("\u00b0\u00af\3\2\2\2\u00b1\u00b4\3\2\2\2\u00b2\u00b3\3")
        buf.write("\2\2\2\u00b2\u00b0\3\2\2\2\u00b3\u00b5\3\2\2\2\u00b4\u00b2")
        buf.write("\3\2\2\2\u00b5\u00b6\7,\2\2\u00b6\u00b7\7\61\2\2\u00b7")
        buf.write("\b\3\2\2\2\u00b8\u00cd\7\62\2\2\u00b9\u00bd\t\3\2\2\u00ba")
        buf.write("\u00bc\t\4\2\2\u00bb\u00ba\3\2\2\2\u00bc\u00bf\3\2\2\2")
        buf.write("\u00bd\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00c8\3")
        buf.write("\2\2\2\u00bf\u00bd\3\2\2\2\u00c0\u00c2\5\13\6\2\u00c1")
        buf.write("\u00c3\t\4\2\2\u00c2\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2")
        buf.write("\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c7\3")
        buf.write("\2\2\2\u00c6\u00c0\3\2\2\2\u00c7\u00ca\3\2\2\2\u00c8\u00c6")
        buf.write("\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00cb\3\2\2\2\u00ca")
        buf.write("\u00c8\3\2\2\2\u00cb\u00cd\b\5\2\2\u00cc\u00b8\3\2\2\2")
        buf.write("\u00cc\u00b9\3\2\2\2\u00cd\n\3\2\2\2\u00ce\u00cf\7a\2")
        buf.write("\2\u00cf\f\3\2\2\2\u00d0\u00d5\5\21\t\2\u00d1\u00d2\5")
        buf.write("\17\b\2\u00d2\u00d3\b\7\3\2\u00d3\u00d5\3\2\2\2\u00d4")
        buf.write("\u00d0\3\2\2\2\u00d4\u00d1\3\2\2\2\u00d5\16\3\2\2\2\u00d6")
        buf.write("\u00d7\5\t\5\2\u00d7\u00d9\5}?\2\u00d8\u00da\t\4\2\2\u00d9")
        buf.write("\u00d8\3\2\2\2\u00da\u00db\3\2\2\2\u00db\u00d9\3\2\2\2")
        buf.write("\u00db\u00dc\3\2\2\2\u00dc\u00e4\3\2\2\2\u00dd\u00e1\t")
        buf.write("\5\2\2\u00de\u00e0\t\4\2\2\u00df\u00de\3\2\2\2\u00e0\u00e3")
        buf.write("\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2")
        buf.write("\u00e5\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e4\u00dd\3\2\2\2")
        buf.write("\u00e4\u00e5\3\2\2\2\u00e5\20\3\2\2\2\u00e6\u00e8\t\4")
        buf.write("\2\2\u00e7\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00e7")
        buf.write("\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb")
        buf.write("\u00ec\t\5\2\2\u00ec\u00ee\5a\61\2\u00ed\u00ef\t\4\2\2")
        buf.write("\u00ee\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00ee\3")
        buf.write("\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\22\3\2\2\2\u00f2\u00f5")
        buf.write("\5\25\13\2\u00f3\u00f5\5\27\f\2\u00f4\u00f2\3\2\2\2\u00f4")
        buf.write("\u00f3\3\2\2\2\u00f5\24\3\2\2\2\u00f6\u00f7\7h\2\2\u00f7")
        buf.write("\u00f8\7c\2\2\u00f8\u00f9\7n\2\2\u00f9\u00fa\7u\2\2\u00fa")
        buf.write("\u00fb\7g\2\2\u00fb\26\3\2\2\2\u00fc\u00fd\7v\2\2\u00fd")
        buf.write("\u00fe\7t\2\2\u00fe\u00ff\7w\2\2\u00ff\u0100\7g\2\2\u0100")
        buf.write("\30\3\2\2\2\u0101\u0106\5\'\24\2\u0102\u0105\n\6\2\2\u0103")
        buf.write("\u0105\5\33\16\2\u0104\u0102\3\2\2\2\u0104\u0103\3\2\2")
        buf.write("\2\u0105\u0108\3\2\2\2\u0106\u0107\3\2\2\2\u0106\u0104")
        buf.write("\3\2\2\2\u0107\u0109\3\2\2\2\u0108\u0106\3\2\2\2\u0109")
        buf.write("\u010a\5\'\24\2\u010a\u010b\b\r\4\2\u010b\32\3\2\2\2\u010c")
        buf.write("\u010d\7^\2\2\u010d\u010e\7$\2\2\u010e\u0112\3\2\2\2\u010f")
        buf.write("\u0111\13\2\2\2\u0110\u010f\3\2\2\2\u0111\u0114\3\2\2")
        buf.write("\2\u0112\u0113\3\2\2\2\u0112\u0110\3\2\2\2\u0113\u0115")
        buf.write("\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u0116\7^\2\2\u0116")
        buf.write("\u0117\7$\2\2\u0117\34\3\2\2\2\u0118\u011a\5\u008fH\2")
        buf.write("\u0119\u011b\5\37\20\2\u011a\u0119\3\2\2\2\u011a\u011b")
        buf.write("\3\2\2\2\u011b\u011c\3\2\2\2\u011c\u011d\5\u0091I\2\u011d")
        buf.write("\36\3\2\2\2\u011e\u0121\5!\21\2\u011f\u0121\5#\22\2\u0120")
        buf.write("\u011e\3\2\2\2\u0120\u011f\3\2\2\2\u0121 \3\2\2\2\u0122")
        buf.write("\u0128\5\u0095K\2\u0123\u0124\5\177@\2\u0124\u0125\5!")
        buf.write("\21\2\u0125\u0127\3\2\2\2\u0126\u0123\3\2\2\2\u0127\u012a")
        buf.write("\3\2\2\2\u0128\u0126\3\2\2\2\u0128\u0129\3\2\2\2\u0129")
        buf.write("\u012d\3\2\2\2\u012a\u0128\3\2\2\2\u012b\u012d\5\u0095")
        buf.write("K\2\u012c\u0122\3\2\2\2\u012c\u012b\3\2\2\2\u012d\"\3")
        buf.write("\2\2\2\u012e\u0134\5\31\r\2\u012f\u0130\5\177@\2\u0130")
        buf.write("\u0131\5#\22\2\u0131\u0133\3\2\2\2\u0132\u012f\3\2\2\2")
        buf.write("\u0133\u0136\3\2\2\2\u0134\u0132\3\2\2\2\u0134\u0135\3")
        buf.write("\2\2\2\u0135\u0139\3\2\2\2\u0136\u0134\3\2\2\2\u0137\u0139")
        buf.write("\5\31\r\2\u0138\u012e\3\2\2\2\u0138\u0137\3\2\2\2\u0139")
        buf.write("$\3\2\2\2\u013a\u0142\5+\26\2\u013b\u0142\5-\27\2\u013c")
        buf.write("\u0142\5/\30\2\u013d\u0142\5\61\31\2\u013e\u0142\5\63")
        buf.write("\32\2\u013f\u0142\5\67\34\2\u0140\u0142\5\65\33\2\u0141")
        buf.write("\u013a\3\2\2\2\u0141\u013b\3\2\2\2\u0141\u013c\3\2\2\2")
        buf.write("\u0141\u013d\3\2\2\2\u0141\u013e\3\2\2\2\u0141\u013f\3")
        buf.write("\2\2\2\u0141\u0140\3\2\2\2\u0142&\3\2\2\2\u0143\u0144")
        buf.write("\t\7\2\2\u0144(\3\2\2\2\u0145\u0146\t\b\2\2\u0146*\3\2")
        buf.write("\2\2\u0147\u0148\t\t\2\2\u0148,\3\2\2\2\u0149\u014a\t")
        buf.write("\n\2\2\u014a.\3\2\2\2\u014b\u014c\t\13\2\2\u014c\60\3")
        buf.write("\2\2\2\u014d\u014e\t\f\2\2\u014e\62\3\2\2\2\u014f\u0150")
        buf.write("\7)\2\2\u0150\64\3\2\2\2\u0151\u0152\t\r\2\2\u0152\66")
        buf.write("\3\2\2\2\u0153\u0154\7^\2\2\u0154\u0155\7$\2\2\u01558")
        buf.write("\3\2\2\2\u0156\u0157\7c\2\2\u0157\u0158\7w\2\2\u0158\u0159")
        buf.write("\7v\2\2\u0159\u015a\7q\2\2\u015a:\3\2\2\2\u015b\u015c")
        buf.write("\7d\2\2\u015c\u015d\7t\2\2\u015d\u015e\7g\2\2\u015e\u015f")
        buf.write("\7c\2\2\u015f\u0160\7m\2\2\u0160<\3\2\2\2\u0161\u0162")
        buf.write("\7k\2\2\u0162\u0163\7p\2\2\u0163\u0164\7v\2\2\u0164\u0165")
        buf.write("\7g\2\2\u0165\u0166\7i\2\2\u0166\u0167\7g\2\2\u0167\u0168")
        buf.write("\7t\2\2\u0168>\3\2\2\2\u0169\u016a\7x\2\2\u016a\u016b")
        buf.write("\7q\2\2\u016b\u016c\7k\2\2\u016c\u016d\7f\2\2\u016d@\3")
        buf.write("\2\2\2\u016e\u016f\7c\2\2\u016f\u0170\7t\2\2\u0170\u0171")
        buf.write("\7t\2\2\u0171\u0172\7c\2\2\u0172\u0173\7{\2\2\u0173B\3")
        buf.write("\2\2\2\u0174\u0175\7h\2\2\u0175\u0176\7n\2\2\u0176\u0177")
        buf.write("\7q\2\2\u0177\u0178\7c\2\2\u0178\u0179\7v\2\2\u0179D\3")
        buf.write("\2\2\2\u017a\u017b\7t\2\2\u017b\u017c\7g\2\2\u017c\u017d")
        buf.write("\7v\2\2\u017d\u017e\7w\2\2\u017e\u017f\7t\2\2\u017f\u0180")
        buf.write("\7p\2\2\u0180F\3\2\2\2\u0181\u0182\7q\2\2\u0182\u0183")
        buf.write("\7w\2\2\u0183\u0184\7v\2\2\u0184H\3\2\2\2\u0185\u0186")
        buf.write("\7d\2\2\u0186\u0187\7q\2\2\u0187\u0188\7q\2\2\u0188\u0189")
        buf.write("\7n\2\2\u0189\u018a\7g\2\2\u018a\u018b\7c\2\2\u018b\u018c")
        buf.write("\7p\2\2\u018cJ\3\2\2\2\u018d\u018e\7h\2\2\u018e\u018f")
        buf.write("\7q\2\2\u018f\u0190\7t\2\2\u0190L\3\2\2\2\u0191\u0192")
        buf.write("\7u\2\2\u0192\u0193\7v\2\2\u0193\u0194\7t\2\2\u0194\u0195")
        buf.write("\7k\2\2\u0195\u0196\7p\2\2\u0196\u0197\7i\2\2\u0197N\3")
        buf.write("\2\2\2\u0198\u0199\7e\2\2\u0199\u019a\7q\2\2\u019a\u019b")
        buf.write("\7p\2\2\u019b\u019c\7v\2\2\u019c\u019d\7k\2\2\u019d\u019e")
        buf.write("\7p\2\2\u019e\u019f\7w\2\2\u019f\u01a0\7g\2\2\u01a0P\3")
        buf.write("\2\2\2\u01a1\u01a2\7f\2\2\u01a2\u01a3\7q\2\2\u01a3R\3")
        buf.write("\2\2\2\u01a4\u01a5\7h\2\2\u01a5\u01a6\7w\2\2\u01a6\u01a7")
        buf.write("\7p\2\2\u01a7\u01a8\7e\2\2\u01a8\u01a9\7v\2\2\u01a9\u01aa")
        buf.write("\7k\2\2\u01aa\u01ab\7q\2\2\u01ab\u01ac\7p\2\2\u01acT\3")
        buf.write("\2\2\2\u01ad\u01ae\7q\2\2\u01ae\u01af\7h\2\2\u01afV\3")
        buf.write("\2\2\2\u01b0\u01b1\7g\2\2\u01b1\u01b2\7n\2\2\u01b2\u01b3")
        buf.write("\7u\2\2\u01b3\u01b4\7g\2\2\u01b4X\3\2\2\2\u01b5\u01b6")
        buf.write("\7k\2\2\u01b6\u01b7\7h\2\2\u01b7Z\3\2\2\2\u01b8\u01b9")
        buf.write("\7y\2\2\u01b9\u01ba\7j\2\2\u01ba\u01bb\7k\2\2\u01bb\u01bc")
        buf.write("\7n\2\2\u01bc\u01bd\7g\2\2\u01bd\\\3\2\2\2\u01be\u01bf")
        buf.write("\7k\2\2\u01bf\u01c0\7p\2\2\u01c0\u01c1\7j\2\2\u01c1\u01c2")
        buf.write("\7g\2\2\u01c2\u01c3\7t\2\2\u01c3\u01c4\7k\2\2\u01c4\u01c5")
        buf.write("\7v\2\2\u01c5^\3\2\2\2\u01c6\u01c7\7-\2\2\u01c7`\3\2\2")
        buf.write("\2\u01c8\u01c9\7/\2\2\u01c9b\3\2\2\2\u01ca\u01cb\7,\2")
        buf.write("\2\u01cbd\3\2\2\2\u01cc\u01cd\7\61\2\2\u01cdf\3\2\2\2")
        buf.write("\u01ce\u01cf\7\'\2\2\u01cfh\3\2\2\2\u01d0\u01d1\7#\2\2")
        buf.write("\u01d1j\3\2\2\2\u01d2\u01d3\7(\2\2\u01d3\u01d4\7(\2\2")
        buf.write("\u01d4l\3\2\2\2\u01d5\u01d6\7~\2\2\u01d6\u01d7\7~\2\2")
        buf.write("\u01d7n\3\2\2\2\u01d8\u01d9\7?\2\2\u01d9\u01da\7?\2\2")
        buf.write("\u01dap\3\2\2\2\u01db\u01dc\7#\2\2\u01dc\u01dd\7?\2\2")
        buf.write("\u01ddr\3\2\2\2\u01de\u01df\7>\2\2\u01dft\3\2\2\2\u01e0")
        buf.write("\u01e1\7@\2\2\u01e1v\3\2\2\2\u01e2\u01e3\7>\2\2\u01e3")
        buf.write("\u01e4\7?\2\2\u01e4x\3\2\2\2\u01e5\u01e6\7@\2\2\u01e6")
        buf.write("\u01e7\7?\2\2\u01e7z\3\2\2\2\u01e8\u01e9\7<\2\2\u01e9")
        buf.write("\u01ea\7<\2\2\u01ea|\3\2\2\2\u01eb\u01ec\7\60\2\2\u01ec")
        buf.write("~\3\2\2\2\u01ed\u01ee\7.\2\2\u01ee\u0080\3\2\2\2\u01ef")
        buf.write("\u01f0\7=\2\2\u01f0\u0082\3\2\2\2\u01f1\u01f2\7?\2\2\u01f2")
        buf.write("\u0084\3\2\2\2\u01f3\u01f4\7<\2\2\u01f4\u0086\3\2\2\2")
        buf.write("\u01f5\u01f6\7*\2\2\u01f6\u0088\3\2\2\2\u01f7\u01f8\7")
        buf.write("+\2\2\u01f8\u008a\3\2\2\2\u01f9\u01fa\7]\2\2\u01fa\u008c")
        buf.write("\3\2\2\2\u01fb\u01fc\7_\2\2\u01fc\u008e\3\2\2\2\u01fd")
        buf.write("\u01fe\7}\2\2\u01fe\u0090\3\2\2\2\u01ff\u0200\7\177\2")
        buf.write("\2\u0200\u0092\3\2\2\2\u0201\u0203\t\16\2\2\u0202\u0201")
        buf.write("\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0202\3\2\2\2\u0204")
        buf.write("\u0205\3\2\2\2\u0205\u0209\3\2\2\2\u0206\u0208\t\17\2")
        buf.write("\2\u0207\u0206\3\2\2\2\u0208\u020b\3\2\2\2\u0209\u0207")
        buf.write("\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u0094\3\2\2\2\u020b")
        buf.write("\u0209\3\2\2\2\u020c\u020e\t\4\2\2\u020d\u020c\3\2\2\2")
        buf.write("\u020e\u020f\3\2\2\2\u020f\u020d\3\2\2\2\u020f\u0210\3")
        buf.write("\2\2\2\u0210\u0096\3\2\2\2\u0211\u0213\t\20\2\2\u0212")
        buf.write("\u0211\3\2\2\2\u0213\u0214\3\2\2\2\u0214\u0212\3\2\2\2")
        buf.write("\u0214\u0215\3\2\2\2\u0215\u0216\3\2\2\2\u0216\u0217\b")
        buf.write("L\5\2\u0217\u0098\3\2\2\2\u0218\u0219\13\2\2\2\u0219\u021a")
        buf.write("\bM\6\2\u021a\u009a\3\2\2\2\u021b\u021c\13\2\2\2\u021c")
        buf.write("\u009c\3\2\2\2\u021d\u021e\13\2\2\2\u021e\u009e\3\2\2")
        buf.write("\2\37\2\u00a1\u00a9\u00b2\u00bd\u00c4\u00c8\u00cc\u00d4")
        buf.write("\u00db\u00e1\u00e4\u00e9\u00f0\u00f4\u0104\u0106\u0112")
        buf.write("\u011a\u0120\u0128\u012c\u0134\u0138\u0141\u0204\u0209")
        buf.write("\u020f\u0214\7\3\5\2\3\7\3\3\r\4\b\2\2\3M\5")
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
    IDENTIFIER = 26
    NUMBER = 27
    WS = 28
    ERROR_CHAR = 29
    UNCLOSE_STRING = 30
    ILLEGAL_ESCAPE = 31

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'integer'", "'void'", "'array'", "'float'", 
            "'return'", "'out'", "'boolean'", "'for'", "'string'", "'continue'", 
            "'do'", "'function'", "'of'", "'else'", "'if'", "'while'", "'inherit'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "INTEGER_LIT", "FLOAT_LIT", "BOOLEAN_LIT", "STRING_LIT", 
            "ARRAY_LIT", "AUTO", "BREAK", "INTEGER", "VOID", "ARRAY", "FLOAT", 
            "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", 
            "FUNCTION", "OF", "ELSE", "IF", "WHILE", "INHERIT", "IDENTIFIER", 
            "NUMBER", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMMENT", "SingleLineComment", "MultiLineComment", "INTEGER_LIT", 
                  "UNDERSCORE", "FLOAT_LIT", "DECPART", "EXPPART", "BOOLEAN_LIT", 
                  "FALSE", "TRUE", "STRING_LIT", "SUBSTRING", "ARRAY_LIT", 
                  "EXPS", "NUMLIST", "STRINGLIST", "Escape_Sequence", "DUO_QUOTE", 
                  "SINGLE_QUOTE", "BackSpace", "FormFeed", "CarriageReturn", 
                  "NewLine", "SingleQuote", "BackSlash", "Dou_quote", "AUTO", 
                  "BREAK", "INTEGER", "VOID", "ARRAY", "FLOAT", "RETURN", 
                  "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", "FUNCTION", 
                  "OF", "ELSE", "IF", "WHILE", "INHERIT", "PLUS", "MINUS", 
                  "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL_TO", "NOT_EQUAL", 
                  "LESS", "GREATER", "LESS_THAN_OR_EQUAL", "GREATER_THAN_OR_EQUAL", 
                  "SCOPE_RES", "PERIOD", "COMMA", "SEMI", "EQUAL", "COLON", 
                  "LB", "RB", "LSB", "RSB", "LCB", "RCB", "IDENTIFIER", 
                  "NUMBER", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[75] = self.ERROR_CHAR_action 
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
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


