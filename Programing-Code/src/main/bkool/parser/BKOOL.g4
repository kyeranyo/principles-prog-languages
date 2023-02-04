grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: EOF;

/*
 LEXER PROGRAMING CODE:
 
 * -> greedy
 *? -> non-greedy

 */
// // Q1
// INDENIFIER: [a-z] [a-z0-9]*;

// // Q2
// fragment DECIMAL_POINT: [0-9]+ '.' [0-9]+; 
// fragment SCIENTIC_NONTATION: [0-9]+ '.'? [0-9]* ('e'|'E') '-'? [0-9]+; 
// REAL: (DECIMAL_POINT | SCIENTIC_NONTATION);

// Q3
// STRINGLIT: SingQ (~['] | SingQ SingQ)* SingQ;
// fragment SingQ: ['];
INDENIFIER: [a-z] [a-z0-9]*;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;