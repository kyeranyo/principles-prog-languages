grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}
program : EOF;

IP: (STR1 | ZERO) '.' (STR1 | ZERO) '.' (STR1 | ZERO) '.' (STR1 | ZERO);

fragment STR1: [1-9][0-9]?[0-9]?;
fragment ZERO: '0';

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;