# Generated from c:\Users\84865\Documents\HCMUT-cse20\CSE-PPL\test\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("\u0247\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\3\2")
        buf.write("\6\2\u0088\n\2\r\2\16\2\u0089\3\2\3\2\3\3\3\3\5\3\u0090")
        buf.write("\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\5\6\u009d")
        buf.write("\n\6\3\7\3\7\3\7\3\7\5\7\u00a3\n\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\5\t\u00ac\n\t\3\n\3\n\3\n\3\n\5\n\u00b2\n\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00bc\n\13\3")
        buf.write("\13\3\13\5\13\u00c0\n\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\5\f\u00cb\n\f\3\f\3\f\5\f\u00cf\n\f\3\f\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\r\3\16\3\16\5\16\u00da\n\16\3\17\3")
        buf.write("\17\3\17\3\17\5\17\u00e0\n\17\3\20\3\20\3\20\3\20\5\20")
        buf.write("\u00e6\n\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00ee\n")
        buf.write("\20\5\20\u00f0\n\20\3\21\3\21\3\21\3\21\5\21\u00f6\n\21")
        buf.write("\3\22\3\22\3\22\3\22\5\22\u00fc\n\22\3\23\3\23\3\23\3")
        buf.write("\23\5\23\u0102\n\23\3\24\3\24\5\24\u0106\n\24\3\24\3\24")
        buf.write("\5\24\u010a\n\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3")
        buf.write("\25\3\25\5\25\u0115\n\25\3\26\3\26\3\26\3\26\3\26\5\26")
        buf.write("\u011c\n\26\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u0124\n")
        buf.write("\27\f\27\16\27\u0127\13\27\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\7\30\u012f\n\30\f\30\16\30\u0132\13\30\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\7\31\u013a\n\31\f\31\16\31\u013d\13")
        buf.write("\31\3\32\3\32\3\32\5\32\u0142\n\32\3\33\3\33\3\33\5\33")
        buf.write("\u0147\n\33\3\34\3\34\3\34\3\34\3\34\7\34\u014e\n\34\f")
        buf.write("\34\16\34\u0151\13\34\3\35\3\35\3\35\3\35\3\35\5\35\u0158")
        buf.write("\n\35\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0160\n\36\3")
        buf.write("\36\3\36\3\36\3\36\5\36\u0166\n\36\3\36\3\36\5\36\u016a")
        buf.write("\n\36\3\37\3\37\3\37\3\37\3\37\3 \3 \5 \u0173\n \3!\3")
        buf.write("!\3!\3!\3!\5!\u017a\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\5\"\u0187\n\"\3#\3#\3#\3#\3#\3$\3$\3$\3$")
        buf.write("\3$\3$\5$\u0194\n$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u01a0")
        buf.write("\n%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3(\3(\3)")
        buf.write("\3)\3)\3)\5)\u01b5\n)\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3")
        buf.write(",\3,\3,\3,\3,\3,\3-\3-\5-\u01c9\n-\3-\3-\3.\3.\3.\3.\3")
        buf.write("/\3/\5/\u01d3\n/\3\60\3\60\3\60\3\60\5\60\u01d9\n\60\3")
        buf.write("\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\65\5\65\u01f2\n\65\3\66\3\66\3\67\3\67\5\67\u01f8\n")
        buf.write("\67\38\38\38\38\38\58\u01ff\n8\39\39\3:\3:\3:\3:\3:\3")
        buf.write(":\3:\3:\3:\5:\u020c\n:\3;\3;\3;\3;\3<\3<\3<\3<\3<\5<\u0217")
        buf.write("\n<\3<\3<\3=\3=\3=\3=\3>\3>\3>\3>\3>\5>\u0224\n>\3>\3")
        buf.write(">\3?\3?\3?\3?\3?\5?\u022d\n?\3?\3?\3@\3@\3@\3@\3A\3A\3")
        buf.write("A\3A\3A\5A\u023a\nA\3A\3A\3B\3B\3B\3B\3B\3C\3C\3C\3C\3")
        buf.write("C\2\6,.\60\66D\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprt")
        buf.write("vxz|~\u0080\u0082\u0084\2\n\7\2\25\25\27\27\32\32\35\35")
        buf.write("\37\37\4\2-\60\64\65\3\2\62\63\3\2()\3\2*,\4\2\r\rBB\4")
        buf.write("\2(*,,\7\2\25\25\27\30\32\32\35\35\37\37\2\u0251\2\u0087")
        buf.write("\3\2\2\2\4\u008f\3\2\2\2\6\u0091\3\2\2\2\b\u0098\3\2\2")
        buf.write("\2\n\u009c\3\2\2\2\f\u00a2\3\2\2\2\16\u00a4\3\2\2\2\20")
        buf.write("\u00ab\3\2\2\2\22\u00ad\3\2\2\2\24\u00b5\3\2\2\2\26\u00c4")
        buf.write("\3\2\2\2\30\u00d3\3\2\2\2\32\u00d9\3\2\2\2\34\u00df\3")
        buf.write("\2\2\2\36\u00ef\3\2\2\2 \u00f5\3\2\2\2\"\u00fb\3\2\2\2")
        buf.write("$\u0101\3\2\2\2&\u0105\3\2\2\2(\u0114\3\2\2\2*\u011b\3")
        buf.write("\2\2\2,\u011d\3\2\2\2.\u0128\3\2\2\2\60\u0133\3\2\2\2")
        buf.write("\62\u0141\3\2\2\2\64\u0146\3\2\2\2\66\u0148\3\2\2\28\u0157")
        buf.write("\3\2\2\2:\u0169\3\2\2\2<\u016b\3\2\2\2>\u0172\3\2\2\2")
        buf.write("@\u0179\3\2\2\2B\u0186\3\2\2\2D\u0188\3\2\2\2F\u0193\3")
        buf.write("\2\2\2H\u019f\3\2\2\2J\u01a1\3\2\2\2L\u01ac\3\2\2\2N\u01ae")
        buf.write("\3\2\2\2P\u01b0\3\2\2\2R\u01b6\3\2\2\2T\u01ba\3\2\2\2")
        buf.write("V\u01c0\3\2\2\2X\u01c8\3\2\2\2Z\u01cc\3\2\2\2\\\u01d2")
        buf.write("\3\2\2\2^\u01d8\3\2\2\2`\u01da\3\2\2\2b\u01dd\3\2\2\2")
        buf.write("d\u01e0\3\2\2\2f\u01e4\3\2\2\2h\u01f1\3\2\2\2j\u01f3\3")
        buf.write("\2\2\2l\u01f7\3\2\2\2n\u01fe\3\2\2\2p\u0200\3\2\2\2r\u020b")
        buf.write("\3\2\2\2t\u020d\3\2\2\2v\u0211\3\2\2\2x\u021a\3\2\2\2")
        buf.write("z\u021e\3\2\2\2|\u0227\3\2\2\2~\u0230\3\2\2\2\u0080\u0234")
        buf.write("\3\2\2\2\u0082\u023d\3\2\2\2\u0084\u0242\3\2\2\2\u0086")
        buf.write("\u0088\5\4\3\2\u0087\u0086\3\2\2\2\u0088\u0089\3\2\2\2")
        buf.write("\u0089\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008b\3")
        buf.write("\2\2\2\u008b\u008c\7\2\2\3\u008c\3\3\2\2\2\u008d\u0090")
        buf.write("\5\20\t\2\u008e\u0090\5f\64\2\u008f\u008d\3\2\2\2\u008f")
        buf.write("\u008e\3\2\2\2\u0090\5\3\2\2\2\u0091\u0092\7\31\2\2\u0092")
        buf.write("\u0093\7>\2\2\u0093\u0094\5\n\6\2\u0094\u0095\7?\2\2\u0095")
        buf.write("\u0096\7#\2\2\u0096\u0097\5\b\5\2\u0097\7\3\2\2\2\u0098")
        buf.write("\u0099\t\2\2\2\u0099\t\3\2\2\2\u009a\u009d\5\f\7\2\u009b")
        buf.write("\u009d\5\16\b\2\u009c\u009a\3\2\2\2\u009c\u009b\3\2\2")
        buf.write("\2\u009d\13\3\2\2\2\u009e\u009f\7\r\2\2\u009f\u00a0\7")
        buf.write("8\2\2\u00a0\u00a3\5\f\7\2\u00a1\u00a3\7\r\2\2\u00a2\u009e")
        buf.write("\3\2\2\2\u00a2\u00a1\3\2\2\2\u00a3\r\3\2\2\2\u00a4\u00a5")
        buf.write("\7\16\2\2\u00a5\u00a6\78\2\2\u00a6\u00a7\5\16\b\2\u00a7")
        buf.write("\u00a8\7\16\2\2\u00a8\17\3\2\2\2\u00a9\u00ac\5\22\n\2")
        buf.write("\u00aa\u00ac\5\24\13\2\u00ab\u00a9\3\2\2\2\u00ab\u00aa")
        buf.write("\3\2\2\2\u00ac\21\3\2\2\2\u00ad\u00ae\5\34\17\2\u00ae")
        buf.write("\u00b1\7;\2\2\u00af\u00b2\5\b\5\2\u00b0\u00b2\5\6\4\2")
        buf.write("\u00b1\u00af\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\u00b3\3")
        buf.write("\2\2\2\u00b3\u00b4\79\2\2\u00b4\23\3\2\2\2\u00b5\u00bf")
        buf.write("\7B\2\2\u00b6\u00b7\78\2\2\u00b7\u00c0\5\26\f\2\u00b8")
        buf.write("\u00bb\7;\2\2\u00b9\u00bc\5\b\5\2\u00ba\u00bc\5\6\4\2")
        buf.write("\u00bb\u00b9\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc\u00bd\3")
        buf.write("\2\2\2\u00bd\u00be\7:\2\2\u00be\u00c0\3\2\2\2\u00bf\u00b6")
        buf.write("\3\2\2\2\u00bf\u00b8\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1")
        buf.write("\u00c2\5(\25\2\u00c2\u00c3\79\2\2\u00c3\25\3\2\2\2\u00c4")
        buf.write("\u00ce\7B\2\2\u00c5\u00c6\78\2\2\u00c6\u00cf\5\26\f\2")
        buf.write("\u00c7\u00ca\7;\2\2\u00c8\u00cb\5\b\5\2\u00c9\u00cb\5")
        buf.write("\6\4\2\u00ca\u00c8\3\2\2\2\u00ca\u00c9\3\2\2\2\u00cb\u00cc")
        buf.write("\3\2\2\2\u00cc\u00cd\7:\2\2\u00cd\u00cf\3\2\2\2\u00ce")
        buf.write("\u00c5\3\2\2\2\u00ce\u00c7\3\2\2\2\u00cf\u00d0\3\2\2\2")
        buf.write("\u00d0\u00d1\5(\25\2\u00d1\u00d2\78\2\2\u00d2\27\3\2\2")
        buf.write("\2\u00d3\u00d4\7@\2\2\u00d4\u00d5\5\32\16\2\u00d5\u00d6")
        buf.write("\7A\2\2\u00d6\31\3\2\2\2\u00d7\u00da\5\36\20\2\u00d8\u00da")
        buf.write("\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00d8\3\2\2\2\u00da")
        buf.write("\33\3\2\2\2\u00db\u00dc\7B\2\2\u00dc\u00dd\78\2\2\u00dd")
        buf.write("\u00e0\5\34\17\2\u00de\u00e0\7B\2\2\u00df\u00db\3\2\2")
        buf.write("\2\u00df\u00de\3\2\2\2\u00e0\35\3\2\2\2\u00e1\u00e6\7")
        buf.write("\16\2\2\u00e2\u00e6\7\20\2\2\u00e3\u00e6\5(\25\2\u00e4")
        buf.write("\u00e6\7\r\2\2\u00e5\u00e1\3\2\2\2\u00e5\u00e2\3\2\2\2")
        buf.write("\u00e5\u00e3\3\2\2\2\u00e5\u00e4\3\2\2\2\u00e6\u00e7\3")
        buf.write("\2\2\2\u00e7\u00e8\78\2\2\u00e8\u00f0\5\36\20\2\u00e9")
        buf.write("\u00ee\7\16\2\2\u00ea\u00ee\7\20\2\2\u00eb\u00ee\5(\25")
        buf.write("\2\u00ec\u00ee\7\r\2\2\u00ed\u00e9\3\2\2\2\u00ed\u00ea")
        buf.write("\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ec\3\2\2\2\u00ee")
        buf.write("\u00f0\3\2\2\2\u00ef\u00e5\3\2\2\2\u00ef\u00ed\3\2\2\2")
        buf.write("\u00f0\37\3\2\2\2\u00f1\u00f2\7\r\2\2\u00f2\u00f3\78\2")
        buf.write("\2\u00f3\u00f6\5 \21\2\u00f4\u00f6\7\r\2\2\u00f5\u00f1")
        buf.write("\3\2\2\2\u00f5\u00f4\3\2\2\2\u00f6!\3\2\2\2\u00f7\u00f8")
        buf.write("\7\16\2\2\u00f8\u00f9\78\2\2\u00f9\u00fc\5\"\22\2\u00fa")
        buf.write("\u00fc\7\16\2\2\u00fb\u00f7\3\2\2\2\u00fb\u00fa\3\2\2")
        buf.write("\2\u00fc#\3\2\2\2\u00fd\u00fe\7\20\2\2\u00fe\u00ff\78")
        buf.write("\2\2\u00ff\u0102\5$\23\2\u0100\u0102\7\20\2\2\u0101\u00fd")
        buf.write("\3\2\2\2\u0101\u0100\3\2\2\2\u0102%\3\2\2\2\u0103\u0106")
        buf.write("\7\'\2\2\u0104\u0106\3\2\2\2\u0105\u0103\3\2\2\2\u0105")
        buf.write("\u0104\3\2\2\2\u0106\u0109\3\2\2\2\u0107\u010a\7\34\2")
        buf.write("\2\u0108\u010a\3\2\2\2\u0109\u0107\3\2\2\2\u0109\u0108")
        buf.write("\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u010c\7B\2\2\u010c")
        buf.write("\u010d\7;\2\2\u010d\u010e\5\b\5\2\u010e\'\3\2\2\2\u010f")
        buf.write("\u0110\5*\26\2\u0110\u0111\7\66\2\2\u0111\u0112\5*\26")
        buf.write("\2\u0112\u0115\3\2\2\2\u0113\u0115\5*\26\2\u0114\u010f")
        buf.write("\3\2\2\2\u0114\u0113\3\2\2\2\u0115)\3\2\2\2\u0116\u0117")
        buf.write("\5,\27\2\u0117\u0118\t\3\2\2\u0118\u0119\5,\27\2\u0119")
        buf.write("\u011c\3\2\2\2\u011a\u011c\5,\27\2\u011b\u0116\3\2\2\2")
        buf.write("\u011b\u011a\3\2\2\2\u011c+\3\2\2\2\u011d\u011e\b\27\1")
        buf.write("\2\u011e\u011f\5.\30\2\u011f\u0125\3\2\2\2\u0120\u0121")
        buf.write("\f\4\2\2\u0121\u0122\t\4\2\2\u0122\u0124\5.\30\2\u0123")
        buf.write("\u0120\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123\3\2\2\2")
        buf.write("\u0125\u0126\3\2\2\2\u0126-\3\2\2\2\u0127\u0125\3\2\2")
        buf.write("\2\u0128\u0129\b\30\1\2\u0129\u012a\5\60\31\2\u012a\u0130")
        buf.write("\3\2\2\2\u012b\u012c\f\4\2\2\u012c\u012d\t\5\2\2\u012d")
        buf.write("\u012f\5\60\31\2\u012e\u012b\3\2\2\2\u012f\u0132\3\2\2")
        buf.write("\2\u0130\u012e\3\2\2\2\u0130\u0131\3\2\2\2\u0131/\3\2")
        buf.write("\2\2\u0132\u0130\3\2\2\2\u0133\u0134\b\31\1\2\u0134\u0135")
        buf.write("\5\62\32\2\u0135\u013b\3\2\2\2\u0136\u0137\f\4\2\2\u0137")
        buf.write("\u0138\t\6\2\2\u0138\u013a\5\62\32\2\u0139\u0136\3\2\2")
        buf.write("\2\u013a\u013d\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013c")
        buf.write("\3\2\2\2\u013c\61\3\2\2\2\u013d\u013b\3\2\2\2\u013e\u013f")
        buf.write("\7\61\2\2\u013f\u0142\5\62\32\2\u0140\u0142\5\64\33\2")
        buf.write("\u0141\u013e\3\2\2\2\u0141\u0140\3\2\2\2\u0142\63\3\2")
        buf.write("\2\2\u0143\u0144\7)\2\2\u0144\u0147\5\64\33\2\u0145\u0147")
        buf.write("\5\66\34\2\u0146\u0143\3\2\2\2\u0146\u0145\3\2\2\2\u0147")
        buf.write("\65\3\2\2\2\u0148\u0149\b\34\1\2\u0149\u014a\58\35\2\u014a")
        buf.write("\u014f\3\2\2\2\u014b\u014c\f\4\2\2\u014c\u014e\5:\36\2")
        buf.write("\u014d\u014b\3\2\2\2\u014e\u0151\3\2\2\2\u014f\u014d\3")
        buf.write("\2\2\2\u014f\u0150\3\2\2\2\u0150\67\3\2\2\2\u0151\u014f")
        buf.write("\3\2\2\2\u0152\u0153\7<\2\2\u0153\u0154\5(\25\2\u0154")
        buf.write("\u0155\7=\2\2\u0155\u0158\3\2\2\2\u0156\u0158\5:\36\2")
        buf.write("\u0157\u0152\3\2\2\2\u0157\u0156\3\2\2\2\u01589\3\2\2")
        buf.write("\2\u0159\u0160\7\r\2\2\u015a\u0160\7\16\2\2\u015b\u0160")
        buf.write("\7\20\2\2\u015c\u0160\7B\2\2\u015d\u0160\5<\37\2\u015e")
        buf.write("\u0160\5\30\r\2\u015f\u0159\3\2\2\2\u015f\u015a\3\2\2")
        buf.write("\2\u015f\u015b\3\2\2\2\u015f\u015c\3\2\2\2\u015f\u015d")
        buf.write("\3\2\2\2\u015f\u015e\3\2\2\2\u0160\u016a\3\2\2\2\u0161")
        buf.write("\u0162\7B\2\2\u0162\u0165\7>\2\2\u0163\u0166\5 \21\2\u0164")
        buf.write("\u0166\5:\36\2\u0165\u0163\3\2\2\2\u0165\u0164\3\2\2\2")
        buf.write("\u0166\u0167\3\2\2\2\u0167\u0168\7?\2\2\u0168\u016a\3")
        buf.write("\2\2\2\u0169\u015f\3\2\2\2\u0169\u0161\3\2\2\2\u016a;")
        buf.write("\3\2\2\2\u016b\u016c\7B\2\2\u016c\u016d\7<\2\2\u016d\u016e")
        buf.write("\5> \2\u016e\u016f\7=\2\2\u016f=\3\2\2\2\u0170\u0173\5")
        buf.write("@!\2\u0171\u0173\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0171")
        buf.write("\3\2\2\2\u0173?\3\2\2\2\u0174\u0175\5(\25\2\u0175\u0176")
        buf.write("\78\2\2\u0176\u0177\5@!\2\u0177\u017a\3\2\2\2\u0178\u017a")
        buf.write("\5(\25\2\u0179\u0174\3\2\2\2\u0179\u0178\3\2\2\2\u017a")
        buf.write("A\3\2\2\2\u017b\u0187\5D#\2\u017c\u0187\5H%\2\u017d\u0187")
        buf.write("\5J&\2\u017e\u0187\5T+\2\u017f\u0187\5V,\2\u0180\u0187")
        buf.write("\5Z.\2\u0181\u0187\5d\63\2\u0182\u0187\5b\62\2\u0183\u0187")
        buf.write("\5`\61\2\u0184\u0187\5X-\2\u0185\u0187\5\20\t\2\u0186")
        buf.write("\u017b\3\2\2\2\u0186\u017c\3\2\2\2\u0186\u017d\3\2\2\2")
        buf.write("\u0186\u017e\3\2\2\2\u0186\u017f\3\2\2\2\u0186\u0180\3")
        buf.write("\2\2\2\u0186\u0181\3\2\2\2\u0186\u0182\3\2\2\2\u0186\u0183")
        buf.write("\3\2\2\2\u0186\u0184\3\2\2\2\u0186\u0185\3\2\2\2\u0187")
        buf.write("C\3\2\2\2\u0188\u0189\5F$\2\u0189\u018a\7:\2\2\u018a\u018b")
        buf.write("\5(\25\2\u018b\u018c\79\2\2\u018cE\3\2\2\2\u018d\u018e")
        buf.write("\7B\2\2\u018e\u018f\7>\2\2\u018f\u0190\5 \21\2\u0190\u0191")
        buf.write("\7?\2\2\u0191\u0194\3\2\2\2\u0192\u0194\7B\2\2\u0193\u018d")
        buf.write("\3\2\2\2\u0193\u0192\3\2\2\2\u0194G\3\2\2\2\u0195\u0196")
        buf.write("\7%\2\2\u0196\u0197\5(\25\2\u0197\u0198\5B\"\2\u0198\u0199")
        buf.write("\7$\2\2\u0199\u019a\5B\"\2\u019a\u01a0\3\2\2\2\u019b\u019c")
        buf.write("\7%\2\2\u019c\u019d\5(\25\2\u019d\u019e\5B\"\2\u019e\u01a0")
        buf.write("\3\2\2\2\u019f\u0195\3\2\2\2\u019f\u019b\3\2\2\2\u01a0")
        buf.write("I\3\2\2\2\u01a1\u01a2\7<\2\2\u01a2\u01a3\5L\'\2\u01a3")
        buf.write("\u01a4\7:\2\2\u01a4\u01a5\5N(\2\u01a5\u01a6\78\2\2\u01a6")
        buf.write("\u01a7\5P)\2\u01a7\u01a8\78\2\2\u01a8\u01a9\5R*\2\u01a9")
        buf.write("\u01aa\7=\2\2\u01aa\u01ab\5B\"\2\u01abK\3\2\2\2\u01ac")
        buf.write("\u01ad\7B\2\2\u01adM\3\2\2\2\u01ae\u01af\t\7\2\2\u01af")
        buf.write("O\3\2\2\2\u01b0\u01b1\7B\2\2\u01b1\u01b4\t\3\2\2\u01b2")
        buf.write("\u01b5\7B\2\2\u01b3\u01b5\5(\25\2\u01b4\u01b2\3\2\2\2")
        buf.write("\u01b4\u01b3\3\2\2\2\u01b5Q\3\2\2\2\u01b6\u01b7\7B\2\2")
        buf.write("\u01b7\u01b8\t\b\2\2\u01b8\u01b9\5(\25\2\u01b9S\3\2\2")
        buf.write("\2\u01ba\u01bb\7&\2\2\u01bb\u01bc\7<\2\2\u01bc\u01bd\5")
        buf.write("(\25\2\u01bd\u01be\7=\2\2\u01be\u01bf\5B\"\2\u01bfU\3")
        buf.write("\2\2\2\u01c0\u01c1\7!\2\2\u01c1\u01c2\5Z.\2\u01c2\u01c3")
        buf.write("\7&\2\2\u01c3\u01c4\5(\25\2\u01c4\u01c5\79\2\2\u01c5W")
        buf.write("\3\2\2\2\u01c6\u01c9\5<\37\2\u01c7\u01c9\5r:\2\u01c8\u01c6")
        buf.write("\3\2\2\2\u01c8\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca")
        buf.write("\u01cb\79\2\2\u01cbY\3\2\2\2\u01cc\u01cd\7@\2\2\u01cd")
        buf.write("\u01ce\5\\/\2\u01ce\u01cf\7A\2\2\u01cf[\3\2\2\2\u01d0")
        buf.write("\u01d3\5^\60\2\u01d1\u01d3\3\2\2\2\u01d2\u01d0\3\2\2\2")
        buf.write("\u01d2\u01d1\3\2\2\2\u01d3]\3\2\2\2\u01d4\u01d5\5B\"\2")
        buf.write("\u01d5\u01d6\5^\60\2\u01d6\u01d9\3\2\2\2\u01d7\u01d9\5")
        buf.write("B\"\2\u01d8\u01d4\3\2\2\2\u01d8\u01d7\3\2\2\2\u01d9_\3")
        buf.write("\2\2\2\u01da\u01db\7\26\2\2\u01db\u01dc\79\2\2\u01dca")
        buf.write("\3\2\2\2\u01dd\u01de\7 \2\2\u01de\u01df\79\2\2\u01dfc")
        buf.write("\3\2\2\2\u01e0\u01e1\7\33\2\2\u01e1\u01e2\5(\25\2\u01e2")
        buf.write("\u01e3\79\2\2\u01e3e\3\2\2\2\u01e4\u01e5\7B\2\2\u01e5")
        buf.write("\u01e6\7;\2\2\u01e6\u01e7\7\"\2\2\u01e7\u01e8\5p9\2\u01e8")
        buf.write("\u01e9\7<\2\2\u01e9\u01ea\5l\67\2\u01ea\u01eb\7=\2\2\u01eb")
        buf.write("\u01ec\5h\65\2\u01ec\u01ed\5B\"\2\u01edg\3\2\2\2\u01ee")
        buf.write("\u01ef\7\'\2\2\u01ef\u01f2\5j\66\2\u01f0\u01f2\3\2\2\2")
        buf.write("\u01f1\u01ee\3\2\2\2\u01f1\u01f0\3\2\2\2\u01f2i\3\2\2")
        buf.write("\2\u01f3\u01f4\7B\2\2\u01f4k\3\2\2\2\u01f5\u01f8\5n8\2")
        buf.write("\u01f6\u01f8\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7\u01f6\3")
        buf.write("\2\2\2\u01f8m\3\2\2\2\u01f9\u01fa\5&\24\2\u01fa\u01fb")
        buf.write("\78\2\2\u01fb\u01fc\5n8\2\u01fc\u01ff\3\2\2\2\u01fd\u01ff")
        buf.write("\5&\24\2\u01fe\u01f9\3\2\2\2\u01fe\u01fd\3\2\2\2\u01ff")
        buf.write("o\3\2\2\2\u0200\u0201\t\t\2\2\u0201q\3\2\2\2\u0202\u020c")
        buf.write("\5t;\2\u0203\u020c\5v<\2\u0204\u020c\5x=\2\u0205\u020c")
        buf.write("\5z>\2\u0206\u020c\5|?\2\u0207\u020c\5~@\2\u0208\u020c")
        buf.write("\5\u0080A\2\u0209\u020c\5\u0082B\2\u020a\u020c\5\u0084")
        buf.write("C\2\u020b\u0202\3\2\2\2\u020b\u0203\3\2\2\2\u020b\u0204")
        buf.write("\3\2\2\2\u020b\u0205\3\2\2\2\u020b\u0206\3\2\2\2\u020b")
        buf.write("\u0207\3\2\2\2\u020b\u0208\3\2\2\2\u020b\u0209\3\2\2\2")
        buf.write("\u020b\u020a\3\2\2\2\u020cs\3\2\2\2\u020d\u020e\7\3\2")
        buf.write("\2\u020e\u020f\7<\2\2\u020f\u0210\7=\2\2\u0210u\3\2\2")
        buf.write("\2\u0211\u0212\7\4\2\2\u0212\u0216\7<\2\2\u0213\u0217")
        buf.write("\7\r\2\2\u0214\u0217\7B\2\2\u0215\u0217\5(\25\2\u0216")
        buf.write("\u0213\3\2\2\2\u0216\u0214\3\2\2\2\u0216\u0215\3\2\2\2")
        buf.write("\u0217\u0218\3\2\2\2\u0218\u0219\7=\2\2\u0219w\3\2\2\2")
        buf.write("\u021a\u021b\7\5\2\2\u021b\u021c\7<\2\2\u021c\u021d\7")
        buf.write("=\2\2\u021dy\3\2\2\2\u021e\u021f\7\6\2\2\u021f\u0223\7")
        buf.write("<\2\2\u0220\u0224\7\16\2\2\u0221\u0224\7B\2\2\u0222\u0224")
        buf.write("\5(\25\2\u0223\u0220\3\2\2\2\u0223\u0221\3\2\2\2\u0223")
        buf.write("\u0222\3\2\2\2\u0224\u0225\3\2\2\2\u0225\u0226\7=\2\2")
        buf.write("\u0226{\3\2\2\2\u0227\u0228\7\7\2\2\u0228\u022c\7<\2\2")
        buf.write("\u0229\u022d\7\17\2\2\u022a\u022d\7B\2\2\u022b\u022d\5")
        buf.write("(\25\2\u022c\u0229\3\2\2\2\u022c\u022a\3\2\2\2\u022c\u022b")
        buf.write("\3\2\2\2\u022d\u022e\3\2\2\2\u022e\u022f\7=\2\2\u022f")
        buf.write("}\3\2\2\2\u0230\u0231\7\b\2\2\u0231\u0232\7<\2\2\u0232")
        buf.write("\u0233\7=\2\2\u0233\177\3\2\2\2\u0234\u0235\7\t\2\2\u0235")
        buf.write("\u0239\7<\2\2\u0236\u023a\7\20\2\2\u0237\u023a\7B\2\2")
        buf.write("\u0238\u023a\5(\25\2\u0239\u0236\3\2\2\2\u0239\u0237\3")
        buf.write("\2\2\2\u0239\u0238\3\2\2\2\u023a\u023b\3\2\2\2\u023b\u023c")
        buf.write("\7=\2\2\u023c\u0081\3\2\2\2\u023d\u023e\7\n\2\2\u023e")
        buf.write("\u023f\7<\2\2\u023f\u0240\5\36\20\2\u0240\u0241\7=\2\2")
        buf.write("\u0241\u0083\3\2\2\2\u0242\u0243\7\13\2\2\u0243\u0244")
        buf.write("\7<\2\2\u0244\u0245\7=\2\2\u0245\u0085\3\2\2\2\63\u0089")
        buf.write("\u008f\u009c\u00a2\u00ab\u00b1\u00bb\u00bf\u00ca\u00ce")
        buf.write("\u00d9\u00df\u00e5\u00ed\u00ef\u00f5\u00fb\u0101\u0105")
        buf.write("\u0109\u0114\u011b\u0125\u0130\u013b\u0141\u0146\u014f")
        buf.write("\u0157\u015f\u0165\u0169\u0172\u0179\u0186\u0193\u019f")
        buf.write("\u01b4\u01c8\u01d2\u01d8\u01f1\u01f7\u01fe\u020b\u0216")
        buf.write("\u0223\u022c\u0239")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'readInteger'", "'printInteger'", "'readFloat'", 
                     "'writeFloat'", "'printBoolean'", "'readString'", "'printString'", 
                     "'super'", "'preventDefault'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'auto'", "'break'", 
                     "'integer'", "'void'", "'array'", "'float'", "'return'", 
                     "'out'", "'boolean'", "'for'", "'string'", "'continue'", 
                     "'do'", "'function'", "'of'", "'else'", "'if'", "'while'", 
                     "'inherit'", "'+'", "'-'", "'*'", "'/'", "'%'", "'<'", 
                     "'>'", "'<='", "'>='", "'!'", "'&&'", "'||'", "'=='", 
                     "'!='", "'::'", "'.'", "','", "';'", "'='", "':'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "COMMENT", "INTEGER_LIT", 
                      "FLOAT_LIT", "BOOLEAN_LIT", "STRING_LIT", "ARRAY_LIT", 
                      "ARRAY_LIT_INT", "ARRAY_LIT_FLOAT", "ARRAY_LIT_STRINGLIST", 
                      "AUTO", "BREAK", "INTEGER", "VOID", "ARRAY", "FLOAT", 
                      "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", 
                      "DO", "FUNCTION", "OF", "ELSE", "IF", "WHILE", "INHERIT", 
                      "PLUS", "MINUS", "MUL", "DIV", "MOD", "LESS", "GREATER", 
                      "LTE", "GTE", "NOT", "AND", "OR", "EQUAL_TO", "NOT_EQUAL", 
                      "CONCAT", "PERIOD", "COMMA", "SEMI", "EQUAL", "COLON", 
                      "LB", "RB", "LSB", "RSB", "LCB", "RCB", "IDENTIFIER", 
                      "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_array_type = 2
    RULE_element_type = 3
    RULE_dimesion = 4
    RULE_dimesion_type_int = 5
    RULE_dimesion_type_float = 6
    RULE_variable_decl = 7
    RULE_var_decl_no_eq = 8
    RULE_var_decl_eq = 9
    RULE_recursive = 10
    RULE_array_list = 11
    RULE_exp_list_term = 12
    RULE_identifier_list = 13
    RULE_expression_list = 14
    RULE_exp_list_type_int = 15
    RULE_exp_list_type_float = 16
    RULE_exp_list_type_string = 17
    RULE_parameter = 18
    RULE_expression = 19
    RULE_expression_1 = 20
    RULE_expression_2 = 21
    RULE_expression_3 = 22
    RULE_expression_4 = 23
    RULE_expression_5 = 24
    RULE_expression_6 = 25
    RULE_expression_7 = 26
    RULE_expression_8 = 27
    RULE_factor = 28
    RULE_function_call = 29
    RULE_exps_list = 30
    RULE_exp_list = 31
    RULE_statement = 32
    RULE_assign_stmt = 33
    RULE_lhs = 34
    RULE_if_stmt = 35
    RULE_for_stmt = 36
    RULE_scala_val = 37
    RULE_init_expr = 38
    RULE_condition_expr = 39
    RULE_update_expr = 40
    RULE_while_stmt = 41
    RULE_do_while_stmt = 42
    RULE_call_stmt = 43
    RULE_block_stmt = 44
    RULE_statement_term = 45
    RULE_statement_list = 46
    RULE_break_stmt = 47
    RULE_continue_stmt = 48
    RULE_return_stmt = 49
    RULE_function_decl = 50
    RULE_inheritance = 51
    RULE_function_name = 52
    RULE_paramter_list = 53
    RULE_paramter_list_term = 54
    RULE_return_type = 55
    RULE_s_func_decl = 56
    RULE_read_integer = 57
    RULE_print_integer = 58
    RULE_read_float = 59
    RULE_write_float = 60
    RULE_print_boolean = 61
    RULE_read_string = 62
    RULE_print_string = 63
    RULE_super_ = 64
    RULE_prevent_default = 65

    ruleNames =  [ "program", "decls", "array_type", "element_type", "dimesion", 
                   "dimesion_type_int", "dimesion_type_float", "variable_decl", 
                   "var_decl_no_eq", "var_decl_eq", "recursive", "array_list", 
                   "exp_list_term", "identifier_list", "expression_list", 
                   "exp_list_type_int", "exp_list_type_float", "exp_list_type_string", 
                   "parameter", "expression", "expression_1", "expression_2", 
                   "expression_3", "expression_4", "expression_5", "expression_6", 
                   "expression_7", "expression_8", "factor", "function_call", 
                   "exps_list", "exp_list", "statement", "assign_stmt", 
                   "lhs", "if_stmt", "for_stmt", "scala_val", "init_expr", 
                   "condition_expr", "update_expr", "while_stmt", "do_while_stmt", 
                   "call_stmt", "block_stmt", "statement_term", "statement_list", 
                   "break_stmt", "continue_stmt", "return_stmt", "function_decl", 
                   "inheritance", "function_name", "paramter_list", "paramter_list_term", 
                   "return_type", "s_func_decl", "read_integer", "print_integer", 
                   "read_float", "write_float", "print_boolean", "read_string", 
                   "print_string", "super_", "prevent_default" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    COMMENT=10
    INTEGER_LIT=11
    FLOAT_LIT=12
    BOOLEAN_LIT=13
    STRING_LIT=14
    ARRAY_LIT=15
    ARRAY_LIT_INT=16
    ARRAY_LIT_FLOAT=17
    ARRAY_LIT_STRINGLIST=18
    AUTO=19
    BREAK=20
    INTEGER=21
    VOID=22
    ARRAY=23
    FLOAT=24
    RETURN=25
    OUT=26
    BOOLEAN=27
    FOR=28
    STRING=29
    CONTINUE=30
    DO=31
    FUNCTION=32
    OF=33
    ELSE=34
    IF=35
    WHILE=36
    INHERIT=37
    PLUS=38
    MINUS=39
    MUL=40
    DIV=41
    MOD=42
    LESS=43
    GREATER=44
    LTE=45
    GTE=46
    NOT=47
    AND=48
    OR=49
    EQUAL_TO=50
    NOT_EQUAL=51
    CONCAT=52
    PERIOD=53
    COMMA=54
    SEMI=55
    EQUAL=56
    COLON=57
    LB=58
    RB=59
    LSB=60
    RSB=61
    LCB=62
    RCB=63
    IDENTIFIER=64
    WS=65
    UNCLOSE_STRING=66
    ILLEGAL_ESCAPE=67
    ERROR_CHAR=68

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def decls(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.DeclsContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.DeclsContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 132
                self.decls()
                self.state = 135 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.IDENTIFIER):
                    break

            self.state = 137
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Variable_declContext,0)


        def function_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Function_declContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_decls




    def decls(self):

        localctx = BKOOLParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.variable_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.function_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(BKOOLParser.ARRAY, 0)

        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def dimesion(self):
            return self.getTypedRuleContext(BKOOLParser.DimesionContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def OF(self):
            return self.getToken(BKOOLParser.OF, 0)

        def element_type(self):
            return self.getTypedRuleContext(BKOOLParser.Element_typeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_array_type




    def array_type(self):

        localctx = BKOOLParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(BKOOLParser.ARRAY)
            self.state = 144
            self.match(BKOOLParser.LSB)
            self.state = 145
            self.dimesion()
            self.state = 146
            self.match(BKOOLParser.RSB)
            self.state = 147
            self.match(BKOOLParser.OF)
            self.state = 148
            self.element_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(BKOOLParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def AUTO(self):
            return self.getToken(BKOOLParser.AUTO, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_element_type




    def element_type(self):

        localctx = BKOOLParser.Element_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_element_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.AUTO) | (1 << BKOOLParser.INTEGER) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimesionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimesion_type_int(self):
            return self.getTypedRuleContext(BKOOLParser.Dimesion_type_intContext,0)


        def dimesion_type_float(self):
            return self.getTypedRuleContext(BKOOLParser.Dimesion_type_floatContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_dimesion




    def dimesion(self):

        localctx = BKOOLParser.DimesionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dimesion)
        try:
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTEGER_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.dimesion_type_int()
                pass
            elif token in [BKOOLParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.dimesion_type_float()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimesion_type_intContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LIT(self):
            return self.getToken(BKOOLParser.INTEGER_LIT, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def dimesion_type_int(self):
            return self.getTypedRuleContext(BKOOLParser.Dimesion_type_intContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_dimesion_type_int




    def dimesion_type_int(self):

        localctx = BKOOLParser.Dimesion_type_intContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_dimesion_type_int)
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.match(BKOOLParser.INTEGER_LIT)
                self.state = 157
                self.match(BKOOLParser.COMMA)
                self.state = 158
                self.dimesion_type_int()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.match(BKOOLParser.INTEGER_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimesion_type_floatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.FLOAT_LIT)
            else:
                return self.getToken(BKOOLParser.FLOAT_LIT, i)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def dimesion_type_float(self):
            return self.getTypedRuleContext(BKOOLParser.Dimesion_type_floatContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_dimesion_type_float




    def dimesion_type_float(self):

        localctx = BKOOLParser.Dimesion_type_floatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_dimesion_type_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(BKOOLParser.FLOAT_LIT)
            self.state = 163
            self.match(BKOOLParser.COMMA)
            self.state = 164
            self.dimesion_type_float()
            self.state = 165
            self.match(BKOOLParser.FLOAT_LIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl_no_eq(self):
            return self.getTypedRuleContext(BKOOLParser.Var_decl_no_eqContext,0)


        def var_decl_eq(self):
            return self.getTypedRuleContext(BKOOLParser.Var_decl_eqContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_variable_decl




    def variable_decl(self):

        localctx = BKOOLParser.Variable_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variable_decl)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.var_decl_no_eq()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.var_decl_eq()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_no_eqContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier_list(self):
            return self.getTypedRuleContext(BKOOLParser.Identifier_listContext,0)


        def COLON(self):
            return self.getToken(BKOOLParser.COLON, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def element_type(self):
            return self.getTypedRuleContext(BKOOLParser.Element_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_typeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_var_decl_no_eq




    def var_decl_no_eq(self):

        localctx = BKOOLParser.Var_decl_no_eqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_var_decl_no_eq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.identifier_list()
            self.state = 172
            self.match(BKOOLParser.COLON)
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.AUTO, BKOOLParser.INTEGER, BKOOLParser.FLOAT, BKOOLParser.BOOLEAN, BKOOLParser.STRING]:
                self.state = 173
                self.element_type()
                pass
            elif token in [BKOOLParser.ARRAY]:
                self.state = 174
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 177
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_eqContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BKOOLParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def recursive(self):
            return self.getTypedRuleContext(BKOOLParser.RecursiveContext,0)


        def COLON(self):
            return self.getToken(BKOOLParser.COLON, 0)

        def EQUAL(self):
            return self.getToken(BKOOLParser.EQUAL, 0)

        def element_type(self):
            return self.getTypedRuleContext(BKOOLParser.Element_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_typeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_var_decl_eq




    def var_decl_eq(self):

        localctx = BKOOLParser.Var_decl_eqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_var_decl_eq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(BKOOLParser.IDENTIFIER)
            self.state = 189
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.COMMA]:
                self.state = 180
                self.match(BKOOLParser.COMMA)
                self.state = 181
                self.recursive()
                pass
            elif token in [BKOOLParser.COLON]:
                self.state = 182
                self.match(BKOOLParser.COLON)
                self.state = 185
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.AUTO, BKOOLParser.INTEGER, BKOOLParser.FLOAT, BKOOLParser.BOOLEAN, BKOOLParser.STRING]:
                    self.state = 183
                    self.element_type()
                    pass
                elif token in [BKOOLParser.ARRAY]:
                    self.state = 184
                    self.array_type()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 187
                self.match(BKOOLParser.EQUAL)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 191
            self.expression()
            self.state = 192
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RecursiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BKOOLParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def recursive(self):
            return self.getTypedRuleContext(BKOOLParser.RecursiveContext,0)


        def COLON(self):
            return self.getToken(BKOOLParser.COLON, 0)

        def EQUAL(self):
            return self.getToken(BKOOLParser.EQUAL, 0)

        def element_type(self):
            return self.getTypedRuleContext(BKOOLParser.Element_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_typeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_recursive




    def recursive(self):

        localctx = BKOOLParser.RecursiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_recursive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(BKOOLParser.IDENTIFIER)
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.COMMA]:
                self.state = 195
                self.match(BKOOLParser.COMMA)
                self.state = 196
                self.recursive()
                pass
            elif token in [BKOOLParser.COLON]:
                self.state = 197
                self.match(BKOOLParser.COLON)
                self.state = 200
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.AUTO, BKOOLParser.INTEGER, BKOOLParser.FLOAT, BKOOLParser.BOOLEAN, BKOOLParser.STRING]:
                    self.state = 198
                    self.element_type()
                    pass
                elif token in [BKOOLParser.ARRAY]:
                    self.state = 199
                    self.array_type()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 202
                self.match(BKOOLParser.EQUAL)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 206
            self.expression()
            self.state = 207
            self.match(BKOOLParser.COMMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(BKOOLParser.LCB, 0)

        def RCB(self):
            return self.getToken(BKOOLParser.RCB, 0)

        def exp_list_term(self):
            return self.getTypedRuleContext(BKOOLParser.Exp_list_termContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_array_list




    def array_list(self):

        localctx = BKOOLParser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_array_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(BKOOLParser.LCB)

            self.state = 210
            self.exp_list_term()
            self.state = 211
            self.match(BKOOLParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_list_termContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_list(self):
            return self.getTypedRuleContext(BKOOLParser.Expression_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp_list_term




    def exp_list_term(self):

        localctx = BKOOLParser.Exp_list_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exp_list_term)
        try:
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTEGER_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.MINUS, BKOOLParser.NOT, BKOOLParser.LB, BKOOLParser.LCB, BKOOLParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.expression_list()
                pass
            elif token in [BKOOLParser.RCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Identifier_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BKOOLParser.IDENTIFIER, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def identifier_list(self):
            return self.getTypedRuleContext(BKOOLParser.Identifier_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_identifier_list




    def identifier_list(self):

        localctx = BKOOLParser.Identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_identifier_list)
        try:
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.match(BKOOLParser.IDENTIFIER)
                self.state = 218
                self.match(BKOOLParser.COMMA)
                self.state = 219
                self.identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.match(BKOOLParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def expression_list(self):
            return self.getTypedRuleContext(BKOOLParser.Expression_listContext,0)


        def FLOAT_LIT(self):
            return self.getToken(BKOOLParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(BKOOLParser.STRING_LIT, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def INTEGER_LIT(self):
            return self.getToken(BKOOLParser.INTEGER_LIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expression_list




    def expression_list(self):

        localctx = BKOOLParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expression_list)
        try:
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 223
                    self.match(BKOOLParser.FLOAT_LIT)
                    pass

                elif la_ == 2:
                    self.state = 224
                    self.match(BKOOLParser.STRING_LIT)
                    pass

                elif la_ == 3:
                    self.state = 225
                    self.expression()
                    pass

                elif la_ == 4:
                    self.state = 226
                    self.match(BKOOLParser.INTEGER_LIT)
                    pass


                self.state = 229
                self.match(BKOOLParser.COMMA)
                self.state = 230
                self.expression_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 231
                    self.match(BKOOLParser.FLOAT_LIT)
                    pass

                elif la_ == 2:
                    self.state = 232
                    self.match(BKOOLParser.STRING_LIT)
                    pass

                elif la_ == 3:
                    self.state = 233
                    self.expression()
                    pass

                elif la_ == 4:
                    self.state = 234
                    self.match(BKOOLParser.INTEGER_LIT)
                    pass


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_list_type_intContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LIT(self):
            return self.getToken(BKOOLParser.INTEGER_LIT, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def exp_list_type_int(self):
            return self.getTypedRuleContext(BKOOLParser.Exp_list_type_intContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp_list_type_int




    def exp_list_type_int(self):

        localctx = BKOOLParser.Exp_list_type_intContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_exp_list_type_int)
        try:
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.match(BKOOLParser.INTEGER_LIT)
                self.state = 240
                self.match(BKOOLParser.COMMA)
                self.state = 241
                self.exp_list_type_int()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.match(BKOOLParser.INTEGER_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_list_type_floatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT_LIT(self):
            return self.getToken(BKOOLParser.FLOAT_LIT, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def exp_list_type_float(self):
            return self.getTypedRuleContext(BKOOLParser.Exp_list_type_floatContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp_list_type_float




    def exp_list_type_float(self):

        localctx = BKOOLParser.Exp_list_type_floatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_exp_list_type_float)
        try:
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.match(BKOOLParser.FLOAT_LIT)
                self.state = 246
                self.match(BKOOLParser.COMMA)
                self.state = 247
                self.exp_list_type_float()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.match(BKOOLParser.FLOAT_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_list_type_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LIT(self):
            return self.getToken(BKOOLParser.STRING_LIT, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def exp_list_type_string(self):
            return self.getTypedRuleContext(BKOOLParser.Exp_list_type_stringContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp_list_type_string




    def exp_list_type_string(self):

        localctx = BKOOLParser.Exp_list_type_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exp_list_type_string)
        try:
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.match(BKOOLParser.STRING_LIT)
                self.state = 252
                self.match(BKOOLParser.COMMA)
                self.state = 253
                self.exp_list_type_string()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.match(BKOOLParser.STRING_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BKOOLParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(BKOOLParser.COLON, 0)

        def element_type(self):
            return self.getTypedRuleContext(BKOOLParser.Element_typeContext,0)


        def INHERIT(self):
            return self.getToken(BKOOLParser.INHERIT, 0)

        def OUT(self):
            return self.getToken(BKOOLParser.OUT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_parameter




    def parameter(self):

        localctx = BKOOLParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INHERIT]:
                self.state = 257
                self.match(BKOOLParser.INHERIT)
                pass
            elif token in [BKOOLParser.OUT, BKOOLParser.IDENTIFIER]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.OUT]:
                self.state = 261
                self.match(BKOOLParser.OUT)
                pass
            elif token in [BKOOLParser.IDENTIFIER]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 265
            self.match(BKOOLParser.IDENTIFIER)
            self.state = 266
            self.match(BKOOLParser.COLON)
            self.state = 267
            self.element_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expression_1Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expression_1Context,i)


        def CONCAT(self):
            return self.getToken(BKOOLParser.CONCAT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expression




    def expression(self):

        localctx = BKOOLParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expression)
        try:
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.expression_1()
                self.state = 270
                self.match(BKOOLParser.CONCAT)
                self.state = 271
                self.expression_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.expression_1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expression_2Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expression_2Context,i)


        def EQUAL_TO(self):
            return self.getToken(BKOOLParser.EQUAL_TO, 0)

        def NOT_EQUAL(self):
            return self.getToken(BKOOLParser.NOT_EQUAL, 0)

        def LESS(self):
            return self.getToken(BKOOLParser.LESS, 0)

        def GREATER(self):
            return self.getToken(BKOOLParser.GREATER, 0)

        def LTE(self):
            return self.getToken(BKOOLParser.LTE, 0)

        def GTE(self):
            return self.getToken(BKOOLParser.GTE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expression_1




    def expression_1(self):

        localctx = BKOOLParser.Expression_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expression_1)
        self._la = 0 # Token type
        try:
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.expression_2(0)
                self.state = 277
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LESS) | (1 << BKOOLParser.GREATER) | (1 << BKOOLParser.LTE) | (1 << BKOOLParser.GTE) | (1 << BKOOLParser.EQUAL_TO) | (1 << BKOOLParser.NOT_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 278
                self.expression_2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.expression_2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_3(self):
            return self.getTypedRuleContext(BKOOLParser.Expression_3Context,0)


        def expression_2(self):
            return self.getTypedRuleContext(BKOOLParser.Expression_2Context,0)


        def AND(self):
            return self.getToken(BKOOLParser.AND, 0)

        def OR(self):
            return self.getToken(BKOOLParser.OR, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expression_2



    def expression_2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expression_2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expression_2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.expression_3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expression_2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_2)
                    self.state = 286
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 287
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.AND or _la==BKOOLParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 288
                    self.expression_3(0) 
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression_3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_4(self):
            return self.getTypedRuleContext(BKOOLParser.Expression_4Context,0)


        def expression_3(self):
            return self.getTypedRuleContext(BKOOLParser.Expression_3Context,0)


        def PLUS(self):
            return self.getToken(BKOOLParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(BKOOLParser.MINUS, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expression_3



    def expression_3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expression_3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expression_3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.expression_4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 302
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expression_3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_3)
                    self.state = 297
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 298
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.PLUS or _la==BKOOLParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 299
                    self.expression_4(0) 
                self.state = 304
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression_4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_5(self):
            return self.getTypedRuleContext(BKOOLParser.Expression_5Context,0)


        def expression_4(self):
            return self.getTypedRuleContext(BKOOLParser.Expression_4Context,0)


        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def DIV(self):
            return self.getToken(BKOOLParser.DIV, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expression_4



    def expression_4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expression_4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expression_4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.expression_5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 313
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expression_4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_4)
                    self.state = 308
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 309
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.DIV) | (1 << BKOOLParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 310
                    self.expression_5() 
                self.state = 315
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression_5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def expression_5(self):
            return self.getTypedRuleContext(BKOOLParser.Expression_5Context,0)


        def expression_6(self):
            return self.getTypedRuleContext(BKOOLParser.Expression_6Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expression_5




    def expression_5(self):

        localctx = BKOOLParser.Expression_5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expression_5)
        try:
            self.state = 319
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.match(BKOOLParser.NOT)
                self.state = 317
                self.expression_5()
                pass
            elif token in [BKOOLParser.INTEGER_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.MINUS, BKOOLParser.LB, BKOOLParser.LCB, BKOOLParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.expression_6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(BKOOLParser.MINUS, 0)

        def expression_6(self):
            return self.getTypedRuleContext(BKOOLParser.Expression_6Context,0)


        def expression_7(self):
            return self.getTypedRuleContext(BKOOLParser.Expression_7Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expression_6




    def expression_6(self):

        localctx = BKOOLParser.Expression_6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expression_6)
        try:
            self.state = 324
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.match(BKOOLParser.MINUS)
                self.state = 322
                self.expression_6()
                pass
            elif token in [BKOOLParser.INTEGER_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.LB, BKOOLParser.LCB, BKOOLParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
                self.expression_7(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_8(self):
            return self.getTypedRuleContext(BKOOLParser.Expression_8Context,0)


        def expression_7(self):
            return self.getTypedRuleContext(BKOOLParser.Expression_7Context,0)


        def factor(self):
            return self.getTypedRuleContext(BKOOLParser.FactorContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expression_7



    def expression_7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expression_7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expression_7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.expression_8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 333
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expression_7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_7)
                    self.state = 329
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 330
                    self.factor() 
                self.state = 335
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression_8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def factor(self):
            return self.getTypedRuleContext(BKOOLParser.FactorContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expression_8




    def expression_8(self):

        localctx = BKOOLParser.Expression_8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expression_8)
        try:
            self.state = 341
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.match(BKOOLParser.LB)
                self.state = 337
                self.expression()
                self.state = 338
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.INTEGER_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.LCB, BKOOLParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
                self.factor()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LIT(self):
            return self.getToken(BKOOLParser.INTEGER_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(BKOOLParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(BKOOLParser.STRING_LIT, 0)

        def IDENTIFIER(self):
            return self.getToken(BKOOLParser.IDENTIFIER, 0)

        def function_call(self):
            return self.getTypedRuleContext(BKOOLParser.Function_callContext,0)


        def array_list(self):
            return self.getTypedRuleContext(BKOOLParser.Array_listContext,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def exp_list_type_int(self):
            return self.getTypedRuleContext(BKOOLParser.Exp_list_type_intContext,0)


        def factor(self):
            return self.getTypedRuleContext(BKOOLParser.FactorContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_factor




    def factor(self):

        localctx = BKOOLParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_factor)
        try:
            self.state = 359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                if la_ == 1:
                    self.state = 343
                    self.match(BKOOLParser.INTEGER_LIT)
                    pass

                elif la_ == 2:
                    self.state = 344
                    self.match(BKOOLParser.FLOAT_LIT)
                    pass

                elif la_ == 3:
                    self.state = 345
                    self.match(BKOOLParser.STRING_LIT)
                    pass

                elif la_ == 4:
                    self.state = 346
                    self.match(BKOOLParser.IDENTIFIER)
                    pass

                elif la_ == 5:
                    self.state = 347
                    self.function_call()
                    pass

                elif la_ == 6:
                    self.state = 348
                    self.array_list()
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self.match(BKOOLParser.IDENTIFIER)
                self.state = 352
                self.match(BKOOLParser.LSB)
                self.state = 355
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 353
                    self.exp_list_type_int()
                    pass

                elif la_ == 2:
                    self.state = 354
                    self.factor()
                    pass


                self.state = 357
                self.match(BKOOLParser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BKOOLParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def exps_list(self):
            return self.getTypedRuleContext(BKOOLParser.Exps_listContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_function_call




    def function_call(self):

        localctx = BKOOLParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(BKOOLParser.IDENTIFIER)
            self.state = 362
            self.match(BKOOLParser.LB)
            self.state = 363
            self.exps_list()
            self.state = 364
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exps_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_list(self):
            return self.getTypedRuleContext(BKOOLParser.Exp_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exps_list




    def exps_list(self):

        localctx = BKOOLParser.Exps_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_exps_list)
        try:
            self.state = 368
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTEGER_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.MINUS, BKOOLParser.NOT, BKOOLParser.LB, BKOOLParser.LCB, BKOOLParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.exp_list()
                pass
            elif token in [BKOOLParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def exp_list(self):
            return self.getTypedRuleContext(BKOOLParser.Exp_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp_list




    def exp_list(self):

        localctx = BKOOLParser.Exp_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_exp_list)
        try:
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                self.expression()
                self.state = 371
                self.match(BKOOLParser.COMMA)
                self.state = 372
                self.exp_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 374
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.While_stmtContext,0)


        def do_while_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Do_while_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Return_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Continue_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Break_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Call_stmtContext,0)


        def variable_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Variable_declContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_statement




    def statement(self):

        localctx = BKOOLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_statement)
        try:
            self.state = 388
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 379
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 380
                self.while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 381
                self.do_while_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 382
                self.block_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 383
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 384
                self.continue_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 385
                self.break_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 386
                self.call_stmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 387
                self.variable_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(BKOOLParser.LhsContext,0)


        def EQUAL(self):
            return self.getToken(BKOOLParser.EQUAL, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = BKOOLParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.lhs()
            self.state = 391
            self.match(BKOOLParser.EQUAL)
            self.state = 392
            self.expression()
            self.state = 393
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BKOOLParser.IDENTIFIER, 0)

        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def exp_list_type_int(self):
            return self.getTypedRuleContext(BKOOLParser.Exp_list_type_intContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_lhs)
        try:
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.match(BKOOLParser.IDENTIFIER)
                self.state = 396
                self.match(BKOOLParser.LSB)
                self.state = 397
                self.exp_list_type_int()
                self.state = 398
                self.match(BKOOLParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
                self.match(BKOOLParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_if_stmt




    def if_stmt(self):

        localctx = BKOOLParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_if_stmt)
        try:
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                self.match(BKOOLParser.IF)
                self.state = 404
                self.expression()
                self.state = 405
                self.statement()
                self.state = 406
                self.match(BKOOLParser.ELSE)
                self.state = 407
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
                self.match(BKOOLParser.IF)
                self.state = 410
                self.expression()
                self.state = 411
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def scala_val(self):
            return self.getTypedRuleContext(BKOOLParser.Scala_valContext,0)


        def EQUAL(self):
            return self.getToken(BKOOLParser.EQUAL, 0)

        def init_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Init_exprContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def condition_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Condition_exprContext,0)


        def update_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Update_exprContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def statement(self):
            return self.getTypedRuleContext(BKOOLParser.StatementContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_for_stmt




    def for_stmt(self):

        localctx = BKOOLParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(BKOOLParser.LB)
            self.state = 416
            self.scala_val()
            self.state = 417
            self.match(BKOOLParser.EQUAL)
            self.state = 418
            self.init_expr()
            self.state = 419
            self.match(BKOOLParser.COMMA)
            self.state = 420
            self.condition_expr()
            self.state = 421
            self.match(BKOOLParser.COMMA)
            self.state = 422
            self.update_expr()
            self.state = 423
            self.match(BKOOLParser.RB)
            self.state = 424
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scala_valContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BKOOLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_scala_val




    def scala_val(self):

        localctx = BKOOLParser.Scala_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_scala_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(BKOOLParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LIT(self):
            return self.getToken(BKOOLParser.INTEGER_LIT, 0)

        def IDENTIFIER(self):
            return self.getToken(BKOOLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_init_expr




    def init_expr(self):

        localctx = BKOOLParser.Init_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_init_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.INTEGER_LIT or _la==BKOOLParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.IDENTIFIER)
            else:
                return self.getToken(BKOOLParser.IDENTIFIER, i)

        def LESS(self):
            return self.getToken(BKOOLParser.LESS, 0)

        def GREATER(self):
            return self.getToken(BKOOLParser.GREATER, 0)

        def LTE(self):
            return self.getToken(BKOOLParser.LTE, 0)

        def GTE(self):
            return self.getToken(BKOOLParser.GTE, 0)

        def NOT_EQUAL(self):
            return self.getToken(BKOOLParser.NOT_EQUAL, 0)

        def EQUAL_TO(self):
            return self.getToken(BKOOLParser.EQUAL_TO, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_condition_expr




    def condition_expr(self):

        localctx = BKOOLParser.Condition_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_condition_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.match(BKOOLParser.IDENTIFIER)
            self.state = 431
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LESS) | (1 << BKOOLParser.GREATER) | (1 << BKOOLParser.LTE) | (1 << BKOOLParser.GTE) | (1 << BKOOLParser.EQUAL_TO) | (1 << BKOOLParser.NOT_EQUAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 434
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 432
                self.match(BKOOLParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 433
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Update_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BKOOLParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def PLUS(self):
            return self.getToken(BKOOLParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(BKOOLParser.MINUS, 0)

        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_update_expr




    def update_expr(self):

        localctx = BKOOLParser.Update_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_update_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.match(BKOOLParser.IDENTIFIER)
            self.state = 437
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.PLUS) | (1 << BKOOLParser.MINUS) | (1 << BKOOLParser.MUL) | (1 << BKOOLParser.MOD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 438
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKOOLParser.WHILE, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def statement(self):
            return self.getTypedRuleContext(BKOOLParser.StatementContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_while_stmt




    def while_stmt(self):

        localctx = BKOOLParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.match(BKOOLParser.WHILE)
            self.state = 441
            self.match(BKOOLParser.LB)
            self.state = 442
            self.expression()
            self.state = 443
            self.match(BKOOLParser.RB)
            self.state = 444
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def WHILE(self):
            return self.getToken(BKOOLParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_do_while_stmt




    def do_while_stmt(self):

        localctx = BKOOLParser.Do_while_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_do_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.match(BKOOLParser.DO)
            self.state = 447
            self.block_stmt()
            self.state = 448
            self.match(BKOOLParser.WHILE)
            self.state = 449
            self.expression()
            self.state = 450
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def function_call(self):
            return self.getTypedRuleContext(BKOOLParser.Function_callContext,0)


        def s_func_decl(self):
            return self.getTypedRuleContext(BKOOLParser.S_func_declContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_call_stmt




    def call_stmt(self):

        localctx = BKOOLParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.IDENTIFIER]:
                self.state = 452
                self.function_call()
                pass
            elif token in [BKOOLParser.T__0, BKOOLParser.T__1, BKOOLParser.T__2, BKOOLParser.T__3, BKOOLParser.T__4, BKOOLParser.T__5, BKOOLParser.T__6, BKOOLParser.T__7, BKOOLParser.T__8]:
                self.state = 453
                self.s_func_decl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 456
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(BKOOLParser.LCB, 0)

        def statement_term(self):
            return self.getTypedRuleContext(BKOOLParser.Statement_termContext,0)


        def RCB(self):
            return self.getToken(BKOOLParser.RCB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_block_stmt




    def block_stmt(self):

        localctx = BKOOLParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.match(BKOOLParser.LCB)
            self.state = 459
            self.statement_term()
            self.state = 460
            self.match(BKOOLParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_termContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_list(self):
            return self.getTypedRuleContext(BKOOLParser.Statement_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_statement_term




    def statement_term(self):

        localctx = BKOOLParser.Statement_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_statement_term)
        try:
            self.state = 464
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.T__0, BKOOLParser.T__1, BKOOLParser.T__2, BKOOLParser.T__3, BKOOLParser.T__4, BKOOLParser.T__5, BKOOLParser.T__6, BKOOLParser.T__7, BKOOLParser.T__8, BKOOLParser.BREAK, BKOOLParser.RETURN, BKOOLParser.CONTINUE, BKOOLParser.DO, BKOOLParser.IF, BKOOLParser.WHILE, BKOOLParser.LB, BKOOLParser.LCB, BKOOLParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.statement_list()
                pass
            elif token in [BKOOLParser.RCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(BKOOLParser.StatementContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(BKOOLParser.Statement_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_statement_list




    def statement_list(self):

        localctx = BKOOLParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_statement_list)
        try:
            self.state = 470
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 466
                self.statement()
                self.state = 467
                self.statement_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 469
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_break_stmt




    def break_stmt(self):

        localctx = BKOOLParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self.match(BKOOLParser.BREAK)
            self.state = 473
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_continue_stmt




    def continue_stmt(self):

        localctx = BKOOLParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.match(BKOOLParser.CONTINUE)
            self.state = 476
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_return_stmt




    def return_stmt(self):

        localctx = BKOOLParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.match(BKOOLParser.RETURN)
            self.state = 479
            self.expression()
            self.state = 480
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BKOOLParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(BKOOLParser.COLON, 0)

        def FUNCTION(self):
            return self.getToken(BKOOLParser.FUNCTION, 0)

        def return_type(self):
            return self.getTypedRuleContext(BKOOLParser.Return_typeContext,0)


        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def paramter_list(self):
            return self.getTypedRuleContext(BKOOLParser.Paramter_listContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def inheritance(self):
            return self.getTypedRuleContext(BKOOLParser.InheritanceContext,0)


        def statement(self):
            return self.getTypedRuleContext(BKOOLParser.StatementContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_function_decl




    def function_decl(self):

        localctx = BKOOLParser.Function_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_function_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.match(BKOOLParser.IDENTIFIER)
            self.state = 483
            self.match(BKOOLParser.COLON)
            self.state = 484
            self.match(BKOOLParser.FUNCTION)
            self.state = 485
            self.return_type()
            self.state = 486
            self.match(BKOOLParser.LB)
            self.state = 487
            self.paramter_list()
            self.state = 488
            self.match(BKOOLParser.RB)
            self.state = 489
            self.inheritance()
            self.state = 490
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InheritanceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INHERIT(self):
            return self.getToken(BKOOLParser.INHERIT, 0)

        def function_name(self):
            return self.getTypedRuleContext(BKOOLParser.Function_nameContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_inheritance




    def inheritance(self):

        localctx = BKOOLParser.InheritanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_inheritance)
        try:
            self.state = 495
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INHERIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 492
                self.match(BKOOLParser.INHERIT)
                self.state = 493
                self.function_name()
                pass
            elif token in [BKOOLParser.T__0, BKOOLParser.T__1, BKOOLParser.T__2, BKOOLParser.T__3, BKOOLParser.T__4, BKOOLParser.T__5, BKOOLParser.T__6, BKOOLParser.T__7, BKOOLParser.T__8, BKOOLParser.BREAK, BKOOLParser.RETURN, BKOOLParser.CONTINUE, BKOOLParser.DO, BKOOLParser.IF, BKOOLParser.WHILE, BKOOLParser.LB, BKOOLParser.LCB, BKOOLParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BKOOLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_function_name




    def function_name(self):

        localctx = BKOOLParser.Function_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_function_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.match(BKOOLParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Paramter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramter_list_term(self):
            return self.getTypedRuleContext(BKOOLParser.Paramter_list_termContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramter_list




    def paramter_list(self):

        localctx = BKOOLParser.Paramter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_paramter_list)
        try:
            self.state = 501
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.OUT, BKOOLParser.INHERIT, BKOOLParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 499
                self.paramter_list_term()
                pass
            elif token in [BKOOLParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Paramter_list_termContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(BKOOLParser.ParameterContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def paramter_list_term(self):
            return self.getTypedRuleContext(BKOOLParser.Paramter_list_termContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramter_list_term




    def paramter_list_term(self):

        localctx = BKOOLParser.Paramter_list_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_paramter_list_term)
        try:
            self.state = 508
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 503
                self.parameter()
                self.state = 504
                self.match(BKOOLParser.COMMA)
                self.state = 505
                self.paramter_list_term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 507
                self.parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(BKOOLParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def AUTO(self):
            return self.getToken(BKOOLParser.AUTO, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_return_type




    def return_type(self):

        localctx = BKOOLParser.Return_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_return_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.AUTO) | (1 << BKOOLParser.INTEGER) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class S_func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def read_integer(self):
            return self.getTypedRuleContext(BKOOLParser.Read_integerContext,0)


        def print_integer(self):
            return self.getTypedRuleContext(BKOOLParser.Print_integerContext,0)


        def read_float(self):
            return self.getTypedRuleContext(BKOOLParser.Read_floatContext,0)


        def write_float(self):
            return self.getTypedRuleContext(BKOOLParser.Write_floatContext,0)


        def print_boolean(self):
            return self.getTypedRuleContext(BKOOLParser.Print_booleanContext,0)


        def read_string(self):
            return self.getTypedRuleContext(BKOOLParser.Read_stringContext,0)


        def print_string(self):
            return self.getTypedRuleContext(BKOOLParser.Print_stringContext,0)


        def super_(self):
            return self.getTypedRuleContext(BKOOLParser.Super_Context,0)


        def prevent_default(self):
            return self.getTypedRuleContext(BKOOLParser.Prevent_defaultContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_s_func_decl




    def s_func_decl(self):

        localctx = BKOOLParser.S_func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_s_func_decl)
        try:
            self.state = 521
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 512
                self.read_integer()
                pass
            elif token in [BKOOLParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 513
                self.print_integer()
                pass
            elif token in [BKOOLParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 514
                self.read_float()
                pass
            elif token in [BKOOLParser.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 515
                self.write_float()
                pass
            elif token in [BKOOLParser.T__4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 516
                self.print_boolean()
                pass
            elif token in [BKOOLParser.T__5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 517
                self.read_string()
                pass
            elif token in [BKOOLParser.T__6]:
                self.enterOuterAlt(localctx, 7)
                self.state = 518
                self.print_string()
                pass
            elif token in [BKOOLParser.T__7]:
                self.enterOuterAlt(localctx, 8)
                self.state = 519
                self.super_()
                pass
            elif token in [BKOOLParser.T__8]:
                self.enterOuterAlt(localctx, 9)
                self.state = 520
                self.prevent_default()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_integerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_read_integer




    def read_integer(self):

        localctx = BKOOLParser.Read_integerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_read_integer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.match(BKOOLParser.T__0)
            self.state = 524
            self.match(BKOOLParser.LB)
            self.state = 525
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_integerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def INTEGER_LIT(self):
            return self.getToken(BKOOLParser.INTEGER_LIT, 0)

        def IDENTIFIER(self):
            return self.getToken(BKOOLParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_print_integer




    def print_integer(self):

        localctx = BKOOLParser.Print_integerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_print_integer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            self.match(BKOOLParser.T__1)
            self.state = 528
            self.match(BKOOLParser.LB)
            self.state = 532
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 529
                self.match(BKOOLParser.INTEGER_LIT)
                pass

            elif la_ == 2:
                self.state = 530
                self.match(BKOOLParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.state = 531
                self.expression()
                pass


            self.state = 534
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_floatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_read_float




    def read_float(self):

        localctx = BKOOLParser.Read_floatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_read_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self.match(BKOOLParser.T__2)
            self.state = 537
            self.match(BKOOLParser.LB)
            self.state = 538
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Write_floatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def FLOAT_LIT(self):
            return self.getToken(BKOOLParser.FLOAT_LIT, 0)

        def IDENTIFIER(self):
            return self.getToken(BKOOLParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_write_float




    def write_float(self):

        localctx = BKOOLParser.Write_floatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_write_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
            self.match(BKOOLParser.T__3)
            self.state = 541
            self.match(BKOOLParser.LB)
            self.state = 545
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 542
                self.match(BKOOLParser.FLOAT_LIT)
                pass

            elif la_ == 2:
                self.state = 543
                self.match(BKOOLParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.state = 544
                self.expression()
                pass


            self.state = 547
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_booleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def BOOLEAN_LIT(self):
            return self.getToken(BKOOLParser.BOOLEAN_LIT, 0)

        def IDENTIFIER(self):
            return self.getToken(BKOOLParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_print_boolean




    def print_boolean(self):

        localctx = BKOOLParser.Print_booleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_print_boolean)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            self.match(BKOOLParser.T__4)
            self.state = 550
            self.match(BKOOLParser.LB)
            self.state = 554
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.state = 551
                self.match(BKOOLParser.BOOLEAN_LIT)
                pass

            elif la_ == 2:
                self.state = 552
                self.match(BKOOLParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.state = 553
                self.expression()
                pass


            self.state = 556
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_read_string




    def read_string(self):

        localctx = BKOOLParser.Read_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_read_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 558
            self.match(BKOOLParser.T__5)
            self.state = 559
            self.match(BKOOLParser.LB)
            self.state = 560
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def STRING_LIT(self):
            return self.getToken(BKOOLParser.STRING_LIT, 0)

        def IDENTIFIER(self):
            return self.getToken(BKOOLParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_print_string




    def print_string(self):

        localctx = BKOOLParser.Print_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_print_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562
            self.match(BKOOLParser.T__6)
            self.state = 563
            self.match(BKOOLParser.LB)
            self.state = 567
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 564
                self.match(BKOOLParser.STRING_LIT)
                pass

            elif la_ == 2:
                self.state = 565
                self.match(BKOOLParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.state = 566
                self.expression()
                pass


            self.state = 569
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Super_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def expression_list(self):
            return self.getTypedRuleContext(BKOOLParser.Expression_listContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_super_




    def super_(self):

        localctx = BKOOLParser.Super_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_super_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 571
            self.match(BKOOLParser.T__7)
            self.state = 572
            self.match(BKOOLParser.LB)
            self.state = 573
            self.expression_list()
            self.state = 574
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prevent_defaultContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_prevent_default




    def prevent_default(self):

        localctx = BKOOLParser.Prevent_defaultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_prevent_default)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            self.match(BKOOLParser.T__8)
            self.state = 577
            self.match(BKOOLParser.LB)
            self.state = 578
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[21] = self.expression_2_sempred
        self._predicates[22] = self.expression_3_sempred
        self._predicates[23] = self.expression_4_sempred
        self._predicates[26] = self.expression_7_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_2_sempred(self, localctx:Expression_2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression_3_sempred(self, localctx:Expression_3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression_4_sempred(self, localctx:Expression_4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression_7_sempred(self, localctx:Expression_7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




