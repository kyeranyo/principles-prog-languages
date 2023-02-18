grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: decls+ EOF;

decls: dimesion;
dimesion: NUMBER ',' dimesion | NUMBER;

array_type: 'array' '[' dimesion ']' 'of' element_type;
element_type: 'integer' | 'float' | 'boolean' | 'string';

variable_decl:
	identifier_list ';' element_type ('=' expression_list)? ';';
identifier_list: IDENTIFIER ',' identifier_list | IDENTIFIER;
expression_list: dimesion;

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
fragment NUMLIST: (NUMBER COMMA NUMLIST) | NUMBER;
fragment STRINGLIST: (STRING_LIT COMMA STRINGLIST) | STRING_LIT;

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

// AUTO: 'auto';
// BREAK: 'break';
// INTEGER: 'integer';
// VOID: 'void';
// ARRAY: 'array';
// FLOAT: 'float';
// RETURN: 'return';
// OUT: 'out';
// BOOLEAN: 'boolean';
// FOR: 'for';
// STRING: 'string';
// CONTINUE: 'continue';
// DO: 'do';
// FUNCTION: 'function';
// OF: 'of';
// ELSE: 'else';
// IF: 'if';
// WHILE: 'while';
// INHERIT: 'inherit';

fragment PLUS: '+';
fragment MINUS: '-';
fragment MUL: '*';
fragment DIV: '/';
fragment MOD: '%';
fragment LESS: '<';
fragment GREATER: '>';
fragment LESS_THAN_OR_EQUAL: '<=';
fragment GREATER_THAN_OR_EQUAL: '>=';
fragment NOT: '!';
fragment AND: '&&';
fragment OR: '||';
fragment EQUAL_TO: '==';
fragment NOT_EQUAL: '!=';

fragment SCOPE_RES: '::';
fragment PERIOD: '.';
fragment COMMA: ',';
fragment SEMI: ';';
fragment EQUAL: '=';
fragment COLON: ':';
fragment LB: '(';
fragment RB: ')';
fragment LSB: '[';
fragment RSB: ']';
fragment LCB: '{';
fragment RCB: '}';

IDENTIFIER: [a-zA-Z_]+ [a-zA-Z0-9_]*;
NUMBER: INTEGER_LIT | FLOAT_LIT;
WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

UNCLOSE_STRING:
	'"' (~[\\"] | SUBSTRING)*? {raise UncloseString(self.text)};
ILLEGAL_ESCAPE:
	(~[\\"] | SUBSTRING)*? '"' {raise IllegalEscape(self.text)};
ERROR_CHAR: .{raise ErrorToken(self.text)};