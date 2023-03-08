grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: decls+ EOF;

decls: variable_decl | function_decl;

// Array type -------------------------------------------------------------
array_type: ARRAY LSB dimesion RSB OF element_type;

element_type: INTEGER | FLOAT | BOOLEAN | STRING | AUTO;
dimesion: dimesion_type_int | dimesion_type_float;
dimesion_type_int:
	INTEGER_LIT COMMA dimesion_type_int
	| INTEGER_LIT;
dimesion_type_float:
	FLOAT_LIT COMMA dimesion_type_float FLOAT_LIT;

//Variables ---------------------------------------------------------------

variable_decl: var_decl_no_eq | var_decl_eq;

var_decl_no_eq:
	identifier_list COLON (element_type | array_type) SEMI;
var_decl_eq:
	IDENTIFIER (
		COMMA recursive
		| COLON (element_type | array_type) EQUAL
	) expression SEMI;
recursive:
	IDENTIFIER (
		COMMA recursive
		| COLON (element_type | array_type) EQUAL
	) expression COMMA;
// {5e10 + "hello", -0.0e8}, "hello \\n", 123456789;

// var_decl_list: IDENTIFIER ( COMMA recursive_factor | COLON element_type EQUAL ) expression SEMI;
// recursive_factor: IDENTIFIER ( COMMA recursive_factor | COLON element_type EQUAL ) expression
// COMMA;

//var_decl_func:
// IDENTIFIER (COMMA recursive_func | COLON element_type EQUAL) function_call SEMI; recursive_func:
// IDENTIFIER (COMMA recursive_func | COLON element_type EQUAL) function_call COMMA;
// 
// var_decl_array: IDENTIFIER (COMMA recursive_array | COLON array_type EQUAL) array_list SEMI;
// recursive_array: IDENTIFIER (COMMA recursive_array | COLON array_type EQUAL) array_list COMMA;

// var_decl_eq: var_decl_no_eq EQUAL array_list SEMI; equal_exp: (EQUAL expression_list SEMI) |
// SEMI; equal_func_call: (EQUAL function_call SEMI) | SEMI; equal_array_type: (EQUAL array_list
// SEMI) | SEMI;

array_list: LCB (exp_list_term) RCB;
exp_list_term: expression_list |;

identifier_list: IDENTIFIER COMMA identifier_list | IDENTIFIER;
expression_list:
	(FLOAT_LIT | STRING_LIT | expression | INTEGER_LIT) COMMA expression_list
	| (FLOAT_LIT | STRING_LIT | expression | INTEGER_LIT);
exp_list_type_int:
	INTEGER_LIT COMMA exp_list_type_int
	| INTEGER_LIT;
exp_list_type_float:
	FLOAT_LIT COMMA exp_list_type_float
	| FLOAT_LIT;
exp_list_type_string:
	STRING_LIT COMMA exp_list_type_string
	| STRING_LIT;

//Parameters ----------------------------------------------------------------
parameter: (INHERIT |) (OUT |) IDENTIFIER COLON element_type;

// expression declarations --------------------------------------------------
expression: expression_1 CONCAT expression_1 | expression_1;

expression_1:
	expression_2 (
		EQUAL_TO
		| NOT_EQUAL
		| LESS
		| GREATER
		| LTE
		| GTE
	) expression_2
	| expression_2;
expression_2:
	expression_2 (AND | OR) expression_3
	| expression_3;
expression_3:
	expression_3 (PLUS | MINUS) expression_4
	| expression_4;
expression_4:
	expression_4 (MUL | DIV | MOD) expression_5
	| expression_5;
expression_5: NOT expression_5 | expression_6;
expression_6: MINUS expression_6 | expression_7;
expression_7: expression_7 factor | expression_8;
expression_8: (LB expression RB) | factor;

factor: (
		INTEGER_LIT
		| FLOAT_LIT
		| STRING_LIT
		| IDENTIFIER
		| function_call
		| array_list
	)
	| IDENTIFIER LSB (exp_list_type_int | factor) RSB;

// function call ------------------------------------------------------------
function_call: IDENTIFIER LB exps_list RB;
exps_list: exp_list |;
exp_list: expression COMMA exp_list | expression;

// statement ----------------------------------------------------------------
statement:
	assign_stmt
	| if_stmt
	| for_stmt
	| while_stmt
	| do_while_stmt
	| block_stmt
	| return_stmt
	| continue_stmt
	| break_stmt
	| call_stmt
	| variable_decl;

// assignment statement ------------------------------------------------------
assign_stmt: lhs EQUAL expression SEMI;
lhs: IDENTIFIER LSB exp_list_type_int RSB | IDENTIFIER;

// if statement --------------------------------------------------------------
if_stmt: (IF expression statement ELSE statement)
	| IF expression statement;

// for statement -------------------------------------------------------------
for_stmt:
	LB scala_val EQUAL init_expr COMMA condition_expr COMMA update_expr RB statement;
scala_val: IDENTIFIER;
init_expr: INTEGER_LIT | IDENTIFIER;
condition_expr:
	IDENTIFIER (
		LESS
		| GREATER
		| LTE
		| GTE
		| NOT_EQUAL
		| EQUAL_TO
	) (IDENTIFIER | expression);
update_expr: IDENTIFIER (PLUS | MINUS | MUL | MOD) expression;

// while statement ------------------------------------------------------------
while_stmt: WHILE LB expression RB statement;

// Do while statement ---------------------------------------------------------
do_while_stmt: DO block_stmt WHILE expression SEMI;

// call statement -------------------------------------------------------------
call_stmt: (function_call | s_func_decl) SEMI;

// block statement ------------------------------------------------------------
block_stmt: (LCB statement_term RCB);
statement_term: statement_list |;
statement_list: statement statement_list | statement;

//break statement -------------------------------------------------------------
break_stmt: BREAK SEMI;

// continue statement ---------------------------------------------------------
continue_stmt: CONTINUE SEMI;

// return statement -----------------------------------------------------------
return_stmt: RETURN expression SEMI;

// Function declarations ------------------------------------------------------
function_decl:
	IDENTIFIER COLON FUNCTION return_type LB paramter_list RB inheritance statement;
inheritance: INHERIT function_name |;
function_name: IDENTIFIER;

paramter_list: paramter_list_term |;
paramter_list_term:
	parameter COMMA paramter_list_term
	| parameter;

return_type: INTEGER | FLOAT | BOOLEAN | STRING | VOID | AUTO;

// Special Functions ------------------------------------------------------------
s_func_decl:
	read_integer
	| print_integer
	| read_float
	| write_float
	| print_boolean
	| read_string
	| print_string
	| super_
	| prevent_default;

read_integer: 'readInteger' LB RB;
print_integer:
	'printInteger' LB (INTEGER_LIT | IDENTIFIER | expression) RB;
read_float: 'readFloat' LB RB;
write_float:
	'writeFloat' LB (FLOAT_LIT | IDENTIFIER | expression) RB;
print_boolean:
	'printBoolean' LB (BOOLEAN_LIT | IDENTIFIER | expression) RB;
read_string: 'readString' LB RB;
print_string:
	'printString' LB (STRING_LIT | IDENTIFIER | expression) RB;
super_: 'super' LB expression_list RB;
prevent_default: 'preventDefault' LB RB;

/* --------------------------------------TOKEN------------------------------------------------------- */
COMMENT: (SingleLineComment | MultiLineComment | CommentAll) -> skip;
fragment SingleLineComment: '//' ~('\r' | '\n')*;
fragment MultiLineComment: '/*' .*? '*/';
fragment CommentAll: '/*' .*? EOF;

// NUMBER: (INTEGER_LIT | FLOAT_LIT) {self.text = self.text.replace("_","")};

INTEGER_LIT:
	'0'
	| [1-9][0-9]* (UNDERSCORE [0-9]+)* {self.text = self.text.replace("_","")};

fragment UNDERSCORE: '_';

FLOAT_LIT: (EXPPART | DECPART) {self.text = self.text.replace("_","")};
fragment DECPART:
	INTEGER_LIT PERIOD (
		INTEGER_LIT
		| [0-9]+ (UNDERSCORE [0-9]+)*
	) ([eE] (MINUS | PLUS)? INTEGER_LIT)?;
fragment EXPPART: INTEGER_LIT [eE] (MINUS | PLUS)? INTEGER_LIT;

BOOLEAN_LIT: FALSE | TRUE;
fragment FALSE: 'false';
fragment TRUE: 'true';

STRING_LIT:
	DUO_QUOTE (~[\\"] | SUBSTRING | Escape_Sequence)* DUO_QUOTE {self.text=str(self.text[1:-1])};
fragment SUBSTRING:
	'\\"' (~[\\"] | SUBSTRING | Escape_Sequence)*? '\\"';

ARRAY_LIT:
	ARRAY_LIT_INT
	| ARRAY_LIT_FLOAT
	| ARRAY_LIT_STRINGLIST;
ARRAY_LIT_INT: LCB INT_TYPE RCB;
ARRAY_LIT_FLOAT: LCB FLOAT_TYPE RCB;
ARRAY_LIT_STRINGLIST: LCB STRINGLIST RCB;
fragment INT_TYPE: (INTEGER_LIT COMMA INT_TYPE) | INTEGER_LIT;
fragment FLOAT_TYPE: (FLOAT_LIT COMMA FLOAT_TYPE) | FLOAT_LIT;
fragment STRINGLIST: (STRING_LIT COMMA STRINGLIST) | STRING_LIT;

fragment Not_Escape_Sequence:
	'\\' ~('b' | 'f' | 'n' | 'r' | 't' | '"' | '\'' | '\\');
fragment Escape_Sequence:
	'\\' ('b' | 'f' | 'n' | 'r' | 't' | '\'' | '\\' | '"');
fragment AllEscSeq: '\\' ~["];
fragment DUO_QUOTE: ["];
fragment SINGLE_QUOTE: ['];

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
LTE: '<=';
GTE: '>=';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL_TO: '==';
NOT_EQUAL: '!=';

CONCAT: '::';
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
	DUO_QUOTE (~["] | SUBSTRING)*? ([\r\n] | EOF) {raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE:
	DUO_QUOTE (~[\\"] | SUBSTRING | Escape_Sequence)* Not_Escape_Sequence {raise IllegalEscape(self.text[1:])
		};
ERROR_CHAR: .{raise ErrorToken(self.text)};