# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3,")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\2\2\3\5\3\3\2\2\2\2")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'auto'", "'break'", "'integer'", "'void'", 
                     "'array'", "'float'", "'return'", "'out'", "'boolean'", 
                     "'for'", "'string'", "'continue'", "'do'", "'function'", 
                     "'of'", "'else'", "'if'", "'while'", "'inherit'", "'&&'", 
                     "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'::'", "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "INTEGER_LIT", "FLOAT_LIT", "BOOLEAN_LIT", 
                      "STRING_LIT", "AUTO", "BREAK", "INTEGER", "VOID", 
                      "ARRAY", "FLOAT", "RETURN", "OUT", "BOOLEAN", "FOR", 
                      "STRING", "CONTINUE", "DO", "FUNCTION", "OF", "ELSE", 
                      "IF", "WHILE", "INHERIT", "AND", "OR", "EQUAL_TO", 
                      "NOT_EQUAL", "LESS", "GREATER", "LESS_THAN_OR_EQUAL", 
                      "GREATER_THAN_OR_EQUAL", "SCOPE_RES", "LB", "RB", 
                      "LSB", "RSB", "LCB", "RCB", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    INTEGER_LIT=1
    FLOAT_LIT=2
    BOOLEAN_LIT=3
    STRING_LIT=4
    AUTO=5
    BREAK=6
    INTEGER=7
    VOID=8
    ARRAY=9
    FLOAT=10
    RETURN=11
    OUT=12
    BOOLEAN=13
    FOR=14
    STRING=15
    CONTINUE=16
    DO=17
    FUNCTION=18
    OF=19
    ELSE=20
    IF=21
    WHILE=22
    INHERIT=23
    AND=24
    OR=25
    EQUAL_TO=26
    NOT_EQUAL=27
    LESS=28
    GREATER=29
    LESS_THAN_OR_EQUAL=30
    GREATER_THAN_OR_EQUAL=31
    SCOPE_RES=32
    LB=33
    RB=34
    LSB=35
    RSB=36
    LCB=37
    RCB=38
    WS=39
    ERROR_CHAR=40
    UNCLOSE_STRING=41
    ILLEGAL_ESCAPE=42

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

        def getRuleIndex(self):
            return MT22Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





