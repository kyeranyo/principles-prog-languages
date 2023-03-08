grammar BKOOL;

program: decls* EOF;

decls:
	array_type
	| variable_decl
	| function_decl
	| statement
	| expression;

// Array type -------------------------------------------------------------
array_type: ARRAY LSB dimesion RSB OF element_type;

element_type: INTEGER | FLOAT | BOOLEAN | STRING;
dimesion: dimesion_type_int | dimesion_type_float;
dimesion_type_int:
	INTEGER_LIT COMMA dimesion_type_int
	| INTEGER_LIT;
dimesion_type_float:
	FLOAT_LIT COMMA dimesion_type_float FLOAT_LIT;

//Variables ---------------------------------------------------------------
variable_decl:
	identifier_list COLON (element_type | array_type) (
		equal_exp
		| equal_func_call
	) {

};

equal_exp: (EQUAL expression_list SEMI) | SEMI;
equal_func_call: (EQUAL function_call SEMI) | SEMI;

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
	)
	| IDENTIFIER LSB exp_list_type_int RSB;

// function call ------------------------------------------------------------
function_call: IDENTIFIER LB exp_list RB;
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
do_while_stmt: DO block_stmt WHILE expression;

// call statement -------------------------------------------------------------
call_stmt: function_call SEMI;

// block statement ------------------------------------------------------------
block_stmt: (LCB statement* RCB) | '{}';
// statement_list: statement statement_list | statement;

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

/* --------------------------------------TOKEN------------------------------------------------------- */
COMMENT: (SingleLineComment | MultiLineComment) -> skip;
fragment SingleLineComment: '//' ~('\r' | '\n')*;
fragment MultiLineComment: '/*' .*? '*/';

// NUMBER: (INTEGER_LIT | FLOAT_LIT) {self.text = self.text.replace("_","")};

INTEGER_LIT:
	'0'
	| [1-9][0-9]* (UNDERSCORE [0-9]+)*;

fragment UNDERSCORE: '_';

FLOAT_LIT:
	EXPPART
	| DECPART ;
fragment DECPART: INTEGER_LIT PERIOD [0-9]+ ([eE] [0-9]*)?;
fragment EXPPART: [0-9]+ [eE] MINUS [0-9]+;

BOOLEAN_LIT: FALSE | TRUE;
fragment FALSE: 'false';
fragment TRUE: 'true';

STRING_LIT:
	DUO_QUOTE (~[\\"] | SUBSTRING)*? DUO_QUOTE;
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

ERROR_CHAR: .;
UNCLOSE_STRING: .;
// '"' (~[\\"] | SUBSTRING)*? {raise UncloseString(self.text)};
ILLEGAL_ESCAPE: .;
// (~[\\"] | SUBSTRING)*? '"' {raise IllegalEscape(self.text)};
