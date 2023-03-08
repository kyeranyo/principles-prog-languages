// Generated from c:\Users\84865\Documents\HCMUT-cse20\CSE-PPL\test\src\test\gui\BKOOL.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class BKOOLParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		COMMENT=10, INTEGER_LIT=11, FLOAT_LIT=12, BOOLEAN_LIT=13, STRING_LIT=14, 
		ARRAY_LIT=15, ARRAY_LIT_INT=16, ARRAY_LIT_FLOAT=17, ARRAY_LIT_STRINGLIST=18, 
		AUTO=19, BREAK=20, INTEGER=21, VOID=22, ARRAY=23, FLOAT=24, RETURN=25, 
		OUT=26, BOOLEAN=27, FOR=28, STRING=29, CONTINUE=30, DO=31, FUNCTION=32, 
		OF=33, ELSE=34, IF=35, WHILE=36, INHERIT=37, PLUS=38, MINUS=39, MUL=40, 
		DIV=41, MOD=42, LESS=43, GREATER=44, LTE=45, GTE=46, NOT=47, AND=48, OR=49, 
		EQUAL_TO=50, NOT_EQUAL=51, CONCAT=52, PERIOD=53, COMMA=54, SEMI=55, EQUAL=56, 
		COLON=57, LB=58, RB=59, LSB=60, RSB=61, LCB=62, RCB=63, IDENTIFIER=64, 
		WS=65, UNCLOSE_STRING=66, ILLEGAL_ESCAPE=67, ERROR_CHAR=68;
	public static final int
		RULE_program = 0, RULE_decls = 1, RULE_array_type = 2, RULE_element_type = 3, 
		RULE_dimesion = 4, RULE_dimesion_type_int = 5, RULE_dimesion_type_float = 6, 
		RULE_variable_decl = 7, RULE_var_decl_no_eq = 8, RULE_var_decl_eq = 9, 
		RULE_recursive = 10, RULE_array_list = 11, RULE_exp_list_term = 12, RULE_identifier_list = 13, 
		RULE_expression_list = 14, RULE_exp_list_type_int = 15, RULE_exp_list_type_float = 16, 
		RULE_exp_list_type_string = 17, RULE_parameter = 18, RULE_expression = 19, 
		RULE_expression_1 = 20, RULE_expression_2 = 21, RULE_expression_3 = 22, 
		RULE_expression_4 = 23, RULE_expression_5 = 24, RULE_expression_6 = 25, 
		RULE_expression_7 = 26, RULE_expression_8 = 27, RULE_factor = 28, RULE_function_call = 29, 
		RULE_exps_list = 30, RULE_exp_list = 31, RULE_statement = 32, RULE_assign_stmt = 33, 
		RULE_lhs = 34, RULE_if_stmt = 35, RULE_for_stmt = 36, RULE_init_expr = 37, 
		RULE_condition_expr = 38, RULE_update_expr = 39, RULE_while_stmt = 40, 
		RULE_do_while_stmt = 41, RULE_call_stmt = 42, RULE_block_stmt = 43, RULE_statement_term = 44, 
		RULE_statement_list = 45, RULE_break_stmt = 46, RULE_continue_stmt = 47, 
		RULE_return_stmt = 48, RULE_function_decl = 49, RULE_inheritance = 50, 
		RULE_function_name = 51, RULE_paramter_list = 52, RULE_paramter_list_term = 53, 
		RULE_return_type = 54, RULE_s_func_decl = 55, RULE_read_integer = 56, 
		RULE_print_integer = 57, RULE_read_float = 58, RULE_write_float = 59, 
		RULE_print_boolean = 60, RULE_read_string = 61, RULE_print_string = 62, 
		RULE_super_ = 63, RULE_prevent_default = 64;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "decls", "array_type", "element_type", "dimesion", "dimesion_type_int", 
			"dimesion_type_float", "variable_decl", "var_decl_no_eq", "var_decl_eq", 
			"recursive", "array_list", "exp_list_term", "identifier_list", "expression_list", 
			"exp_list_type_int", "exp_list_type_float", "exp_list_type_string", "parameter", 
			"expression", "expression_1", "expression_2", "expression_3", "expression_4", 
			"expression_5", "expression_6", "expression_7", "expression_8", "factor", 
			"function_call", "exps_list", "exp_list", "statement", "assign_stmt", 
			"lhs", "if_stmt", "for_stmt", "init_expr", "condition_expr", "update_expr", 
			"while_stmt", "do_while_stmt", "call_stmt", "block_stmt", "statement_term", 
			"statement_list", "break_stmt", "continue_stmt", "return_stmt", "function_decl", 
			"inheritance", "function_name", "paramter_list", "paramter_list_term", 
			"return_type", "s_func_decl", "read_integer", "print_integer", "read_float", 
			"write_float", "print_boolean", "read_string", "print_string", "super_", 
			"prevent_default"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'readInteger'", "'printInteger'", "'readFloat'", "'writeFloat'", 
			"'printBoolean'", "'readString'", "'printString'", "'super'", "'preventDefault'", 
			null, null, null, null, null, null, null, null, null, "'auto'", "'break'", 
			"'integer'", "'void'", "'array'", "'float'", "'return'", "'out'", "'boolean'", 
			"'for'", "'string'", "'continue'", "'do'", "'function'", "'of'", "'else'", 
			"'if'", "'while'", "'inherit'", "'+'", "'-'", "'*'", "'/'", "'%'", "'<'", 
			"'>'", "'<='", "'>='", "'!'", "'&&'", "'||'", "'=='", "'!='", "'::'", 
			"'.'", "','", "';'", "'='", "':'", "'('", "')'", "'['", "']'", "'{'", 
			"'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, "COMMENT", 
			"INTEGER_LIT", "FLOAT_LIT", "BOOLEAN_LIT", "STRING_LIT", "ARRAY_LIT", 
			"ARRAY_LIT_INT", "ARRAY_LIT_FLOAT", "ARRAY_LIT_STRINGLIST", "AUTO", "BREAK", 
			"INTEGER", "VOID", "ARRAY", "FLOAT", "RETURN", "OUT", "BOOLEAN", "FOR", 
			"STRING", "CONTINUE", "DO", "FUNCTION", "OF", "ELSE", "IF", "WHILE", 
			"INHERIT", "PLUS", "MINUS", "MUL", "DIV", "MOD", "LESS", "GREATER", "LTE", 
			"GTE", "NOT", "AND", "OR", "EQUAL_TO", "NOT_EQUAL", "CONCAT", "PERIOD", 
			"COMMA", "SEMI", "EQUAL", "COLON", "LB", "RB", "LSB", "RSB", "LCB", "RCB", 
			"IDENTIFIER", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "BKOOL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public BKOOLParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(BKOOLParser.EOF, 0); }
		public List<DeclsContext> decls() {
			return getRuleContexts(DeclsContext.class);
		}
		public DeclsContext decls(int i) {
			return getRuleContext(DeclsContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(131); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(130);
				decls();
				}
				}
				setState(133); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==IDENTIFIER );
			setState(135);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclsContext extends ParserRuleContext {
		public Variable_declContext variable_decl() {
			return getRuleContext(Variable_declContext.class,0);
		}
		public Function_declContext function_decl() {
			return getRuleContext(Function_declContext.class,0);
		}
		public DeclsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_decls; }
	}

	public final DeclsContext decls() throws RecognitionException {
		DeclsContext _localctx = new DeclsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_decls);
		try {
			setState(139);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(137);
				variable_decl();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(138);
				function_decl();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Array_typeContext extends ParserRuleContext {
		public TerminalNode ARRAY() { return getToken(BKOOLParser.ARRAY, 0); }
		public TerminalNode LSB() { return getToken(BKOOLParser.LSB, 0); }
		public DimesionContext dimesion() {
			return getRuleContext(DimesionContext.class,0);
		}
		public TerminalNode RSB() { return getToken(BKOOLParser.RSB, 0); }
		public TerminalNode OF() { return getToken(BKOOLParser.OF, 0); }
		public Element_typeContext element_type() {
			return getRuleContext(Element_typeContext.class,0);
		}
		public Array_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_type; }
	}

	public final Array_typeContext array_type() throws RecognitionException {
		Array_typeContext _localctx = new Array_typeContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_array_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(141);
			match(ARRAY);
			setState(142);
			match(LSB);
			setState(143);
			dimesion();
			setState(144);
			match(RSB);
			setState(145);
			match(OF);
			setState(146);
			element_type();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Element_typeContext extends ParserRuleContext {
		public TerminalNode INTEGER() { return getToken(BKOOLParser.INTEGER, 0); }
		public TerminalNode FLOAT() { return getToken(BKOOLParser.FLOAT, 0); }
		public TerminalNode BOOLEAN() { return getToken(BKOOLParser.BOOLEAN, 0); }
		public TerminalNode STRING() { return getToken(BKOOLParser.STRING, 0); }
		public TerminalNode AUTO() { return getToken(BKOOLParser.AUTO, 0); }
		public Element_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_element_type; }
	}

	public final Element_typeContext element_type() throws RecognitionException {
		Element_typeContext _localctx = new Element_typeContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_element_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(148);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << AUTO) | (1L << INTEGER) | (1L << FLOAT) | (1L << BOOLEAN) | (1L << STRING))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DimesionContext extends ParserRuleContext {
		public Dimesion_type_intContext dimesion_type_int() {
			return getRuleContext(Dimesion_type_intContext.class,0);
		}
		public Dimesion_type_floatContext dimesion_type_float() {
			return getRuleContext(Dimesion_type_floatContext.class,0);
		}
		public DimesionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dimesion; }
	}

	public final DimesionContext dimesion() throws RecognitionException {
		DimesionContext _localctx = new DimesionContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_dimesion);
		try {
			setState(152);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTEGER_LIT:
				enterOuterAlt(_localctx, 1);
				{
				setState(150);
				dimesion_type_int();
				}
				break;
			case FLOAT_LIT:
				enterOuterAlt(_localctx, 2);
				{
				setState(151);
				dimesion_type_float();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Dimesion_type_intContext extends ParserRuleContext {
		public TerminalNode INTEGER_LIT() { return getToken(BKOOLParser.INTEGER_LIT, 0); }
		public TerminalNode COMMA() { return getToken(BKOOLParser.COMMA, 0); }
		public Dimesion_type_intContext dimesion_type_int() {
			return getRuleContext(Dimesion_type_intContext.class,0);
		}
		public Dimesion_type_intContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dimesion_type_int; }
	}

	public final Dimesion_type_intContext dimesion_type_int() throws RecognitionException {
		Dimesion_type_intContext _localctx = new Dimesion_type_intContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_dimesion_type_int);
		try {
			setState(158);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(154);
				match(INTEGER_LIT);
				setState(155);
				match(COMMA);
				setState(156);
				dimesion_type_int();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(157);
				match(INTEGER_LIT);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Dimesion_type_floatContext extends ParserRuleContext {
		public List<TerminalNode> FLOAT_LIT() { return getTokens(BKOOLParser.FLOAT_LIT); }
		public TerminalNode FLOAT_LIT(int i) {
			return getToken(BKOOLParser.FLOAT_LIT, i);
		}
		public TerminalNode COMMA() { return getToken(BKOOLParser.COMMA, 0); }
		public Dimesion_type_floatContext dimesion_type_float() {
			return getRuleContext(Dimesion_type_floatContext.class,0);
		}
		public Dimesion_type_floatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dimesion_type_float; }
	}

	public final Dimesion_type_floatContext dimesion_type_float() throws RecognitionException {
		Dimesion_type_floatContext _localctx = new Dimesion_type_floatContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_dimesion_type_float);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(160);
			match(FLOAT_LIT);
			setState(161);
			match(COMMA);
			setState(162);
			dimesion_type_float();
			setState(163);
			match(FLOAT_LIT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Variable_declContext extends ParserRuleContext {
		public Var_decl_no_eqContext var_decl_no_eq() {
			return getRuleContext(Var_decl_no_eqContext.class,0);
		}
		public Var_decl_eqContext var_decl_eq() {
			return getRuleContext(Var_decl_eqContext.class,0);
		}
		public Variable_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_decl; }
	}

	public final Variable_declContext variable_decl() throws RecognitionException {
		Variable_declContext _localctx = new Variable_declContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_variable_decl);
		try {
			setState(167);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(165);
				var_decl_no_eq();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(166);
				var_decl_eq();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_decl_no_eqContext extends ParserRuleContext {
		public Identifier_listContext identifier_list() {
			return getRuleContext(Identifier_listContext.class,0);
		}
		public TerminalNode COLON() { return getToken(BKOOLParser.COLON, 0); }
		public TerminalNode SEMI() { return getToken(BKOOLParser.SEMI, 0); }
		public Element_typeContext element_type() {
			return getRuleContext(Element_typeContext.class,0);
		}
		public Array_typeContext array_type() {
			return getRuleContext(Array_typeContext.class,0);
		}
		public Var_decl_no_eqContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_decl_no_eq; }
	}

	public final Var_decl_no_eqContext var_decl_no_eq() throws RecognitionException {
		Var_decl_no_eqContext _localctx = new Var_decl_no_eqContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_var_decl_no_eq);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(169);
			identifier_list();
			setState(170);
			match(COLON);
			setState(173);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AUTO:
			case INTEGER:
			case FLOAT:
			case BOOLEAN:
			case STRING:
				{
				setState(171);
				element_type();
				}
				break;
			case ARRAY:
				{
				setState(172);
				array_type();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(175);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_decl_eqContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(BKOOLParser.IDENTIFIER, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKOOLParser.SEMI, 0); }
		public TerminalNode COMMA() { return getToken(BKOOLParser.COMMA, 0); }
		public RecursiveContext recursive() {
			return getRuleContext(RecursiveContext.class,0);
		}
		public TerminalNode COLON() { return getToken(BKOOLParser.COLON, 0); }
		public TerminalNode EQUAL() { return getToken(BKOOLParser.EQUAL, 0); }
		public Element_typeContext element_type() {
			return getRuleContext(Element_typeContext.class,0);
		}
		public Array_typeContext array_type() {
			return getRuleContext(Array_typeContext.class,0);
		}
		public Var_decl_eqContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_decl_eq; }
	}

	public final Var_decl_eqContext var_decl_eq() throws RecognitionException {
		Var_decl_eqContext _localctx = new Var_decl_eqContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_var_decl_eq);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(177);
			match(IDENTIFIER);
			setState(187);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMMA:
				{
				setState(178);
				match(COMMA);
				setState(179);
				recursive();
				}
				break;
			case COLON:
				{
				setState(180);
				match(COLON);
				setState(183);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case AUTO:
				case INTEGER:
				case FLOAT:
				case BOOLEAN:
				case STRING:
					{
					setState(181);
					element_type();
					}
					break;
				case ARRAY:
					{
					setState(182);
					array_type();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(185);
				match(EQUAL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(189);
			expression();
			setState(190);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RecursiveContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(BKOOLParser.IDENTIFIER, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<TerminalNode> COMMA() { return getTokens(BKOOLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKOOLParser.COMMA, i);
		}
		public RecursiveContext recursive() {
			return getRuleContext(RecursiveContext.class,0);
		}
		public TerminalNode COLON() { return getToken(BKOOLParser.COLON, 0); }
		public TerminalNode EQUAL() { return getToken(BKOOLParser.EQUAL, 0); }
		public Element_typeContext element_type() {
			return getRuleContext(Element_typeContext.class,0);
		}
		public Array_typeContext array_type() {
			return getRuleContext(Array_typeContext.class,0);
		}
		public RecursiveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_recursive; }
	}

	public final RecursiveContext recursive() throws RecognitionException {
		RecursiveContext _localctx = new RecursiveContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_recursive);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(192);
			match(IDENTIFIER);
			setState(202);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMMA:
				{
				setState(193);
				match(COMMA);
				setState(194);
				recursive();
				}
				break;
			case COLON:
				{
				setState(195);
				match(COLON);
				setState(198);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case AUTO:
				case INTEGER:
				case FLOAT:
				case BOOLEAN:
				case STRING:
					{
					setState(196);
					element_type();
					}
					break;
				case ARRAY:
					{
					setState(197);
					array_type();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(200);
				match(EQUAL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(204);
			expression();
			setState(205);
			match(COMMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Array_listContext extends ParserRuleContext {
		public TerminalNode LCB() { return getToken(BKOOLParser.LCB, 0); }
		public TerminalNode RCB() { return getToken(BKOOLParser.RCB, 0); }
		public Exp_list_termContext exp_list_term() {
			return getRuleContext(Exp_list_termContext.class,0);
		}
		public Array_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_list; }
	}

	public final Array_listContext array_list() throws RecognitionException {
		Array_listContext _localctx = new Array_listContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_array_list);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(207);
			match(LCB);
			{
			setState(208);
			exp_list_term();
			}
			setState(209);
			match(RCB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Exp_list_termContext extends ParserRuleContext {
		public Expression_listContext expression_list() {
			return getRuleContext(Expression_listContext.class,0);
		}
		public Exp_list_termContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp_list_term; }
	}

	public final Exp_list_termContext exp_list_term() throws RecognitionException {
		Exp_list_termContext _localctx = new Exp_list_termContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_exp_list_term);
		try {
			setState(213);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTEGER_LIT:
			case FLOAT_LIT:
			case BOOLEAN_LIT:
			case STRING_LIT:
			case MINUS:
			case NOT:
			case LB:
			case LCB:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(211);
				expression_list();
				}
				break;
			case RCB:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Identifier_listContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(BKOOLParser.IDENTIFIER, 0); }
		public TerminalNode COMMA() { return getToken(BKOOLParser.COMMA, 0); }
		public Identifier_listContext identifier_list() {
			return getRuleContext(Identifier_listContext.class,0);
		}
		public Identifier_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifier_list; }
	}

	public final Identifier_listContext identifier_list() throws RecognitionException {
		Identifier_listContext _localctx = new Identifier_listContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_identifier_list);
		try {
			setState(219);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(215);
				match(IDENTIFIER);
				setState(216);
				match(COMMA);
				setState(217);
				identifier_list();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(218);
				match(IDENTIFIER);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expression_listContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(BKOOLParser.COMMA, 0); }
		public Expression_listContext expression_list() {
			return getRuleContext(Expression_listContext.class,0);
		}
		public Expression_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression_list; }
	}

	public final Expression_listContext expression_list() throws RecognitionException {
		Expression_listContext _localctx = new Expression_listContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_expression_list);
		try {
			setState(226);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(221);
				expression();
				setState(222);
				match(COMMA);
				setState(223);
				expression_list();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(225);
				expression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Exp_list_type_intContext extends ParserRuleContext {
		public TerminalNode INTEGER_LIT() { return getToken(BKOOLParser.INTEGER_LIT, 0); }
		public TerminalNode COMMA() { return getToken(BKOOLParser.COMMA, 0); }
		public Exp_list_type_intContext exp_list_type_int() {
			return getRuleContext(Exp_list_type_intContext.class,0);
		}
		public Exp_list_type_intContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp_list_type_int; }
	}

	public final Exp_list_type_intContext exp_list_type_int() throws RecognitionException {
		Exp_list_type_intContext _localctx = new Exp_list_type_intContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_exp_list_type_int);
		try {
			setState(232);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(228);
				match(INTEGER_LIT);
				setState(229);
				match(COMMA);
				setState(230);
				exp_list_type_int();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(231);
				match(INTEGER_LIT);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Exp_list_type_floatContext extends ParserRuleContext {
		public TerminalNode FLOAT_LIT() { return getToken(BKOOLParser.FLOAT_LIT, 0); }
		public TerminalNode COMMA() { return getToken(BKOOLParser.COMMA, 0); }
		public Exp_list_type_floatContext exp_list_type_float() {
			return getRuleContext(Exp_list_type_floatContext.class,0);
		}
		public Exp_list_type_floatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp_list_type_float; }
	}

	public final Exp_list_type_floatContext exp_list_type_float() throws RecognitionException {
		Exp_list_type_floatContext _localctx = new Exp_list_type_floatContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_exp_list_type_float);
		try {
			setState(238);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(234);
				match(FLOAT_LIT);
				setState(235);
				match(COMMA);
				setState(236);
				exp_list_type_float();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(237);
				match(FLOAT_LIT);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Exp_list_type_stringContext extends ParserRuleContext {
		public TerminalNode STRING_LIT() { return getToken(BKOOLParser.STRING_LIT, 0); }
		public TerminalNode COMMA() { return getToken(BKOOLParser.COMMA, 0); }
		public Exp_list_type_stringContext exp_list_type_string() {
			return getRuleContext(Exp_list_type_stringContext.class,0);
		}
		public Exp_list_type_stringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp_list_type_string; }
	}

	public final Exp_list_type_stringContext exp_list_type_string() throws RecognitionException {
		Exp_list_type_stringContext _localctx = new Exp_list_type_stringContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_exp_list_type_string);
		try {
			setState(244);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(240);
				match(STRING_LIT);
				setState(241);
				match(COMMA);
				setState(242);
				exp_list_type_string();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(243);
				match(STRING_LIT);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParameterContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(BKOOLParser.IDENTIFIER, 0); }
		public TerminalNode COLON() { return getToken(BKOOLParser.COLON, 0); }
		public Element_typeContext element_type() {
			return getRuleContext(Element_typeContext.class,0);
		}
		public TerminalNode INHERIT() { return getToken(BKOOLParser.INHERIT, 0); }
		public TerminalNode OUT() { return getToken(BKOOLParser.OUT, 0); }
		public ParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter; }
	}

	public final ParameterContext parameter() throws RecognitionException {
		ParameterContext _localctx = new ParameterContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_parameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(248);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INHERIT:
				{
				setState(246);
				match(INHERIT);
				}
				break;
			case OUT:
			case IDENTIFIER:
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(252);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OUT:
				{
				setState(250);
				match(OUT);
				}
				break;
			case IDENTIFIER:
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(254);
			match(IDENTIFIER);
			setState(255);
			match(COLON);
			setState(256);
			element_type();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public List<Expression_1Context> expression_1() {
			return getRuleContexts(Expression_1Context.class);
		}
		public Expression_1Context expression_1(int i) {
			return getRuleContext(Expression_1Context.class,i);
		}
		public TerminalNode CONCAT() { return getToken(BKOOLParser.CONCAT, 0); }
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_expression);
		try {
			setState(263);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(258);
				expression_1();
				setState(259);
				match(CONCAT);
				setState(260);
				expression_1();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(262);
				expression_1();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expression_1Context extends ParserRuleContext {
		public List<Expression_2Context> expression_2() {
			return getRuleContexts(Expression_2Context.class);
		}
		public Expression_2Context expression_2(int i) {
			return getRuleContext(Expression_2Context.class,i);
		}
		public TerminalNode EQUAL_TO() { return getToken(BKOOLParser.EQUAL_TO, 0); }
		public TerminalNode NOT_EQUAL() { return getToken(BKOOLParser.NOT_EQUAL, 0); }
		public TerminalNode LESS() { return getToken(BKOOLParser.LESS, 0); }
		public TerminalNode GREATER() { return getToken(BKOOLParser.GREATER, 0); }
		public TerminalNode LTE() { return getToken(BKOOLParser.LTE, 0); }
		public TerminalNode GTE() { return getToken(BKOOLParser.GTE, 0); }
		public Expression_1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression_1; }
	}

	public final Expression_1Context expression_1() throws RecognitionException {
		Expression_1Context _localctx = new Expression_1Context(_ctx, getState());
		enterRule(_localctx, 40, RULE_expression_1);
		int _la;
		try {
			setState(270);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(265);
				expression_2(0);
				setState(266);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LESS) | (1L << GREATER) | (1L << LTE) | (1L << GTE) | (1L << EQUAL_TO) | (1L << NOT_EQUAL))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(267);
				expression_2(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(269);
				expression_2(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expression_2Context extends ParserRuleContext {
		public Expression_3Context expression_3() {
			return getRuleContext(Expression_3Context.class,0);
		}
		public Expression_2Context expression_2() {
			return getRuleContext(Expression_2Context.class,0);
		}
		public TerminalNode AND() { return getToken(BKOOLParser.AND, 0); }
		public TerminalNode OR() { return getToken(BKOOLParser.OR, 0); }
		public Expression_2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression_2; }
	}

	public final Expression_2Context expression_2() throws RecognitionException {
		return expression_2(0);
	}

	private Expression_2Context expression_2(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expression_2Context _localctx = new Expression_2Context(_ctx, _parentState);
		Expression_2Context _prevctx = _localctx;
		int _startState = 42;
		enterRecursionRule(_localctx, 42, RULE_expression_2, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(273);
			expression_3(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(280);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expression_2Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expression_2);
					setState(275);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(276);
					_la = _input.LA(1);
					if ( !(_la==AND || _la==OR) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(277);
					expression_3(0);
					}
					} 
				}
				setState(282);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Expression_3Context extends ParserRuleContext {
		public Expression_4Context expression_4() {
			return getRuleContext(Expression_4Context.class,0);
		}
		public Expression_3Context expression_3() {
			return getRuleContext(Expression_3Context.class,0);
		}
		public TerminalNode PLUS() { return getToken(BKOOLParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(BKOOLParser.MINUS, 0); }
		public Expression_3Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression_3; }
	}

	public final Expression_3Context expression_3() throws RecognitionException {
		return expression_3(0);
	}

	private Expression_3Context expression_3(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expression_3Context _localctx = new Expression_3Context(_ctx, _parentState);
		Expression_3Context _prevctx = _localctx;
		int _startState = 44;
		enterRecursionRule(_localctx, 44, RULE_expression_3, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(284);
			expression_4(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(291);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expression_3Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expression_3);
					setState(286);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(287);
					_la = _input.LA(1);
					if ( !(_la==PLUS || _la==MINUS) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(288);
					expression_4(0);
					}
					} 
				}
				setState(293);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Expression_4Context extends ParserRuleContext {
		public Expression_5Context expression_5() {
			return getRuleContext(Expression_5Context.class,0);
		}
		public Expression_4Context expression_4() {
			return getRuleContext(Expression_4Context.class,0);
		}
		public TerminalNode MUL() { return getToken(BKOOLParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(BKOOLParser.DIV, 0); }
		public TerminalNode MOD() { return getToken(BKOOLParser.MOD, 0); }
		public Expression_4Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression_4; }
	}

	public final Expression_4Context expression_4() throws RecognitionException {
		return expression_4(0);
	}

	private Expression_4Context expression_4(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expression_4Context _localctx = new Expression_4Context(_ctx, _parentState);
		Expression_4Context _prevctx = _localctx;
		int _startState = 46;
		enterRecursionRule(_localctx, 46, RULE_expression_4, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(295);
			expression_5();
			}
			_ctx.stop = _input.LT(-1);
			setState(302);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expression_4Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expression_4);
					setState(297);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(298);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << MUL) | (1L << DIV) | (1L << MOD))) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(299);
					expression_5();
					}
					} 
				}
				setState(304);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Expression_5Context extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(BKOOLParser.NOT, 0); }
		public Expression_5Context expression_5() {
			return getRuleContext(Expression_5Context.class,0);
		}
		public Expression_6Context expression_6() {
			return getRuleContext(Expression_6Context.class,0);
		}
		public Expression_5Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression_5; }
	}

	public final Expression_5Context expression_5() throws RecognitionException {
		Expression_5Context _localctx = new Expression_5Context(_ctx, getState());
		enterRule(_localctx, 48, RULE_expression_5);
		try {
			setState(308);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(305);
				match(NOT);
				setState(306);
				expression_5();
				}
				break;
			case INTEGER_LIT:
			case FLOAT_LIT:
			case BOOLEAN_LIT:
			case STRING_LIT:
			case MINUS:
			case LB:
			case LCB:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(307);
				expression_6();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expression_6Context extends ParserRuleContext {
		public TerminalNode MINUS() { return getToken(BKOOLParser.MINUS, 0); }
		public Expression_6Context expression_6() {
			return getRuleContext(Expression_6Context.class,0);
		}
		public Expression_7Context expression_7() {
			return getRuleContext(Expression_7Context.class,0);
		}
		public Expression_6Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression_6; }
	}

	public final Expression_6Context expression_6() throws RecognitionException {
		Expression_6Context _localctx = new Expression_6Context(_ctx, getState());
		enterRule(_localctx, 50, RULE_expression_6);
		try {
			setState(313);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MINUS:
				enterOuterAlt(_localctx, 1);
				{
				setState(310);
				match(MINUS);
				setState(311);
				expression_6();
				}
				break;
			case INTEGER_LIT:
			case FLOAT_LIT:
			case BOOLEAN_LIT:
			case STRING_LIT:
			case LB:
			case LCB:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(312);
				expression_7(0);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expression_7Context extends ParserRuleContext {
		public Expression_8Context expression_8() {
			return getRuleContext(Expression_8Context.class,0);
		}
		public Expression_7Context expression_7() {
			return getRuleContext(Expression_7Context.class,0);
		}
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public Expression_7Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression_7; }
	}

	public final Expression_7Context expression_7() throws RecognitionException {
		return expression_7(0);
	}

	private Expression_7Context expression_7(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expression_7Context _localctx = new Expression_7Context(_ctx, _parentState);
		Expression_7Context _prevctx = _localctx;
		int _startState = 52;
		enterRecursionRule(_localctx, 52, RULE_expression_7, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(316);
			expression_8();
			}
			_ctx.stop = _input.LT(-1);
			setState(322);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expression_7Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expression_7);
					setState(318);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(319);
					factor();
					}
					} 
				}
				setState(324);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Expression_8Context extends ParserRuleContext {
		public TerminalNode LB() { return getToken(BKOOLParser.LB, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RB() { return getToken(BKOOLParser.RB, 0); }
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public Expression_8Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression_8; }
	}

	public final Expression_8Context expression_8() throws RecognitionException {
		Expression_8Context _localctx = new Expression_8Context(_ctx, getState());
		enterRule(_localctx, 54, RULE_expression_8);
		try {
			setState(330);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LB:
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(325);
				match(LB);
				setState(326);
				expression();
				setState(327);
				match(RB);
				}
				}
				break;
			case INTEGER_LIT:
			case FLOAT_LIT:
			case BOOLEAN_LIT:
			case STRING_LIT:
			case LCB:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(329);
				factor();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FactorContext extends ParserRuleContext {
		public TerminalNode INTEGER_LIT() { return getToken(BKOOLParser.INTEGER_LIT, 0); }
		public TerminalNode FLOAT_LIT() { return getToken(BKOOLParser.FLOAT_LIT, 0); }
		public TerminalNode STRING_LIT() { return getToken(BKOOLParser.STRING_LIT, 0); }
		public TerminalNode IDENTIFIER() { return getToken(BKOOLParser.IDENTIFIER, 0); }
		public Function_callContext function_call() {
			return getRuleContext(Function_callContext.class,0);
		}
		public Array_listContext array_list() {
			return getRuleContext(Array_listContext.class,0);
		}
		public TerminalNode BOOLEAN_LIT() { return getToken(BKOOLParser.BOOLEAN_LIT, 0); }
		public TerminalNode LSB() { return getToken(BKOOLParser.LSB, 0); }
		public TerminalNode RSB() { return getToken(BKOOLParser.RSB, 0); }
		public Exp_list_type_intContext exp_list_type_int() {
			return getRuleContext(Exp_list_type_intContext.class,0);
		}
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_factor);
		try {
			setState(349);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(339);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
				case 1:
					{
					setState(332);
					match(INTEGER_LIT);
					}
					break;
				case 2:
					{
					setState(333);
					match(FLOAT_LIT);
					}
					break;
				case 3:
					{
					setState(334);
					match(STRING_LIT);
					}
					break;
				case 4:
					{
					setState(335);
					match(IDENTIFIER);
					}
					break;
				case 5:
					{
					setState(336);
					function_call();
					}
					break;
				case 6:
					{
					setState(337);
					array_list();
					}
					break;
				case 7:
					{
					setState(338);
					match(BOOLEAN_LIT);
					}
					break;
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(341);
				match(IDENTIFIER);
				setState(342);
				match(LSB);
				setState(345);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,28,_ctx) ) {
				case 1:
					{
					setState(343);
					exp_list_type_int();
					}
					break;
				case 2:
					{
					setState(344);
					factor();
					}
					break;
				}
				setState(347);
				match(RSB);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_callContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(BKOOLParser.IDENTIFIER, 0); }
		public TerminalNode LB() { return getToken(BKOOLParser.LB, 0); }
		public Exps_listContext exps_list() {
			return getRuleContext(Exps_listContext.class,0);
		}
		public TerminalNode RB() { return getToken(BKOOLParser.RB, 0); }
		public Function_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_call; }
	}

	public final Function_callContext function_call() throws RecognitionException {
		Function_callContext _localctx = new Function_callContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_function_call);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(351);
			match(IDENTIFIER);
			setState(352);
			match(LB);
			setState(353);
			exps_list();
			setState(354);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Exps_listContext extends ParserRuleContext {
		public Exp_listContext exp_list() {
			return getRuleContext(Exp_listContext.class,0);
		}
		public Exps_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exps_list; }
	}

	public final Exps_listContext exps_list() throws RecognitionException {
		Exps_listContext _localctx = new Exps_listContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_exps_list);
		try {
			setState(358);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTEGER_LIT:
			case FLOAT_LIT:
			case BOOLEAN_LIT:
			case STRING_LIT:
			case MINUS:
			case NOT:
			case LB:
			case LCB:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(356);
				exp_list();
				}
				break;
			case RB:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Exp_listContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(BKOOLParser.COMMA, 0); }
		public Exp_listContext exp_list() {
			return getRuleContext(Exp_listContext.class,0);
		}
		public Exp_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp_list; }
	}

	public final Exp_listContext exp_list() throws RecognitionException {
		Exp_listContext _localctx = new Exp_listContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_exp_list);
		try {
			setState(365);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(360);
				expression();
				setState(361);
				match(COMMA);
				setState(362);
				exp_list();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(364);
				expression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public Assign_stmtContext assign_stmt() {
			return getRuleContext(Assign_stmtContext.class,0);
		}
		public If_stmtContext if_stmt() {
			return getRuleContext(If_stmtContext.class,0);
		}
		public For_stmtContext for_stmt() {
			return getRuleContext(For_stmtContext.class,0);
		}
		public While_stmtContext while_stmt() {
			return getRuleContext(While_stmtContext.class,0);
		}
		public Do_while_stmtContext do_while_stmt() {
			return getRuleContext(Do_while_stmtContext.class,0);
		}
		public Block_stmtContext block_stmt() {
			return getRuleContext(Block_stmtContext.class,0);
		}
		public Return_stmtContext return_stmt() {
			return getRuleContext(Return_stmtContext.class,0);
		}
		public Continue_stmtContext continue_stmt() {
			return getRuleContext(Continue_stmtContext.class,0);
		}
		public Break_stmtContext break_stmt() {
			return getRuleContext(Break_stmtContext.class,0);
		}
		public Call_stmtContext call_stmt() {
			return getRuleContext(Call_stmtContext.class,0);
		}
		public Variable_declContext variable_decl() {
			return getRuleContext(Variable_declContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_statement);
		try {
			setState(378);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,32,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(367);
				assign_stmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(368);
				if_stmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(369);
				for_stmt();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(370);
				while_stmt();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(371);
				do_while_stmt();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(372);
				block_stmt();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(373);
				return_stmt();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(374);
				continue_stmt();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(375);
				break_stmt();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(376);
				call_stmt();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(377);
				variable_decl();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Assign_stmtContext extends ParserRuleContext {
		public LhsContext lhs() {
			return getRuleContext(LhsContext.class,0);
		}
		public TerminalNode EQUAL() { return getToken(BKOOLParser.EQUAL, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKOOLParser.SEMI, 0); }
		public Assign_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_stmt; }
	}

	public final Assign_stmtContext assign_stmt() throws RecognitionException {
		Assign_stmtContext _localctx = new Assign_stmtContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_assign_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(380);
			lhs();
			setState(381);
			match(EQUAL);
			setState(382);
			expression();
			setState(383);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LhsContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(BKOOLParser.IDENTIFIER, 0); }
		public TerminalNode LSB() { return getToken(BKOOLParser.LSB, 0); }
		public Exp_list_type_intContext exp_list_type_int() {
			return getRuleContext(Exp_list_type_intContext.class,0);
		}
		public TerminalNode RSB() { return getToken(BKOOLParser.RSB, 0); }
		public LhsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lhs; }
	}

	public final LhsContext lhs() throws RecognitionException {
		LhsContext _localctx = new LhsContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_lhs);
		try {
			setState(391);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,33,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(385);
				match(IDENTIFIER);
				setState(386);
				match(LSB);
				setState(387);
				exp_list_type_int();
				setState(388);
				match(RSB);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(390);
				match(IDENTIFIER);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_stmtContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(BKOOLParser.IF, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(BKOOLParser.ELSE, 0); }
		public If_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_stmt; }
	}

	public final If_stmtContext if_stmt() throws RecognitionException {
		If_stmtContext _localctx = new If_stmtContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_if_stmt);
		try {
			setState(403);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,34,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(393);
				match(IF);
				setState(394);
				expression();
				setState(395);
				statement();
				setState(396);
				match(ELSE);
				setState(397);
				statement();
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(399);
				match(IF);
				setState(400);
				expression();
				setState(401);
				statement();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class For_stmtContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(BKOOLParser.FOR, 0); }
		public TerminalNode LB() { return getToken(BKOOLParser.LB, 0); }
		public List<TerminalNode> COMMA() { return getTokens(BKOOLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKOOLParser.COMMA, i);
		}
		public TerminalNode RB() { return getToken(BKOOLParser.RB, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public Init_exprContext init_expr() {
			return getRuleContext(Init_exprContext.class,0);
		}
		public Condition_exprContext condition_expr() {
			return getRuleContext(Condition_exprContext.class,0);
		}
		public Update_exprContext update_expr() {
			return getRuleContext(Update_exprContext.class,0);
		}
		public For_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_stmt; }
	}

	public final For_stmtContext for_stmt() throws RecognitionException {
		For_stmtContext _localctx = new For_stmtContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_for_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(405);
			match(FOR);
			setState(406);
			match(LB);
			setState(409);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				{
				setState(407);
				init_expr();
				}
				break;
			case COMMA:
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(411);
			match(COMMA);
			setState(414);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				{
				setState(412);
				condition_expr();
				}
				break;
			case COMMA:
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(416);
			match(COMMA);
			setState(419);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				{
				setState(417);
				update_expr();
				}
				break;
			case RB:
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(421);
			match(RB);
			setState(422);
			statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Init_exprContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(BKOOLParser.IDENTIFIER, 0); }
		public TerminalNode EQUAL() { return getToken(BKOOLParser.EQUAL, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Init_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_init_expr; }
	}

	public final Init_exprContext init_expr() throws RecognitionException {
		Init_exprContext _localctx = new Init_exprContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_init_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(424);
			match(IDENTIFIER);
			setState(425);
			match(EQUAL);
			setState(426);
			expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Condition_exprContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(BKOOLParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(BKOOLParser.IDENTIFIER, i);
		}
		public TerminalNode LESS() { return getToken(BKOOLParser.LESS, 0); }
		public TerminalNode GREATER() { return getToken(BKOOLParser.GREATER, 0); }
		public TerminalNode LTE() { return getToken(BKOOLParser.LTE, 0); }
		public TerminalNode GTE() { return getToken(BKOOLParser.GTE, 0); }
		public TerminalNode NOT_EQUAL() { return getToken(BKOOLParser.NOT_EQUAL, 0); }
		public TerminalNode EQUAL_TO() { return getToken(BKOOLParser.EQUAL_TO, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Condition_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition_expr; }
	}

	public final Condition_exprContext condition_expr() throws RecognitionException {
		Condition_exprContext _localctx = new Condition_exprContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_condition_expr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(428);
			match(IDENTIFIER);
			setState(429);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LESS) | (1L << GREATER) | (1L << LTE) | (1L << GTE) | (1L << EQUAL_TO) | (1L << NOT_EQUAL))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(432);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,38,_ctx) ) {
			case 1:
				{
				setState(430);
				match(IDENTIFIER);
				}
				break;
			case 2:
				{
				setState(431);
				expression();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Update_exprContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(BKOOLParser.IDENTIFIER, 0); }
		public TerminalNode EQUAL() { return getToken(BKOOLParser.EQUAL, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Update_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_update_expr; }
	}

	public final Update_exprContext update_expr() throws RecognitionException {
		Update_exprContext _localctx = new Update_exprContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_update_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(434);
			match(IDENTIFIER);
			setState(435);
			match(EQUAL);
			setState(436);
			expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class While_stmtContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(BKOOLParser.WHILE, 0); }
		public TerminalNode LB() { return getToken(BKOOLParser.LB, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RB() { return getToken(BKOOLParser.RB, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public While_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_stmt; }
	}

	public final While_stmtContext while_stmt() throws RecognitionException {
		While_stmtContext _localctx = new While_stmtContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_while_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(438);
			match(WHILE);
			setState(439);
			match(LB);
			setState(440);
			expression();
			setState(441);
			match(RB);
			setState(442);
			statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Do_while_stmtContext extends ParserRuleContext {
		public TerminalNode DO() { return getToken(BKOOLParser.DO, 0); }
		public Block_stmtContext block_stmt() {
			return getRuleContext(Block_stmtContext.class,0);
		}
		public TerminalNode WHILE() { return getToken(BKOOLParser.WHILE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKOOLParser.SEMI, 0); }
		public Do_while_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_do_while_stmt; }
	}

	public final Do_while_stmtContext do_while_stmt() throws RecognitionException {
		Do_while_stmtContext _localctx = new Do_while_stmtContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_do_while_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(444);
			match(DO);
			setState(445);
			block_stmt();
			setState(446);
			match(WHILE);
			setState(447);
			expression();
			setState(448);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Call_stmtContext extends ParserRuleContext {
		public TerminalNode SEMI() { return getToken(BKOOLParser.SEMI, 0); }
		public Function_callContext function_call() {
			return getRuleContext(Function_callContext.class,0);
		}
		public S_func_declContext s_func_decl() {
			return getRuleContext(S_func_declContext.class,0);
		}
		public Call_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call_stmt; }
	}

	public final Call_stmtContext call_stmt() throws RecognitionException {
		Call_stmtContext _localctx = new Call_stmtContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_call_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(452);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				{
				setState(450);
				function_call();
				}
				break;
			case T__0:
			case T__1:
			case T__2:
			case T__3:
			case T__4:
			case T__5:
			case T__6:
			case T__7:
			case T__8:
				{
				setState(451);
				s_func_decl();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(454);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Block_stmtContext extends ParserRuleContext {
		public TerminalNode LCB() { return getToken(BKOOLParser.LCB, 0); }
		public Statement_termContext statement_term() {
			return getRuleContext(Statement_termContext.class,0);
		}
		public TerminalNode RCB() { return getToken(BKOOLParser.RCB, 0); }
		public Block_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block_stmt; }
	}

	public final Block_stmtContext block_stmt() throws RecognitionException {
		Block_stmtContext _localctx = new Block_stmtContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_block_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(456);
			match(LCB);
			setState(457);
			statement_term();
			setState(458);
			match(RCB);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Statement_termContext extends ParserRuleContext {
		public Statement_listContext statement_list() {
			return getRuleContext(Statement_listContext.class,0);
		}
		public Statement_termContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement_term; }
	}

	public final Statement_termContext statement_term() throws RecognitionException {
		Statement_termContext _localctx = new Statement_termContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_statement_term);
		try {
			setState(462);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
			case T__1:
			case T__2:
			case T__3:
			case T__4:
			case T__5:
			case T__6:
			case T__7:
			case T__8:
			case BREAK:
			case RETURN:
			case FOR:
			case CONTINUE:
			case DO:
			case IF:
			case WHILE:
			case LCB:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(460);
				statement_list();
				}
				break;
			case RCB:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Statement_listContext extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public Statement_listContext statement_list() {
			return getRuleContext(Statement_listContext.class,0);
		}
		public Statement_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement_list; }
	}

	public final Statement_listContext statement_list() throws RecognitionException {
		Statement_listContext _localctx = new Statement_listContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_statement_list);
		try {
			setState(468);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,41,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(464);
				statement();
				setState(465);
				statement_list();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(467);
				statement();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Break_stmtContext extends ParserRuleContext {
		public TerminalNode BREAK() { return getToken(BKOOLParser.BREAK, 0); }
		public TerminalNode SEMI() { return getToken(BKOOLParser.SEMI, 0); }
		public Break_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_break_stmt; }
	}

	public final Break_stmtContext break_stmt() throws RecognitionException {
		Break_stmtContext _localctx = new Break_stmtContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_break_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(470);
			match(BREAK);
			setState(471);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Continue_stmtContext extends ParserRuleContext {
		public TerminalNode CONTINUE() { return getToken(BKOOLParser.CONTINUE, 0); }
		public TerminalNode SEMI() { return getToken(BKOOLParser.SEMI, 0); }
		public Continue_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continue_stmt; }
	}

	public final Continue_stmtContext continue_stmt() throws RecognitionException {
		Continue_stmtContext _localctx = new Continue_stmtContext(_ctx, getState());
		enterRule(_localctx, 94, RULE_continue_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(473);
			match(CONTINUE);
			setState(474);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Return_stmtContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(BKOOLParser.RETURN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKOOLParser.SEMI, 0); }
		public Return_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_stmt; }
	}

	public final Return_stmtContext return_stmt() throws RecognitionException {
		Return_stmtContext _localctx = new Return_stmtContext(_ctx, getState());
		enterRule(_localctx, 96, RULE_return_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(476);
			match(RETURN);
			setState(477);
			expression();
			setState(478);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_declContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(BKOOLParser.IDENTIFIER, 0); }
		public TerminalNode COLON() { return getToken(BKOOLParser.COLON, 0); }
		public TerminalNode FUNCTION() { return getToken(BKOOLParser.FUNCTION, 0); }
		public Return_typeContext return_type() {
			return getRuleContext(Return_typeContext.class,0);
		}
		public TerminalNode LB() { return getToken(BKOOLParser.LB, 0); }
		public Paramter_listContext paramter_list() {
			return getRuleContext(Paramter_listContext.class,0);
		}
		public TerminalNode RB() { return getToken(BKOOLParser.RB, 0); }
		public InheritanceContext inheritance() {
			return getRuleContext(InheritanceContext.class,0);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public Function_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_decl; }
	}

	public final Function_declContext function_decl() throws RecognitionException {
		Function_declContext _localctx = new Function_declContext(_ctx, getState());
		enterRule(_localctx, 98, RULE_function_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(480);
			match(IDENTIFIER);
			setState(481);
			match(COLON);
			setState(482);
			match(FUNCTION);
			setState(483);
			return_type();
			setState(484);
			match(LB);
			setState(485);
			paramter_list();
			setState(486);
			match(RB);
			setState(487);
			inheritance();
			setState(488);
			statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InheritanceContext extends ParserRuleContext {
		public TerminalNode INHERIT() { return getToken(BKOOLParser.INHERIT, 0); }
		public Function_nameContext function_name() {
			return getRuleContext(Function_nameContext.class,0);
		}
		public InheritanceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inheritance; }
	}

	public final InheritanceContext inheritance() throws RecognitionException {
		InheritanceContext _localctx = new InheritanceContext(_ctx, getState());
		enterRule(_localctx, 100, RULE_inheritance);
		try {
			setState(493);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INHERIT:
				enterOuterAlt(_localctx, 1);
				{
				setState(490);
				match(INHERIT);
				setState(491);
				function_name();
				}
				break;
			case T__0:
			case T__1:
			case T__2:
			case T__3:
			case T__4:
			case T__5:
			case T__6:
			case T__7:
			case T__8:
			case BREAK:
			case RETURN:
			case FOR:
			case CONTINUE:
			case DO:
			case IF:
			case WHILE:
			case LCB:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_nameContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(BKOOLParser.IDENTIFIER, 0); }
		public Function_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_name; }
	}

	public final Function_nameContext function_name() throws RecognitionException {
		Function_nameContext _localctx = new Function_nameContext(_ctx, getState());
		enterRule(_localctx, 102, RULE_function_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(495);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Paramter_listContext extends ParserRuleContext {
		public Paramter_list_termContext paramter_list_term() {
			return getRuleContext(Paramter_list_termContext.class,0);
		}
		public Paramter_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramter_list; }
	}

	public final Paramter_listContext paramter_list() throws RecognitionException {
		Paramter_listContext _localctx = new Paramter_listContext(_ctx, getState());
		enterRule(_localctx, 104, RULE_paramter_list);
		try {
			setState(499);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OUT:
			case INHERIT:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(497);
				paramter_list_term();
				}
				break;
			case RB:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Paramter_list_termContext extends ParserRuleContext {
		public ParameterContext parameter() {
			return getRuleContext(ParameterContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(BKOOLParser.COMMA, 0); }
		public Paramter_list_termContext paramter_list_term() {
			return getRuleContext(Paramter_list_termContext.class,0);
		}
		public Paramter_list_termContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramter_list_term; }
	}

	public final Paramter_list_termContext paramter_list_term() throws RecognitionException {
		Paramter_list_termContext _localctx = new Paramter_list_termContext(_ctx, getState());
		enterRule(_localctx, 106, RULE_paramter_list_term);
		try {
			setState(506);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,44,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(501);
				parameter();
				setState(502);
				match(COMMA);
				setState(503);
				paramter_list_term();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(505);
				parameter();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Return_typeContext extends ParserRuleContext {
		public TerminalNode INTEGER() { return getToken(BKOOLParser.INTEGER, 0); }
		public TerminalNode FLOAT() { return getToken(BKOOLParser.FLOAT, 0); }
		public TerminalNode BOOLEAN() { return getToken(BKOOLParser.BOOLEAN, 0); }
		public TerminalNode STRING() { return getToken(BKOOLParser.STRING, 0); }
		public TerminalNode VOID() { return getToken(BKOOLParser.VOID, 0); }
		public TerminalNode AUTO() { return getToken(BKOOLParser.AUTO, 0); }
		public Return_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_type; }
	}

	public final Return_typeContext return_type() throws RecognitionException {
		Return_typeContext _localctx = new Return_typeContext(_ctx, getState());
		enterRule(_localctx, 108, RULE_return_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(508);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << AUTO) | (1L << INTEGER) | (1L << VOID) | (1L << FLOAT) | (1L << BOOLEAN) | (1L << STRING))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class S_func_declContext extends ParserRuleContext {
		public Read_integerContext read_integer() {
			return getRuleContext(Read_integerContext.class,0);
		}
		public Print_integerContext print_integer() {
			return getRuleContext(Print_integerContext.class,0);
		}
		public Read_floatContext read_float() {
			return getRuleContext(Read_floatContext.class,0);
		}
		public Write_floatContext write_float() {
			return getRuleContext(Write_floatContext.class,0);
		}
		public Print_booleanContext print_boolean() {
			return getRuleContext(Print_booleanContext.class,0);
		}
		public Read_stringContext read_string() {
			return getRuleContext(Read_stringContext.class,0);
		}
		public Print_stringContext print_string() {
			return getRuleContext(Print_stringContext.class,0);
		}
		public Super_Context super_() {
			return getRuleContext(Super_Context.class,0);
		}
		public Prevent_defaultContext prevent_default() {
			return getRuleContext(Prevent_defaultContext.class,0);
		}
		public S_func_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_s_func_decl; }
	}

	public final S_func_declContext s_func_decl() throws RecognitionException {
		S_func_declContext _localctx = new S_func_declContext(_ctx, getState());
		enterRule(_localctx, 110, RULE_s_func_decl);
		try {
			setState(519);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				enterOuterAlt(_localctx, 1);
				{
				setState(510);
				read_integer();
				}
				break;
			case T__1:
				enterOuterAlt(_localctx, 2);
				{
				setState(511);
				print_integer();
				}
				break;
			case T__2:
				enterOuterAlt(_localctx, 3);
				{
				setState(512);
				read_float();
				}
				break;
			case T__3:
				enterOuterAlt(_localctx, 4);
				{
				setState(513);
				write_float();
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 5);
				{
				setState(514);
				print_boolean();
				}
				break;
			case T__5:
				enterOuterAlt(_localctx, 6);
				{
				setState(515);
				read_string();
				}
				break;
			case T__6:
				enterOuterAlt(_localctx, 7);
				{
				setState(516);
				print_string();
				}
				break;
			case T__7:
				enterOuterAlt(_localctx, 8);
				{
				setState(517);
				super_();
				}
				break;
			case T__8:
				enterOuterAlt(_localctx, 9);
				{
				setState(518);
				prevent_default();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Read_integerContext extends ParserRuleContext {
		public TerminalNode LB() { return getToken(BKOOLParser.LB, 0); }
		public TerminalNode RB() { return getToken(BKOOLParser.RB, 0); }
		public Read_integerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_read_integer; }
	}

	public final Read_integerContext read_integer() throws RecognitionException {
		Read_integerContext _localctx = new Read_integerContext(_ctx, getState());
		enterRule(_localctx, 112, RULE_read_integer);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(521);
			match(T__0);
			setState(522);
			match(LB);
			setState(523);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Print_integerContext extends ParserRuleContext {
		public TerminalNode LB() { return getToken(BKOOLParser.LB, 0); }
		public TerminalNode RB() { return getToken(BKOOLParser.RB, 0); }
		public TerminalNode INTEGER_LIT() { return getToken(BKOOLParser.INTEGER_LIT, 0); }
		public TerminalNode IDENTIFIER() { return getToken(BKOOLParser.IDENTIFIER, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Print_integerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print_integer; }
	}

	public final Print_integerContext print_integer() throws RecognitionException {
		Print_integerContext _localctx = new Print_integerContext(_ctx, getState());
		enterRule(_localctx, 114, RULE_print_integer);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(525);
			match(T__1);
			setState(526);
			match(LB);
			setState(530);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,46,_ctx) ) {
			case 1:
				{
				setState(527);
				match(INTEGER_LIT);
				}
				break;
			case 2:
				{
				setState(528);
				match(IDENTIFIER);
				}
				break;
			case 3:
				{
				setState(529);
				expression();
				}
				break;
			}
			setState(532);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Read_floatContext extends ParserRuleContext {
		public TerminalNode LB() { return getToken(BKOOLParser.LB, 0); }
		public TerminalNode RB() { return getToken(BKOOLParser.RB, 0); }
		public Read_floatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_read_float; }
	}

	public final Read_floatContext read_float() throws RecognitionException {
		Read_floatContext _localctx = new Read_floatContext(_ctx, getState());
		enterRule(_localctx, 116, RULE_read_float);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(534);
			match(T__2);
			setState(535);
			match(LB);
			setState(536);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Write_floatContext extends ParserRuleContext {
		public TerminalNode LB() { return getToken(BKOOLParser.LB, 0); }
		public TerminalNode RB() { return getToken(BKOOLParser.RB, 0); }
		public TerminalNode FLOAT_LIT() { return getToken(BKOOLParser.FLOAT_LIT, 0); }
		public TerminalNode IDENTIFIER() { return getToken(BKOOLParser.IDENTIFIER, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Write_floatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_write_float; }
	}

	public final Write_floatContext write_float() throws RecognitionException {
		Write_floatContext _localctx = new Write_floatContext(_ctx, getState());
		enterRule(_localctx, 118, RULE_write_float);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(538);
			match(T__3);
			setState(539);
			match(LB);
			setState(543);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,47,_ctx) ) {
			case 1:
				{
				setState(540);
				match(FLOAT_LIT);
				}
				break;
			case 2:
				{
				setState(541);
				match(IDENTIFIER);
				}
				break;
			case 3:
				{
				setState(542);
				expression();
				}
				break;
			}
			setState(545);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Print_booleanContext extends ParserRuleContext {
		public TerminalNode LB() { return getToken(BKOOLParser.LB, 0); }
		public TerminalNode RB() { return getToken(BKOOLParser.RB, 0); }
		public TerminalNode BOOLEAN_LIT() { return getToken(BKOOLParser.BOOLEAN_LIT, 0); }
		public TerminalNode IDENTIFIER() { return getToken(BKOOLParser.IDENTIFIER, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Print_booleanContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print_boolean; }
	}

	public final Print_booleanContext print_boolean() throws RecognitionException {
		Print_booleanContext _localctx = new Print_booleanContext(_ctx, getState());
		enterRule(_localctx, 120, RULE_print_boolean);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(547);
			match(T__4);
			setState(548);
			match(LB);
			setState(552);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,48,_ctx) ) {
			case 1:
				{
				setState(549);
				match(BOOLEAN_LIT);
				}
				break;
			case 2:
				{
				setState(550);
				match(IDENTIFIER);
				}
				break;
			case 3:
				{
				setState(551);
				expression();
				}
				break;
			}
			setState(554);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Read_stringContext extends ParserRuleContext {
		public TerminalNode LB() { return getToken(BKOOLParser.LB, 0); }
		public TerminalNode RB() { return getToken(BKOOLParser.RB, 0); }
		public Read_stringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_read_string; }
	}

	public final Read_stringContext read_string() throws RecognitionException {
		Read_stringContext _localctx = new Read_stringContext(_ctx, getState());
		enterRule(_localctx, 122, RULE_read_string);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(556);
			match(T__5);
			setState(557);
			match(LB);
			setState(558);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Print_stringContext extends ParserRuleContext {
		public TerminalNode LB() { return getToken(BKOOLParser.LB, 0); }
		public TerminalNode RB() { return getToken(BKOOLParser.RB, 0); }
		public TerminalNode STRING_LIT() { return getToken(BKOOLParser.STRING_LIT, 0); }
		public TerminalNode IDENTIFIER() { return getToken(BKOOLParser.IDENTIFIER, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Print_stringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print_string; }
	}

	public final Print_stringContext print_string() throws RecognitionException {
		Print_stringContext _localctx = new Print_stringContext(_ctx, getState());
		enterRule(_localctx, 124, RULE_print_string);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(560);
			match(T__6);
			setState(561);
			match(LB);
			setState(565);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,49,_ctx) ) {
			case 1:
				{
				setState(562);
				match(STRING_LIT);
				}
				break;
			case 2:
				{
				setState(563);
				match(IDENTIFIER);
				}
				break;
			case 3:
				{
				setState(564);
				expression();
				}
				break;
			}
			setState(567);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Super_Context extends ParserRuleContext {
		public TerminalNode LB() { return getToken(BKOOLParser.LB, 0); }
		public Expression_listContext expression_list() {
			return getRuleContext(Expression_listContext.class,0);
		}
		public TerminalNode RB() { return getToken(BKOOLParser.RB, 0); }
		public Super_Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_super_; }
	}

	public final Super_Context super_() throws RecognitionException {
		Super_Context _localctx = new Super_Context(_ctx, getState());
		enterRule(_localctx, 126, RULE_super_);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(569);
			match(T__7);
			setState(570);
			match(LB);
			setState(571);
			expression_list();
			setState(572);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Prevent_defaultContext extends ParserRuleContext {
		public TerminalNode LB() { return getToken(BKOOLParser.LB, 0); }
		public TerminalNode RB() { return getToken(BKOOLParser.RB, 0); }
		public Prevent_defaultContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prevent_default; }
	}

	public final Prevent_defaultContext prevent_default() throws RecognitionException {
		Prevent_defaultContext _localctx = new Prevent_defaultContext(_ctx, getState());
		enterRule(_localctx, 128, RULE_prevent_default);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(574);
			match(T__8);
			setState(575);
			match(LB);
			setState(576);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 21:
			return expression_2_sempred((Expression_2Context)_localctx, predIndex);
		case 22:
			return expression_3_sempred((Expression_3Context)_localctx, predIndex);
		case 23:
			return expression_4_sempred((Expression_4Context)_localctx, predIndex);
		case 26:
			return expression_7_sempred((Expression_7Context)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_2_sempred(Expression_2Context _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expression_3_sempred(Expression_3Context _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expression_4_sempred(Expression_4Context _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expression_7_sempred(Expression_7Context _localctx, int predIndex) {
		switch (predIndex) {
		case 3:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F\u0245\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\6\2\u0086\n\2\r\2\16\2\u0087\3\2\3"+
		"\2\3\3\3\3\5\3\u008e\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\5"+
		"\6\u009b\n\6\3\7\3\7\3\7\3\7\5\7\u00a1\n\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t"+
		"\5\t\u00aa\n\t\3\n\3\n\3\n\3\n\5\n\u00b0\n\n\3\n\3\n\3\13\3\13\3\13\3"+
		"\13\3\13\3\13\5\13\u00ba\n\13\3\13\3\13\5\13\u00be\n\13\3\13\3\13\3\13"+
		"\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00c9\n\f\3\f\3\f\5\f\u00cd\n\f\3\f\3\f\3"+
		"\f\3\r\3\r\3\r\3\r\3\16\3\16\5\16\u00d8\n\16\3\17\3\17\3\17\3\17\5\17"+
		"\u00de\n\17\3\20\3\20\3\20\3\20\3\20\5\20\u00e5\n\20\3\21\3\21\3\21\3"+
		"\21\5\21\u00eb\n\21\3\22\3\22\3\22\3\22\5\22\u00f1\n\22\3\23\3\23\3\23"+
		"\3\23\5\23\u00f7\n\23\3\24\3\24\5\24\u00fb\n\24\3\24\3\24\5\24\u00ff\n"+
		"\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\5\25\u010a\n\25\3\26"+
		"\3\26\3\26\3\26\3\26\5\26\u0111\n\26\3\27\3\27\3\27\3\27\3\27\3\27\7\27"+
		"\u0119\n\27\f\27\16\27\u011c\13\27\3\30\3\30\3\30\3\30\3\30\3\30\7\30"+
		"\u0124\n\30\f\30\16\30\u0127\13\30\3\31\3\31\3\31\3\31\3\31\3\31\7\31"+
		"\u012f\n\31\f\31\16\31\u0132\13\31\3\32\3\32\3\32\5\32\u0137\n\32\3\33"+
		"\3\33\3\33\5\33\u013c\n\33\3\34\3\34\3\34\3\34\3\34\7\34\u0143\n\34\f"+
		"\34\16\34\u0146\13\34\3\35\3\35\3\35\3\35\3\35\5\35\u014d\n\35\3\36\3"+
		"\36\3\36\3\36\3\36\3\36\3\36\5\36\u0156\n\36\3\36\3\36\3\36\3\36\5\36"+
		"\u015c\n\36\3\36\3\36\5\36\u0160\n\36\3\37\3\37\3\37\3\37\3\37\3 \3 \5"+
		" \u0169\n \3!\3!\3!\3!\3!\5!\u0170\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\""+
		"\3\"\3\"\3\"\5\"\u017d\n\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\5$\u018a\n"+
		"$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u0196\n%\3&\3&\3&\3&\5&\u019c\n&\3"+
		"&\3&\3&\5&\u01a1\n&\3&\3&\3&\5&\u01a6\n&\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3"+
		"(\3(\3(\5(\u01b3\n(\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3"+
		",\3,\5,\u01c7\n,\3,\3,\3-\3-\3-\3-\3.\3.\5.\u01d1\n.\3/\3/\3/\3/\5/\u01d7"+
		"\n/\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3"+
		"\63\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\5\64\u01f0\n\64\3\65"+
		"\3\65\3\66\3\66\5\66\u01f6\n\66\3\67\3\67\3\67\3\67\3\67\5\67\u01fd\n"+
		"\67\38\38\39\39\39\39\39\39\39\39\39\59\u020a\n9\3:\3:\3:\3:\3;\3;\3;"+
		"\3;\3;\5;\u0215\n;\3;\3;\3<\3<\3<\3<\3=\3=\3=\3=\3=\5=\u0222\n=\3=\3="+
		"\3>\3>\3>\3>\3>\5>\u022b\n>\3>\3>\3?\3?\3?\3?\3@\3@\3@\3@\3@\5@\u0238"+
		"\n@\3@\3@\3A\3A\3A\3A\3A\3B\3B\3B\3B\3B\2\6,.\60\66C\2\4\6\b\n\f\16\20"+
		"\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhj"+
		"lnprtvxz|~\u0080\u0082\2\b\7\2\25\25\27\27\32\32\35\35\37\37\4\2-\60\64"+
		"\65\3\2\62\63\3\2()\3\2*,\7\2\25\25\27\30\32\32\35\35\37\37\2\u024e\2"+
		"\u0085\3\2\2\2\4\u008d\3\2\2\2\6\u008f\3\2\2\2\b\u0096\3\2\2\2\n\u009a"+
		"\3\2\2\2\f\u00a0\3\2\2\2\16\u00a2\3\2\2\2\20\u00a9\3\2\2\2\22\u00ab\3"+
		"\2\2\2\24\u00b3\3\2\2\2\26\u00c2\3\2\2\2\30\u00d1\3\2\2\2\32\u00d7\3\2"+
		"\2\2\34\u00dd\3\2\2\2\36\u00e4\3\2\2\2 \u00ea\3\2\2\2\"\u00f0\3\2\2\2"+
		"$\u00f6\3\2\2\2&\u00fa\3\2\2\2(\u0109\3\2\2\2*\u0110\3\2\2\2,\u0112\3"+
		"\2\2\2.\u011d\3\2\2\2\60\u0128\3\2\2\2\62\u0136\3\2\2\2\64\u013b\3\2\2"+
		"\2\66\u013d\3\2\2\28\u014c\3\2\2\2:\u015f\3\2\2\2<\u0161\3\2\2\2>\u0168"+
		"\3\2\2\2@\u016f\3\2\2\2B\u017c\3\2\2\2D\u017e\3\2\2\2F\u0189\3\2\2\2H"+
		"\u0195\3\2\2\2J\u0197\3\2\2\2L\u01aa\3\2\2\2N\u01ae\3\2\2\2P\u01b4\3\2"+
		"\2\2R\u01b8\3\2\2\2T\u01be\3\2\2\2V\u01c6\3\2\2\2X\u01ca\3\2\2\2Z\u01d0"+
		"\3\2\2\2\\\u01d6\3\2\2\2^\u01d8\3\2\2\2`\u01db\3\2\2\2b\u01de\3\2\2\2"+
		"d\u01e2\3\2\2\2f\u01ef\3\2\2\2h\u01f1\3\2\2\2j\u01f5\3\2\2\2l\u01fc\3"+
		"\2\2\2n\u01fe\3\2\2\2p\u0209\3\2\2\2r\u020b\3\2\2\2t\u020f\3\2\2\2v\u0218"+
		"\3\2\2\2x\u021c\3\2\2\2z\u0225\3\2\2\2|\u022e\3\2\2\2~\u0232\3\2\2\2\u0080"+
		"\u023b\3\2\2\2\u0082\u0240\3\2\2\2\u0084\u0086\5\4\3\2\u0085\u0084\3\2"+
		"\2\2\u0086\u0087\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088"+
		"\u0089\3\2\2\2\u0089\u008a\7\2\2\3\u008a\3\3\2\2\2\u008b\u008e\5\20\t"+
		"\2\u008c\u008e\5d\63\2\u008d\u008b\3\2\2\2\u008d\u008c\3\2\2\2\u008e\5"+
		"\3\2\2\2\u008f\u0090\7\31\2\2\u0090\u0091\7>\2\2\u0091\u0092\5\n\6\2\u0092"+
		"\u0093\7?\2\2\u0093\u0094\7#\2\2\u0094\u0095\5\b\5\2\u0095\7\3\2\2\2\u0096"+
		"\u0097\t\2\2\2\u0097\t\3\2\2\2\u0098\u009b\5\f\7\2\u0099\u009b\5\16\b"+
		"\2\u009a\u0098\3\2\2\2\u009a\u0099\3\2\2\2\u009b\13\3\2\2\2\u009c\u009d"+
		"\7\r\2\2\u009d\u009e\78\2\2\u009e\u00a1\5\f\7\2\u009f\u00a1\7\r\2\2\u00a0"+
		"\u009c\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1\r\3\2\2\2\u00a2\u00a3\7\16\2"+
		"\2\u00a3\u00a4\78\2\2\u00a4\u00a5\5\16\b\2\u00a5\u00a6\7\16\2\2\u00a6"+
		"\17\3\2\2\2\u00a7\u00aa\5\22\n\2\u00a8\u00aa\5\24\13\2\u00a9\u00a7\3\2"+
		"\2\2\u00a9\u00a8\3\2\2\2\u00aa\21\3\2\2\2\u00ab\u00ac\5\34\17\2\u00ac"+
		"\u00af\7;\2\2\u00ad\u00b0\5\b\5\2\u00ae\u00b0\5\6\4\2\u00af\u00ad\3\2"+
		"\2\2\u00af\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\79\2\2\u00b2"+
		"\23\3\2\2\2\u00b3\u00bd\7B\2\2\u00b4\u00b5\78\2\2\u00b5\u00be\5\26\f\2"+
		"\u00b6\u00b9\7;\2\2\u00b7\u00ba\5\b\5\2\u00b8\u00ba\5\6\4\2\u00b9\u00b7"+
		"\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\7:\2\2\u00bc"+
		"\u00be\3\2\2\2\u00bd\u00b4\3\2\2\2\u00bd\u00b6\3\2\2\2\u00be\u00bf\3\2"+
		"\2\2\u00bf\u00c0\5(\25\2\u00c0\u00c1\79\2\2\u00c1\25\3\2\2\2\u00c2\u00cc"+
		"\7B\2\2\u00c3\u00c4\78\2\2\u00c4\u00cd\5\26\f\2\u00c5\u00c8\7;\2\2\u00c6"+
		"\u00c9\5\b\5\2\u00c7\u00c9\5\6\4\2\u00c8\u00c6\3\2\2\2\u00c8\u00c7\3\2"+
		"\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cb\7:\2\2\u00cb\u00cd\3\2\2\2\u00cc"+
		"\u00c3\3\2\2\2\u00cc\u00c5\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cf\5("+
		"\25\2\u00cf\u00d0\78\2\2\u00d0\27\3\2\2\2\u00d1\u00d2\7@\2\2\u00d2\u00d3"+
		"\5\32\16\2\u00d3\u00d4\7A\2\2\u00d4\31\3\2\2\2\u00d5\u00d8\5\36\20\2\u00d6"+
		"\u00d8\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7\u00d6\3\2\2\2\u00d8\33\3\2\2"+
		"\2\u00d9\u00da\7B\2\2\u00da\u00db\78\2\2\u00db\u00de\5\34\17\2\u00dc\u00de"+
		"\7B\2\2\u00dd\u00d9\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de\35\3\2\2\2\u00df"+
		"\u00e0\5(\25\2\u00e0\u00e1\78\2\2\u00e1\u00e2\5\36\20\2\u00e2\u00e5\3"+
		"\2\2\2\u00e3\u00e5\5(\25\2\u00e4\u00df\3\2\2\2\u00e4\u00e3\3\2\2\2\u00e5"+
		"\37\3\2\2\2\u00e6\u00e7\7\r\2\2\u00e7\u00e8\78\2\2\u00e8\u00eb\5 \21\2"+
		"\u00e9\u00eb\7\r\2\2\u00ea\u00e6\3\2\2\2\u00ea\u00e9\3\2\2\2\u00eb!\3"+
		"\2\2\2\u00ec\u00ed\7\16\2\2\u00ed\u00ee\78\2\2\u00ee\u00f1\5\"\22\2\u00ef"+
		"\u00f1\7\16\2\2\u00f0\u00ec\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1#\3\2\2\2"+
		"\u00f2\u00f3\7\20\2\2\u00f3\u00f4\78\2\2\u00f4\u00f7\5$\23\2\u00f5\u00f7"+
		"\7\20\2\2\u00f6\u00f2\3\2\2\2\u00f6\u00f5\3\2\2\2\u00f7%\3\2\2\2\u00f8"+
		"\u00fb\7\'\2\2\u00f9\u00fb\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00f9\3\2"+
		"\2\2\u00fb\u00fe\3\2\2\2\u00fc\u00ff\7\34\2\2\u00fd\u00ff\3\2\2\2\u00fe"+
		"\u00fc\3\2\2\2\u00fe\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0101\7B"+
		"\2\2\u0101\u0102\7;\2\2\u0102\u0103\5\b\5\2\u0103\'\3\2\2\2\u0104\u0105"+
		"\5*\26\2\u0105\u0106\7\66\2\2\u0106\u0107\5*\26\2\u0107\u010a\3\2\2\2"+
		"\u0108\u010a\5*\26\2\u0109\u0104\3\2\2\2\u0109\u0108\3\2\2\2\u010a)\3"+
		"\2\2\2\u010b\u010c\5,\27\2\u010c\u010d\t\3\2\2\u010d\u010e\5,\27\2\u010e"+
		"\u0111\3\2\2\2\u010f\u0111\5,\27\2\u0110\u010b\3\2\2\2\u0110\u010f\3\2"+
		"\2\2\u0111+\3\2\2\2\u0112\u0113\b\27\1\2\u0113\u0114\5.\30\2\u0114\u011a"+
		"\3\2\2\2\u0115\u0116\f\4\2\2\u0116\u0117\t\4\2\2\u0117\u0119\5.\30\2\u0118"+
		"\u0115\3\2\2\2\u0119\u011c\3\2\2\2\u011a\u0118\3\2\2\2\u011a\u011b\3\2"+
		"\2\2\u011b-\3\2\2\2\u011c\u011a\3\2\2\2\u011d\u011e\b\30\1\2\u011e\u011f"+
		"\5\60\31\2\u011f\u0125\3\2\2\2\u0120\u0121\f\4\2\2\u0121\u0122\t\5\2\2"+
		"\u0122\u0124\5\60\31\2\u0123\u0120\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123"+
		"\3\2\2\2\u0125\u0126\3\2\2\2\u0126/\3\2\2\2\u0127\u0125\3\2\2\2\u0128"+
		"\u0129\b\31\1\2\u0129\u012a\5\62\32\2\u012a\u0130\3\2\2\2\u012b\u012c"+
		"\f\4\2\2\u012c\u012d\t\6\2\2\u012d\u012f\5\62\32\2\u012e\u012b\3\2\2\2"+
		"\u012f\u0132\3\2\2\2\u0130\u012e\3\2\2\2\u0130\u0131\3\2\2\2\u0131\61"+
		"\3\2\2\2\u0132\u0130\3\2\2\2\u0133\u0134\7\61\2\2\u0134\u0137\5\62\32"+
		"\2\u0135\u0137\5\64\33\2\u0136\u0133\3\2\2\2\u0136\u0135\3\2\2\2\u0137"+
		"\63\3\2\2\2\u0138\u0139\7)\2\2\u0139\u013c\5\64\33\2\u013a\u013c\5\66"+
		"\34\2\u013b\u0138\3\2\2\2\u013b\u013a\3\2\2\2\u013c\65\3\2\2\2\u013d\u013e"+
		"\b\34\1\2\u013e\u013f\58\35\2\u013f\u0144\3\2\2\2\u0140\u0141\f\4\2\2"+
		"\u0141\u0143\5:\36\2\u0142\u0140\3\2\2\2\u0143\u0146\3\2\2\2\u0144\u0142"+
		"\3\2\2\2\u0144\u0145\3\2\2\2\u0145\67\3\2\2\2\u0146\u0144\3\2\2\2\u0147"+
		"\u0148\7<\2\2\u0148\u0149\5(\25\2\u0149\u014a\7=\2\2\u014a\u014d\3\2\2"+
		"\2\u014b\u014d\5:\36\2\u014c\u0147\3\2\2\2\u014c\u014b\3\2\2\2\u014d9"+
		"\3\2\2\2\u014e\u0156\7\r\2\2\u014f\u0156\7\16\2\2\u0150\u0156\7\20\2\2"+
		"\u0151\u0156\7B\2\2\u0152\u0156\5<\37\2\u0153\u0156\5\30\r\2\u0154\u0156"+
		"\7\17\2\2\u0155\u014e\3\2\2\2\u0155\u014f\3\2\2\2\u0155\u0150\3\2\2\2"+
		"\u0155\u0151\3\2\2\2\u0155\u0152\3\2\2\2\u0155\u0153\3\2\2\2\u0155\u0154"+
		"\3\2\2\2\u0156\u0160\3\2\2\2\u0157\u0158\7B\2\2\u0158\u015b\7>\2\2\u0159"+
		"\u015c\5 \21\2\u015a\u015c\5:\36\2\u015b\u0159\3\2\2\2\u015b\u015a\3\2"+
		"\2\2\u015c\u015d\3\2\2\2\u015d\u015e\7?\2\2\u015e\u0160\3\2\2\2\u015f"+
		"\u0155\3\2\2\2\u015f\u0157\3\2\2\2\u0160;\3\2\2\2\u0161\u0162\7B\2\2\u0162"+
		"\u0163\7<\2\2\u0163\u0164\5> \2\u0164\u0165\7=\2\2\u0165=\3\2\2\2\u0166"+
		"\u0169\5@!\2\u0167\u0169\3\2\2\2\u0168\u0166\3\2\2\2\u0168\u0167\3\2\2"+
		"\2\u0169?\3\2\2\2\u016a\u016b\5(\25\2\u016b\u016c\78\2\2\u016c\u016d\5"+
		"@!\2\u016d\u0170\3\2\2\2\u016e\u0170\5(\25\2\u016f\u016a\3\2\2\2\u016f"+
		"\u016e\3\2\2\2\u0170A\3\2\2\2\u0171\u017d\5D#\2\u0172\u017d\5H%\2\u0173"+
		"\u017d\5J&\2\u0174\u017d\5R*\2\u0175\u017d\5T+\2\u0176\u017d\5X-\2\u0177"+
		"\u017d\5b\62\2\u0178\u017d\5`\61\2\u0179\u017d\5^\60\2\u017a\u017d\5V"+
		",\2\u017b\u017d\5\20\t\2\u017c\u0171\3\2\2\2\u017c\u0172\3\2\2\2\u017c"+
		"\u0173\3\2\2\2\u017c\u0174\3\2\2\2\u017c\u0175\3\2\2\2\u017c\u0176\3\2"+
		"\2\2\u017c\u0177\3\2\2\2\u017c\u0178\3\2\2\2\u017c\u0179\3\2\2\2\u017c"+
		"\u017a\3\2\2\2\u017c\u017b\3\2\2\2\u017dC\3\2\2\2\u017e\u017f\5F$\2\u017f"+
		"\u0180\7:\2\2\u0180\u0181\5(\25\2\u0181\u0182\79\2\2\u0182E\3\2\2\2\u0183"+
		"\u0184\7B\2\2\u0184\u0185\7>\2\2\u0185\u0186\5 \21\2\u0186\u0187\7?\2"+
		"\2\u0187\u018a\3\2\2\2\u0188\u018a\7B\2\2\u0189\u0183\3\2\2\2\u0189\u0188"+
		"\3\2\2\2\u018aG\3\2\2\2\u018b\u018c\7%\2\2\u018c\u018d\5(\25\2\u018d\u018e"+
		"\5B\"\2\u018e\u018f\7$\2\2\u018f\u0190\5B\"\2\u0190\u0196\3\2\2\2\u0191"+
		"\u0192\7%\2\2\u0192\u0193\5(\25\2\u0193\u0194\5B\"\2\u0194\u0196\3\2\2"+
		"\2\u0195\u018b\3\2\2\2\u0195\u0191\3\2\2\2\u0196I\3\2\2\2\u0197\u0198"+
		"\7\36\2\2\u0198\u019b\7<\2\2\u0199\u019c\5L\'\2\u019a\u019c\3\2\2\2\u019b"+
		"\u0199\3\2\2\2\u019b\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u01a0\78"+
		"\2\2\u019e\u01a1\5N(\2\u019f\u01a1\3\2\2\2\u01a0\u019e\3\2\2\2\u01a0\u019f"+
		"\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a5\78\2\2\u01a3\u01a6\5P)\2\u01a4"+
		"\u01a6\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a4\3\2\2\2\u01a6\u01a7\3\2"+
		"\2\2\u01a7\u01a8\7=\2\2\u01a8\u01a9\5B\"\2\u01a9K\3\2\2\2\u01aa\u01ab"+
		"\7B\2\2\u01ab\u01ac\7:\2\2\u01ac\u01ad\5(\25\2\u01adM\3\2\2\2\u01ae\u01af"+
		"\7B\2\2\u01af\u01b2\t\3\2\2\u01b0\u01b3\7B\2\2\u01b1\u01b3\5(\25\2\u01b2"+
		"\u01b0\3\2\2\2\u01b2\u01b1\3\2\2\2\u01b3O\3\2\2\2\u01b4\u01b5\7B\2\2\u01b5"+
		"\u01b6\7:\2\2\u01b6\u01b7\5(\25\2\u01b7Q\3\2\2\2\u01b8\u01b9\7&\2\2\u01b9"+
		"\u01ba\7<\2\2\u01ba\u01bb\5(\25\2\u01bb\u01bc\7=\2\2\u01bc\u01bd\5B\""+
		"\2\u01bdS\3\2\2\2\u01be\u01bf\7!\2\2\u01bf\u01c0\5X-\2\u01c0\u01c1\7&"+
		"\2\2\u01c1\u01c2\5(\25\2\u01c2\u01c3\79\2\2\u01c3U\3\2\2\2\u01c4\u01c7"+
		"\5<\37\2\u01c5\u01c7\5p9\2\u01c6\u01c4\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7"+
		"\u01c8\3\2\2\2\u01c8\u01c9\79\2\2\u01c9W\3\2\2\2\u01ca\u01cb\7@\2\2\u01cb"+
		"\u01cc\5Z.\2\u01cc\u01cd\7A\2\2\u01cdY\3\2\2\2\u01ce\u01d1\5\\/\2\u01cf"+
		"\u01d1\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0\u01cf\3\2\2\2\u01d1[\3\2\2\2"+
		"\u01d2\u01d3\5B\"\2\u01d3\u01d4\5\\/\2\u01d4\u01d7\3\2\2\2\u01d5\u01d7"+
		"\5B\"\2\u01d6\u01d2\3\2\2\2\u01d6\u01d5\3\2\2\2\u01d7]\3\2\2\2\u01d8\u01d9"+
		"\7\26\2\2\u01d9\u01da\79\2\2\u01da_\3\2\2\2\u01db\u01dc\7 \2\2\u01dc\u01dd"+
		"\79\2\2\u01dda\3\2\2\2\u01de\u01df\7\33\2\2\u01df\u01e0\5(\25\2\u01e0"+
		"\u01e1\79\2\2\u01e1c\3\2\2\2\u01e2\u01e3\7B\2\2\u01e3\u01e4\7;\2\2\u01e4"+
		"\u01e5\7\"\2\2\u01e5\u01e6\5n8\2\u01e6\u01e7\7<\2\2\u01e7\u01e8\5j\66"+
		"\2\u01e8\u01e9\7=\2\2\u01e9\u01ea\5f\64\2\u01ea\u01eb\5B\"\2\u01ebe\3"+
		"\2\2\2\u01ec\u01ed\7\'\2\2\u01ed\u01f0\5h\65\2\u01ee\u01f0\3\2\2\2\u01ef"+
		"\u01ec\3\2\2\2\u01ef\u01ee\3\2\2\2\u01f0g\3\2\2\2\u01f1\u01f2\7B\2\2\u01f2"+
		"i\3\2\2\2\u01f3\u01f6\5l\67\2\u01f4\u01f6\3\2\2\2\u01f5\u01f3\3\2\2\2"+
		"\u01f5\u01f4\3\2\2\2\u01f6k\3\2\2\2\u01f7\u01f8\5&\24\2\u01f8\u01f9\7"+
		"8\2\2\u01f9\u01fa\5l\67\2\u01fa\u01fd\3\2\2\2\u01fb\u01fd\5&\24\2\u01fc"+
		"\u01f7\3\2\2\2\u01fc\u01fb\3\2\2\2\u01fdm\3\2\2\2\u01fe\u01ff\t\7\2\2"+
		"\u01ffo\3\2\2\2\u0200\u020a\5r:\2\u0201\u020a\5t;\2\u0202\u020a\5v<\2"+
		"\u0203\u020a\5x=\2\u0204\u020a\5z>\2\u0205\u020a\5|?\2\u0206\u020a\5~"+
		"@\2\u0207\u020a\5\u0080A\2\u0208\u020a\5\u0082B\2\u0209\u0200\3\2\2\2"+
		"\u0209\u0201\3\2\2\2\u0209\u0202\3\2\2\2\u0209\u0203\3\2\2\2\u0209\u0204"+
		"\3\2\2\2\u0209\u0205\3\2\2\2\u0209\u0206\3\2\2\2\u0209\u0207\3\2\2\2\u0209"+
		"\u0208\3\2\2\2\u020aq\3\2\2\2\u020b\u020c\7\3\2\2\u020c\u020d\7<\2\2\u020d"+
		"\u020e\7=\2\2\u020es\3\2\2\2\u020f\u0210\7\4\2\2\u0210\u0214\7<\2\2\u0211"+
		"\u0215\7\r\2\2\u0212\u0215\7B\2\2\u0213\u0215\5(\25\2\u0214\u0211\3\2"+
		"\2\2\u0214\u0212\3\2\2\2\u0214\u0213\3\2\2\2\u0215\u0216\3\2\2\2\u0216"+
		"\u0217\7=\2\2\u0217u\3\2\2\2\u0218\u0219\7\5\2\2\u0219\u021a\7<\2\2\u021a"+
		"\u021b\7=\2\2\u021bw\3\2\2\2\u021c\u021d\7\6\2\2\u021d\u0221\7<\2\2\u021e"+
		"\u0222\7\16\2\2\u021f\u0222\7B\2\2\u0220\u0222\5(\25\2\u0221\u021e\3\2"+
		"\2\2\u0221\u021f\3\2\2\2\u0221\u0220\3\2\2\2\u0222\u0223\3\2\2\2\u0223"+
		"\u0224\7=\2\2\u0224y\3\2\2\2\u0225\u0226\7\7\2\2\u0226\u022a\7<\2\2\u0227"+
		"\u022b\7\17\2\2\u0228\u022b\7B\2\2\u0229\u022b\5(\25\2\u022a\u0227\3\2"+
		"\2\2\u022a\u0228\3\2\2\2\u022a\u0229\3\2\2\2\u022b\u022c\3\2\2\2\u022c"+
		"\u022d\7=\2\2\u022d{\3\2\2\2\u022e\u022f\7\b\2\2\u022f\u0230\7<\2\2\u0230"+
		"\u0231\7=\2\2\u0231}\3\2\2\2\u0232\u0233\7\t\2\2\u0233\u0237\7<\2\2\u0234"+
		"\u0238\7\20\2\2\u0235\u0238\7B\2\2\u0236\u0238\5(\25\2\u0237\u0234\3\2"+
		"\2\2\u0237\u0235\3\2\2\2\u0237\u0236\3\2\2\2\u0238\u0239\3\2\2\2\u0239"+
		"\u023a\7=\2\2\u023a\177\3\2\2\2\u023b\u023c\7\n\2\2\u023c\u023d\7<\2\2"+
		"\u023d\u023e\5\36\20\2\u023e\u023f\7=\2\2\u023f\u0081\3\2\2\2\u0240\u0241"+
		"\7\13\2\2\u0241\u0242\7<\2\2\u0242\u0243\7=\2\2\u0243\u0083\3\2\2\2\64"+
		"\u0087\u008d\u009a\u00a0\u00a9\u00af\u00b9\u00bd\u00c8\u00cc\u00d7\u00dd"+
		"\u00e4\u00ea\u00f0\u00f6\u00fa\u00fe\u0109\u0110\u011a\u0125\u0130\u0136"+
		"\u013b\u0144\u014c\u0155\u015b\u015f\u0168\u016f\u017c\u0189\u0195\u019b"+
		"\u01a0\u01a5\u01b2\u01c6\u01d0\u01d6\u01ef\u01f5\u01fc\u0209\u0214\u0221"+
		"\u022a\u0237";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}