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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u0226\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\16\3\17\3\17\5\17\u011d\n\17\3\17\3\17\3\20\3\20\5\20")
        buf.write("\u0123\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u012c")
        buf.write("\n\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3")
        buf.write("!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#")
        buf.write("\3#\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3)\3")
        buf.write(")\3)\3*\3*\3*\3*\3*\3+\3+\3+\3,\3,\3,\3,\3,\3,\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62")
        buf.write("\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\67\3\67\38\38\38\39\39\39\3:\3:\3:\3;\3;\3;\3<\6<\u01d4")
        buf.write("\n<\r<\16<\u01d5\3<\7<\u01d9\n<\f<\16<\u01dc\13<\3=\3")
        buf.write("=\5=\u01e0\n=\3>\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3")
        buf.write("D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3J\3J\3J\5J\u0200")
        buf.write("\nJ\3K\3K\3K\3K\3K\5K\u0207\nK\3L\6L\u020a\nL\rL\16L\u020b")
        buf.write("\3L\3L\3M\3M\3M\7M\u0213\nM\fM\16M\u0216\13M\3M\3M\3N")
        buf.write("\3N\7N\u021c\nN\fN\16N\u021f\13N\3N\3N\3N\3O\3O\3O\7\u00b4")
        buf.write("\u0108\u0114\u0214\u021d\2P\3\3\5\2\7\2\t\4\13\2\r\5\17")
        buf.write("\2\21\2\23\6\25\2\27\2\31\7\33\2\35\b\37\2!\2#\2%\2\'")
        buf.write("\2)\2+\2-\2/\2\61\2\63\2\65\t\67\n9\13;\f=\r?\16A\17C")
        buf.write("\20E\21G\22I\23K\24M\25O\26Q\27S\30U\31W\32Y\33[\34]\35")
        buf.write("_\36a\37c e!g\"i#k$m%o&q\'s(u)w*y+{,}-\177.\u0081/\u0083")
        buf.write("\60\u0085\61\u0087\62\u0089\63\u008b\64\u008d\65\u008f")
        buf.write("\66\u0091\67\u00938\u00959\u0097:\u0099;\u009b<\u009d")
        buf.write("=\3\2\21\4\2\f\f\17\17\3\2\63;\3\2\62;\4\2GGgg\4\2$$^")
        buf.write("^\3\2$$\3\2))\3\2\n\n\3\2\16\16\3\2\17\17\3\2\f\f\3\2")
        buf.write("^^\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2\u0235")
        buf.write("\2\3\3\2\2\2\2\t\3\2\2\2\2\r\3\2\2\2\2\23\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3")
        buf.write("\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write("\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099")
        buf.write("\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\3\u00a1\3\2\2")
        buf.write("\2\5\u00a5\3\2\2\2\7\u00ae\3\2\2\2\t\u00ce\3\2\2\2\13")
        buf.write("\u00d0\3\2\2\2\r\u00d6\3\2\2\2\17\u00d8\3\2\2\2\21\u00e9")
        buf.write("\3\2\2\2\23\u00f6\3\2\2\2\25\u00f8\3\2\2\2\27\u00fe\3")
        buf.write("\2\2\2\31\u0103\3\2\2\2\33\u010e\3\2\2\2\35\u011a\3\2")
        buf.write("\2\2\37\u0122\3\2\2\2!\u012b\3\2\2\2#\u012d\3\2\2\2%\u012f")
        buf.write("\3\2\2\2\'\u0131\3\2\2\2)\u0133\3\2\2\2+\u0135\3\2\2\2")
        buf.write("-\u0137\3\2\2\2/\u0139\3\2\2\2\61\u013b\3\2\2\2\63\u013d")
        buf.write("\3\2\2\2\65\u0140\3\2\2\2\67\u0145\3\2\2\29\u014b\3\2")
        buf.write("\2\2;\u0153\3\2\2\2=\u0158\3\2\2\2?\u015e\3\2\2\2A\u0164")
        buf.write("\3\2\2\2C\u016b\3\2\2\2E\u016f\3\2\2\2G\u0177\3\2\2\2")
        buf.write("I\u017b\3\2\2\2K\u0182\3\2\2\2M\u018b\3\2\2\2O\u018e\3")
        buf.write("\2\2\2Q\u0197\3\2\2\2S\u019a\3\2\2\2U\u019f\3\2\2\2W\u01a2")
        buf.write("\3\2\2\2Y\u01a8\3\2\2\2[\u01b0\3\2\2\2]\u01b2\3\2\2\2")
        buf.write("_\u01b4\3\2\2\2a\u01b6\3\2\2\2c\u01b8\3\2\2\2e\u01ba\3")
        buf.write("\2\2\2g\u01bc\3\2\2\2i\u01be\3\2\2\2k\u01c1\3\2\2\2m\u01c4")
        buf.write("\3\2\2\2o\u01c6\3\2\2\2q\u01c9\3\2\2\2s\u01cc\3\2\2\2")
        buf.write("u\u01cf\3\2\2\2w\u01d3\3\2\2\2y\u01df\3\2\2\2{\u01e1\3")
        buf.write("\2\2\2}\u01e4\3\2\2\2\177\u01e6\3\2\2\2\u0081\u01e8\3")
        buf.write("\2\2\2\u0083\u01ea\3\2\2\2\u0085\u01ec\3\2\2\2\u0087\u01ee")
        buf.write("\3\2\2\2\u0089\u01f0\3\2\2\2\u008b\u01f2\3\2\2\2\u008d")
        buf.write("\u01f4\3\2\2\2\u008f\u01f6\3\2\2\2\u0091\u01f8\3\2\2\2")
        buf.write("\u0093\u01ff\3\2\2\2\u0095\u0206\3\2\2\2\u0097\u0209\3")
        buf.write("\2\2\2\u0099\u020f\3\2\2\2\u009b\u021d\3\2\2\2\u009d\u0223")
        buf.write("\3\2\2\2\u009f\u00a2\5\5\3\2\u00a0\u00a2\5\7\4\2\u00a1")
        buf.write("\u009f\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2")
        buf.write("\u00a3\u00a4\b\2\2\2\u00a4\4\3\2\2\2\u00a5\u00a6\7\61")
        buf.write("\2\2\u00a6\u00a7\7\61\2\2\u00a7\u00ab\3\2\2\2\u00a8\u00aa")
        buf.write("\n\2\2\2\u00a9\u00a8\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab")
        buf.write("\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\6\3\2\2\2\u00ad")
        buf.write("\u00ab\3\2\2\2\u00ae\u00af\7\61\2\2\u00af\u00b0\7,\2\2")
        buf.write("\u00b0\u00b4\3\2\2\2\u00b1\u00b3\13\2\2\2\u00b2\u00b1")
        buf.write("\3\2\2\2\u00b3\u00b6\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b4")
        buf.write("\u00b2\3\2\2\2\u00b5\u00b7\3\2\2\2\u00b6\u00b4\3\2\2\2")
        buf.write("\u00b7\u00b8\7,\2\2\u00b8\u00b9\7\61\2\2\u00b9\b\3\2\2")
        buf.write("\2\u00ba\u00cf\7\62\2\2\u00bb\u00bf\t\3\2\2\u00bc\u00be")
        buf.write("\t\4\2\2\u00bd\u00bc\3\2\2\2\u00be\u00c1\3\2\2\2\u00bf")
        buf.write("\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00ca\3\2\2\2")
        buf.write("\u00c1\u00bf\3\2\2\2\u00c2\u00c4\5\13\6\2\u00c3\u00c5")
        buf.write("\t\4\2\2\u00c4\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c9\3\2\2\2")
        buf.write("\u00c8\u00c2\3\2\2\2\u00c9\u00cc\3\2\2\2\u00ca\u00c8\3")
        buf.write("\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cd\3\2\2\2\u00cc\u00ca")
        buf.write("\3\2\2\2\u00cd\u00cf\b\5\3\2\u00ce\u00ba\3\2\2\2\u00ce")
        buf.write("\u00bb\3\2\2\2\u00cf\n\3\2\2\2\u00d0\u00d1\7a\2\2\u00d1")
        buf.write("\f\3\2\2\2\u00d2\u00d7\5\21\t\2\u00d3\u00d4\5\17\b\2\u00d4")
        buf.write("\u00d5\b\7\4\2\u00d5\u00d7\3\2\2\2\u00d6\u00d2\3\2\2\2")
        buf.write("\u00d6\u00d3\3\2\2\2\u00d7\16\3\2\2\2\u00d8\u00d9\5\t")
        buf.write("\5\2\u00d9\u00db\5}?\2\u00da\u00dc\t\4\2\2\u00db\u00da")
        buf.write("\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd")
        buf.write("\u00de\3\2\2\2\u00de\u00e6\3\2\2\2\u00df\u00e3\t\5\2\2")
        buf.write("\u00e0\u00e2\t\4\2\2\u00e1\u00e0\3\2\2\2\u00e2\u00e5\3")
        buf.write("\2\2\2\u00e3\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e7")
        buf.write("\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e6\u00df\3\2\2\2\u00e6")
        buf.write("\u00e7\3\2\2\2\u00e7\20\3\2\2\2\u00e8\u00ea\t\4\2\2\u00e9")
        buf.write("\u00e8\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00e9\3\2\2\2")
        buf.write("\u00eb\u00ec\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ee\t")
        buf.write("\5\2\2\u00ee\u00f0\5]/\2\u00ef\u00f1\t\4\2\2\u00f0\u00ef")
        buf.write("\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2")
        buf.write("\u00f3\3\2\2\2\u00f3\22\3\2\2\2\u00f4\u00f7\5\25\13\2")
        buf.write("\u00f5\u00f7\5\27\f\2\u00f6\u00f4\3\2\2\2\u00f6\u00f5")
        buf.write("\3\2\2\2\u00f7\24\3\2\2\2\u00f8\u00f9\7h\2\2\u00f9\u00fa")
        buf.write("\7c\2\2\u00fa\u00fb\7n\2\2\u00fb\u00fc\7u\2\2\u00fc\u00fd")
        buf.write("\7g\2\2\u00fd\26\3\2\2\2\u00fe\u00ff\7v\2\2\u00ff\u0100")
        buf.write("\7t\2\2\u0100\u0101\7w\2\2\u0101\u0102\7g\2\2\u0102\30")
        buf.write("\3\2\2\2\u0103\u0108\5#\22\2\u0104\u0107\n\6\2\2\u0105")
        buf.write("\u0107\5\33\16\2\u0106\u0104\3\2\2\2\u0106\u0105\3\2\2")
        buf.write("\2\u0107\u010a\3\2\2\2\u0108\u0109\3\2\2\2\u0108\u0106")
        buf.write("\3\2\2\2\u0109\u010b\3\2\2\2\u010a\u0108\3\2\2\2\u010b")
        buf.write("\u010c\5#\22\2\u010c\u010d\b\r\5\2\u010d\32\3\2\2\2\u010e")
        buf.write("\u010f\7^\2\2\u010f\u0110\7$\2\2\u0110\u0114\3\2\2\2\u0111")
        buf.write("\u0113\13\2\2\2\u0112\u0111\3\2\2\2\u0113\u0116\3\2\2")
        buf.write("\2\u0114\u0115\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u0117")
        buf.write("\3\2\2\2\u0116\u0114\3\2\2\2\u0117\u0118\7^\2\2\u0118")
        buf.write("\u0119\7$\2\2\u0119\34\3\2\2\2\u011a\u011c\5\u008fH\2")
        buf.write("\u011b\u011d\5\37\20\2\u011c\u011b\3\2\2\2\u011c\u011d")
        buf.write("\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u011f\5\u0091I\2\u011f")
        buf.write("\36\3\2\2\2\u0120\u0123\5\u0093J\2\u0121\u0123\5\u0095")
        buf.write("K\2\u0122\u0120\3\2\2\2\u0122\u0121\3\2\2\2\u0123 \3\2")
        buf.write("\2\2\u0124\u012c\5\'\24\2\u0125\u012c\5)\25\2\u0126\u012c")
        buf.write("\5+\26\2\u0127\u012c\5-\27\2\u0128\u012c\5/\30\2\u0129")
        buf.write("\u012c\5\63\32\2\u012a\u012c\5\61\31\2\u012b\u0124\3\2")
        buf.write("\2\2\u012b\u0125\3\2\2\2\u012b\u0126\3\2\2\2\u012b\u0127")
        buf.write("\3\2\2\2\u012b\u0128\3\2\2\2\u012b\u0129\3\2\2\2\u012b")
        buf.write("\u012a\3\2\2\2\u012c\"\3\2\2\2\u012d\u012e\t\7\2\2\u012e")
        buf.write("$\3\2\2\2\u012f\u0130\t\b\2\2\u0130&\3\2\2\2\u0131\u0132")
        buf.write("\t\t\2\2\u0132(\3\2\2\2\u0133\u0134\t\n\2\2\u0134*\3\2")
        buf.write("\2\2\u0135\u0136\t\13\2\2\u0136,\3\2\2\2\u0137\u0138\t")
        buf.write("\f\2\2\u0138.\3\2\2\2\u0139\u013a\7)\2\2\u013a\60\3\2")
        buf.write("\2\2\u013b\u013c\t\r\2\2\u013c\62\3\2\2\2\u013d\u013e")
        buf.write("\7^\2\2\u013e\u013f\7$\2\2\u013f\64\3\2\2\2\u0140\u0141")
        buf.write("\7c\2\2\u0141\u0142\7w\2\2\u0142\u0143\7v\2\2\u0143\u0144")
        buf.write("\7q\2\2\u0144\66\3\2\2\2\u0145\u0146\7d\2\2\u0146\u0147")
        buf.write("\7t\2\2\u0147\u0148\7g\2\2\u0148\u0149\7c\2\2\u0149\u014a")
        buf.write("\7m\2\2\u014a8\3\2\2\2\u014b\u014c\7k\2\2\u014c\u014d")
        buf.write("\7p\2\2\u014d\u014e\7v\2\2\u014e\u014f\7g\2\2\u014f\u0150")
        buf.write("\7i\2\2\u0150\u0151\7g\2\2\u0151\u0152\7t\2\2\u0152:\3")
        buf.write("\2\2\2\u0153\u0154\7x\2\2\u0154\u0155\7q\2\2\u0155\u0156")
        buf.write("\7k\2\2\u0156\u0157\7f\2\2\u0157<\3\2\2\2\u0158\u0159")
        buf.write("\7c\2\2\u0159\u015a\7t\2\2\u015a\u015b\7t\2\2\u015b\u015c")
        buf.write("\7c\2\2\u015c\u015d\7{\2\2\u015d>\3\2\2\2\u015e\u015f")
        buf.write("\7h\2\2\u015f\u0160\7n\2\2\u0160\u0161\7q\2\2\u0161\u0162")
        buf.write("\7c\2\2\u0162\u0163\7v\2\2\u0163@\3\2\2\2\u0164\u0165")
        buf.write("\7t\2\2\u0165\u0166\7g\2\2\u0166\u0167\7v\2\2\u0167\u0168")
        buf.write("\7w\2\2\u0168\u0169\7t\2\2\u0169\u016a\7p\2\2\u016aB\3")
        buf.write("\2\2\2\u016b\u016c\7q\2\2\u016c\u016d\7w\2\2\u016d\u016e")
        buf.write("\7v\2\2\u016eD\3\2\2\2\u016f\u0170\7d\2\2\u0170\u0171")
        buf.write("\7q\2\2\u0171\u0172\7q\2\2\u0172\u0173\7n\2\2\u0173\u0174")
        buf.write("\7g\2\2\u0174\u0175\7c\2\2\u0175\u0176\7p\2\2\u0176F\3")
        buf.write("\2\2\2\u0177\u0178\7h\2\2\u0178\u0179\7q\2\2\u0179\u017a")
        buf.write("\7t\2\2\u017aH\3\2\2\2\u017b\u017c\7u\2\2\u017c\u017d")
        buf.write("\7v\2\2\u017d\u017e\7t\2\2\u017e\u017f\7k\2\2\u017f\u0180")
        buf.write("\7p\2\2\u0180\u0181\7i\2\2\u0181J\3\2\2\2\u0182\u0183")
        buf.write("\7e\2\2\u0183\u0184\7q\2\2\u0184\u0185\7p\2\2\u0185\u0186")
        buf.write("\7v\2\2\u0186\u0187\7k\2\2\u0187\u0188\7p\2\2\u0188\u0189")
        buf.write("\7w\2\2\u0189\u018a\7g\2\2\u018aL\3\2\2\2\u018b\u018c")
        buf.write("\7f\2\2\u018c\u018d\7q\2\2\u018dN\3\2\2\2\u018e\u018f")
        buf.write("\7h\2\2\u018f\u0190\7w\2\2\u0190\u0191\7p\2\2\u0191\u0192")
        buf.write("\7e\2\2\u0192\u0193\7v\2\2\u0193\u0194\7k\2\2\u0194\u0195")
        buf.write("\7q\2\2\u0195\u0196\7p\2\2\u0196P\3\2\2\2\u0197\u0198")
        buf.write("\7q\2\2\u0198\u0199\7h\2\2\u0199R\3\2\2\2\u019a\u019b")
        buf.write("\7g\2\2\u019b\u019c\7n\2\2\u019c\u019d\7u\2\2\u019d\u019e")
        buf.write("\7g\2\2\u019eT\3\2\2\2\u019f\u01a0\7k\2\2\u01a0\u01a1")
        buf.write("\7h\2\2\u01a1V\3\2\2\2\u01a2\u01a3\7y\2\2\u01a3\u01a4")
        buf.write("\7j\2\2\u01a4\u01a5\7k\2\2\u01a5\u01a6\7n\2\2\u01a6\u01a7")
        buf.write("\7g\2\2\u01a7X\3\2\2\2\u01a8\u01a9\7k\2\2\u01a9\u01aa")
        buf.write("\7p\2\2\u01aa\u01ab\7j\2\2\u01ab\u01ac\7g\2\2\u01ac\u01ad")
        buf.write("\7t\2\2\u01ad\u01ae\7k\2\2\u01ae\u01af\7v\2\2\u01afZ\3")
        buf.write("\2\2\2\u01b0\u01b1\7-\2\2\u01b1\\\3\2\2\2\u01b2\u01b3")
        buf.write("\7/\2\2\u01b3^\3\2\2\2\u01b4\u01b5\7,\2\2\u01b5`\3\2\2")
        buf.write("\2\u01b6\u01b7\7\61\2\2\u01b7b\3\2\2\2\u01b8\u01b9\7\'")
        buf.write("\2\2\u01b9d\3\2\2\2\u01ba\u01bb\7>\2\2\u01bbf\3\2\2\2")
        buf.write("\u01bc\u01bd\7@\2\2\u01bdh\3\2\2\2\u01be\u01bf\7>\2\2")
        buf.write("\u01bf\u01c0\7?\2\2\u01c0j\3\2\2\2\u01c1\u01c2\7@\2\2")
        buf.write("\u01c2\u01c3\7?\2\2\u01c3l\3\2\2\2\u01c4\u01c5\7#\2\2")
        buf.write("\u01c5n\3\2\2\2\u01c6\u01c7\7(\2\2\u01c7\u01c8\7(\2\2")
        buf.write("\u01c8p\3\2\2\2\u01c9\u01ca\7~\2\2\u01ca\u01cb\7~\2\2")
        buf.write("\u01cbr\3\2\2\2\u01cc\u01cd\7?\2\2\u01cd\u01ce\7?\2\2")
        buf.write("\u01cet\3\2\2\2\u01cf\u01d0\7#\2\2\u01d0\u01d1\7?\2\2")
        buf.write("\u01d1v\3\2\2\2\u01d2\u01d4\t\16\2\2\u01d3\u01d2\3\2\2")
        buf.write("\2\u01d4\u01d5\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d5\u01d6")
        buf.write("\3\2\2\2\u01d6\u01da\3\2\2\2\u01d7\u01d9\t\17\2\2\u01d8")
        buf.write("\u01d7\3\2\2\2\u01d9\u01dc\3\2\2\2\u01da\u01d8\3\2\2\2")
        buf.write("\u01da\u01db\3\2\2\2\u01dbx\3\2\2\2\u01dc\u01da\3\2\2")
        buf.write("\2\u01dd\u01e0\5\t\5\2\u01de\u01e0\5\r\7\2\u01df\u01dd")
        buf.write("\3\2\2\2\u01df\u01de\3\2\2\2\u01e0z\3\2\2\2\u01e1\u01e2")
        buf.write("\7<\2\2\u01e2\u01e3\7<\2\2\u01e3|\3\2\2\2\u01e4\u01e5")
        buf.write("\7\60\2\2\u01e5~\3\2\2\2\u01e6\u01e7\7.\2\2\u01e7\u0080")
        buf.write("\3\2\2\2\u01e8\u01e9\7=\2\2\u01e9\u0082\3\2\2\2\u01ea")
        buf.write("\u01eb\7?\2\2\u01eb\u0084\3\2\2\2\u01ec\u01ed\7<\2\2\u01ed")
        buf.write("\u0086\3\2\2\2\u01ee\u01ef\7*\2\2\u01ef\u0088\3\2\2\2")
        buf.write("\u01f0\u01f1\7+\2\2\u01f1\u008a\3\2\2\2\u01f2\u01f3\7")
        buf.write("]\2\2\u01f3\u008c\3\2\2\2\u01f4\u01f5\7_\2\2\u01f5\u008e")
        buf.write("\3\2\2\2\u01f6\u01f7\7}\2\2\u01f7\u0090\3\2\2\2\u01f8")
        buf.write("\u01f9\7\177\2\2\u01f9\u0092\3\2\2\2\u01fa\u01fb\5y=\2")
        buf.write("\u01fb\u01fc\5\177@\2\u01fc\u01fd\5\u0093J\2\u01fd\u0200")
        buf.write("\3\2\2\2\u01fe\u0200\5y=\2\u01ff\u01fa\3\2\2\2\u01ff\u01fe")
        buf.write("\3\2\2\2\u0200\u0094\3\2\2\2\u0201\u0202\5\31\r\2\u0202")
        buf.write("\u0203\5\177@\2\u0203\u0204\5\u0095K\2\u0204\u0207\3\2")
        buf.write("\2\2\u0205\u0207\5\31\r\2\u0206\u0201\3\2\2\2\u0206\u0205")
        buf.write("\3\2\2\2\u0207\u0096\3\2\2\2\u0208\u020a\t\20\2\2\u0209")
        buf.write("\u0208\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u0209\3\2\2\2")
        buf.write("\u020b\u020c\3\2\2\2\u020c\u020d\3\2\2\2\u020d\u020e\b")
        buf.write("L\2\2\u020e\u0098\3\2\2\2\u020f\u0214\5#\22\2\u0210\u0213")
        buf.write("\n\6\2\2\u0211\u0213\5\33\16\2\u0212\u0210\3\2\2\2\u0212")
        buf.write("\u0211\3\2\2\2\u0213\u0216\3\2\2\2\u0214\u0215\3\2\2\2")
        buf.write("\u0214\u0212\3\2\2\2\u0215\u0217\3\2\2\2\u0216\u0214\3")
        buf.write("\2\2\2\u0217\u0218\bM\6\2\u0218\u009a\3\2\2\2\u0219\u021c")
        buf.write("\n\6\2\2\u021a\u021c\5\33\16\2\u021b\u0219\3\2\2\2\u021b")
        buf.write("\u021a\3\2\2\2\u021c\u021f\3\2\2\2\u021d\u021e\3\2\2\2")
        buf.write("\u021d\u021b\3\2\2\2\u021e\u0220\3\2\2\2\u021f\u021d\3")
        buf.write("\2\2\2\u0220\u0221\5#\22\2\u0221\u0222\bN\7\2\u0222\u009c")
        buf.write("\3\2\2\2\u0223\u0224\13\2\2\2\u0224\u0225\bO\b\2\u0225")
        buf.write("\u009e\3\2\2\2!\2\u00a1\u00ab\u00b4\u00bf\u00c6\u00ca")
        buf.write("\u00ce\u00d6\u00dd\u00e3\u00e6\u00eb\u00f2\u00f6\u0106")
        buf.write("\u0108\u0114\u011c\u0122\u012b\u01d5\u01da\u01df\u01ff")
        buf.write("\u0206\u020b\u0212\u0214\u021b\u021d\t\b\2\2\3\5\2\3\7")
        buf.write("\3\3\r\4\3M\5\3N\6\3O\7")
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
    LESS_THAN_OR_EQUAL = 33
    GREATER_THAN_OR_EQUAL = 34
    NOT = 35
    AND = 36
    OR = 37
    EQUAL_TO = 38
    NOT_EQUAL = 39
    IDENTIFIER = 40
    NUMBER = 41
    SCOPE_RES = 42
    PERIOD = 43
    COMMA = 44
    SEMI = 45
    EQUAL = 46
    COLON = 47
    LB = 48
    RB = 49
    LSB = 50
    RSB = 51
    LCB = 52
    RCB = 53
    NUMLIST = 54
    STRINGLIST = 55
    WS = 56
    UNCLOSE_STRING = 57
    ILLEGAL_ESCAPE = 58
    ERROR_CHAR = 59

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
            "MINUS", "MUL", "DIV", "MOD", "LESS", "GREATER", "LESS_THAN_OR_EQUAL", 
            "GREATER_THAN_OR_EQUAL", "NOT", "AND", "OR", "EQUAL_TO", "NOT_EQUAL", 
            "IDENTIFIER", "NUMBER", "SCOPE_RES", "PERIOD", "COMMA", "SEMI", 
            "EQUAL", "COLON", "LB", "RB", "LSB", "RSB", "LCB", "RCB", "NUMLIST", 
            "STRINGLIST", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "COMMENT", "SingleLineComment", "MultiLineComment", "INTEGER_LIT", 
                  "UNDERSCORE", "FLOAT_LIT", "DECPART", "EXPPART", "BOOLEAN_LIT", 
                  "FALSE", "TRUE", "STRING_LIT", "SUBSTRING", "ARRAY_LIT", 
                  "EXPS", "Escape_Sequence", "DUO_QUOTE", "SINGLE_QUOTE", 
                  "BackSpace", "FormFeed", "CarriageReturn", "NewLine", 
                  "SingleQuote", "BackSlash", "Dou_quote", "AUTO", "BREAK", 
                  "INTEGER", "VOID", "ARRAY", "FLOAT", "RETURN", "OUT", 
                  "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", "FUNCTION", 
                  "OF", "ELSE", "IF", "WHILE", "INHERIT", "PLUS", "MINUS", 
                  "MUL", "DIV", "MOD", "LESS", "GREATER", "LESS_THAN_OR_EQUAL", 
                  "GREATER_THAN_OR_EQUAL", "NOT", "AND", "OR", "EQUAL_TO", 
                  "NOT_EQUAL", "IDENTIFIER", "NUMBER", "SCOPE_RES", "PERIOD", 
                  "COMMA", "SEMI", "EQUAL", "COLON", "LB", "RB", "LSB", 
                  "RSB", "LCB", "RCB", "NUMLIST", "STRINGLIST", "WS", "UNCLOSE_STRING", 
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
     


