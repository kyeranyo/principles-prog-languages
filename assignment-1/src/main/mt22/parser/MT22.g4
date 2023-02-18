grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: decls+ EOF;

decls: array_type | variable_decl | function_decl;

// Array type
array_type: ARRAY LSB dimesion RSB OF element_type;

element_type: INTEGER | FLOAT | BOOLEAN | STRING;
dimesion: dimesion_type_int | dimesion_type_float;
dimesion_type_int:
	INTEGER_LIT COMMA dimesion_type_int
	| INTEGER_LIT;
dimesion_type_float:
	FLOAT_LIT COMMA dimesion_type_float FLOAT_LIT;

//Variables
variable_decl: identifier_list COLON element_type equal_exp ';';

equal_exp: (EQUAL expression_list) |;

identifier_list: IDENTIFIER COMMA identifier_list | IDENTIFIER;
expression_list: exp_list_type_int | exp_list_type_float;
exp_list_type_int:
	INTEGER_LIT COMMA exp_list_type_int
	| INTEGER_LIT;
exp_list_type_float:
	FLOAT_LIT COMMA exp_list_type_float
	| FLOAT_LIT;
exp_list_type_string:
	STRING_LIT COMMA exp_list_type_string
	| STRING_LIT;

//Parameters
parameter: (INHERIT |) (OUT |) IDENTIFIER COLON element_type;

// Function declarations
function_decl:
	IDENTIFIER COLON FUNCTION return_type LB paramter_list RB inheritance;
inheritance: INHERIT function_name |;
function_name: IDENTIFIER;

paramter_list: paramter_list_term |;
paramter_list_term:
	parameter COMMA paramter_list_term
	| parameter;

return_type: INTEGER | FLOAT | BOOLEAN | STRING | VOID | AUTO;

COMMENT: (SingleLineComment | MultiLineComment) -> skip;
fragment SingleLineComment: '//' ~('\r' | '\n')*;
fragment MultiLineComment: '/*' .*? '*/';

// NUMBER: (INTEGER_LIT | FLOAT_LIT) {self.text = self.text.replace("_","")};

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
fragment EXPS: INT_TYPE | FLOAT_TYPE | STRINGLIST;
fragment INT_TYPE: (INTEGER_LIT COMMA INT_TYPE) | INTEGER_LIT;
fragment FLOAT_TYPE: (FLOAT_LIT COMMA FLOAT_TYPE) | FLOAT_LIT;
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

IDENTIFIER: [a-zA-Z_]+ [a-zA-Z0-9_]*;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

UNCLOSE_STRING:
	'"' (~[\\"] | SUBSTRING)*? {raise UncloseString(self.text)};
ILLEGAL_ESCAPE:
	(~[\\"] | SUBSTRING)*? '"' {raise IllegalEscape(self.text)};
ERROR_CHAR: .{raise ErrorToken(self.text)};