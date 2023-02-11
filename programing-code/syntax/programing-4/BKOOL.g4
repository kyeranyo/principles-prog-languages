grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}
program: decls+ EOF; // write your rule for program here
decls: decl decl | decl;
decl: funcdecl | vardecl;
vardecl: typ idlist SEMI;
funcdecl:
	typ ID paramdecl LCB (vardecl | assign_stmt | call_stmt SEMI)* return_stmt RCB;
//And some other rules for variable declaration, function declaration, statements but using following expr for an expression

expr: ID | INTEGER | REAL;

exp: exp ('+' | '-') term | term;
term: term ('*' | '/') factor | factor;
factor: (INTEGER | REAL | ID | call_stmt) | LB exp RB;

assign_stmt: ID '=' exp SEMI;
return_stmt: 'return' (exp SEMI);
call_stmt: ID LB (param_call_stmt |) RB;
param_call_stmt: expr COMMA param_call_stmt | expr;

paramdecl: LB paramterm RB;
paramterm: param |;
param: typ idlist SEMI param | typ idlist;

idlist: ID COMMA idlist | ID;
typ: INT | FLOAT;
INT: 'int';
FLOAT: 'float';
COMMA: ',';
SEMI: ';';
LB: '(';
RB: ')';
LCB: '{';
RCB: '}';
INTEGER: [0-9]+;
REAL: [0-9]+ '.' [0-9]+;
ID: [a-zA-Z]+; //includes a sequence of alphabetic characters
WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;