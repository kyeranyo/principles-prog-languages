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
        buf.write("\u0275\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\5\13\u0109\n\13\3\13\3\13\3\f\3\f\3\f\3\f\7")
        buf.write("\f\u0111\n\f\f\f\16\f\u0114\13\f\3\r\3\r\3\r\3\r\7\r\u011a")
        buf.write("\n\r\f\r\16\r\u011d\13\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\7\16\u0126\n\16\f\16\16\16\u0129\13\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\7\17\u0130\n\17\f\17\16\17\u0133\13\17\3")
        buf.write("\17\3\17\6\17\u0137\n\17\r\17\16\17\u0138\7\17\u013b\n")
        buf.write("\17\f\17\16\17\u013e\13\17\3\17\5\17\u0141\n\17\3\20\3")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\5\21\u0152\n\21\3\21\3\21\3\22\3\22\7")
        buf.write("\22\u0158\n\22\f\22\16\22\u015b\13\22\3\23\3\23\5\23\u015f")
        buf.write("\n\23\3\23\6\23\u0162\n\23\r\23\16\23\u0163\3\24\3\24")
        buf.write("\5\24\u0168\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\7\27\u0179\n\27")
        buf.write("\f\27\16\27\u017c\13\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\7\30\u0187\n\30\f\30\16\30\u018a\13\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3!\3")
        buf.write("!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)")
        buf.write("\3)\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3+\3,\3")
        buf.write(",\3,\3-\3-\3-\3-\3-\3.\3.\3.\3/\3/\3/\3/\3/\3/\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38")
        buf.write("\38\38\39\39\39\3:\3:\3;\3;\3;\3<\3<\3<\3=\3=\3=\3>\3")
        buf.write(">\3>\3?\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3")
        buf.write("F\3G\3G\3H\3H\3I\3I\3J\3J\3K\6K\u0248\nK\rK\16K\u0249")
        buf.write("\3K\7K\u024d\nK\fK\16K\u0250\13K\3L\6L\u0253\nL\rL\16")
        buf.write("L\u0254\3L\3L\3M\3M\3M\3M\7M\u025d\nM\fM\16M\u0260\13")
        buf.write("M\3M\5M\u0263\nM\3M\3M\3N\3N\3N\3N\7N\u026b\nN\fN\16N")
        buf.write("\u026e\13N\3N\3N\3N\3O\3O\3O\6\u011b\u0127\u0188\u025e")
        buf.write("\2P\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\2")
        buf.write("\31\2\33\2\35\r\37\2!\16#\2%\2\'\17)\2+\2-\20/\2\61\2")
        buf.write("\63\2\65\2\67\29\2;\21=\22?\23A\24C\25E\26G\27I\30K\31")
        buf.write("M\32O\33Q\34S\35U\36W\37Y [!]\"_#a$c%e&g\'i(k)m*o+q,s")
        buf.write("-u.w/y\60{\61}\62\177\63\u0081\64\u0083\65\u0085\66\u0087")
        buf.write("\67\u00898\u008b9\u008d:\u008f;\u0091<\u0093=\u0095>\u0097")
        buf.write("?\u0099@\u009bA\u009dB\3\2\20\4\2\f\f\17\17\3\2\63;\3")
        buf.write("\2\62;\4\2GGgg\4\2--//\5\2\f\f$$^^\n\2$$))^^ddhhppttv")
        buf.write("v\3\2$$\3\2))\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17")
        buf.write("\"\"\4\3\f\f\17\17\4\2$$^^\2\u0284\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2!\3\2\2\2\2\'\3\2\2\2\2-\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write("\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2")
        buf.write("\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b")
        buf.write("\3\2\2\2\2\u009d\3\2\2\2\3\u009f\3\2\2\2\5\u00ab\3\2\2")
        buf.write("\2\7\u00b8\3\2\2\2\t\u00c2\3\2\2\2\13\u00cd\3\2\2\2\r")
        buf.write("\u00da\3\2\2\2\17\u00e5\3\2\2\2\21\u00f1\3\2\2\2\23\u00f7")
        buf.write("\3\2\2\2\25\u0108\3\2\2\2\27\u010c\3\2\2\2\31\u0115\3")
        buf.write("\2\2\2\33\u0121\3\2\2\2\35\u0140\3\2\2\2\37\u0142\3\2")
        buf.write("\2\2!\u0151\3\2\2\2#\u0155\3\2\2\2%\u015c\3\2\2\2\'\u0167")
        buf.write("\3\2\2\2)\u0169\3\2\2\2+\u016f\3\2\2\2-\u0174\3\2\2\2")
        buf.write("/\u0180\3\2\2\2\61\u018e\3\2\2\2\63\u0191\3\2\2\2\65\u0194")
        buf.write("\3\2\2\2\67\u0197\3\2\2\29\u0199\3\2\2\2;\u019b\3\2\2")
        buf.write("\2=\u01a0\3\2\2\2?\u01a6\3\2\2\2A\u01ae\3\2\2\2C\u01b3")
        buf.write("\3\2\2\2E\u01b9\3\2\2\2G\u01bf\3\2\2\2I\u01c6\3\2\2\2")
        buf.write("K\u01ca\3\2\2\2M\u01d2\3\2\2\2O\u01d6\3\2\2\2Q\u01dd\3")
        buf.write("\2\2\2S\u01e6\3\2\2\2U\u01e9\3\2\2\2W\u01f2\3\2\2\2Y\u01f5")
        buf.write("\3\2\2\2[\u01fa\3\2\2\2]\u01fd\3\2\2\2_\u0203\3\2\2\2")
        buf.write("a\u020b\3\2\2\2c\u020d\3\2\2\2e\u020f\3\2\2\2g\u0211\3")
        buf.write("\2\2\2i\u0213\3\2\2\2k\u0215\3\2\2\2m\u0217\3\2\2\2o\u0219")
        buf.write("\3\2\2\2q\u021c\3\2\2\2s\u021f\3\2\2\2u\u0221\3\2\2\2")
        buf.write("w\u0224\3\2\2\2y\u0227\3\2\2\2{\u022a\3\2\2\2}\u022d\3")
        buf.write("\2\2\2\177\u0230\3\2\2\2\u0081\u0232\3\2\2\2\u0083\u0234")
        buf.write("\3\2\2\2\u0085\u0236\3\2\2\2\u0087\u0238\3\2\2\2\u0089")
        buf.write("\u023a\3\2\2\2\u008b\u023c\3\2\2\2\u008d\u023e\3\2\2\2")
        buf.write("\u008f\u0240\3\2\2\2\u0091\u0242\3\2\2\2\u0093\u0244\3")
        buf.write("\2\2\2\u0095\u0247\3\2\2\2\u0097\u0252\3\2\2\2\u0099\u0258")
        buf.write("\3\2\2\2\u009b\u0266\3\2\2\2\u009d\u0272\3\2\2\2\u009f")
        buf.write("\u00a0\7t\2\2\u00a0\u00a1\7g\2\2\u00a1\u00a2\7c\2\2\u00a2")
        buf.write("\u00a3\7f\2\2\u00a3\u00a4\7K\2\2\u00a4\u00a5\7p\2\2\u00a5")
        buf.write("\u00a6\7v\2\2\u00a6\u00a7\7g\2\2\u00a7\u00a8\7i\2\2\u00a8")
        buf.write("\u00a9\7g\2\2\u00a9\u00aa\7t\2\2\u00aa\4\3\2\2\2\u00ab")
        buf.write("\u00ac\7r\2\2\u00ac\u00ad\7t\2\2\u00ad\u00ae\7k\2\2\u00ae")
        buf.write("\u00af\7p\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1\7K\2\2\u00b1")
        buf.write("\u00b2\7p\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4\7g\2\2\u00b4")
        buf.write("\u00b5\7i\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7\7t\2\2\u00b7")
        buf.write("\6\3\2\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba\7g\2\2\u00ba")
        buf.write("\u00bb\7c\2\2\u00bb\u00bc\7f\2\2\u00bc\u00bd\7H\2\2\u00bd")
        buf.write("\u00be\7n\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0\7c\2\2\u00c0")
        buf.write("\u00c1\7v\2\2\u00c1\b\3\2\2\2\u00c2\u00c3\7y\2\2\u00c3")
        buf.write("\u00c4\7t\2\2\u00c4\u00c5\7k\2\2\u00c5\u00c6\7v\2\2\u00c6")
        buf.write("\u00c7\7g\2\2\u00c7\u00c8\7H\2\2\u00c8\u00c9\7n\2\2\u00c9")
        buf.write("\u00ca\7q\2\2\u00ca\u00cb\7c\2\2\u00cb\u00cc\7v\2\2\u00cc")
        buf.write("\n\3\2\2\2\u00cd\u00ce\7r\2\2\u00ce\u00cf\7t\2\2\u00cf")
        buf.write("\u00d0\7k\2\2\u00d0\u00d1\7p\2\2\u00d1\u00d2\7v\2\2\u00d2")
        buf.write("\u00d3\7D\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5\7q\2\2\u00d5")
        buf.write("\u00d6\7n\2\2\u00d6\u00d7\7g\2\2\u00d7\u00d8\7c\2\2\u00d8")
        buf.write("\u00d9\7p\2\2\u00d9\f\3\2\2\2\u00da\u00db\7t\2\2\u00db")
        buf.write("\u00dc\7g\2\2\u00dc\u00dd\7c\2\2\u00dd\u00de\7f\2\2\u00de")
        buf.write("\u00df\7U\2\2\u00df\u00e0\7v\2\2\u00e0\u00e1\7t\2\2\u00e1")
        buf.write("\u00e2\7k\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4\7i\2\2\u00e4")
        buf.write("\16\3\2\2\2\u00e5\u00e6\7r\2\2\u00e6\u00e7\7t\2\2\u00e7")
        buf.write("\u00e8\7k\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea\7v\2\2\u00ea")
        buf.write("\u00eb\7U\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed\7t\2\2\u00ed")
        buf.write("\u00ee\7k\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0\7i\2\2\u00f0")
        buf.write("\20\3\2\2\2\u00f1\u00f2\7u\2\2\u00f2\u00f3\7w\2\2\u00f3")
        buf.write("\u00f4\7r\2\2\u00f4\u00f5\7g\2\2\u00f5\u00f6\7t\2\2\u00f6")
        buf.write("\22\3\2\2\2\u00f7\u00f8\7r\2\2\u00f8\u00f9\7t\2\2\u00f9")
        buf.write("\u00fa\7g\2\2\u00fa\u00fb\7x\2\2\u00fb\u00fc\7g\2\2\u00fc")
        buf.write("\u00fd\7p\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7F\2\2\u00ff")
        buf.write("\u0100\7g\2\2\u0100\u0101\7h\2\2\u0101\u0102\7c\2\2\u0102")
        buf.write("\u0103\7w\2\2\u0103\u0104\7n\2\2\u0104\u0105\7v\2\2\u0105")
        buf.write("\24\3\2\2\2\u0106\u0109\5\27\f\2\u0107\u0109\5\31\r\2")
        buf.write("\u0108\u0106\3\2\2\2\u0108\u0107\3\2\2\2\u0109\u010a\3")
        buf.write("\2\2\2\u010a\u010b\b\13\2\2\u010b\26\3\2\2\2\u010c\u010d")
        buf.write("\7\61\2\2\u010d\u010e\7\61\2\2\u010e\u0112\3\2\2\2\u010f")
        buf.write("\u0111\n\2\2\2\u0110\u010f\3\2\2\2\u0111\u0114\3\2\2\2")
        buf.write("\u0112\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u0113\30\3\2")
        buf.write("\2\2\u0114\u0112\3\2\2\2\u0115\u0116\7\61\2\2\u0116\u0117")
        buf.write("\7,\2\2\u0117\u011b\3\2\2\2\u0118\u011a\13\2\2\2\u0119")
        buf.write("\u0118\3\2\2\2\u011a\u011d\3\2\2\2\u011b\u011c\3\2\2\2")
        buf.write("\u011b\u0119\3\2\2\2\u011c\u011e\3\2\2\2\u011d\u011b\3")
        buf.write("\2\2\2\u011e\u011f\7,\2\2\u011f\u0120\7\61\2\2\u0120\32")
        buf.write("\3\2\2\2\u0121\u0122\7\61\2\2\u0122\u0123\7,\2\2\u0123")
        buf.write("\u0127\3\2\2\2\u0124\u0126\13\2\2\2\u0125\u0124\3\2\2")
        buf.write("\2\u0126\u0129\3\2\2\2\u0127\u0128\3\2\2\2\u0127\u0125")
        buf.write("\3\2\2\2\u0128\u012a\3\2\2\2\u0129\u0127\3\2\2\2\u012a")
        buf.write("\u012b\7\2\2\3\u012b\34\3\2\2\2\u012c\u0141\7\62\2\2\u012d")
        buf.write("\u0131\t\3\2\2\u012e\u0130\t\4\2\2\u012f\u012e\3\2\2\2")
        buf.write("\u0130\u0133\3\2\2\2\u0131\u012f\3\2\2\2\u0131\u0132\3")
        buf.write("\2\2\2\u0132\u013c\3\2\2\2\u0133\u0131\3\2\2\2\u0134\u0136")
        buf.write("\5\37\20\2\u0135\u0137\t\4\2\2\u0136\u0135\3\2\2\2\u0137")
        buf.write("\u0138\3\2\2\2\u0138\u0136\3\2\2\2\u0138\u0139\3\2\2\2")
        buf.write("\u0139\u013b\3\2\2\2\u013a\u0134\3\2\2\2\u013b\u013e\3")
        buf.write("\2\2\2\u013c\u013a\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013f")
        buf.write("\3\2\2\2\u013e\u013c\3\2\2\2\u013f\u0141\b\17\3\2\u0140")
        buf.write("\u012c\3\2\2\2\u0140\u012d\3\2\2\2\u0141\36\3\2\2\2\u0142")
        buf.write("\u0143\7a\2\2\u0143 \3\2\2\2\u0144\u0145\5\35\17\2\u0145")
        buf.write("\u0146\5#\22\2\u0146\u0147\5%\23\2\u0147\u0152\3\2\2\2")
        buf.write("\u0148\u0149\5\35\17\2\u0149\u014a\5#\22\2\u014a\u0152")
        buf.write("\3\2\2\2\u014b\u014c\5\35\17\2\u014c\u014d\5%\23\2\u014d")
        buf.write("\u0152\3\2\2\2\u014e\u014f\5#\22\2\u014f\u0150\5%\23\2")
        buf.write("\u0150\u0152\3\2\2\2\u0151\u0144\3\2\2\2\u0151\u0148\3")
        buf.write("\2\2\2\u0151\u014b\3\2\2\2\u0151\u014e\3\2\2\2\u0152\u0153")
        buf.write("\3\2\2\2\u0153\u0154\b\21\4\2\u0154\"\3\2\2\2\u0155\u0159")
        buf.write("\5\177@\2\u0156\u0158\t\4\2\2\u0157\u0156\3\2\2\2\u0158")
        buf.write("\u015b\3\2\2\2\u0159\u0157\3\2\2\2\u0159\u015a\3\2\2\2")
        buf.write("\u015a$\3\2\2\2\u015b\u0159\3\2\2\2\u015c\u015e\t\5\2")
        buf.write("\2\u015d\u015f\t\6\2\2\u015e\u015d\3\2\2\2\u015e\u015f")
        buf.write("\3\2\2\2\u015f\u0161\3\2\2\2\u0160\u0162\t\4\2\2\u0161")
        buf.write("\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0161\3\2\2\2")
        buf.write("\u0163\u0164\3\2\2\2\u0164&\3\2\2\2\u0165\u0168\5)\25")
        buf.write("\2\u0166\u0168\5+\26\2\u0167\u0165\3\2\2\2\u0167\u0166")
        buf.write("\3\2\2\2\u0168(\3\2\2\2\u0169\u016a\7h\2\2\u016a\u016b")
        buf.write("\7c\2\2\u016b\u016c\7n\2\2\u016c\u016d\7u\2\2\u016d\u016e")
        buf.write("\7g\2\2\u016e*\3\2\2\2\u016f\u0170\7v\2\2\u0170\u0171")
        buf.write("\7t\2\2\u0171\u0172\7w\2\2\u0172\u0173\7g\2\2\u0173,\3")
        buf.write("\2\2\2\u0174\u017a\5\67\34\2\u0175\u0179\n\7\2\2\u0176")
        buf.write("\u0179\5/\30\2\u0177\u0179\5\63\32\2\u0178\u0175\3\2\2")
        buf.write("\2\u0178\u0176\3\2\2\2\u0178\u0177\3\2\2\2\u0179\u017c")
        buf.write("\3\2\2\2\u017a\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b")
        buf.write("\u017d\3\2\2\2\u017c\u017a\3\2\2\2\u017d\u017e\5\67\34")
        buf.write("\2\u017e\u017f\b\27\5\2\u017f.\3\2\2\2\u0180\u0181\7^")
        buf.write("\2\2\u0181\u0182\7$\2\2\u0182\u0188\3\2\2\2\u0183\u0187")
        buf.write("\n\7\2\2\u0184\u0187\5/\30\2\u0185\u0187\5\63\32\2\u0186")
        buf.write("\u0183\3\2\2\2\u0186\u0184\3\2\2\2\u0186\u0185\3\2\2\2")
        buf.write("\u0187\u018a\3\2\2\2\u0188\u0189\3\2\2\2\u0188\u0186\3")
        buf.write("\2\2\2\u0189\u018b\3\2\2\2\u018a\u0188\3\2\2\2\u018b\u018c")
        buf.write("\7^\2\2\u018c\u018d\7$\2\2\u018d\60\3\2\2\2\u018e\u018f")
        buf.write("\7^\2\2\u018f\u0190\n\b\2\2\u0190\62\3\2\2\2\u0191\u0192")
        buf.write("\7^\2\2\u0192\u0193\t\b\2\2\u0193\64\3\2\2\2\u0194\u0195")
        buf.write("\7^\2\2\u0195\u0196\n\t\2\2\u0196\66\3\2\2\2\u0197\u0198")
        buf.write("\t\t\2\2\u01988\3\2\2\2\u0199\u019a\t\n\2\2\u019a:\3\2")
        buf.write("\2\2\u019b\u019c\7c\2\2\u019c\u019d\7w\2\2\u019d\u019e")
        buf.write("\7v\2\2\u019e\u019f\7q\2\2\u019f<\3\2\2\2\u01a0\u01a1")
        buf.write("\7d\2\2\u01a1\u01a2\7t\2\2\u01a2\u01a3\7g\2\2\u01a3\u01a4")
        buf.write("\7c\2\2\u01a4\u01a5\7m\2\2\u01a5>\3\2\2\2\u01a6\u01a7")
        buf.write("\7k\2\2\u01a7\u01a8\7p\2\2\u01a8\u01a9\7v\2\2\u01a9\u01aa")
        buf.write("\7g\2\2\u01aa\u01ab\7i\2\2\u01ab\u01ac\7g\2\2\u01ac\u01ad")
        buf.write("\7t\2\2\u01ad@\3\2\2\2\u01ae\u01af\7x\2\2\u01af\u01b0")
        buf.write("\7q\2\2\u01b0\u01b1\7k\2\2\u01b1\u01b2\7f\2\2\u01b2B\3")
        buf.write("\2\2\2\u01b3\u01b4\7c\2\2\u01b4\u01b5\7t\2\2\u01b5\u01b6")
        buf.write("\7t\2\2\u01b6\u01b7\7c\2\2\u01b7\u01b8\7{\2\2\u01b8D\3")
        buf.write("\2\2\2\u01b9\u01ba\7h\2\2\u01ba\u01bb\7n\2\2\u01bb\u01bc")
        buf.write("\7q\2\2\u01bc\u01bd\7c\2\2\u01bd\u01be\7v\2\2\u01beF\3")
        buf.write("\2\2\2\u01bf\u01c0\7t\2\2\u01c0\u01c1\7g\2\2\u01c1\u01c2")
        buf.write("\7v\2\2\u01c2\u01c3\7w\2\2\u01c3\u01c4\7t\2\2\u01c4\u01c5")
        buf.write("\7p\2\2\u01c5H\3\2\2\2\u01c6\u01c7\7q\2\2\u01c7\u01c8")
        buf.write("\7w\2\2\u01c8\u01c9\7v\2\2\u01c9J\3\2\2\2\u01ca\u01cb")
        buf.write("\7d\2\2\u01cb\u01cc\7q\2\2\u01cc\u01cd\7q\2\2\u01cd\u01ce")
        buf.write("\7n\2\2\u01ce\u01cf\7g\2\2\u01cf\u01d0\7c\2\2\u01d0\u01d1")
        buf.write("\7p\2\2\u01d1L\3\2\2\2\u01d2\u01d3\7h\2\2\u01d3\u01d4")
        buf.write("\7q\2\2\u01d4\u01d5\7t\2\2\u01d5N\3\2\2\2\u01d6\u01d7")
        buf.write("\7u\2\2\u01d7\u01d8\7v\2\2\u01d8\u01d9\7t\2\2\u01d9\u01da")
        buf.write("\7k\2\2\u01da\u01db\7p\2\2\u01db\u01dc\7i\2\2\u01dcP\3")
        buf.write("\2\2\2\u01dd\u01de\7e\2\2\u01de\u01df\7q\2\2\u01df\u01e0")
        buf.write("\7p\2\2\u01e0\u01e1\7v\2\2\u01e1\u01e2\7k\2\2\u01e2\u01e3")
        buf.write("\7p\2\2\u01e3\u01e4\7w\2\2\u01e4\u01e5\7g\2\2\u01e5R\3")
        buf.write("\2\2\2\u01e6\u01e7\7f\2\2\u01e7\u01e8\7q\2\2\u01e8T\3")
        buf.write("\2\2\2\u01e9\u01ea\7h\2\2\u01ea\u01eb\7w\2\2\u01eb\u01ec")
        buf.write("\7p\2\2\u01ec\u01ed\7e\2\2\u01ed\u01ee\7v\2\2\u01ee\u01ef")
        buf.write("\7k\2\2\u01ef\u01f0\7q\2\2\u01f0\u01f1\7p\2\2\u01f1V\3")
        buf.write("\2\2\2\u01f2\u01f3\7q\2\2\u01f3\u01f4\7h\2\2\u01f4X\3")
        buf.write("\2\2\2\u01f5\u01f6\7g\2\2\u01f6\u01f7\7n\2\2\u01f7\u01f8")
        buf.write("\7u\2\2\u01f8\u01f9\7g\2\2\u01f9Z\3\2\2\2\u01fa\u01fb")
        buf.write("\7k\2\2\u01fb\u01fc\7h\2\2\u01fc\\\3\2\2\2\u01fd\u01fe")
        buf.write("\7y\2\2\u01fe\u01ff\7j\2\2\u01ff\u0200\7k\2\2\u0200\u0201")
        buf.write("\7n\2\2\u0201\u0202\7g\2\2\u0202^\3\2\2\2\u0203\u0204")
        buf.write("\7k\2\2\u0204\u0205\7p\2\2\u0205\u0206\7j\2\2\u0206\u0207")
        buf.write("\7g\2\2\u0207\u0208\7t\2\2\u0208\u0209\7k\2\2\u0209\u020a")
        buf.write("\7v\2\2\u020a`\3\2\2\2\u020b\u020c\7-\2\2\u020cb\3\2\2")
        buf.write("\2\u020d\u020e\7/\2\2\u020ed\3\2\2\2\u020f\u0210\7,\2")
        buf.write("\2\u0210f\3\2\2\2\u0211\u0212\7\61\2\2\u0212h\3\2\2\2")
        buf.write("\u0213\u0214\7\'\2\2\u0214j\3\2\2\2\u0215\u0216\7>\2\2")
        buf.write("\u0216l\3\2\2\2\u0217\u0218\7@\2\2\u0218n\3\2\2\2\u0219")
        buf.write("\u021a\7>\2\2\u021a\u021b\7?\2\2\u021bp\3\2\2\2\u021c")
        buf.write("\u021d\7@\2\2\u021d\u021e\7?\2\2\u021er\3\2\2\2\u021f")
        buf.write("\u0220\7#\2\2\u0220t\3\2\2\2\u0221\u0222\7(\2\2\u0222")
        buf.write("\u0223\7(\2\2\u0223v\3\2\2\2\u0224\u0225\7~\2\2\u0225")
        buf.write("\u0226\7~\2\2\u0226x\3\2\2\2\u0227\u0228\7?\2\2\u0228")
        buf.write("\u0229\7?\2\2\u0229z\3\2\2\2\u022a\u022b\7#\2\2\u022b")
        buf.write("\u022c\7?\2\2\u022c|\3\2\2\2\u022d\u022e\7<\2\2\u022e")
        buf.write("\u022f\7<\2\2\u022f~\3\2\2\2\u0230\u0231\7\60\2\2\u0231")
        buf.write("\u0080\3\2\2\2\u0232\u0233\7.\2\2\u0233\u0082\3\2\2\2")
        buf.write("\u0234\u0235\7=\2\2\u0235\u0084\3\2\2\2\u0236\u0237\7")
        buf.write("?\2\2\u0237\u0086\3\2\2\2\u0238\u0239\7<\2\2\u0239\u0088")
        buf.write("\3\2\2\2\u023a\u023b\7*\2\2\u023b\u008a\3\2\2\2\u023c")
        buf.write("\u023d\7+\2\2\u023d\u008c\3\2\2\2\u023e\u023f\7]\2\2\u023f")
        buf.write("\u008e\3\2\2\2\u0240\u0241\7_\2\2\u0241\u0090\3\2\2\2")
        buf.write("\u0242\u0243\7}\2\2\u0243\u0092\3\2\2\2\u0244\u0245\7")
        buf.write("\177\2\2\u0245\u0094\3\2\2\2\u0246\u0248\t\13\2\2\u0247")
        buf.write("\u0246\3\2\2\2\u0248\u0249\3\2\2\2\u0249\u0247\3\2\2\2")
        buf.write("\u0249\u024a\3\2\2\2\u024a\u024e\3\2\2\2\u024b\u024d\t")
        buf.write("\f\2\2\u024c\u024b\3\2\2\2\u024d\u0250\3\2\2\2\u024e\u024c")
        buf.write("\3\2\2\2\u024e\u024f\3\2\2\2\u024f\u0096\3\2\2\2\u0250")
        buf.write("\u024e\3\2\2\2\u0251\u0253\t\r\2\2\u0252\u0251\3\2\2\2")
        buf.write("\u0253\u0254\3\2\2\2\u0254\u0252\3\2\2\2\u0254\u0255\3")
        buf.write("\2\2\2\u0255\u0256\3\2\2\2\u0256\u0257\bL\2\2\u0257\u0098")
        buf.write("\3\2\2\2\u0258\u025e\5\67\34\2\u0259\u025d\n\t\2\2\u025a")
        buf.write("\u025d\5/\30\2\u025b\u025d\5\63\32\2\u025c\u0259\3\2\2")
        buf.write("\2\u025c\u025a\3\2\2\2\u025c\u025b\3\2\2\2\u025d\u0260")
        buf.write("\3\2\2\2\u025e\u025f\3\2\2\2\u025e\u025c\3\2\2\2\u025f")
        buf.write("\u0262\3\2\2\2\u0260\u025e\3\2\2\2\u0261\u0263\t\16\2")
        buf.write("\2\u0262\u0261\3\2\2\2\u0263\u0264\3\2\2\2\u0264\u0265")
        buf.write("\bM\6\2\u0265\u009a\3\2\2\2\u0266\u026c\5\67\34\2\u0267")
        buf.write("\u026b\n\17\2\2\u0268\u026b\5/\30\2\u0269\u026b\5\63\32")
        buf.write("\2\u026a\u0267\3\2\2\2\u026a\u0268\3\2\2\2\u026a\u0269")
        buf.write("\3\2\2\2\u026b\u026e\3\2\2\2\u026c\u026a\3\2\2\2\u026c")
        buf.write("\u026d\3\2\2\2\u026d\u026f\3\2\2\2\u026e\u026c\3\2\2\2")
        buf.write("\u026f\u0270\5\61\31\2\u0270\u0271\bN\7\2\u0271\u009c")
        buf.write("\3\2\2\2\u0272\u0273\13\2\2\2\u0273\u0274\bO\b\2\u0274")
        buf.write("\u009e\3\2\2\2\34\2\u0108\u0112\u011b\u0127\u0131\u0138")
        buf.write("\u013c\u0140\u0151\u0159\u015e\u0163\u0167\u0178\u017a")
        buf.write("\u0186\u0188\u0249\u024e\u0254\u025c\u025e\u0262\u026a")
        buf.write("\u026c\t\b\2\2\3\17\2\3\21\3\3\27\4\3M\5\3N\6\3O\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    COMMENT = 10
    INTEGER_LIT = 11
    FLOAT_LIT = 12
    BOOLEAN_LIT = 13
    STRING_LIT = 14
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
            "'readInteger'", "'printInteger'", "'readFloat'", "'writeFloat'", 
            "'printBoolean'", "'readString'", "'printString'", "'super'", 
            "'preventDefault'", "'auto'", "'break'", "'integer'", "'void'", 
            "'array'", "'float'", "'return'", "'out'", "'boolean'", "'for'", 
            "'string'", "'continue'", "'do'", "'function'", "'of'", "'else'", 
            "'if'", "'while'", "'inherit'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'<'", "'>'", "'<='", "'>='", "'!'", "'&&'", "'||'", 
            "'=='", "'!='", "'::'", "'.'", "','", "';'", "'='", "':'", "'('", 
            "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "INTEGER_LIT", "FLOAT_LIT", "BOOLEAN_LIT", "STRING_LIT", 
            "AUTO", "BREAK", "INTEGER", "VOID", "ARRAY", "FLOAT", "RETURN", 
            "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", "FUNCTION", 
            "OF", "ELSE", "IF", "WHILE", "INHERIT", "PLUS", "MINUS", "MUL", 
            "DIV", "MOD", "LESS", "GREATER", "LTE", "GTE", "NOT", "AND", 
            "OR", "EQUAL_TO", "NOT_EQUAL", "CONCAT", "PERIOD", "COMMA", 
            "SEMI", "EQUAL", "COLON", "LB", "RB", "LSB", "RSB", "LCB", "RCB", 
            "IDENTIFIER", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "COMMENT", "SingleLineComment", "MultiLineComment", 
                  "CommentAll", "INTEGER_LIT", "UNDERSCORE", "FLOAT_LIT", 
                  "DECPART", "EXPPART", "BOOLEAN_LIT", "FALSE", "TRUE", 
                  "STRING_LIT", "SUBSTRING", "Not_Escape_Sequence", "Escape_Sequence", 
                  "AllEscSeq", "DUO_QUOTE", "SINGLE_QUOTE", "AUTO", "BREAK", 
                  "INTEGER", "VOID", "ARRAY", "FLOAT", "RETURN", "OUT", 
                  "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", "FUNCTION", 
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
            actions[13] = self.INTEGER_LIT_action 
            actions[15] = self.FLOAT_LIT_action 
            actions[21] = self.STRING_LIT_action 
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
     


