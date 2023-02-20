# Generated from c:\Users\84865\Documents\HCMUT-cse20\CSE-PPL\assignment-1\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3:")
        buf.write("\u00f6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\3\2\6\2@\n\2\r\2\16\2A\3\2\3\2\3\3\3\3\3\3")
        buf.write("\5\3I\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6")
        buf.write("\5\6V\n\6\3\7\3\7\3\7\3\7\5\7\\\n\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\5\nl\n\n\3\13\3")
        buf.write("\13\3\13\3\13\5\13r\n\13\3\f\3\f\5\fv\n\f\3\r\3\r\3\r")
        buf.write("\3\r\5\r|\n\r\3\16\3\16\3\16\3\16\5\16\u0082\n\16\3\17")
        buf.write("\3\17\3\17\3\17\5\17\u0088\n\17\3\20\3\20\5\20\u008c\n")
        buf.write("\20\3\20\3\20\5\20\u0090\n\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\5\22\u00a2\n\22\3\23\3\23\3\24\3\24\5\24\u00a8\n\24\3")
        buf.write("\25\3\25\3\25\3\25\3\25\5\25\u00af\n\25\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\5\27\u00b8\n\27\3\30\3\30\3\30\3")
        buf.write("\30\3\30\5\30\u00bf\n\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\7\31\u00c7\n\31\f\31\16\31\u00ca\13\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\7\32\u00d2\n\32\f\32\16\32\u00d5\13\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\7\33\u00dd\n\33\f\33\16")
        buf.write("\33\u00e0\13\33\3\34\3\34\3\34\5\34\u00e5\n\34\3\35\3")
        buf.write("\35\3\35\5\35\u00ea\n\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\5\36\u00f2\n\36\3\37\3\37\3\37\2\5\60\62\64 \2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write(":<\2\t\6\2\13\13\16\16\21\21\23\23\7\2\t\t\13\f\16\16")
        buf.write("\21\21\23\23\4\2!$()\3\2&\'\3\2\34\35\3\2\36 \4\2\4\5")
        buf.write("\7\7\2\u00ef\2?\3\2\2\2\4H\3\2\2\2\6J\3\2\2\2\bQ\3\2\2")
        buf.write("\2\nU\3\2\2\2\f[\3\2\2\2\16]\3\2\2\2\20b\3\2\2\2\22k\3")
        buf.write("\2\2\2\24q\3\2\2\2\26u\3\2\2\2\30{\3\2\2\2\32\u0081\3")
        buf.write("\2\2\2\34\u0087\3\2\2\2\36\u008b\3\2\2\2 \u0095\3\2\2")
        buf.write("\2\"\u00a1\3\2\2\2$\u00a3\3\2\2\2&\u00a7\3\2\2\2(\u00ae")
        buf.write("\3\2\2\2*\u00b0\3\2\2\2,\u00b7\3\2\2\2.\u00be\3\2\2\2")
        buf.write("\60\u00c0\3\2\2\2\62\u00cb\3\2\2\2\64\u00d6\3\2\2\2\66")
        buf.write("\u00e4\3\2\2\28\u00e9\3\2\2\2:\u00f1\3\2\2\2<\u00f3\3")
        buf.write("\2\2\2>@\5\4\3\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2AB\3\2\2")
        buf.write("\2BC\3\2\2\2CD\7\2\2\3D\3\3\2\2\2EI\5\6\4\2FI\5\20\t\2")
        buf.write("GI\5 \21\2HE\3\2\2\2HF\3\2\2\2HG\3\2\2\2I\5\3\2\2\2JK")
        buf.write("\7\r\2\2KL\7\62\2\2LM\5\n\6\2MN\7\63\2\2NO\7\27\2\2OP")
        buf.write("\5\b\5\2P\7\3\2\2\2QR\t\2\2\2R\t\3\2\2\2SV\5\f\7\2TV\5")
        buf.write("\16\b\2US\3\2\2\2UT\3\2\2\2V\13\3\2\2\2WX\7\4\2\2XY\7")
        buf.write(",\2\2Y\\\5\f\7\2Z\\\7\4\2\2[W\3\2\2\2[Z\3\2\2\2\\\r\3")
        buf.write("\2\2\2]^\7\5\2\2^_\7,\2\2_`\5\16\b\2`a\7\5\2\2a\17\3\2")
        buf.write("\2\2bc\5\24\13\2cd\7/\2\2de\5\b\5\2ef\5\22\n\2fg\7-\2")
        buf.write("\2g\21\3\2\2\2hi\7.\2\2il\5\26\f\2jl\3\2\2\2kh\3\2\2\2")
        buf.write("kj\3\2\2\2l\23\3\2\2\2mn\7\66\2\2no\7,\2\2or\5\24\13\2")
        buf.write("pr\7\66\2\2qm\3\2\2\2qp\3\2\2\2r\25\3\2\2\2sv\5\30\r\2")
        buf.write("tv\5\32\16\2us\3\2\2\2ut\3\2\2\2v\27\3\2\2\2wx\7\4\2\2")
        buf.write("xy\7,\2\2y|\5\30\r\2z|\7\4\2\2{w\3\2\2\2{z\3\2\2\2|\31")
        buf.write("\3\2\2\2}~\7\5\2\2~\177\7,\2\2\177\u0082\5\32\16\2\u0080")
        buf.write("\u0082\7\5\2\2\u0081}\3\2\2\2\u0081\u0080\3\2\2\2\u0082")
        buf.write("\33\3\2\2\2\u0083\u0084\7\7\2\2\u0084\u0085\7,\2\2\u0085")
        buf.write("\u0088\5\34\17\2\u0086\u0088\7\7\2\2\u0087\u0083\3\2\2")
        buf.write("\2\u0087\u0086\3\2\2\2\u0088\35\3\2\2\2\u0089\u008c\7")
        buf.write("\33\2\2\u008a\u008c\3\2\2\2\u008b\u0089\3\2\2\2\u008b")
        buf.write("\u008a\3\2\2\2\u008c\u008f\3\2\2\2\u008d\u0090\7\20\2")
        buf.write("\2\u008e\u0090\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u008e")
        buf.write("\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0092\7\66\2\2\u0092")
        buf.write("\u0093\7/\2\2\u0093\u0094\5\b\5\2\u0094\37\3\2\2\2\u0095")
        buf.write("\u0096\7\66\2\2\u0096\u0097\7/\2\2\u0097\u0098\7\26\2")
        buf.write("\2\u0098\u0099\5*\26\2\u0099\u009a\7\60\2\2\u009a\u009b")
        buf.write("\5&\24\2\u009b\u009c\7\61\2\2\u009c\u009d\5\"\22\2\u009d")
        buf.write("!\3\2\2\2\u009e\u009f\7\33\2\2\u009f\u00a2\5$\23\2\u00a0")
        buf.write("\u00a2\3\2\2\2\u00a1\u009e\3\2\2\2\u00a1\u00a0\3\2\2\2")
        buf.write("\u00a2#\3\2\2\2\u00a3\u00a4\7\66\2\2\u00a4%\3\2\2\2\u00a5")
        buf.write("\u00a8\5(\25\2\u00a6\u00a8\3\2\2\2\u00a7\u00a5\3\2\2\2")
        buf.write("\u00a7\u00a6\3\2\2\2\u00a8\'\3\2\2\2\u00a9\u00aa\5\36")
        buf.write("\20\2\u00aa\u00ab\7,\2\2\u00ab\u00ac\5(\25\2\u00ac\u00af")
        buf.write("\3\2\2\2\u00ad\u00af\5\36\20\2\u00ae\u00a9\3\2\2\2\u00ae")
        buf.write("\u00ad\3\2\2\2\u00af)\3\2\2\2\u00b0\u00b1\t\3\2\2\u00b1")
        buf.write("+\3\2\2\2\u00b2\u00b3\5.\30\2\u00b3\u00b4\7*\2\2\u00b4")
        buf.write("\u00b5\5.\30\2\u00b5\u00b8\3\2\2\2\u00b6\u00b8\5.\30\2")
        buf.write("\u00b7\u00b2\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8-\3\2\2")
        buf.write("\2\u00b9\u00ba\5\60\31\2\u00ba\u00bb\t\4\2\2\u00bb\u00bc")
        buf.write("\5\60\31\2\u00bc\u00bf\3\2\2\2\u00bd\u00bf\5\60\31\2\u00be")
        buf.write("\u00b9\3\2\2\2\u00be\u00bd\3\2\2\2\u00bf/\3\2\2\2\u00c0")
        buf.write("\u00c1\b\31\1\2\u00c1\u00c2\5\62\32\2\u00c2\u00c8\3\2")
        buf.write("\2\2\u00c3\u00c4\f\4\2\2\u00c4\u00c5\t\5\2\2\u00c5\u00c7")
        buf.write("\5\62\32\2\u00c6\u00c3\3\2\2\2\u00c7\u00ca\3\2\2\2\u00c8")
        buf.write("\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\61\3\2\2\2\u00ca")
        buf.write("\u00c8\3\2\2\2\u00cb\u00cc\b\32\1\2\u00cc\u00cd\5\64\33")
        buf.write("\2\u00cd\u00d3\3\2\2\2\u00ce\u00cf\f\4\2\2\u00cf\u00d0")
        buf.write("\t\6\2\2\u00d0\u00d2\5\64\33\2\u00d1\u00ce\3\2\2\2\u00d2")
        buf.write("\u00d5\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2")
        buf.write("\u00d4\63\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d6\u00d7\b\33")
        buf.write("\1\2\u00d7\u00d8\5\66\34\2\u00d8\u00de\3\2\2\2\u00d9\u00da")
        buf.write("\f\4\2\2\u00da\u00db\t\7\2\2\u00db\u00dd\5\66\34\2\u00dc")
        buf.write("\u00d9\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de\u00dc\3\2\2\2")
        buf.write("\u00de\u00df\3\2\2\2\u00df\65\3\2\2\2\u00e0\u00de\3\2")
        buf.write("\2\2\u00e1\u00e2\7%\2\2\u00e2\u00e5\5\66\34\2\u00e3\u00e5")
        buf.write("\58\35\2\u00e4\u00e1\3\2\2\2\u00e4\u00e3\3\2\2\2\u00e5")
        buf.write("\67\3\2\2\2\u00e6\u00e7\7\35\2\2\u00e7\u00ea\58\35\2\u00e8")
        buf.write("\u00ea\5:\36\2\u00e9\u00e6\3\2\2\2\u00e9\u00e8\3\2\2\2")
        buf.write("\u00ea9\3\2\2\2\u00eb\u00ec\7\66\2\2\u00ec\u00ed\7\62")
        buf.write("\2\2\u00ed\u00ee\5\30\r\2\u00ee\u00ef\7\63\2\2\u00ef\u00f2")
        buf.write("\3\2\2\2\u00f0\u00f2\5<\37\2\u00f1\u00eb\3\2\2\2\u00f1")
        buf.write("\u00f0\3\2\2\2\u00f2;\3\2\2\2\u00f3\u00f4\t\b\2\2\u00f4")
        buf.write("=\3\2\2\2\31AHU[kqu{\u0081\u0087\u008b\u008f\u00a1\u00a7")
        buf.write("\u00ae\u00b7\u00be\u00c8\u00d3\u00de\u00e4\u00e9\u00f1")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'auto'", "'break'", 
                     "'integer'", "'void'", "'array'", "'float'", "'return'", 
                     "'out'", "'boolean'", "'for'", "'string'", "'continue'", 
                     "'do'", "'function'", "'of'", "'else'", "'if'", "'while'", 
                     "'inherit'", "'+'", "'-'", "'*'", "'/'", "'%'", "'<'", 
                     "'>'", "'<='", "'>='", "'!'", "'&&'", "'||'", "'=='", 
                     "'!='", "'::'", "'.'", "','", "';'", "'='", "':'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "INTEGER_LIT", "FLOAT_LIT", 
                      "BOOLEAN_LIT", "STRING_LIT", "ARRAY_LIT", "AUTO", 
                      "BREAK", "INTEGER", "VOID", "ARRAY", "FLOAT", "RETURN", 
                      "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", 
                      "FUNCTION", "OF", "ELSE", "IF", "WHILE", "INHERIT", 
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
    RULE_equal_exp = 8
    RULE_identifier_list = 9
    RULE_expression_list = 10
    RULE_exp_list_type_int = 11
    RULE_exp_list_type_float = 12
    RULE_exp_list_type_string = 13
    RULE_parameter = 14
    RULE_function_decl = 15
    RULE_inheritance = 16
    RULE_function_name = 17
    RULE_paramter_list = 18
    RULE_paramter_list_term = 19
    RULE_return_type = 20
    RULE_expression = 21
    RULE_expression_1 = 22
    RULE_expression_2 = 23
    RULE_expression_3 = 24
    RULE_expression_4 = 25
    RULE_expression_5 = 26
    RULE_expression_6 = 27
    RULE_expression_7 = 28
    RULE_factor = 29

    ruleNames =  [ "program", "decls", "array_type", "element_type", "dimesion", 
                   "dimesion_type_int", "dimesion_type_float", "variable_decl", 
                   "equal_exp", "identifier_list", "expression_list", "exp_list_type_int", 
                   "exp_list_type_float", "exp_list_type_string", "parameter", 
                   "function_decl", "inheritance", "function_name", "paramter_list", 
                   "paramter_list_term", "return_type", "expression", "expression_1", 
                   "expression_2", "expression_3", "expression_4", "expression_5", 
                   "expression_6", "expression_7", "factor" ]

    EOF = Token.EOF
    COMMENT=1
    INTEGER_LIT=2
    FLOAT_LIT=3
    BOOLEAN_LIT=4
    STRING_LIT=5
    ARRAY_LIT=6
    AUTO=7
    BREAK=8
    INTEGER=9
    VOID=10
    ARRAY=11
    FLOAT=12
    RETURN=13
    OUT=14
    BOOLEAN=15
    FOR=16
    STRING=17
    CONTINUE=18
    DO=19
    FUNCTION=20
    OF=21
    ELSE=22
    IF=23
    WHILE=24
    INHERIT=25
    PLUS=26
    MINUS=27
    MUL=28
    DIV=29
    MOD=30
    LESS=31
    GREATER=32
    LTE=33
    GTE=34
    NOT=35
    AND=36
    OR=37
    EQUAL_TO=38
    NOT_EQUAL=39
    CONCAT=40
    PERIOD=41
    COMMA=42
    SEMI=43
    EQUAL=44
    COLON=45
    LB=46
    RB=47
    LSB=48
    RSB=49
    LCB=50
    RCB=51
    IDENTIFIER=52
    WS=53
    UNCLOSE_STRING=54
    ILLEGAL_ESCAPE=55
    ERROR_CHAR=56

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
            return self.getToken(MT22Parser.EOF, 0)

        def decls(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.DeclsContext)
            else:
                return self.getTypedRuleContext(MT22Parser.DeclsContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_program




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60
                self.decls()
                self.state = 63 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MT22Parser.ARRAY or _la==MT22Parser.IDENTIFIER):
                    break

            self.state = 65
            self.match(MT22Parser.EOF)
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
            return self.getTypedRuleContext(MT22Parser.Array_typeContext,0)


        def variable_decl(self):
            return self.getTypedRuleContext(MT22Parser.Variable_declContext,0)


        def function_decl(self):
            return self.getTypedRuleContext(MT22Parser.Function_declContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decls




    def decls(self):

        localctx = MT22Parser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.array_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.variable_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 69
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
            return self.getToken(MT22Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def dimesion(self):
            return self.getTypedRuleContext(MT22Parser.DimesionContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def OF(self):
            return self.getToken(MT22Parser.OF, 0)

        def element_type(self):
            return self.getTypedRuleContext(MT22Parser.Element_typeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_array_type




    def array_type(self):

        localctx = MT22Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(MT22Parser.ARRAY)
            self.state = 73
            self.match(MT22Parser.LSB)
            self.state = 74
            self.dimesion()
            self.state = 75
            self.match(MT22Parser.RSB)
            self.state = 76
            self.match(MT22Parser.OF)
            self.state = 77
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
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_element_type




    def element_type(self):

        localctx = MT22Parser.Element_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_element_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTEGER) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.STRING))) != 0)):
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
            return self.getTypedRuleContext(MT22Parser.Dimesion_type_intContext,0)


        def dimesion_type_float(self):
            return self.getTypedRuleContext(MT22Parser.Dimesion_type_floatContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_dimesion




    def dimesion(self):

        localctx = MT22Parser.DimesionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dimesion)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INTEGER_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.dimesion_type_int()
                pass
            elif token in [MT22Parser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
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
            return self.getToken(MT22Parser.INTEGER_LIT, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def dimesion_type_int(self):
            return self.getTypedRuleContext(MT22Parser.Dimesion_type_intContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_dimesion_type_int




    def dimesion_type_int(self):

        localctx = MT22Parser.Dimesion_type_intContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_dimesion_type_int)
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.match(MT22Parser.INTEGER_LIT)
                self.state = 86
                self.match(MT22Parser.COMMA)
                self.state = 87
                self.dimesion_type_int()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.match(MT22Parser.INTEGER_LIT)
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
                return self.getTokens(MT22Parser.FLOAT_LIT)
            else:
                return self.getToken(MT22Parser.FLOAT_LIT, i)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def dimesion_type_float(self):
            return self.getTypedRuleContext(MT22Parser.Dimesion_type_floatContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_dimesion_type_float




    def dimesion_type_float(self):

        localctx = MT22Parser.Dimesion_type_floatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_dimesion_type_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(MT22Parser.FLOAT_LIT)
            self.state = 92
            self.match(MT22Parser.COMMA)
            self.state = 93
            self.dimesion_type_float()
            self.state = 94
            self.match(MT22Parser.FLOAT_LIT)
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
            return self.getTypedRuleContext(MT22Parser.Identifier_listContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def element_type(self):
            return self.getTypedRuleContext(MT22Parser.Element_typeContext,0)


        def equal_exp(self):
            return self.getTypedRuleContext(MT22Parser.Equal_expContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_variable_decl




    def variable_decl(self):

        localctx = MT22Parser.Variable_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variable_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.identifier_list()
            self.state = 97
            self.match(MT22Parser.COLON)
            self.state = 98
            self.element_type()
            self.state = 99
            self.equal_exp()
            self.state = 100
            self.match(MT22Parser.SEMI)
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
            return self.getToken(MT22Parser.EQUAL, 0)

        def expression_list(self):
            return self.getTypedRuleContext(MT22Parser.Expression_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_equal_exp




    def equal_exp(self):

        localctx = MT22Parser.Equal_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_equal_exp)
        try:
            self.state = 105
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.EQUAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.match(MT22Parser.EQUAL)
                self.state = 103
                self.expression_list()
                pass
            elif token in [MT22Parser.SEMI]:
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
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def identifier_list(self):
            return self.getTypedRuleContext(MT22Parser.Identifier_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_identifier_list




    def identifier_list(self):

        localctx = MT22Parser.Identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_identifier_list)
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.match(MT22Parser.IDENTIFIER)
                self.state = 108
                self.match(MT22Parser.COMMA)
                self.state = 109
                self.identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.match(MT22Parser.IDENTIFIER)
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
            return self.getTypedRuleContext(MT22Parser.Exp_list_type_intContext,0)


        def exp_list_type_float(self):
            return self.getTypedRuleContext(MT22Parser.Exp_list_type_floatContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expression_list




    def expression_list(self):

        localctx = MT22Parser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expression_list)
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INTEGER_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.exp_list_type_int()
                pass
            elif token in [MT22Parser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
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
            return self.getToken(MT22Parser.INTEGER_LIT, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def exp_list_type_int(self):
            return self.getTypedRuleContext(MT22Parser.Exp_list_type_intContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exp_list_type_int




    def exp_list_type_int(self):

        localctx = MT22Parser.Exp_list_type_intContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_exp_list_type_int)
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.match(MT22Parser.INTEGER_LIT)
                self.state = 118
                self.match(MT22Parser.COMMA)
                self.state = 119
                self.exp_list_type_int()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.match(MT22Parser.INTEGER_LIT)
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
            return self.getToken(MT22Parser.FLOAT_LIT, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def exp_list_type_float(self):
            return self.getTypedRuleContext(MT22Parser.Exp_list_type_floatContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exp_list_type_float




    def exp_list_type_float(self):

        localctx = MT22Parser.Exp_list_type_floatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exp_list_type_float)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.match(MT22Parser.FLOAT_LIT)
                self.state = 124
                self.match(MT22Parser.COMMA)
                self.state = 125
                self.exp_list_type_float()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.match(MT22Parser.FLOAT_LIT)
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
            return self.getToken(MT22Parser.STRING_LIT, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def exp_list_type_string(self):
            return self.getTypedRuleContext(MT22Parser.Exp_list_type_stringContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exp_list_type_string




    def exp_list_type_string(self):

        localctx = MT22Parser.Exp_list_type_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_exp_list_type_string)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.match(MT22Parser.STRING_LIT)
                self.state = 130
                self.match(MT22Parser.COMMA)
                self.state = 131
                self.exp_list_type_string()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.match(MT22Parser.STRING_LIT)
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
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def element_type(self):
            return self.getTypedRuleContext(MT22Parser.Element_typeContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def OUT(self):
            return self.getToken(MT22Parser.OUT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_parameter




    def parameter(self):

        localctx = MT22Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INHERIT]:
                self.state = 135
                self.match(MT22Parser.INHERIT)
                pass
            elif token in [MT22Parser.OUT, MT22Parser.IDENTIFIER]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.OUT]:
                self.state = 139
                self.match(MT22Parser.OUT)
                pass
            elif token in [MT22Parser.IDENTIFIER]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 143
            self.match(MT22Parser.IDENTIFIER)
            self.state = 144
            self.match(MT22Parser.COLON)
            self.state = 145
            self.element_type()
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
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def return_type(self):
            return self.getTypedRuleContext(MT22Parser.Return_typeContext,0)


        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def paramter_list(self):
            return self.getTypedRuleContext(MT22Parser.Paramter_listContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def inheritance(self):
            return self.getTypedRuleContext(MT22Parser.InheritanceContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_function_decl




    def function_decl(self):

        localctx = MT22Parser.Function_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_function_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(MT22Parser.IDENTIFIER)
            self.state = 148
            self.match(MT22Parser.COLON)
            self.state = 149
            self.match(MT22Parser.FUNCTION)
            self.state = 150
            self.return_type()
            self.state = 151
            self.match(MT22Parser.LB)
            self.state = 152
            self.paramter_list()
            self.state = 153
            self.match(MT22Parser.RB)
            self.state = 154
            self.inheritance()
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
            return self.getToken(MT22Parser.INHERIT, 0)

        def function_name(self):
            return self.getTypedRuleContext(MT22Parser.Function_nameContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_inheritance




    def inheritance(self):

        localctx = MT22Parser.InheritanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_inheritance)
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INHERIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.match(MT22Parser.INHERIT)
                self.state = 157
                self.function_name()
                pass
            elif token in [MT22Parser.EOF, MT22Parser.ARRAY, MT22Parser.IDENTIFIER]:
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
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_function_name




    def function_name(self):

        localctx = MT22Parser.Function_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_function_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(MT22Parser.IDENTIFIER)
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
            return self.getTypedRuleContext(MT22Parser.Paramter_list_termContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_paramter_list




    def paramter_list(self):

        localctx = MT22Parser.Paramter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_paramter_list)
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.OUT, MT22Parser.INHERIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.paramter_list_term()
                pass
            elif token in [MT22Parser.RB]:
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
            return self.getTypedRuleContext(MT22Parser.ParameterContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def paramter_list_term(self):
            return self.getTypedRuleContext(MT22Parser.Paramter_list_termContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_paramter_list_term




    def paramter_list_term(self):

        localctx = MT22Parser.Paramter_list_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_paramter_list_term)
        try:
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.parameter()
                self.state = 168
                self.match(MT22Parser.COMMA)
                self.state = 169
                self.paramter_list_term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
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
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_return_type




    def return_type(self):

        localctx = MT22Parser.Return_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_return_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.AUTO) | (1 << MT22Parser.INTEGER) | (1 << MT22Parser.VOID) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.STRING))) != 0)):
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


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expression_1Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expression_1Context,i)


        def CONCAT(self):
            return self.getToken(MT22Parser.CONCAT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expression




    def expression(self):

        localctx = MT22Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expression)
        try:
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.expression_1()
                self.state = 177
                self.match(MT22Parser.CONCAT)
                self.state = 178
                self.expression_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
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
                return self.getTypedRuleContexts(MT22Parser.Expression_2Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expression_2Context,i)


        def EQUAL_TO(self):
            return self.getToken(MT22Parser.EQUAL_TO, 0)

        def NOT_EQUAL(self):
            return self.getToken(MT22Parser.NOT_EQUAL, 0)

        def LESS(self):
            return self.getToken(MT22Parser.LESS, 0)

        def GREATER(self):
            return self.getToken(MT22Parser.GREATER, 0)

        def LTE(self):
            return self.getToken(MT22Parser.LTE, 0)

        def GTE(self):
            return self.getToken(MT22Parser.GTE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expression_1




    def expression_1(self):

        localctx = MT22Parser.Expression_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expression_1)
        self._la = 0 # Token type
        try:
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.expression_2(0)
                self.state = 184
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.LESS) | (1 << MT22Parser.GREATER) | (1 << MT22Parser.LTE) | (1 << MT22Parser.GTE) | (1 << MT22Parser.EQUAL_TO) | (1 << MT22Parser.NOT_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 185
                self.expression_2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
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
            return self.getTypedRuleContext(MT22Parser.Expression_3Context,0)


        def expression_2(self):
            return self.getTypedRuleContext(MT22Parser.Expression_2Context,0)


        def AND(self):
            return self.getToken(MT22Parser.AND, 0)

        def OR(self):
            return self.getToken(MT22Parser.OR, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expression_2



    def expression_2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expression_2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expression_2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.expression_3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 198
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expression_2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_2)
                    self.state = 193
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 194
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.AND or _la==MT22Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 195
                    self.expression_3(0) 
                self.state = 200
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
            return self.getTypedRuleContext(MT22Parser.Expression_4Context,0)


        def expression_3(self):
            return self.getTypedRuleContext(MT22Parser.Expression_3Context,0)


        def PLUS(self):
            return self.getToken(MT22Parser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MT22Parser.MINUS, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expression_3



    def expression_3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expression_3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expression_3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.expression_4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 209
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expression_3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_3)
                    self.state = 204
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 205
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.PLUS or _la==MT22Parser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 206
                    self.expression_4(0) 
                self.state = 211
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
            return self.getTypedRuleContext(MT22Parser.Expression_5Context,0)


        def expression_4(self):
            return self.getTypedRuleContext(MT22Parser.Expression_4Context,0)


        def MUL(self):
            return self.getToken(MT22Parser.MUL, 0)

        def DIV(self):
            return self.getToken(MT22Parser.DIV, 0)

        def MOD(self):
            return self.getToken(MT22Parser.MOD, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expression_4



    def expression_4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expression_4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expression_4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.expression_5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 220
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expression_4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression_4)
                    self.state = 215
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 216
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MUL) | (1 << MT22Parser.DIV) | (1 << MT22Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 217
                    self.expression_5() 
                self.state = 222
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
            return self.getToken(MT22Parser.NOT, 0)

        def expression_5(self):
            return self.getTypedRuleContext(MT22Parser.Expression_5Context,0)


        def expression_6(self):
            return self.getTypedRuleContext(MT22Parser.Expression_6Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expression_5




    def expression_5(self):

        localctx = MT22Parser.Expression_5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expression_5)
        try:
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.match(MT22Parser.NOT)
                self.state = 224
                self.expression_5()
                pass
            elif token in [MT22Parser.INTEGER_LIT, MT22Parser.FLOAT_LIT, MT22Parser.STRING_LIT, MT22Parser.MINUS, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
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
            return self.getToken(MT22Parser.MINUS, 0)

        def expression_6(self):
            return self.getTypedRuleContext(MT22Parser.Expression_6Context,0)


        def expression_7(self):
            return self.getTypedRuleContext(MT22Parser.Expression_7Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expression_6




    def expression_6(self):

        localctx = MT22Parser.Expression_6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expression_6)
        try:
            self.state = 231
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.match(MT22Parser.MINUS)
                self.state = 229
                self.expression_6()
                pass
            elif token in [MT22Parser.INTEGER_LIT, MT22Parser.FLOAT_LIT, MT22Parser.STRING_LIT, MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.expression_7()
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

        def IDENTIFIER(self):
            return self.getToken(MT22Parser.IDENTIFIER, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def exp_list_type_int(self):
            return self.getTypedRuleContext(MT22Parser.Exp_list_type_intContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def factor(self):
            return self.getTypedRuleContext(MT22Parser.FactorContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expression_7




    def expression_7(self):

        localctx = MT22Parser.Expression_7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expression_7)
        try:
            self.state = 239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.match(MT22Parser.IDENTIFIER)
                self.state = 234
                self.match(MT22Parser.LSB)
                self.state = 235
                self.exp_list_type_int()
                self.state = 236
                self.match(MT22Parser.RSB)
                pass
            elif token in [MT22Parser.INTEGER_LIT, MT22Parser.FLOAT_LIT, MT22Parser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
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
            return self.getToken(MT22Parser.INTEGER_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MT22Parser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MT22Parser.STRING_LIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_factor




    def factor(self):

        localctx = MT22Parser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTEGER_LIT) | (1 << MT22Parser.FLOAT_LIT) | (1 << MT22Parser.STRING_LIT))) != 0)):
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
        self._predicates[23] = self.expression_2_sempred
        self._predicates[24] = self.expression_3_sempred
        self._predicates[25] = self.expression_4_sempred
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
         




