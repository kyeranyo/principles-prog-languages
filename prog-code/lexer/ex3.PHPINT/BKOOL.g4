grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}
program: EOF;

INTLIT:
	'0'
	| ([1-9][0-9]* ('_' [0-9]+)*) {self.text = self.text.replace("_","")};

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;