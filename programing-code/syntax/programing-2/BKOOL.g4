grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}
program: decls+ EOF; // write your rule here
decls : decl decl | decl;
decl: funcdecl | vardecl;
vardecl: typ idlist SEMI;
funcdecl: typ ID paramlist body;

//And some other rules for variable declaration, function declaration and other rules
paramlist: LB paramterm RB;
paramterm: param |;
param: typ idlist SEMI param | typ idlist;
typ: INT | FLOAT;
idlist: ID COMMA idlist | ID;
body: 'body';
INT: 'int';
FLOAT: 'float';
COMMA: ',';
SEMI: ';';
LB: '(';
RB: ')';
ID: [a-zA-Z]+; // includes a sequence of alphabetic characters.
WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;