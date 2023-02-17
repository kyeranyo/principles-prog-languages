grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: decls* EOF;

decls: array_type | variable_decl;

COMMENT: (SingleLineComment | MultiLineComment) -> skip;
fragment SingleLineComment: '//' ~('\r' | '\n')*;
fragment MultiLineComment: '/*' .*? '*/';

INTEGER_LIT:
	'0'
	| [1-9][0-9]* (UNDERSCORE [0-9]+)* {self.text = self.text.replace("_","")};

fragment UNDERSCORE: '_';

FLOAT_LIT:
	EXPPART
	| DECPART {self.text = self.text.replace("_","")};
fragment DECPART: INTEGER_LIT PERIOD [0-9]+ ([eE] [0-9]*)?;
fragment EXPPART: [0-9]+ [eE] MINUS [0-9]+;

BOOLEAN_LIT: FALSE | TRUE;
fragment FALSE: 'false';
fragment TRUE: 'true';

STRING_LIT:
	DUO_QUOTE (~[\\"] | SUBSTRING)*? DUO_QUOTE {self.text=self.text[1:-1]};
fragment SUBSTRING: '\\"' .*? '\\"';

ARRAY_LIT: LCB EXPS? RCB;
fragment EXPS: NUMLIST | STRINGLIST;

fragment Escape_Sequence:
	BackSpace
	| FormFeed
	| CarriageReturn
	| NewLine
	| SingleQuote
	| Dou_quote
	| BackSlash;
fragment DUO_QUOTE: ["];
fragment SINGLE_QUOTE: ['];
fragment BackSpace: [\b];
fragment FormFeed: [\f];
fragment CarriageReturn: [\r];
fragment NewLine: [\n];
fragment SingleQuote: '\'';
fragment BackSlash: [\\];
fragment Dou_quote: '\\"';

array_type: ARRAY LSB dimesion RSB OF element_type;
variable_decl:
	identifier_list COLON element_type (EQUAL expression_list)? SEMI;



identifier_list: IDENTIFIER COMMA identifier_list | IDENTIFIER;
expression_list: dimesion;
element_type: INTEGER | FLOAT | BOOLEAN | STRING;
dimesion: NUMLIST;

AUTO: 'auto';
BREAK: 'break';
INTEGER: 'integer';
VOID: 'void';
ARRAY: 'array';
FLOAT: 'float';
RETURN: 'return';
OUT: 'out';
BOOLEAN: 'boolean';
FOR: 'for';
STRING: 'string';
CONTINUE: 'continue';
DO: 'do';
FUNCTION: 'function';
OF: 'of';
ELSE: 'else';
IF: 'if';
WHILE: 'while';
INHERIT: 'inherit';

PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
LESS: '<';
GREATER: '>';
LESS_THAN_OR_EQUAL: '<=';
GREATER_THAN_OR_EQUAL: '>=';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL_TO: '==';
NOT_EQUAL: '!=';

IDENTIFIER: [a-zA-Z_]+ [a-zA-Z0-9_]*;
NUMBER: INTEGER_LIT | FLOAT_LIT;

SCOPE_RES: '::';
PERIOD: '.';
COMMA: ',';
SEMI: ';';
EQUAL: '=';
COLON: ':';
LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
LCB: '{';
RCB: '}';

NUMLIST: (NUMBER COMMA NUMLIST) | NUMBER;
STRINGLIST: (STRING_LIT COMMA STRINGLIST) | STRING_LIT;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

UNCLOSE_STRING:
	DUO_QUOTE (~[\\"] | SUBSTRING)*? {raise UncloseString(self.text)};
ILLEGAL_ESCAPE:
	(~[\\"] | SUBSTRING)*? DUO_QUOTE {raise IllegalEscape(self.text)};
ERROR_CHAR: .{raise ErrorToken(self.text)};