grammar BKOOL;

// program:   (expr NEWLINE)* EOF;
// expr:   expr ('*'|'/') expr
//     |   expr ('+'|'-') expr
//     |   INT
//     |   '(' expr ')'
//     ;
// NEWLINE : [\r\n]+ ;
// INT     : [0-9]+ ;
program: EOF;

SHEXA: EVEN | DIGITNUM;

EVEN: [1-9][0-9]* [2468];
DIGITNUM: [1-9]+ [a-zA-Z]* [aceACE];

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
