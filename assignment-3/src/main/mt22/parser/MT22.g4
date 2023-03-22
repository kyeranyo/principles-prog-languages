/*
 ID: 2013381
 Author: Hồ Đức Hưng 
 Email: hung.hoduccse@hcmut.edu.vn
 */

grammar MT22
;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: decls+ EOF;

decls: vardecl | funcdecl;

// Array type -------------------------------------------------------------
arraytype: ARRAY LSB dimension RSB OF eletype;

number: INTLIT | FLOATLIT;
eletype: INTEGER | FLOAT | BOOLEAN | STRING | AUTO;
dimension: INTLIT COMMA dimension | INTLIT;

//Variables ---------------------------------------------------------------
vardecl: vardeclNoEq | vardeclEq;

vardeclNoEq: idlist COLON (eletype | arraytype) SEMI;

// remove arraytype
// vardeclEq
// 	: IDENTIFIER (COMMA assignRecur | COLON (eletype) EQUAL) expr SEMI
// ;
vardeclEq
	: IDENTIFIER COMMA assignment COMMA expr SEMI
	| IDENTIFIER COLON (eletype | arraytype) EQUAL expr SEMI
;
assignment
	: IDENTIFIER COMMA assignment COMMA expr
	| IDENTIFIER COLON (eletype | arraytype) EQUAL expr
;

// assignRecur
// 	: IDENTIFIER (COMMA assignRecur | COLON (eletype) EQUAL) expr COMMA
// ;

arraylit: LCB (exprlist |) RCB;
idlist: IDENTIFIER COMMA idlist | IDENTIFIER;
exprlist: expr COMMA exprlist | expr;

//Parameters ----------------------------------------------------------------
parameter
	: (INHERIT |) (OUT |) IDENTIFIER COLON (eletype | arraytype)
;

// expression declarations --------------------------------------------------
expr: expr1 CONCAT expr1 | expr1;

expr1: expr2 compare expr2 | expr2;
compare: EQUAL_TO | NOT_EQUAL | LESS | GREATER | LTE | GTE;

expr2: expr2 (AND | OR) expr3 | expr3;

expr3: expr3 (PLUS | MINUS) expr4 | expr4;

expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;

expr5: NOT expr5 | expr6;

expr6: MINUS expr6 | expr7;

expr7: IDENTIFIER LSB exprlist RSB | expr8;

expr8: (LB expr RB) | factor;

factor
	: INTLIT
	| FLOATLIT
	| STRINGLIT
	| IDENTIFIER
	| funccall
	| arraylit
	| BOOLEANLIT
;

arrayCell: IDENTIFIER LSB exprlist RSB;
// function call ------------------------------------------------------------
funccall: (IDENTIFIER LB (exprlist |) RB) | sfuncdecl;

// statement ----------------------------------------------------------------
stmt
	: assignStmt
	| ifStmt
	| forStmt
	| whileStmt
	| doWhileStmt
	| returnStmt
	| continueStmt
	| blockStmt
	| breakStmt
	| callStmt
	| vardecl
;

stmtlocal: stmt | blockStmt;

// assignment statement ------------------------------------------------------
assignStmt: lhs EQUAL expr SEMI;
lhs: IDENTIFIER LSB exprlist RSB | IDENTIFIER;

// if statement --------------------------------------------------------------
ifStmt:  IF LB expr RB stmt | (IF LB expr RB stmt ELSE stmt);

// for statement -------------------------------------------------------------
forStmt
	: FOR LB initExpr COMMA conditionExpr COMMA updateExpr RB stmt
;

initExpr: IDENTIFIER EQUAL expr;

conditionExpr: (expr operator expr) | BOOLEANLIT;
operator: LESS | GREATER | LTE | GTE | NOT_EQUAL | EQUAL_TO;

updateExpr: expr;

// while statement ------------------------------------------------------------
whileStmt: WHILE LB expr RB stmt;

// Do while statement ---------------------------------------------------------
doWhileStmt: DO blockStmt WHILE LB expr RB SEMI;

// call statement -------------------------------------------------------------
callStmt: (sfuncdecl | (IDENTIFIER LB (exprlist |) RB)) SEMI;

// block statement ------------------------------------------------------------
blockStmt: LCB stmtTerm RCB;
stmtTerm: stmtList |;
stmtList: stmt stmtList | stmt;

//break statement -------------------------------------------------------------
breakStmt: BREAK SEMI;

// continue statement ---------------------------------------------------------
continueStmt: CONTINUE SEMI;

// return statement -----------------------------------------------------------
returnStmt: RETURN (expr |) SEMI;

// Function declarations ------------------------------------------------------
funcdecl
	: IDENTIFIER COLON FUNCTION returnType LB paramterList RB inheritance blockStmt
;

inheritance: INHERIT IDENTIFIER |;
paramterList: paramterListTerm |;
paramterListTerm: parameter COMMA paramterListTerm | parameter;
returnType
	: INTEGER
	| FLOAT
	| BOOLEAN
	| STRING
	| VOID
	| AUTO
	| arraytype
;

// Special Functions ------------------------------------------------------------
sfuncdecl
	: readInteger
	| readFloat
	| printInteger
	| writeFloat
	| printBoolean
	| readString
	| printString
	| superCall
	| preventDefault
;

readInteger: READINTEGER LB RB;
printInteger: PRINTINTEGER LB expr RB;
readFloat: READFLOAT LB RB;
writeFloat: WRITEFLOAT LB expr RB;
printBoolean: PRINTBOOLEAN LB expr RB;
readString: READSTRING LB RB;
printString: PRINTSTRING LB expr RB;
superCall: SUPER LB exprlist RB;
preventDefault: PREVENTDEFAULT LB RB;

PREVENTDEFAULT: 'preventDefault';
SUPER: 'super';
PRINTSTRING: 'printString';
READSTRING: 'readString';
PRINTBOOLEAN: 'printBoolean';
WRITEFLOAT: 'writeFloat';
READFLOAT: 'readFloat';
PRINTINTEGER: 'printInteger';
READINTEGER: 'readInteger';

/* --------------------------------------TOKEN---------------------------------*/
COMMENT: (SingleLineComment | MultiLineComment) -> skip;
fragment SingleLineComment: '//' ~('\r' | '\n')*;
fragment MultiLineComment: '/*' .*? '*/';
fragment CommentAll: '/*' .*? EOF;

INTLIT
	: '0'
	| [1-9][0-9]* (UNDERSCORE [0-9]+)* {self.text = self.text.replace("_","")}
;

fragment UNDERSCORE: '_';

FLOATLIT
	: (
		INTLIT DECPART EXPPART
		| INTLIT DECPART
		| INTLIT EXPPART
		| DECPART EXPPART
	) {self.text = self.text.replace("_","")}
;
fragment DECPART: PERIOD [0-9]*;
fragment EXPPART: [eE] [-+]? [0-9]+;

BOOLEANLIT: FALSE | TRUE;
fragment FALSE: 'false';
fragment TRUE: 'true';

STRINGLIT
	: DUO_QUOTE (ESC | ~[\n\r"])* DUO_QUOTE {self.text=str(self.text[1:-1])}
;
fragment NOTESC
	: '\\' ~('b' | 'f' | 'n' | 'r' | 't' | '"' | '\'' | '\\')
;
fragment ESC
	: '\\' ('b' | 'f' | 'n' | 'r' | 't' | '\'' | '\\' | '"')
;
fragment AllEscSeq: '\\' ~["];
fragment DUO_QUOTE: ["];
fragment SINGLE_QUOTE: ['];

AUTO: 'auto';
BREAK: 'break';
INTEGER: 'integer';
VOID: 'void';
ARRAY: 'array';
FLOAT: 'float';
RETURN: 'return';
OUT: 'out';
BOOLEAN: 'boolean';
FOR: 'for';
STRING: 'string';
CONTINUE: 'continue';
DO: 'do';
FUNCTION: 'function';
OF: 'of';
ELSE: 'else';
IF: 'if';
WHILE: 'while';
INHERIT: 'inherit';

PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
LESS: '<';
GREATER: '>';
LTE: '<=';
GTE: '>=';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL_TO: '==';
NOT_EQUAL: '!=';

CONCAT: '::';
PERIOD: '.';
COMMA: ',';
SEMI: ';';
EQUAL: '=';
COLON: ':';
LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
LCB: '{';
RCB: '}';

IDENTIFIER: [a-zA-Z_]+ [a-zA-Z0-9_]*;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

UNCLOSE_STRING
	: DUO_QUOTE (~["] | ESC)*? ([\r\n] | EOF) {
s = self.text
if s[len(s) - 1] == '\n' or s[len(s) - 1] == '\r':
    raise UncloseString(self.text[1:-1])
raise UncloseString(self.text[1:])
}
;
ILLEGAL_ESCAPE
	: DUO_QUOTE (~[\\"] | ESC)* NOTESC {raise IllegalEscape(self.text[1:])
		}
;
ERROR_CHAR: .{raise ErrorToken(self.text)};