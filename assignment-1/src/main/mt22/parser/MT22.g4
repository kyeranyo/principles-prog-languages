grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: EOF;

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

STRING_LIT: DUO_QUOTE (.~[\\]*?Escape_Sequence*?)? DUO_QUOTE;
fragment Escape_Sequence:
	BackSpace
	| FormFeed
	| CarriageReturn
	| NewLine
	| SingleQuote
	;
fragment DUO_QUOTE: ["];
fragment SINGLE_QUOTE: ['];
fragment BackSpace: [\b];
fragment FormFeed: [\f];
fragment CarriageReturn: [\r];
fragment NewLine: [\n];
fragment SingleQuote: '\'';
fragment BackSlash: [\\];

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

fragment PLUS: '+';
fragment MINUS: '-';
fragment MUL: '*';
fragment DIV: '/';
fragment MOD: '%';
fragment NOT: '!';
AND: '&&';
OR: '||';
EQUAL_TO: '==';
NOT_EQUAL: '!=';
LESS: '<';
GREATER: '>';
LESS_THAN_OR_EQUAL: '<=';
GREATER_THAN_OR_EQUAL: '>=';
SCOPE_RES: '::';

LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
LCB: '{';
RCB: '}';
fragment PERIOD: '.';
fragment COMMA: ',';
fragment SEMI: ';';
fragment EQUAL: '=';
fragment COLON: ':';

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;