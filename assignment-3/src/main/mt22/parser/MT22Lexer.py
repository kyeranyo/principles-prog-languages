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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u0262\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\5\13\u0107\n\13\3\13\3\13\3\f\3\f\3\f\3\f\7\f\u010f")
        buf.write("\n\f\f\f\16\f\u0112\13\f\3\r\3\r\3\r\3\r\7\r\u0118\n\r")
        buf.write("\f\r\16\r\u011b\13\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\7")
        buf.write("\16\u0124\n\16\f\16\16\16\u0127\13\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\7\17\u012e\n\17\f\17\16\17\u0131\13\17\3\17\3")
        buf.write("\17\6\17\u0135\n\17\r\17\16\17\u0136\7\17\u0139\n\17\f")
        buf.write("\17\16\17\u013c\13\17\3\17\5\17\u013f\n\17\3\20\3\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\5\21\u0150\n\21\3\21\3\21\3\22\3\22\7\22\u0156")
        buf.write("\n\22\f\22\16\22\u0159\13\22\3\23\3\23\5\23\u015d\n\23")
        buf.write("\3\23\6\23\u0160\n\23\r\23\16\23\u0161\3\24\3\24\5\24")
        buf.write("\u0166\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\27\3\27\3\27\7\27\u0176\n\27\f\27\16\27")
        buf.write("\u0179\13\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3")
        buf.write("\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3")
        buf.write("!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3$\3")
        buf.write("$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3")
        buf.write(")\3*\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3,\3,\3,\3,\3,\3")
        buf.write("-\3-\3-\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3/\3\60")
        buf.write("\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\3\67\38\38\38\39\39\3:\3:\3:\3;\3")
        buf.write(";\3;\3<\3<\3<\3=\3=\3=\3>\3>\3>\3?\3?\3@\3@\3A\3A\3B\3")
        buf.write("B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\6J\u0237")
        buf.write("\nJ\rJ\16J\u0238\3J\7J\u023c\nJ\fJ\16J\u023f\13J\3K\6")
        buf.write("K\u0242\nK\rK\16K\u0243\3K\3K\3L\3L\3L\7L\u024b\nL\fL")
        buf.write("\16L\u024e\13L\3L\5L\u0251\nL\3L\3L\3M\3M\3M\7M\u0258")
        buf.write("\nM\fM\16M\u025b\13M\3M\3M\3M\3N\3N\3N\5\u0119\u0125\u024c")
        buf.write("\2O\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\2")
        buf.write("\31\2\33\2\35\r\37\2!\16#\2%\2\'\17)\2+\2-\20/\2\61\2")
        buf.write("\63\2\65\2\67\29\21;\22=\23?\24A\25C\26E\27G\30I\31K\32")
        buf.write("M\33O\34Q\35S\36U\37W Y![\"]#_$a%c&e\'g(i)k*m+o,q-s.u")
        buf.write("/w\60y\61{\62}\63\177\64\u0081\65\u0083\66\u0085\67\u0087")
        buf.write("8\u00899\u008b:\u008d;\u008f<\u0091=\u0093>\u0095?\u0097")
        buf.write("@\u0099A\u009bB\3\2\20\4\2\f\f\17\17\3\2\63;\3\2\62;\4")
        buf.write("\2GGgg\4\2--//\5\2\f\f\17\17$$\n\2$$))^^ddhhppttvv\3\2")
        buf.write("$$\3\2))\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"")
        buf.write("\4\3\f\f\17\17\4\2$$^^\2\u026c\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2!\3\2\2\2\2\'\3\2\2\2\2-\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2")
        buf.write("u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2")
        buf.write("\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2")
        buf.write("\2\2\u009b\3\2\2\2\3\u009d\3\2\2\2\5\u00ac\3\2\2\2\7\u00b2")
        buf.write("\3\2\2\2\t\u00be\3\2\2\2\13\u00c9\3\2\2\2\r\u00d6\3\2")
        buf.write("\2\2\17\u00e1\3\2\2\2\21\u00eb\3\2\2\2\23\u00f8\3\2\2")
        buf.write("\2\25\u0106\3\2\2\2\27\u010a\3\2\2\2\31\u0113\3\2\2\2")
        buf.write("\33\u011f\3\2\2\2\35\u013e\3\2\2\2\37\u0140\3\2\2\2!\u014f")
        buf.write("\3\2\2\2#\u0153\3\2\2\2%\u015a\3\2\2\2\'\u0165\3\2\2\2")
        buf.write(")\u0167\3\2\2\2+\u016d\3\2\2\2-\u0172\3\2\2\2/\u017d\3")
        buf.write("\2\2\2\61\u0180\3\2\2\2\63\u0183\3\2\2\2\65\u0186\3\2")
        buf.write("\2\2\67\u0188\3\2\2\29\u018a\3\2\2\2;\u018f\3\2\2\2=\u0195")
        buf.write("\3\2\2\2?\u019d\3\2\2\2A\u01a2\3\2\2\2C\u01a8\3\2\2\2")
        buf.write("E\u01ae\3\2\2\2G\u01b5\3\2\2\2I\u01b9\3\2\2\2K\u01c1\3")
        buf.write("\2\2\2M\u01c5\3\2\2\2O\u01cc\3\2\2\2Q\u01d5\3\2\2\2S\u01d8")
        buf.write("\3\2\2\2U\u01e1\3\2\2\2W\u01e4\3\2\2\2Y\u01e9\3\2\2\2")
        buf.write("[\u01ec\3\2\2\2]\u01f2\3\2\2\2_\u01fa\3\2\2\2a\u01fc\3")
        buf.write("\2\2\2c\u01fe\3\2\2\2e\u0200\3\2\2\2g\u0202\3\2\2\2i\u0204")
        buf.write("\3\2\2\2k\u0206\3\2\2\2m\u0208\3\2\2\2o\u020b\3\2\2\2")
        buf.write("q\u020e\3\2\2\2s\u0210\3\2\2\2u\u0213\3\2\2\2w\u0216\3")
        buf.write("\2\2\2y\u0219\3\2\2\2{\u021c\3\2\2\2}\u021f\3\2\2\2\177")
        buf.write("\u0221\3\2\2\2\u0081\u0223\3\2\2\2\u0083\u0225\3\2\2\2")
        buf.write("\u0085\u0227\3\2\2\2\u0087\u0229\3\2\2\2\u0089\u022b\3")
        buf.write("\2\2\2\u008b\u022d\3\2\2\2\u008d\u022f\3\2\2\2\u008f\u0231")
        buf.write("\3\2\2\2\u0091\u0233\3\2\2\2\u0093\u0236\3\2\2\2\u0095")
        buf.write("\u0241\3\2\2\2\u0097\u0247\3\2\2\2\u0099\u0254\3\2\2\2")
        buf.write("\u009b\u025f\3\2\2\2\u009d\u009e\7r\2\2\u009e\u009f\7")
        buf.write("t\2\2\u009f\u00a0\7g\2\2\u00a0\u00a1\7x\2\2\u00a1\u00a2")
        buf.write("\7g\2\2\u00a2\u00a3\7p\2\2\u00a3\u00a4\7v\2\2\u00a4\u00a5")
        buf.write("\7F\2\2\u00a5\u00a6\7g\2\2\u00a6\u00a7\7h\2\2\u00a7\u00a8")
        buf.write("\7c\2\2\u00a8\u00a9\7w\2\2\u00a9\u00aa\7n\2\2\u00aa\u00ab")
        buf.write("\7v\2\2\u00ab\4\3\2\2\2\u00ac\u00ad\7u\2\2\u00ad\u00ae")
        buf.write("\7w\2\2\u00ae\u00af\7r\2\2\u00af\u00b0\7g\2\2\u00b0\u00b1")
        buf.write("\7t\2\2\u00b1\6\3\2\2\2\u00b2\u00b3\7r\2\2\u00b3\u00b4")
        buf.write("\7t\2\2\u00b4\u00b5\7k\2\2\u00b5\u00b6\7p\2\2\u00b6\u00b7")
        buf.write("\7v\2\2\u00b7\u00b8\7U\2\2\u00b8\u00b9\7v\2\2\u00b9\u00ba")
        buf.write("\7t\2\2\u00ba\u00bb\7k\2\2\u00bb\u00bc\7p\2\2\u00bc\u00bd")
        buf.write("\7i\2\2\u00bd\b\3\2\2\2\u00be\u00bf\7t\2\2\u00bf\u00c0")
        buf.write("\7g\2\2\u00c0\u00c1\7c\2\2\u00c1\u00c2\7f\2\2\u00c2\u00c3")
        buf.write("\7U\2\2\u00c3\u00c4\7v\2\2\u00c4\u00c5\7t\2\2\u00c5\u00c6")
        buf.write("\7k\2\2\u00c6\u00c7\7p\2\2\u00c7\u00c8\7i\2\2\u00c8\n")
        buf.write("\3\2\2\2\u00c9\u00ca\7r\2\2\u00ca\u00cb\7t\2\2\u00cb\u00cc")
        buf.write("\7k\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce\7v\2\2\u00ce\u00cf")
        buf.write("\7D\2\2\u00cf\u00d0\7q\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2")
        buf.write("\7n\2\2\u00d2\u00d3\7g\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5")
        buf.write("\7p\2\2\u00d5\f\3\2\2\2\u00d6\u00d7\7y\2\2\u00d7\u00d8")
        buf.write("\7t\2\2\u00d8\u00d9\7k\2\2\u00d9\u00da\7v\2\2\u00da\u00db")
        buf.write("\7g\2\2\u00db\u00dc\7H\2\2\u00dc\u00dd\7n\2\2\u00dd\u00de")
        buf.write("\7q\2\2\u00de\u00df\7c\2\2\u00df\u00e0\7v\2\2\u00e0\16")
        buf.write("\3\2\2\2\u00e1\u00e2\7t\2\2\u00e2\u00e3\7g\2\2\u00e3\u00e4")
        buf.write("\7c\2\2\u00e4\u00e5\7f\2\2\u00e5\u00e6\7H\2\2\u00e6\u00e7")
        buf.write("\7n\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9\7c\2\2\u00e9\u00ea")
        buf.write("\7v\2\2\u00ea\20\3\2\2\2\u00eb\u00ec\7r\2\2\u00ec\u00ed")
        buf.write("\7t\2\2\u00ed\u00ee\7k\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0")
        buf.write("\7v\2\2\u00f0\u00f1\7K\2\2\u00f1\u00f2\7p\2\2\u00f2\u00f3")
        buf.write("\7v\2\2\u00f3\u00f4\7g\2\2\u00f4\u00f5\7i\2\2\u00f5\u00f6")
        buf.write("\7g\2\2\u00f6\u00f7\7t\2\2\u00f7\22\3\2\2\2\u00f8\u00f9")
        buf.write("\7t\2\2\u00f9\u00fa\7g\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc")
        buf.write("\7f\2\2\u00fc\u00fd\7K\2\2\u00fd\u00fe\7p\2\2\u00fe\u00ff")
        buf.write("\7v\2\2\u00ff\u0100\7g\2\2\u0100\u0101\7i\2\2\u0101\u0102")
        buf.write("\7g\2\2\u0102\u0103\7t\2\2\u0103\24\3\2\2\2\u0104\u0107")
        buf.write("\5\27\f\2\u0105\u0107\5\31\r\2\u0106\u0104\3\2\2\2\u0106")
        buf.write("\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u0109\b\13\2")
        buf.write("\2\u0109\26\3\2\2\2\u010a\u010b\7\61\2\2\u010b\u010c\7")
        buf.write("\61\2\2\u010c\u0110\3\2\2\2\u010d\u010f\n\2\2\2\u010e")
        buf.write("\u010d\3\2\2\2\u010f\u0112\3\2\2\2\u0110\u010e\3\2\2\2")
        buf.write("\u0110\u0111\3\2\2\2\u0111\30\3\2\2\2\u0112\u0110\3\2")
        buf.write("\2\2\u0113\u0114\7\61\2\2\u0114\u0115\7,\2\2\u0115\u0119")
        buf.write("\3\2\2\2\u0116\u0118\13\2\2\2\u0117\u0116\3\2\2\2\u0118")
        buf.write("\u011b\3\2\2\2\u0119\u011a\3\2\2\2\u0119\u0117\3\2\2\2")
        buf.write("\u011a\u011c\3\2\2\2\u011b\u0119\3\2\2\2\u011c\u011d\7")
        buf.write(",\2\2\u011d\u011e\7\61\2\2\u011e\32\3\2\2\2\u011f\u0120")
        buf.write("\7\61\2\2\u0120\u0121\7,\2\2\u0121\u0125\3\2\2\2\u0122")
        buf.write("\u0124\13\2\2\2\u0123\u0122\3\2\2\2\u0124\u0127\3\2\2")
        buf.write("\2\u0125\u0126\3\2\2\2\u0125\u0123\3\2\2\2\u0126\u0128")
        buf.write("\3\2\2\2\u0127\u0125\3\2\2\2\u0128\u0129\7\2\2\3\u0129")
        buf.write("\34\3\2\2\2\u012a\u013f\7\62\2\2\u012b\u012f\t\3\2\2\u012c")
        buf.write("\u012e\t\4\2\2\u012d\u012c\3\2\2\2\u012e\u0131\3\2\2\2")
        buf.write("\u012f\u012d\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u013a\3")
        buf.write("\2\2\2\u0131\u012f\3\2\2\2\u0132\u0134\5\37\20\2\u0133")
        buf.write("\u0135\t\4\2\2\u0134\u0133\3\2\2\2\u0135\u0136\3\2\2\2")
        buf.write("\u0136\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0139\3")
        buf.write("\2\2\2\u0138\u0132\3\2\2\2\u0139\u013c\3\2\2\2\u013a\u0138")
        buf.write("\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013d\3\2\2\2\u013c")
        buf.write("\u013a\3\2\2\2\u013d\u013f\b\17\3\2\u013e\u012a\3\2\2")
        buf.write("\2\u013e\u012b\3\2\2\2\u013f\36\3\2\2\2\u0140\u0141\7")
        buf.write("a\2\2\u0141 \3\2\2\2\u0142\u0143\5\35\17\2\u0143\u0144")
        buf.write("\5#\22\2\u0144\u0145\5%\23\2\u0145\u0150\3\2\2\2\u0146")
        buf.write("\u0147\5\35\17\2\u0147\u0148\5#\22\2\u0148\u0150\3\2\2")
        buf.write("\2\u0149\u014a\5\35\17\2\u014a\u014b\5%\23\2\u014b\u0150")
        buf.write("\3\2\2\2\u014c\u014d\5#\22\2\u014d\u014e\5%\23\2\u014e")
        buf.write("\u0150\3\2\2\2\u014f\u0142\3\2\2\2\u014f\u0146\3\2\2\2")
        buf.write("\u014f\u0149\3\2\2\2\u014f\u014c\3\2\2\2\u0150\u0151\3")
        buf.write("\2\2\2\u0151\u0152\b\21\4\2\u0152\"\3\2\2\2\u0153\u0157")
        buf.write("\5}?\2\u0154\u0156\t\4\2\2\u0155\u0154\3\2\2\2\u0156\u0159")
        buf.write("\3\2\2\2\u0157\u0155\3\2\2\2\u0157\u0158\3\2\2\2\u0158")
        buf.write("$\3\2\2\2\u0159\u0157\3\2\2\2\u015a\u015c\t\5\2\2\u015b")
        buf.write("\u015d\t\6\2\2\u015c\u015b\3\2\2\2\u015c\u015d\3\2\2\2")
        buf.write("\u015d\u015f\3\2\2\2\u015e\u0160\t\4\2\2\u015f\u015e\3")
        buf.write("\2\2\2\u0160\u0161\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162")
        buf.write("\3\2\2\2\u0162&\3\2\2\2\u0163\u0166\5)\25\2\u0164\u0166")
        buf.write("\5+\26\2\u0165\u0163\3\2\2\2\u0165\u0164\3\2\2\2\u0166")
        buf.write("(\3\2\2\2\u0167\u0168\7h\2\2\u0168\u0169\7c\2\2\u0169")
        buf.write("\u016a\7n\2\2\u016a\u016b\7u\2\2\u016b\u016c\7g\2\2\u016c")
        buf.write("*\3\2\2\2\u016d\u016e\7v\2\2\u016e\u016f\7t\2\2\u016f")
        buf.write("\u0170\7w\2\2\u0170\u0171\7g\2\2\u0171,\3\2\2\2\u0172")
        buf.write("\u0177\5\65\33\2\u0173\u0176\5\61\31\2\u0174\u0176\n\7")
        buf.write("\2\2\u0175\u0173\3\2\2\2\u0175\u0174\3\2\2\2\u0176\u0179")
        buf.write("\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0178\3\2\2\2\u0178")
        buf.write("\u017a\3\2\2\2\u0179\u0177\3\2\2\2\u017a\u017b\5\65\33")
        buf.write("\2\u017b\u017c\b\27\5\2\u017c.\3\2\2\2\u017d\u017e\7^")
        buf.write("\2\2\u017e\u017f\n\b\2\2\u017f\60\3\2\2\2\u0180\u0181")
        buf.write("\7^\2\2\u0181\u0182\t\b\2\2\u0182\62\3\2\2\2\u0183\u0184")
        buf.write("\7^\2\2\u0184\u0185\n\t\2\2\u0185\64\3\2\2\2\u0186\u0187")
        buf.write("\t\t\2\2\u0187\66\3\2\2\2\u0188\u0189\t\n\2\2\u01898\3")
        buf.write("\2\2\2\u018a\u018b\7c\2\2\u018b\u018c\7w\2\2\u018c\u018d")
        buf.write("\7v\2\2\u018d\u018e\7q\2\2\u018e:\3\2\2\2\u018f\u0190")
        buf.write("\7d\2\2\u0190\u0191\7t\2\2\u0191\u0192\7g\2\2\u0192\u0193")
        buf.write("\7c\2\2\u0193\u0194\7m\2\2\u0194<\3\2\2\2\u0195\u0196")
        buf.write("\7k\2\2\u0196\u0197\7p\2\2\u0197\u0198\7v\2\2\u0198\u0199")
        buf.write("\7g\2\2\u0199\u019a\7i\2\2\u019a\u019b\7g\2\2\u019b\u019c")
        buf.write("\7t\2\2\u019c>\3\2\2\2\u019d\u019e\7x\2\2\u019e\u019f")
        buf.write("\7q\2\2\u019f\u01a0\7k\2\2\u01a0\u01a1\7f\2\2\u01a1@\3")
        buf.write("\2\2\2\u01a2\u01a3\7c\2\2\u01a3\u01a4\7t\2\2\u01a4\u01a5")
        buf.write("\7t\2\2\u01a5\u01a6\7c\2\2\u01a6\u01a7\7{\2\2\u01a7B\3")
        buf.write("\2\2\2\u01a8\u01a9\7h\2\2\u01a9\u01aa\7n\2\2\u01aa\u01ab")
        buf.write("\7q\2\2\u01ab\u01ac\7c\2\2\u01ac\u01ad\7v\2\2\u01adD\3")
        buf.write("\2\2\2\u01ae\u01af\7t\2\2\u01af\u01b0\7g\2\2\u01b0\u01b1")
        buf.write("\7v\2\2\u01b1\u01b2\7w\2\2\u01b2\u01b3\7t\2\2\u01b3\u01b4")
        buf.write("\7p\2\2\u01b4F\3\2\2\2\u01b5\u01b6\7q\2\2\u01b6\u01b7")
        buf.write("\7w\2\2\u01b7\u01b8\7v\2\2\u01b8H\3\2\2\2\u01b9\u01ba")
        buf.write("\7d\2\2\u01ba\u01bb\7q\2\2\u01bb\u01bc\7q\2\2\u01bc\u01bd")
        buf.write("\7n\2\2\u01bd\u01be\7g\2\2\u01be\u01bf\7c\2\2\u01bf\u01c0")
        buf.write("\7p\2\2\u01c0J\3\2\2\2\u01c1\u01c2\7h\2\2\u01c2\u01c3")
        buf.write("\7q\2\2\u01c3\u01c4\7t\2\2\u01c4L\3\2\2\2\u01c5\u01c6")
        buf.write("\7u\2\2\u01c6\u01c7\7v\2\2\u01c7\u01c8\7t\2\2\u01c8\u01c9")
        buf.write("\7k\2\2\u01c9\u01ca\7p\2\2\u01ca\u01cb\7i\2\2\u01cbN\3")
        buf.write("\2\2\2\u01cc\u01cd\7e\2\2\u01cd\u01ce\7q\2\2\u01ce\u01cf")
        buf.write("\7p\2\2\u01cf\u01d0\7v\2\2\u01d0\u01d1\7k\2\2\u01d1\u01d2")
        buf.write("\7p\2\2\u01d2\u01d3\7w\2\2\u01d3\u01d4\7g\2\2\u01d4P\3")
        buf.write("\2\2\2\u01d5\u01d6\7f\2\2\u01d6\u01d7\7q\2\2\u01d7R\3")
        buf.write("\2\2\2\u01d8\u01d9\7h\2\2\u01d9\u01da\7w\2\2\u01da\u01db")
        buf.write("\7p\2\2\u01db\u01dc\7e\2\2\u01dc\u01dd\7v\2\2\u01dd\u01de")
        buf.write("\7k\2\2\u01de\u01df\7q\2\2\u01df\u01e0\7p\2\2\u01e0T\3")
        buf.write("\2\2\2\u01e1\u01e2\7q\2\2\u01e2\u01e3\7h\2\2\u01e3V\3")
        buf.write("\2\2\2\u01e4\u01e5\7g\2\2\u01e5\u01e6\7n\2\2\u01e6\u01e7")
        buf.write("\7u\2\2\u01e7\u01e8\7g\2\2\u01e8X\3\2\2\2\u01e9\u01ea")
        buf.write("\7k\2\2\u01ea\u01eb\7h\2\2\u01ebZ\3\2\2\2\u01ec\u01ed")
        buf.write("\7y\2\2\u01ed\u01ee\7j\2\2\u01ee\u01ef\7k\2\2\u01ef\u01f0")
        buf.write("\7n\2\2\u01f0\u01f1\7g\2\2\u01f1\\\3\2\2\2\u01f2\u01f3")
        buf.write("\7k\2\2\u01f3\u01f4\7p\2\2\u01f4\u01f5\7j\2\2\u01f5\u01f6")
        buf.write("\7g\2\2\u01f6\u01f7\7t\2\2\u01f7\u01f8\7k\2\2\u01f8\u01f9")
        buf.write("\7v\2\2\u01f9^\3\2\2\2\u01fa\u01fb\7-\2\2\u01fb`\3\2\2")
        buf.write("\2\u01fc\u01fd\7/\2\2\u01fdb\3\2\2\2\u01fe\u01ff\7,\2")
        buf.write("\2\u01ffd\3\2\2\2\u0200\u0201\7\61\2\2\u0201f\3\2\2\2")
        buf.write("\u0202\u0203\7\'\2\2\u0203h\3\2\2\2\u0204\u0205\7>\2\2")
        buf.write("\u0205j\3\2\2\2\u0206\u0207\7@\2\2\u0207l\3\2\2\2\u0208")
        buf.write("\u0209\7>\2\2\u0209\u020a\7?\2\2\u020an\3\2\2\2\u020b")
        buf.write("\u020c\7@\2\2\u020c\u020d\7?\2\2\u020dp\3\2\2\2\u020e")
        buf.write("\u020f\7#\2\2\u020fr\3\2\2\2\u0210\u0211\7(\2\2\u0211")
        buf.write("\u0212\7(\2\2\u0212t\3\2\2\2\u0213\u0214\7~\2\2\u0214")
        buf.write("\u0215\7~\2\2\u0215v\3\2\2\2\u0216\u0217\7?\2\2\u0217")
        buf.write("\u0218\7?\2\2\u0218x\3\2\2\2\u0219\u021a\7#\2\2\u021a")
        buf.write("\u021b\7?\2\2\u021bz\3\2\2\2\u021c\u021d\7<\2\2\u021d")
        buf.write("\u021e\7<\2\2\u021e|\3\2\2\2\u021f\u0220\7\60\2\2\u0220")
        buf.write("~\3\2\2\2\u0221\u0222\7.\2\2\u0222\u0080\3\2\2\2\u0223")
        buf.write("\u0224\7=\2\2\u0224\u0082\3\2\2\2\u0225\u0226\7?\2\2\u0226")
        buf.write("\u0084\3\2\2\2\u0227\u0228\7<\2\2\u0228\u0086\3\2\2\2")
        buf.write("\u0229\u022a\7*\2\2\u022a\u0088\3\2\2\2\u022b\u022c\7")
        buf.write("+\2\2\u022c\u008a\3\2\2\2\u022d\u022e\7]\2\2\u022e\u008c")
        buf.write("\3\2\2\2\u022f\u0230\7_\2\2\u0230\u008e\3\2\2\2\u0231")
        buf.write("\u0232\7}\2\2\u0232\u0090\3\2\2\2\u0233\u0234\7\177\2")
        buf.write("\2\u0234\u0092\3\2\2\2\u0235\u0237\t\13\2\2\u0236\u0235")
        buf.write("\3\2\2\2\u0237\u0238\3\2\2\2\u0238\u0236\3\2\2\2\u0238")
        buf.write("\u0239\3\2\2\2\u0239\u023d\3\2\2\2\u023a\u023c\t\f\2\2")
        buf.write("\u023b\u023a\3\2\2\2\u023c\u023f\3\2\2\2\u023d\u023b\3")
        buf.write("\2\2\2\u023d\u023e\3\2\2\2\u023e\u0094\3\2\2\2\u023f\u023d")
        buf.write("\3\2\2\2\u0240\u0242\t\r\2\2\u0241\u0240\3\2\2\2\u0242")
        buf.write("\u0243\3\2\2\2\u0243\u0241\3\2\2\2\u0243\u0244\3\2\2\2")
        buf.write("\u0244\u0245\3\2\2\2\u0245\u0246\bK\2\2\u0246\u0096\3")
        buf.write("\2\2\2\u0247\u024c\5\65\33\2\u0248\u024b\n\t\2\2\u0249")
        buf.write("\u024b\5\61\31\2\u024a\u0248\3\2\2\2\u024a\u0249\3\2\2")
        buf.write("\2\u024b\u024e\3\2\2\2\u024c\u024d\3\2\2\2\u024c\u024a")
        buf.write("\3\2\2\2\u024d\u0250\3\2\2\2\u024e\u024c\3\2\2\2\u024f")
        buf.write("\u0251\t\16\2\2\u0250\u024f\3\2\2\2\u0251\u0252\3\2\2")
        buf.write("\2\u0252\u0253\bL\6\2\u0253\u0098\3\2\2\2\u0254\u0259")
        buf.write("\5\65\33\2\u0255\u0258\n\17\2\2\u0256\u0258\5\61\31\2")
        buf.write("\u0257\u0255\3\2\2\2\u0257\u0256\3\2\2\2\u0258\u025b\3")
        buf.write("\2\2\2\u0259\u0257\3\2\2\2\u0259\u025a\3\2\2\2\u025a\u025c")
        buf.write("\3\2\2\2\u025b\u0259\3\2\2\2\u025c\u025d\5/\30\2\u025d")
        buf.write("\u025e\bM\7\2\u025e\u009a\3\2\2\2\u025f\u0260\13\2\2\2")
        buf.write("\u0260\u0261\bN\b\2\u0261\u009c\3\2\2\2\32\2\u0106\u0110")
        buf.write("\u0119\u0125\u012f\u0136\u013a\u013e\u014f\u0157\u015c")
        buf.write("\u0161\u0165\u0175\u0177\u0238\u023d\u0243\u024a\u024c")
        buf.write("\u0250\u0257\u0259\t\b\2\2\3\17\2\3\21\3\3\27\4\3L\5\3")
        buf.write("M\6\3N\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PREVENTDEFAULT = 1
    SUPER = 2
    PRINTSTRING = 3
    READSTRING = 4
    PRINTBOOLEAN = 5
    WRITEFLOAT = 6
    READFLOAT = 7
    PRINTINTEGER = 8
    READINTEGER = 9
    COMMENT = 10
    INTLIT = 11
    FLOATLIT = 12
    BOOLEANLIT = 13
    STRINGLIT = 14
    AUTO = 15
    BREAK = 16
    INTEGER = 17
    VOID = 18
    ARRAY = 19
    FLOAT = 20
    RETURN = 21
    OUT = 22
    BOOLEAN = 23
    FOR = 24
    STRING = 25
    CONTINUE = 26
    DO = 27
    FUNCTION = 28
    OF = 29
    ELSE = 30
    IF = 31
    WHILE = 32
    INHERIT = 33
    PLUS = 34
    MINUS = 35
    MUL = 36
    DIV = 37
    MOD = 38
    LESS = 39
    GREATER = 40
    LTE = 41
    GTE = 42
    NOT = 43
    AND = 44
    OR = 45
    EQUAL_TO = 46
    NOT_EQUAL = 47
    CONCAT = 48
    PERIOD = 49
    COMMA = 50
    SEMI = 51
    EQUAL = 52
    COLON = 53
    LB = 54
    RB = 55
    LSB = 56
    RSB = 57
    LCB = 58
    RCB = 59
    IDENTIFIER = 60
    WS = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63
    ERROR_CHAR = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'preventDefault'", "'super'", "'printString'", "'readString'", 
            "'printBoolean'", "'writeFloat'", "'readFloat'", "'printInteger'", 
            "'readInteger'", "'auto'", "'break'", "'integer'", "'void'", 
            "'array'", "'float'", "'return'", "'out'", "'boolean'", "'for'", 
            "'string'", "'continue'", "'do'", "'function'", "'of'", "'else'", 
            "'if'", "'while'", "'inherit'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'<'", "'>'", "'<='", "'>='", "'!'", "'&&'", "'||'", 
            "'=='", "'!='", "'::'", "'.'", "','", "';'", "'='", "':'", "'('", 
            "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "PREVENTDEFAULT", "SUPER", "PRINTSTRING", "READSTRING", "PRINTBOOLEAN", 
            "WRITEFLOAT", "READFLOAT", "PRINTINTEGER", "READINTEGER", "COMMENT", 
            "INTLIT", "FLOATLIT", "BOOLEANLIT", "STRINGLIT", "AUTO", "BREAK", 
            "INTEGER", "VOID", "ARRAY", "FLOAT", "RETURN", "OUT", "BOOLEAN", 
            "FOR", "STRING", "CONTINUE", "DO", "FUNCTION", "OF", "ELSE", 
            "IF", "WHILE", "INHERIT", "PLUS", "MINUS", "MUL", "DIV", "MOD", 
            "LESS", "GREATER", "LTE", "GTE", "NOT", "AND", "OR", "EQUAL_TO", 
            "NOT_EQUAL", "CONCAT", "PERIOD", "COMMA", "SEMI", "EQUAL", "COLON", 
            "LB", "RB", "LSB", "RSB", "LCB", "RCB", "IDENTIFIER", "WS", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "PREVENTDEFAULT", "SUPER", "PRINTSTRING", "READSTRING", 
                  "PRINTBOOLEAN", "WRITEFLOAT", "READFLOAT", "PRINTINTEGER", 
                  "READINTEGER", "COMMENT", "SingleLineComment", "MultiLineComment", 
                  "CommentAll", "INTLIT", "UNDERSCORE", "FLOATLIT", "DECPART", 
                  "EXPPART", "BOOLEANLIT", "FALSE", "TRUE", "STRINGLIT", 
                  "NOTESC", "ESC", "AllEscSeq", "DUO_QUOTE", "SINGLE_QUOTE", 
                  "AUTO", "BREAK", "INTEGER", "VOID", "ARRAY", "FLOAT", 
                  "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", 
                  "DO", "FUNCTION", "OF", "ELSE", "IF", "WHILE", "INHERIT", 
                  "PLUS", "MINUS", "MUL", "DIV", "MOD", "LESS", "GREATER", 
                  "LTE", "GTE", "NOT", "AND", "OR", "EQUAL_TO", "NOT_EQUAL", 
                  "CONCAT", "PERIOD", "COMMA", "SEMI", "EQUAL", "COLON", 
                  "LB", "RB", "LSB", "RSB", "LCB", "RCB", "IDENTIFIER", 
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
            actions[13] = self.INTLIT_action 
            actions[15] = self.FLOATLIT_action 
            actions[21] = self.STRINGLIT_action 
            actions[74] = self.UNCLOSE_STRING_action 
            actions[75] = self.ILLEGAL_ESCAPE_action 
            actions[76] = self.ERROR_CHAR_action 
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
     


