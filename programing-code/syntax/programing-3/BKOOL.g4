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
	typ ID paramdecl LCB (vardecl | assign_stmt | call_stmt)* return_stmt RCB;
assign_stmt: ID '=' expr SEMI;
call_stmt: ID LB (param_call_stmt |) RB SEMI;
return_stmt: 'return' expr SEMI;
param_call_stmt: expr COMMA param_call_stmt | expr;
//And some other rules for variable declaration, function declaration, statements but using following expr for an expression
expr: 'expr';
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
ID: [a-zA-Z]+; //includes a sequence of alphabetic characters
WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;