grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}
program : EOF;

BKNETID : A '.' B C;

fragment A: [a-zA-Z]+;
fragment B: [a-zA-Z0-9_.]+;
fragment C: [a-zA-Z0-9];

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;