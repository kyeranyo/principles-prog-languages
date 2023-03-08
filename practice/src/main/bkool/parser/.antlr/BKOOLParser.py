# Generated from c:\Users\84865\Documents\HCMUT-cse20\CSE-PPL\practice\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


from antlr4.error.ErrorListener import ConsoleErrorListener, ErrorListener

class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
	    return SyntaxException("Error on line " + str(line) +
                              " col " + str(column) + ": " + offendingSymbol.text)

NewErrorListener.INSTANCE = NewErrorListener()

class SyntaxException(Exception):
    def __init__(self, msg):
        self.message = msg


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3;")
        buf.write("\u01b9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\3\2\6\2j\n\2\r\2\16\2k\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3u\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\5")
        buf.write("\6\u0082\n\6\3\7\3\7\3\7\3\7\5\7\u0088\n\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\5\t\u0093\n\t\3\t\3\t\5\t\u0097")
        buf.write("\n\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\5\n\u00a0\n\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\5\13\u00a7\n\13\3\f\3\f\3\f\3\f\5\f")
        buf.write("\u00ad\n\f\3\r\3\r\5\r\u00b1\n\r\3\16\3\16\3\16\3\16\5")
        buf.write("\16\u00b7\n\16\3\17\3\17\3\17\3\17\5\17\u00bd\n\17\3\20")
        buf.write("\3\20\3\20\3\20\5\20\u00c3\n\20\3\21\3\21\5\21\u00c7\n")
        buf.write("\21\3\21\3\21\5\21\u00cb\n\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\5\22\u00d6\n\22\3\23\3\23\3\23\3")
        buf.write("\23\3\23\5\23\u00dd\n\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\7\24\u00e5\n\24\f\24\16\24\u00e8\13\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\7\25\u00f0\n\25\f\25\16\25\u00f3\13\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u00fb\n\26\f\26\16")
        buf.write("\26\u00fe\13\26\3\27\3\27\3\27\5\27\u0103\n\27\3\30\3")
        buf.write("\30\3\30\5\30\u0108\n\30\3\31\3\31\3\31\3\31\3\31\7\31")
        buf.write("\u010f\n\31\f\31\16\31\u0112\13\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\5\32\u0119\n\32\3\33\3\33\3\33\3\33\3\33\5\33\u0120")
        buf.write("\n\33\3\33\3\33\3\33\3\33\3\33\5\33\u0127\n\33\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\35\3\35\5\35\u0130\n\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\5\36\u0137\n\36\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0144\n\37\3 \3")
        buf.write(" \3 \3 \3 \3!\3!\3!\3!\3!\3!\5!\u0151\n!\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u015d\n\"\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3$\3$\3%\3%\3&\3&\3&\3&\5&\u0172\n")
        buf.write("&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3*")
        buf.write("\3*\3*\3+\3+\7+\u0188\n+\f+\16+\u018b\13+\3+\3+\5+\u018f")
        buf.write("\n+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3")
        buf.write("/\3/\3/\3/\3\60\3\60\3\60\5\60\u01a8\n\60\3\61\3\61\3")
        buf.write("\62\3\62\5\62\u01ae\n\62\3\63\3\63\3\63\3\63\3\63\5\63")
        buf.write("\u01b5\n\63\3\64\3\64\3\64\2\6&(*\60\65\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`bdf\2\n\6\2\f\f\17\17\22\22\24\24\4\2\"")
        buf.write("%)*\3\2\'(\3\2\35\36\3\2\37!\4\2\5\5\67\67\4\2\35\37!")
        buf.write("!\7\2\n\n\f\r\17\17\22\22\24\24\2\u01b9\2i\3\2\2\2\4t")
        buf.write("\3\2\2\2\6v\3\2\2\2\b}\3\2\2\2\n\u0081\3\2\2\2\f\u0087")
        buf.write("\3\2\2\2\16\u0089\3\2\2\2\20\u008e\3\2\2\2\22\u009f\3")
        buf.write("\2\2\2\24\u00a6\3\2\2\2\26\u00ac\3\2\2\2\30\u00b0\3\2")
        buf.write("\2\2\32\u00b6\3\2\2\2\34\u00bc\3\2\2\2\36\u00c2\3\2\2")
        buf.write("\2 \u00c6\3\2\2\2\"\u00d5\3\2\2\2$\u00dc\3\2\2\2&\u00de")
        buf.write("\3\2\2\2(\u00e9\3\2\2\2*\u00f4\3\2\2\2,\u0102\3\2\2\2")
        buf.write(".\u0107\3\2\2\2\60\u0109\3\2\2\2\62\u0118\3\2\2\2\64\u0126")
        buf.write("\3\2\2\2\66\u0128\3\2\2\28\u012f\3\2\2\2:\u0136\3\2\2")
        buf.write("\2<\u0143\3\2\2\2>\u0145\3\2\2\2@\u0150\3\2\2\2B\u015c")
        buf.write("\3\2\2\2D\u015e\3\2\2\2F\u0169\3\2\2\2H\u016b\3\2\2\2")
        buf.write("J\u016d\3\2\2\2L\u0173\3\2\2\2N\u0177\3\2\2\2P\u017d\3")
        buf.write("\2\2\2R\u0182\3\2\2\2T\u018e\3\2\2\2V\u0190\3\2\2\2X\u0193")
        buf.write("\3\2\2\2Z\u0196\3\2\2\2\\\u019a\3\2\2\2^\u01a7\3\2\2\2")
        buf.write("`\u01a9\3\2\2\2b\u01ad\3\2\2\2d\u01b4\3\2\2\2f\u01b6\3")
        buf.write("\2\2\2hj\5\4\3\2ih\3\2\2\2jk\3\2\2\2ki\3\2\2\2kl\3\2\2")
        buf.write("\2lm\3\2\2\2mn\7\2\2\3n\3\3\2\2\2ou\5\6\4\2pu\5\20\t\2")
        buf.write("qu\5\\/\2ru\5<\37\2su\5\"\22\2to\3\2\2\2tp\3\2\2\2tq\3")
        buf.write("\2\2\2tr\3\2\2\2ts\3\2\2\2u\5\3\2\2\2vw\7\16\2\2wx\7\63")
        buf.write("\2\2xy\5\n\6\2yz\7\64\2\2z{\7\30\2\2{|\5\b\5\2|\7\3\2")
        buf.write("\2\2}~\t\2\2\2~\t\3\2\2\2\177\u0082\5\f\7\2\u0080\u0082")
        buf.write("\5\16\b\2\u0081\177\3\2\2\2\u0081\u0080\3\2\2\2\u0082")
        buf.write("\13\3\2\2\2\u0083\u0084\7\5\2\2\u0084\u0085\7-\2\2\u0085")
        buf.write("\u0088\5\f\7\2\u0086\u0088\7\5\2\2\u0087\u0083\3\2\2\2")
        buf.write("\u0087\u0086\3\2\2\2\u0088\r\3\2\2\2\u0089\u008a\7\6\2")
        buf.write("\2\u008a\u008b\7-\2\2\u008b\u008c\5\16\b\2\u008c\u008d")
        buf.write("\7\6\2\2\u008d\17\3\2\2\2\u008e\u008f\5\26\f\2\u008f\u0092")
        buf.write("\7\60\2\2\u0090\u0093\5\b\5\2\u0091\u0093\5\6\4\2\u0092")
        buf.write("\u0090\3\2\2\2\u0092\u0091\3\2\2\2\u0093\u0096\3\2\2\2")
        buf.write("\u0094\u0097\5\22\n\2\u0095\u0097\5\24\13\2\u0096\u0094")
        buf.write("\3\2\2\2\u0096\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098")
        buf.write("\u0099\b\t\1\2\u0099\21\3\2\2\2\u009a\u009b\7/\2\2\u009b")
        buf.write("\u009c\5\30\r\2\u009c\u009d\7.\2\2\u009d\u00a0\3\2\2\2")
        buf.write("\u009e\u00a0\7.\2\2\u009f\u009a\3\2\2\2\u009f\u009e\3")
        buf.write("\2\2\2\u00a0\23\3\2\2\2\u00a1\u00a2\7/\2\2\u00a2\u00a3")
        buf.write("\5\66\34\2\u00a3\u00a4\7.\2\2\u00a4\u00a7\3\2\2\2\u00a5")
        buf.write("\u00a7\7.\2\2\u00a6\u00a1\3\2\2\2\u00a6\u00a5\3\2\2\2")
        buf.write("\u00a7\25\3\2\2\2\u00a8\u00a9\7\67\2\2\u00a9\u00aa\7-")
        buf.write("\2\2\u00aa\u00ad\5\26\f\2\u00ab\u00ad\7\67\2\2\u00ac\u00a8")
        buf.write("\3\2\2\2\u00ac\u00ab\3\2\2\2\u00ad\27\3\2\2\2\u00ae\u00b1")
        buf.write("\5\32\16\2\u00af\u00b1\5\34\17\2\u00b0\u00ae\3\2\2\2\u00b0")
        buf.write("\u00af\3\2\2\2\u00b1\31\3\2\2\2\u00b2\u00b3\7\5\2\2\u00b3")
        buf.write("\u00b4\7-\2\2\u00b4\u00b7\5\32\16\2\u00b5\u00b7\7\5\2")
        buf.write("\2\u00b6\u00b2\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7\33\3")
        buf.write("\2\2\2\u00b8\u00b9\7\6\2\2\u00b9\u00ba\7-\2\2\u00ba\u00bd")
        buf.write("\5\34\17\2\u00bb\u00bd\7\6\2\2\u00bc\u00b8\3\2\2\2\u00bc")
        buf.write("\u00bb\3\2\2\2\u00bd\35\3\2\2\2\u00be\u00bf\7\b\2\2\u00bf")
        buf.write("\u00c0\7-\2\2\u00c0\u00c3\5\36\20\2\u00c1\u00c3\7\b\2")
        buf.write("\2\u00c2\u00be\3\2\2\2\u00c2\u00c1\3\2\2\2\u00c3\37\3")
        buf.write("\2\2\2\u00c4\u00c7\7\34\2\2\u00c5\u00c7\3\2\2\2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c7\u00ca\3\2\2\2")
        buf.write("\u00c8\u00cb\7\21\2\2\u00c9\u00cb\3\2\2\2\u00ca\u00c8")
        buf.write("\3\2\2\2\u00ca\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc")
        buf.write("\u00cd\7\67\2\2\u00cd\u00ce\7\60\2\2\u00ce\u00cf\5\b\5")
        buf.write("\2\u00cf!\3\2\2\2\u00d0\u00d1\5$\23\2\u00d1\u00d2\7+\2")
        buf.write("\2\u00d2\u00d3\5$\23\2\u00d3\u00d6\3\2\2\2\u00d4\u00d6")
        buf.write("\5$\23\2\u00d5\u00d0\3\2\2\2\u00d5\u00d4\3\2\2\2\u00d6")
        buf.write("#\3\2\2\2\u00d7\u00d8\5&\24\2\u00d8\u00d9\t\3\2\2\u00d9")
        buf.write("\u00da\5&\24\2\u00da\u00dd\3\2\2\2\u00db\u00dd\5&\24\2")
        buf.write("\u00dc\u00d7\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd%\3\2\2")
        buf.write("\2\u00de\u00df\b\24\1\2\u00df\u00e0\5(\25\2\u00e0\u00e6")
        buf.write("\3\2\2\2\u00e1\u00e2\f\4\2\2\u00e2\u00e3\t\4\2\2\u00e3")
        buf.write("\u00e5\5(\25\2\u00e4\u00e1\3\2\2\2\u00e5\u00e8\3\2\2\2")
        buf.write("\u00e6\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\'\3\2\2")
        buf.write("\2\u00e8\u00e6\3\2\2\2\u00e9\u00ea\b\25\1\2\u00ea\u00eb")
        buf.write("\5*\26\2\u00eb\u00f1\3\2\2\2\u00ec\u00ed\f\4\2\2\u00ed")
        buf.write("\u00ee\t\5\2\2\u00ee\u00f0\5*\26\2\u00ef\u00ec\3\2\2\2")
        buf.write("\u00f0\u00f3\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f2\3")
        buf.write("\2\2\2\u00f2)\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f4\u00f5")
        buf.write("\b\26\1\2\u00f5\u00f6\5,\27\2\u00f6\u00fc\3\2\2\2\u00f7")
        buf.write("\u00f8\f\4\2\2\u00f8\u00f9\t\6\2\2\u00f9\u00fb\5,\27\2")
        buf.write("\u00fa\u00f7\3\2\2\2\u00fb\u00fe\3\2\2\2\u00fc\u00fa\3")
        buf.write("\2\2\2\u00fc\u00fd\3\2\2\2\u00fd+\3\2\2\2\u00fe\u00fc")
        buf.write("\3\2\2\2\u00ff\u0100\7&\2\2\u0100\u0103\5,\27\2\u0101")
        buf.write("\u0103\5.\30\2\u0102\u00ff\3\2\2\2\u0102\u0101\3\2\2\2")
        buf.write("\u0103-\3\2\2\2\u0104\u0105\7\36\2\2\u0105\u0108\5.\30")
        buf.write("\2\u0106\u0108\5\60\31\2\u0107\u0104\3\2\2\2\u0107\u0106")
        buf.write("\3\2\2\2\u0108/\3\2\2\2\u0109\u010a\b\31\1\2\u010a\u010b")
        buf.write("\5\62\32\2\u010b\u0110\3\2\2\2\u010c\u010d\f\4\2\2\u010d")
        buf.write("\u010f\5\64\33\2\u010e\u010c\3\2\2\2\u010f\u0112\3\2\2")
        buf.write("\2\u0110\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111\61\3")
        buf.write("\2\2\2\u0112\u0110\3\2\2\2\u0113\u0114\7\61\2\2\u0114")
        buf.write("\u0115\5\"\22\2\u0115\u0116\7\62\2\2\u0116\u0119\3\2\2")
        buf.write("\2\u0117\u0119\5\64\33\2\u0118\u0113\3\2\2\2\u0118\u0117")
        buf.write("\3\2\2\2\u0119\63\3\2\2\2\u011a\u0120\7\5\2\2\u011b\u0120")
        buf.write("\7\6\2\2\u011c\u0120\7\b\2\2\u011d\u0120\7\67\2\2\u011e")
        buf.write("\u0120\5\66\34\2\u011f\u011a\3\2\2\2\u011f\u011b\3\2\2")
        buf.write("\2\u011f\u011c\3\2\2\2\u011f\u011d\3\2\2\2\u011f\u011e")
        buf.write("\3\2\2\2\u0120\u0127\3\2\2\2\u0121\u0122\7\67\2\2\u0122")
        buf.write("\u0123\7\63\2\2\u0123\u0124\5\32\16\2\u0124\u0125\7\64")
        buf.write("\2\2\u0125\u0127\3\2\2\2\u0126\u011f\3\2\2\2\u0126\u0121")
        buf.write("\3\2\2\2\u0127\65\3\2\2\2\u0128\u0129\7\67\2\2\u0129\u012a")
        buf.write("\7\61\2\2\u012a\u012b\5:\36\2\u012b\u012c\7\62\2\2\u012c")
        buf.write("\67\3\2\2\2\u012d\u0130\5:\36\2\u012e\u0130\3\2\2\2\u012f")
        buf.write("\u012d\3\2\2\2\u012f\u012e\3\2\2\2\u01309\3\2\2\2\u0131")
        buf.write("\u0132\5\"\22\2\u0132\u0133\7-\2\2\u0133\u0134\5:\36\2")
        buf.write("\u0134\u0137\3\2\2\2\u0135\u0137\5\"\22\2\u0136\u0131")
        buf.write("\3\2\2\2\u0136\u0135\3\2\2\2\u0137;\3\2\2\2\u0138\u0144")
        buf.write("\5> \2\u0139\u0144\5B\"\2\u013a\u0144\5D#\2\u013b\u0144")
        buf.write("\5N(\2\u013c\u0144\5P)\2\u013d\u0144\5T+\2\u013e\u0144")
        buf.write("\5Z.\2\u013f\u0144\5X-\2\u0140\u0144\5V,\2\u0141\u0144")
        buf.write("\5R*\2\u0142\u0144\5\20\t\2\u0143\u0138\3\2\2\2\u0143")
        buf.write("\u0139\3\2\2\2\u0143\u013a\3\2\2\2\u0143\u013b\3\2\2\2")
        buf.write("\u0143\u013c\3\2\2\2\u0143\u013d\3\2\2\2\u0143\u013e\3")
        buf.write("\2\2\2\u0143\u013f\3\2\2\2\u0143\u0140\3\2\2\2\u0143\u0141")
        buf.write("\3\2\2\2\u0143\u0142\3\2\2\2\u0144=\3\2\2\2\u0145\u0146")
        buf.write("\5@!\2\u0146\u0147\7/\2\2\u0147\u0148\5\"\22\2\u0148\u0149")
        buf.write("\7.\2\2\u0149?\3\2\2\2\u014a\u014b\7\67\2\2\u014b\u014c")
        buf.write("\7\63\2\2\u014c\u014d\5\32\16\2\u014d\u014e\7\64\2\2\u014e")
        buf.write("\u0151\3\2\2\2\u014f\u0151\7\67\2\2\u0150\u014a\3\2\2")
        buf.write("\2\u0150\u014f\3\2\2\2\u0151A\3\2\2\2\u0152\u0153\7\32")
        buf.write("\2\2\u0153\u0154\5\"\22\2\u0154\u0155\5<\37\2\u0155\u0156")
        buf.write("\7\31\2\2\u0156\u0157\5<\37\2\u0157\u015d\3\2\2\2\u0158")
        buf.write("\u0159\7\32\2\2\u0159\u015a\5\"\22\2\u015a\u015b\5<\37")
        buf.write("\2\u015b\u015d\3\2\2\2\u015c\u0152\3\2\2\2\u015c\u0158")
        buf.write("\3\2\2\2\u015dC\3\2\2\2\u015e\u015f\7\61\2\2\u015f\u0160")
        buf.write("\5F$\2\u0160\u0161\7/\2\2\u0161\u0162\5H%\2\u0162\u0163")
        buf.write("\7-\2\2\u0163\u0164\5J&\2\u0164\u0165\7-\2\2\u0165\u0166")
        buf.write("\5L\'\2\u0166\u0167\7\62\2\2\u0167\u0168\5<\37\2\u0168")
        buf.write("E\3\2\2\2\u0169\u016a\7\67\2\2\u016aG\3\2\2\2\u016b\u016c")
        buf.write("\t\7\2\2\u016cI\3\2\2\2\u016d\u016e\7\67\2\2\u016e\u0171")
        buf.write("\t\3\2\2\u016f\u0172\7\67\2\2\u0170\u0172\5\"\22\2\u0171")
        buf.write("\u016f\3\2\2\2\u0171\u0170\3\2\2\2\u0172K\3\2\2\2\u0173")
        buf.write("\u0174\7\67\2\2\u0174\u0175\t\b\2\2\u0175\u0176\5\"\22")
        buf.write("\2\u0176M\3\2\2\2\u0177\u0178\7\33\2\2\u0178\u0179\7\61")
        buf.write("\2\2\u0179\u017a\5\"\22\2\u017a\u017b\7\62\2\2\u017b\u017c")
        buf.write("\5<\37\2\u017cO\3\2\2\2\u017d\u017e\7\26\2\2\u017e\u017f")
        buf.write("\5T+\2\u017f\u0180\7\33\2\2\u0180\u0181\5\"\22\2\u0181")
        buf.write("Q\3\2\2\2\u0182\u0183\5\66\34\2\u0183\u0184\7.\2\2\u0184")
        buf.write("S\3\2\2\2\u0185\u0189\7\65\2\2\u0186\u0188\5<\37\2\u0187")
        buf.write("\u0186\3\2\2\2\u0188\u018b\3\2\2\2\u0189\u0187\3\2\2\2")
        buf.write("\u0189\u018a\3\2\2\2\u018a\u018c\3\2\2\2\u018b\u0189\3")
        buf.write("\2\2\2\u018c\u018f\7\66\2\2\u018d\u018f\7\3\2\2\u018e")
        buf.write("\u0185\3\2\2\2\u018e\u018d\3\2\2\2\u018fU\3\2\2\2\u0190")
        buf.write("\u0191\7\13\2\2\u0191\u0192\7.\2\2\u0192W\3\2\2\2\u0193")
        buf.write("\u0194\7\25\2\2\u0194\u0195\7.\2\2\u0195Y\3\2\2\2\u0196")
        buf.write("\u0197\7\20\2\2\u0197\u0198\5\"\22\2\u0198\u0199\7.\2")
        buf.write("\2\u0199[\3\2\2\2\u019a\u019b\7\67\2\2\u019b\u019c\7\60")
        buf.write("\2\2\u019c\u019d\7\27\2\2\u019d\u019e\5f\64\2\u019e\u019f")
        buf.write("\7\61\2\2\u019f\u01a0\5b\62\2\u01a0\u01a1\7\62\2\2\u01a1")
        buf.write("\u01a2\5^\60\2\u01a2\u01a3\5<\37\2\u01a3]\3\2\2\2\u01a4")
        buf.write("\u01a5\7\34\2\2\u01a5\u01a8\5`\61\2\u01a6\u01a8\3\2\2")
        buf.write("\2\u01a7\u01a4\3\2\2\2\u01a7\u01a6\3\2\2\2\u01a8_\3\2")
        buf.write("\2\2\u01a9\u01aa\7\67\2\2\u01aaa\3\2\2\2\u01ab\u01ae\5")
        buf.write("d\63\2\u01ac\u01ae\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ac")
        buf.write("\3\2\2\2\u01aec\3\2\2\2\u01af\u01b0\5 \21\2\u01b0\u01b1")
        buf.write("\7-\2\2\u01b1\u01b2\5d\63\2\u01b2\u01b5\3\2\2\2\u01b3")
        buf.write("\u01b5\5 \21\2\u01b4\u01af\3\2\2\2\u01b4\u01b3\3\2\2\2")
        buf.write("\u01b5e\3\2\2\2\u01b6\u01b7\t\t\2\2\u01b7g\3\2\2\2\'k")
        buf.write("t\u0081\u0087\u0092\u0096\u009f\u00a6\u00ac\u00b0\u00b6")
        buf.write("\u00bc\u00c2\u00c6\u00ca\u00d5\u00dc\u00e6\u00f1\u00fc")
        buf.write("\u0102\u0107\u0110\u0118\u011f\u0126\u012f\u0136\u0143")
        buf.write("\u0150\u015c\u0171\u0189\u018e\u01a7\u01ad\u01b4")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{}'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'auto'", "'break'", 
                     "'integer'", "'void'", "'array'", "'float'", "'return'", 
                     "'out'", "'boolean'", "'for'", "'string'", "'continue'", 
                     "'do'", "'function'", "'of'", "'else'", "'if'", "'while'", 
                     "'inherit'", "'+'", "'-'", "'*'", "'/'", "'%'", "'<'", 
                     "'>'", "'<='", "'>='", "'!'", "'&&'", "'||'", "'=='", 
                     "'!='", "'::'", "'.'", "','", "';'", "'='", "':'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "COMMENT", "INTEGER_LIT", 
                      "FLOAT_LIT", "BOOLEAN_LIT", "STRING_LIT", "ARRAY_LIT", 
                      "AUTO", "BREAK", "INTEGER", "VOID", "ARRAY", "FLOAT", 
                      "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", 
                      "DO", "FUNCTION", "OF", "ELSE", "IF", "WHILE", "INHERIT", 
                      "PLUS", "MINUS", "MUL", "DIV", "MOD", "LESS", "GREATER", 
                      "LTE", "GTE", "NOT", "AND", "OR", "EQUAL_TO", "NOT_EQUAL", 
                      "CONCAT", "PERIOD", "COMMA", "SEMI", "EQUAL", "COLON", 
                      "LB", "RB", "LSB", "RSB", "LCB", "RCB", "IDENTIFIER", 
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_array_type = 2
    RULE_element_type = 3
    RULE_dimesion = 4
    RULE_dimesion_type_int = 5
    RULE_dimesion_type_float = 6
    RULE_variable_decl = 7
    RULE_equal_exp = 8
    RULE_equal_func_call = 9
    RULE_identifier_list = 10
    RULE_expression_list = 11
    RULE_exp_list_type_int = 12
    RULE_exp_list_type_float = 13
    RULE_exp_list_type_string = 14
    RULE_parameter = 15
    RULE_expression = 16
    RULE_expression_1 = 17
    RULE_expression_2 = 18
    RULE_expression_3 = 19
    RULE_expression_4 = 20
    RULE_expression_5 = 21
    RULE_expression_6 = 22
    RULE_expression_7 = 23
    RULE_expression_8 = 24
    RULE_factor = 25
    RULE_function_call = 26
    RULE_exps_list = 27
    RULE_exp_list = 28
    RULE_statement = 29
    RULE_assign_stmt = 30
    RULE_lhs = 31
    RULE_if_stmt = 32
    RULE_for_stmt = 33
    RULE_scala_val = 34
    RULE_init_expr = 35
    RULE_condition_expr = 36
    RULE_update_expr = 37
    RULE_while_stmt = 38
    RULE_do_while_stmt = 39
    RULE_call_stmt = 40
    RULE_block_stmt = 41
    RULE_break_stmt = 42
    RULE_continue_stmt = 43
    RULE_return_stmt = 44
    RULE_function_decl = 45
    RULE_inheritance = 46
    RULE_function_name = 47
    RULE_paramter_list = 48
    RULE_paramter_list_term = 49
    RULE_return_type = 50

    ruleNames =  [ "program", "decls", "array_type", "element_type", "dimesion", 
                   "dimesion_type_int", "dimesion_type_float", "variable_decl", 
                   "equal_exp", "equal_func_call", "identifier_list", "expression_list", 
                   "exp_list_type_int", "exp_list_type_float", "exp_list_type_string", 
                   "parameter", "expression", "expression_1", "expression_2", 
                   "expression_3", "expression_4", "expression_5", "expression_6", 
                   "expression_7", "expression_8", "factor", "function_call", 
                   "exps_list", "exp_list", "statement", "assign_stmt", 
                   "lhs", "if_stmt", "for_stmt", "scala_val", "init_expr", 
                   "condition_expr", "update_expr", "while_stmt", "do_while_stmt", 
                   "call_stmt", "block_stmt", "break_stmt", "continue_stmt", 
                   "return_stmt", "function_decl", "inheritance", "function_name", 
                   "paramter_list", "paramter_list_term", "return_type" ]

    EOF = Token.EOF
    T__0=1
    COMMENT=2
    INTEGER_LIT=3
    FLOAT_LIT=4
    BOOLEAN_LIT=5
    STRING_LIT=6
    ARRAY_LIT=7
    AUTO=8
    BREAK=9
    INTEGER=10
    VOID=11
    ARRAY=12
    FLOAT=13
    RETURN=14
    OUT=15
    BOOLEAN=16
    FOR=17
    STRING=18
    CONTINUE=19
    DO=20
    FUNCTION=21
    OF=22
    ELSE=23
    IF=24
    WHILE=25
    INHERIT=26
    PLUS=27
    MINUS=28
    MUL=29
    DIV=30
    MOD=31
    LESS=32
    GREATER=33
    LTE=34
    GTE=35
    NOT=36
    AND=37
    OR=38
    EQUAL_TO=39
    NOT_EQUAL=40
    CONCAT=41
    PERIOD=42
    COMMA=43
    SEMI=44
    EQUAL=45
    COLON=46
    LB=47
    RB=48
    LSB=49
    RSB=50
    LCB=51
    RCB=52
    IDENTIFIER=53
    WS=54
    ERROR_CHAR=55
    UNCLOSE_STRING=56
    ILLEGAL_ESCAPE=57

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
            self.state = 103 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 102
                self.decls()
                self.state = 105 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.T__0) | (1 << BKOOLParser.INTEGER_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.ARRAY) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.DO) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.WHILE) | (1 << BKOOLParser.MINUS) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LCB) | (1 << BKOOLParser.IDENTIFIER))) != 0)):
                    break

            self.state = 107
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

        def array_type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_typeContext,0)


        def variable_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Variable_declContext,0)


        def function_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Function_declContext,0)


        def statement(self):
            return self.getTypedRuleContext(BKOOLParser.StatementContext,0)


        def expression(self):
            return self.getTypedRuleContext(BKOOLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_decls




    def decls(self):

        localctx = BKOOLParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.array_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.variable_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 111
                self.function_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 112
                self.statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 113
                self.expression()
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
            self.state = 116
            self.match(BKOOLParser.ARRAY)
            self.state = 117
            self.match(BKOOLParser.LSB)
            self.state = 118
            self.dimesion()
            self.state = 119
            self.match(BKOOLParser.RSB)
            self.state = 120
            self.match(BKOOLParser.OF)
            self.state = 121
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

        def getRuleIndex(self):
            return BKOOLParser.RULE_element_type




    def element_type(self):

        localctx = BKOOLParser.Element_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_element_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INTEGER) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.STRING))) != 0)):
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
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTEGER_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.dimesion_type_int()
                pass
            elif token in [BKOOLParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
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
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.match(BKOOLParser.INTEGER_LIT)
                self.state = 130
                self.match(BKOOLParser.COMMA)
                self.state = 131
                self.dimesion_type_int()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
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
            self.state = 135
            self.match(BKOOLParser.FLOAT_LIT)
            self.state = 136
            self.match(BKOOLParser.COMMA)
            self.state = 137
            self.dimesion_type_float()
            self.state = 138
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

        def identifier_list(self):
            return self.getTypedRuleContext(BKOOLParser.Identifier_listContext,0)


        def COLON(self):
            return self.getToken(BKOOLParser.COLON, 0)

        def element_type(self):
            return self.getTypedRuleContext(BKOOLParser.Element_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_typeContext,0)


        def equal_exp(self):
            return self.getTypedRuleContext(BKOOLParser.Equal_expContext,0)


        def equal_func_call(self):
            return self.getTypedRuleContext(BKOOLParser.Equal_func_callContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_variable_decl




    def variable_decl(self):

        localctx = BKOOLParser.Variable_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variable_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.identifier_list()
            self.state = 141
            self.match(BKOOLParser.COLON)
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTEGER, BKOOLParser.FLOAT, BKOOLParser.BOOLEAN, BKOOLParser.STRING]:
                self.state = 142
                self.element_type()
                pass
            elif token in [BKOOLParser.ARRAY]:
                self.state = 143
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 146
                self.equal_exp()
                pass

            elif la_ == 2:
                self.state = 147
                self.equal_func_call()
                pass





        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Equal_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(BKOOLParser.EQUAL, 0)

        def expression_list(self):
            return self.getTypedRuleContext(BKOOLParser.Expression_listContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_equal_exp




    def equal_exp(self):

        localctx = BKOOLParser.Equal_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_equal_exp)
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.EQUAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.match(BKOOLParser.EQUAL)
                self.state = 153
                self.expression_list()
                self.state = 154
                self.match(BKOOLParser.SEMI)
                pass
            elif token in [BKOOLParser.SEMI]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.match(BKOOLParser.SEMI)
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


    class Equal_func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(BKOOLParser.EQUAL, 0)

        def function_call(self):
            return self.getTypedRuleContext(BKOOLParser.Function_callContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_equal_func_call




    def equal_func_call(self):

        localctx = BKOOLParser.Equal_func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_equal_func_call)
        try:
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.EQUAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.match(BKOOLParser.EQUAL)
                self.state = 160
                self.function_call()
                self.state = 161
                self.match(BKOOLParser.SEMI)
                pass
            elif token in [BKOOLParser.SEMI]:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(BKOOLParser.SEMI)
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
        self.enterRule(localctx, 20, self.RULE_identifier_list)
        try:
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(BKOOLParser.IDENTIFIER)
                self.state = 167
                self.match(BKOOLParser.COMMA)
                self.state = 168
                self.identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
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

        def exp_list_type_int(self):
            return self.getTypedRuleContext(BKOOLParser.Exp_list_type_intContext,0)


        def exp_list_type_float(self):
            return self.getTypedRuleContext(BKOOLParser.Exp_list_type_floatContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expression_list




    def expression_list(self):

        localctx = BKOOLParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expression_list)
        try:
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTEGER_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.exp_list_type_int()
                pass
            elif token in [BKOOLParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.exp_list_type_float()
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
        self.enterRule(localctx, 24, self.RULE_exp_list_type_int)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.match(BKOOLParser.INTEGER_LIT)
                self.state = 177
                self.match(BKOOLParser.COMMA)
                self.state = 178
                self.exp_list_type_int()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
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
        self.enterRule(localctx, 26, self.RULE_exp_list_type_float)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(BKOOLParser.FLOAT_LIT)
                self.state = 183
                self.match(BKOOLParser.COMMA)
                self.state = 184
                self.exp_list_type_float()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
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
        self.enterRule(localctx, 28, self.RULE_exp_list_type_string)
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.match(BKOOLParser.STRING_LIT)
                self.state = 189
                self.match(BKOOLParser.COMMA)
                self.state = 190
                self.exp_list_type_string()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
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
        self.enterRule(localctx, 30, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INHERIT]:
                self.state = 194
                self.match(BKOOLParser.INHERIT)
                pass
            elif token in [BKOOLParser.OUT, BKOOLParser.IDENTIFIER]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.OUT]:
                self.state = 198
                self.match(BKOOLParser.OUT)
                pass
            elif token in [BKOOLParser.IDENTIFIER]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 202
            self.match(BKOOLParser.IDENTIFIER)
            self.state = 203
            self.match(BKOOLParser.COLON)
            self.state = 204
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
        self.enterRule(localctx, 32, self.RULE_expression)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.expression_1()
                self.state = 207
                self.match(BKOOLParser.CONCAT)
                self.state = 208
                self.expression_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
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
        self.enterRule(localctx, 34, self.RULE_expression_1)
        self._la = 0 # Token type
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.expression_2(0)
                self.state = 214
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LESS) | (1 << BKOOLParser.GREATER) | (1 << BKOOLParser.LTE) | (1 << BKOOLParser.GTE) | (1 << BKOOLParser.EQUAL_TO) | (1 << BKOOLParser.NOT_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 215
                self.expression_2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
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
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expression_2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.expression_3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expression_2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_2)
                    self.state = 223
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 224
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.AND or _la==BKOOLParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 225
                    self.expression_3(0) 
                self.state = 230
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expression_3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.expression_4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 239
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expression_3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_3)
                    self.state = 234
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 235
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.PLUS or _la==BKOOLParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 236
                    self.expression_4(0) 
                self.state = 241
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expression_4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.expression_5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 250
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expression_4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_4)
                    self.state = 245
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 246
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.DIV) | (1 << BKOOLParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 247
                    self.expression_5() 
                self.state = 252
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        self.enterRule(localctx, 42, self.RULE_expression_5)
        try:
            self.state = 256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(BKOOLParser.NOT)
                self.state = 254
                self.expression_5()
                pass
            elif token in [BKOOLParser.INTEGER_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.MINUS, BKOOLParser.LB, BKOOLParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
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
        self.enterRule(localctx, 44, self.RULE_expression_6)
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.match(BKOOLParser.MINUS)
                self.state = 259
                self.expression_6()
                pass
            elif token in [BKOOLParser.INTEGER_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.LB, BKOOLParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
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
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expression_7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.expression_8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 270
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expression_7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_7)
                    self.state = 266
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 267
                    self.factor() 
                self.state = 272
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
        self.enterRule(localctx, 48, self.RULE_expression_8)
        try:
            self.state = 278
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.match(BKOOLParser.LB)
                self.state = 274
                self.expression()
                self.state = 275
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.INTEGER_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
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


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def exp_list_type_int(self):
            return self.getTypedRuleContext(BKOOLParser.Exp_list_type_intContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_factor




    def factor(self):

        localctx = BKOOLParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_factor)
        try:
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 280
                    self.match(BKOOLParser.INTEGER_LIT)
                    pass

                elif la_ == 2:
                    self.state = 281
                    self.match(BKOOLParser.FLOAT_LIT)
                    pass

                elif la_ == 3:
                    self.state = 282
                    self.match(BKOOLParser.STRING_LIT)
                    pass

                elif la_ == 4:
                    self.state = 283
                    self.match(BKOOLParser.IDENTIFIER)
                    pass

                elif la_ == 5:
                    self.state = 284
                    self.function_call()
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.match(BKOOLParser.IDENTIFIER)
                self.state = 288
                self.match(BKOOLParser.LSB)
                self.state = 289
                self.exp_list_type_int()
                self.state = 290
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

        def exp_list(self):
            return self.getTypedRuleContext(BKOOLParser.Exp_listContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_function_call




    def function_call(self):

        localctx = BKOOLParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(BKOOLParser.IDENTIFIER)
            self.state = 295
            self.match(BKOOLParser.LB)
            self.state = 296
            self.exp_list()
            self.state = 297
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
        self.enterRule(localctx, 54, self.RULE_exps_list)
        try:
            self.state = 301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTEGER_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.MINUS, BKOOLParser.NOT, BKOOLParser.LB, BKOOLParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.exp_list()
                pass
            elif token in [BKOOLParser.EOF]:
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
        self.enterRule(localctx, 56, self.RULE_exp_list)
        try:
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.expression()
                self.state = 304
                self.match(BKOOLParser.COMMA)
                self.state = 305
                self.exp_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
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
        self.enterRule(localctx, 58, self.RULE_statement)
        try:
            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 311
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 312
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 313
                self.while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 314
                self.do_while_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 315
                self.block_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 316
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 317
                self.continue_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 318
                self.break_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 319
                self.call_stmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 320
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
        self.enterRule(localctx, 60, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.lhs()
            self.state = 324
            self.match(BKOOLParser.EQUAL)
            self.state = 325
            self.expression()
            self.state = 326
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
        self.enterRule(localctx, 62, self.RULE_lhs)
        try:
            self.state = 334
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.match(BKOOLParser.IDENTIFIER)
                self.state = 329
                self.match(BKOOLParser.LSB)
                self.state = 330
                self.exp_list_type_int()
                self.state = 331
                self.match(BKOOLParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
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
        self.enterRule(localctx, 64, self.RULE_if_stmt)
        try:
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.match(BKOOLParser.IF)
                self.state = 337
                self.expression()
                self.state = 338
                self.statement()
                self.state = 339
                self.match(BKOOLParser.ELSE)
                self.state = 340
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                self.match(BKOOLParser.IF)
                self.state = 343
                self.expression()
                self.state = 344
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
        self.enterRule(localctx, 66, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(BKOOLParser.LB)
            self.state = 349
            self.scala_val()
            self.state = 350
            self.match(BKOOLParser.EQUAL)
            self.state = 351
            self.init_expr()
            self.state = 352
            self.match(BKOOLParser.COMMA)
            self.state = 353
            self.condition_expr()
            self.state = 354
            self.match(BKOOLParser.COMMA)
            self.state = 355
            self.update_expr()
            self.state = 356
            self.match(BKOOLParser.RB)
            self.state = 357
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
        self.enterRule(localctx, 68, self.RULE_scala_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
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
        self.enterRule(localctx, 70, self.RULE_init_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
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
        self.enterRule(localctx, 72, self.RULE_condition_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(BKOOLParser.IDENTIFIER)
            self.state = 364
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LESS) | (1 << BKOOLParser.GREATER) | (1 << BKOOLParser.LTE) | (1 << BKOOLParser.GTE) | (1 << BKOOLParser.EQUAL_TO) | (1 << BKOOLParser.NOT_EQUAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 365
                self.match(BKOOLParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 366
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
        self.enterRule(localctx, 74, self.RULE_update_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(BKOOLParser.IDENTIFIER)
            self.state = 370
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.PLUS) | (1 << BKOOLParser.MINUS) | (1 << BKOOLParser.MUL) | (1 << BKOOLParser.MOD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 371
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
        self.enterRule(localctx, 76, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.match(BKOOLParser.WHILE)
            self.state = 374
            self.match(BKOOLParser.LB)
            self.state = 375
            self.expression()
            self.state = 376
            self.match(BKOOLParser.RB)
            self.state = 377
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


        def getRuleIndex(self):
            return BKOOLParser.RULE_do_while_stmt




    def do_while_stmt(self):

        localctx = BKOOLParser.Do_while_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_do_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(BKOOLParser.DO)
            self.state = 380
            self.block_stmt()
            self.state = 381
            self.match(BKOOLParser.WHILE)
            self.state = 382
            self.expression()
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

        def function_call(self):
            return self.getTypedRuleContext(BKOOLParser.Function_callContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_call_stmt




    def call_stmt(self):

        localctx = BKOOLParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.function_call()
            self.state = 385
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

        def RCB(self):
            return self.getToken(BKOOLParser.RCB, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StatementContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_block_stmt




    def block_stmt(self):

        localctx = BKOOLParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.state = 396
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LCB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.match(BKOOLParser.LCB)
                self.state = 391
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.T__0) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.RETURN) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.DO) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.WHILE) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LCB) | (1 << BKOOLParser.IDENTIFIER))) != 0):
                    self.state = 388
                    self.statement()
                    self.state = 393
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 394
                self.match(BKOOLParser.RCB)
                pass
            elif token in [BKOOLParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.match(BKOOLParser.T__0)
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
        self.enterRule(localctx, 84, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.match(BKOOLParser.BREAK)
            self.state = 399
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
        self.enterRule(localctx, 86, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(BKOOLParser.CONTINUE)
            self.state = 402
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
        self.enterRule(localctx, 88, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.match(BKOOLParser.RETURN)
            self.state = 405
            self.expression()
            self.state = 406
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
        self.enterRule(localctx, 90, self.RULE_function_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(BKOOLParser.IDENTIFIER)
            self.state = 409
            self.match(BKOOLParser.COLON)
            self.state = 410
            self.match(BKOOLParser.FUNCTION)
            self.state = 411
            self.return_type()
            self.state = 412
            self.match(BKOOLParser.LB)
            self.state = 413
            self.paramter_list()
            self.state = 414
            self.match(BKOOLParser.RB)
            self.state = 415
            self.inheritance()
            self.state = 416
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
        self.enterRule(localctx, 92, self.RULE_inheritance)
        try:
            self.state = 421
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INHERIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.match(BKOOLParser.INHERIT)
                self.state = 419
                self.function_name()
                pass
            elif token in [BKOOLParser.T__0, BKOOLParser.BREAK, BKOOLParser.RETURN, BKOOLParser.CONTINUE, BKOOLParser.DO, BKOOLParser.IF, BKOOLParser.WHILE, BKOOLParser.LB, BKOOLParser.LCB, BKOOLParser.IDENTIFIER]:
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
        self.enterRule(localctx, 94, self.RULE_function_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
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
        self.enterRule(localctx, 96, self.RULE_paramter_list)
        try:
            self.state = 427
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.OUT, BKOOLParser.INHERIT, BKOOLParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 425
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
        self.enterRule(localctx, 98, self.RULE_paramter_list_term)
        try:
            self.state = 434
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.parameter()
                self.state = 430
                self.match(BKOOLParser.COMMA)
                self.state = 431
                self.paramter_list_term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 433
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
        self.enterRule(localctx, 100, self.RULE_return_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[18] = self.expression_2_sempred
        self._predicates[19] = self.expression_3_sempred
        self._predicates[20] = self.expression_4_sempred
        self._predicates[23] = self.expression_7_sempred
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
         




