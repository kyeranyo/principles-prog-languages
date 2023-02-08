grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}
program: EOF;

SHEXA: EVEN | DIGITNUM;

EVEN: [1-9][0-9]* [2468];
DIGITNUM: [1-9]+ [a-zA-Z]* [aceACE];

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;