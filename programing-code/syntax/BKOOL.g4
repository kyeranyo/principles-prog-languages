grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}
// program: funcdecl | vardecl; funcdecl: 'funcdecl'; vardecl: 'vardecl';
program: decls;
decls: decl decl | decl;
decl: vardecl | funcdecl;

vardecl: typ idlist SEMI;
funcdecl: typ ID paradecl body;

paradecl: LB paramlist RB;
paramlist: paramterm |;
paramterm: (typ idlist SEMI paramterm) | (typ idlist);

idlist: ID COMMA idlist | ID; // a,b,c,d,e,f,g,h
body: 'body';

typ: INT | FLOAT;
INT: 'int';
FLOAT: 'float';
LB: '(';
RB: ')';
COMMA: ',';
SEMI: ';';
ID: [a-zA-Z]+;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;