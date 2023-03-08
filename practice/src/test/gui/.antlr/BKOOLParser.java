// Generated from c:\Users\84865\Documents\HCMUT-cse20\CSE-PPL\practice\src\test\gui\BKOOL.g4 by ANTLR 4.9.2
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
		T__0=1, COMMENT=2, INTEGER_LIT=3, FLOAT_LIT=4, BOOLEAN_LIT=5, STRING_LIT=6, 
		ARRAY_LIT=7, AUTO=8, BREAK=9, INTEGER=10, VOID=11, ARRAY=12, FLOAT=13, 
		RETURN=14, OUT=15, BOOLEAN=16, FOR=17, STRING=18, CONTINUE=19, DO=20, 
		FUNCTION=21, OF=22, ELSE=23, IF=24, WHILE=25, INHERIT=26, PLUS=27, MINUS=28, 
		MUL=29, DIV=30, MOD=31, LESS=32, GREATER=33, LTE=34, GTE=35, NOT=36, AND=37, 
		OR=38, EQUAL_TO=39, NOT_EQUAL=40, CONCAT=41, PERIOD=42, COMMA=43, SEMI=44, 
		EQUAL=45, COLON=46, LB=47, RB=48, LSB=49, RSB=50, LCB=51, RCB=52, IDENTIFIER=53, 
		WS=54, ERROR_CHAR=55, UNCLOSE_STRING=56, ILLEGAL_ESCAPE=57;
	public static final int
		RULE_program = 0, RULE_decls = 1, RULE_array_type = 2, RULE_element_type = 3, 
		RULE_dimesion = 4, RULE_dimesion_type_int = 5, RULE_dimesion_type_float = 6, 
		RULE_variable_decl = 7, RULE_equal_exp = 8, RULE_equal_func_call = 9, 
		RULE_identifier_list = 10, RULE_expression_list = 11, RULE_exp_list_type_int = 12, 
		RULE_exp_list_type_float = 13, RULE_exp_list_type_string = 14, RULE_parameter = 15, 
		RULE_expression = 16, RULE_expression_1 = 17, RULE_expression_2 = 18, 
		RULE_expression_3 = 19, RULE_expression_4 = 20, RULE_expression_5 = 21, 
		RULE_expression_6 = 22, RULE_expression_7 = 23, RULE_expression_8 = 24, 
		RULE_factor = 25, RULE_function_call = 26, RULE_exps_list = 27, RULE_exp_list = 28, 
		RULE_statement = 29, RULE_assign_stmt = 30, RULE_lhs = 31, RULE_if_stmt = 32, 
		RULE_for_stmt = 33, RULE_scala_val = 34, RULE_init_expr = 35, RULE_condition_expr = 36, 
		RULE_update_expr = 37, RULE_while_stmt = 38, RULE_do_while_stmt = 39, 
		RULE_call_stmt = 40, RULE_block_stmt = 41, RULE_break_stmt = 42, RULE_continue_stmt = 43, 
		RULE_return_stmt = 44, RULE_function_decl = 45, RULE_inheritance = 46, 
		RULE_function_name = 47, RULE_paramter_list = 48, RULE_paramter_list_term = 49, 
		RULE_return_type = 50;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "decls", "array_type", "element_type", "dimesion", "dimesion_type_int", 
			"dimesion_type_float", "variable_decl", "equal_exp", "equal_func_call", 
			"identifier_list", "expression_list", "exp_list_type_int", "exp_list_type_float", 
			"exp_list_type_string", "parameter", "expression", "expression_1", "expression_2", 
			"expression_3", "expression_4", "expression_5", "expression_6", "expression_7", 
			"expression_8", "factor", "function_call", "exps_list", "exp_list", "statement", 
			"assign_stmt", "lhs", "if_stmt", "for_stmt", "scala_val", "init_expr", 
			"condition_expr", "update_expr", "while_stmt", "do_while_stmt", "call_stmt", 
			"block_stmt", "break_stmt", "continue_stmt", "return_stmt", "function_decl", 
			"inheritance", "function_name", "paramter_list", "paramter_list_term", 
			"return_type"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'{}'", null, null, null, null, null, null, "'auto'", "'break'", 
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
			null, null, "COMMENT", "INTEGER_LIT", "FLOAT_LIT", "BOOLEAN_LIT", "STRING_LIT", 
			"ARRAY_LIT", "AUTO", "BREAK", "INTEGER", "VOID", "ARRAY", "FLOAT", "RETURN", 
			"OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", "FUNCTION", "OF", 
			"ELSE", "IF", "WHILE", "INHERIT", "PLUS", "MINUS", "MUL", "DIV", "MOD", 
			"LESS", "GREATER", "LTE", "GTE", "NOT", "AND", "OR", "EQUAL_TO", "NOT_EQUAL", 
			"CONCAT", "PERIOD", "COMMA", "SEMI", "EQUAL", "COLON", "LB", "RB", "LSB", 
			"RSB", "LCB", "RCB", "IDENTIFIER", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
			"ILLEGAL_ESCAPE"
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
			setState(105);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << INTEGER_LIT) | (1L << FLOAT_LIT) | (1L << STRING_LIT) | (1L << BREAK) | (1L << ARRAY) | (1L << RETURN) | (1L << CONTINUE) | (1L << DO) | (1L << IF) | (1L << WHILE) | (1L << MINUS) | (1L << NOT) | (1L << LB) | (1L << LCB) | (1L << IDENTIFIER))) != 0)) {
				{
				{
				setState(102);
				decls();
				}
				}
				setState(107);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(108);
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
		public Array_typeContext array_type() {
			return getRuleContext(Array_typeContext.class,0);
		}
		public Variable_declContext variable_decl() {
			return getRuleContext(Variable_declContext.class,0);
		}
		public Function_declContext function_decl() {
			return getRuleContext(Function_declContext.class,0);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
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
			setState(115);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(110);
				array_type();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(111);
				variable_decl();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(112);
				function_decl();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(113);
				statement();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(114);
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
			setState(117);
			match(ARRAY);
			setState(118);
			match(LSB);
			setState(119);
			dimesion();
			setState(120);
			match(RSB);
			setState(121);
			match(OF);
			setState(122);
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
			setState(124);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INTEGER) | (1L << FLOAT) | (1L << BOOLEAN) | (1L << STRING))) != 0)) ) {
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
			setState(128);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTEGER_LIT:
				enterOuterAlt(_localctx, 1);
				{
				setState(126);
				dimesion_type_int();
				}
				break;
			case FLOAT_LIT:
				enterOuterAlt(_localctx, 2);
				{
				setState(127);
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
			setState(134);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(130);
				match(INTEGER_LIT);
				setState(131);
				match(COMMA);
				setState(132);
				dimesion_type_int();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(133);
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
			setState(136);
			match(FLOAT_LIT);
			setState(137);
			match(COMMA);
			setState(138);
			dimesion_type_float();
			setState(139);
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
		public Identifier_listContext identifier_list() {
			return getRuleContext(Identifier_listContext.class,0);
		}
		public TerminalNode COLON() { return getToken(BKOOLParser.COLON, 0); }
		public Element_typeContext element_type() {
			return getRuleContext(Element_typeContext.class,0);
		}
		public Array_typeContext array_type() {
			return getRuleContext(Array_typeContext.class,0);
		}
		public Equal_expContext equal_exp() {
			return getRuleContext(Equal_expContext.class,0);
		}
		public Equal_func_callContext equal_func_call() {
			return getRuleContext(Equal_func_callContext.class,0);
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
			enterOuterAlt(_localctx, 1);
			{
			setState(141);
			identifier_list();
			setState(142);
			match(COLON);
			setState(145);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTEGER:
			case FLOAT:
			case BOOLEAN:
			case STRING:
				{
				setState(143);
				element_type();
				}
				break;
			case ARRAY:
				{
				setState(144);
				array_type();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(149);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				setState(147);
				equal_exp();
				}
				break;
			case 2:
				{
				setState(148);
				equal_func_call();
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

	public static class Equal_expContext extends ParserRuleContext {
		public TerminalNode EQUAL() { return getToken(BKOOLParser.EQUAL, 0); }
		public Expression_listContext expression_list() {
			return getRuleContext(Expression_listContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKOOLParser.SEMI, 0); }
		public Equal_expContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_equal_exp; }
	}

	public final Equal_expContext equal_exp() throws RecognitionException {
		Equal_expContext _localctx = new Equal_expContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_equal_exp);
		try {
			setState(158);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case EQUAL:
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(153);
				match(EQUAL);
				setState(154);
				expression_list();
				setState(155);
				match(SEMI);
				}
				}
				break;
			case SEMI:
				enterOuterAlt(_localctx, 2);
				{
				setState(157);
				match(SEMI);
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

	public static class Equal_func_callContext extends ParserRuleContext {
		public TerminalNode EQUAL() { return getToken(BKOOLParser.EQUAL, 0); }
		public Function_callContext function_call() {
			return getRuleContext(Function_callContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKOOLParser.SEMI, 0); }
		public Equal_func_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_equal_func_call; }
	}

	public final Equal_func_callContext equal_func_call() throws RecognitionException {
		Equal_func_callContext _localctx = new Equal_func_callContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_equal_func_call);
		try {
			setState(165);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case EQUAL:
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(160);
				match(EQUAL);
				setState(161);
				function_call();
				setState(162);
				match(SEMI);
				}
				}
				break;
			case SEMI:
				enterOuterAlt(_localctx, 2);
				{
				setState(164);
				match(SEMI);
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
		enterRule(_localctx, 20, RULE_identifier_list);
		try {
			setState(171);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(167);
				match(IDENTIFIER);
				setState(168);
				match(COMMA);
				setState(169);
				identifier_list();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(170);
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
		public Exp_list_type_intContext exp_list_type_int() {
			return getRuleContext(Exp_list_type_intContext.class,0);
		}
		public Exp_list_type_floatContext exp_list_type_float() {
			return getRuleContext(Exp_list_type_floatContext.class,0);
		}
		public Expression_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression_list; }
	}

	public final Expression_listContext expression_list() throws RecognitionException {
		Expression_listContext _localctx = new Expression_listContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_expression_list);
		try {
			setState(175);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTEGER_LIT:
				enterOuterAlt(_localctx, 1);
				{
				setState(173);
				exp_list_type_int();
				}
				break;
			case FLOAT_LIT:
				enterOuterAlt(_localctx, 2);
				{
				setState(174);
				exp_list_type_float();
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
		enterRule(_localctx, 24, RULE_exp_list_type_int);
		try {
			setState(181);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(177);
				match(INTEGER_LIT);
				setState(178);
				match(COMMA);
				setState(179);
				exp_list_type_int();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(180);
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
		enterRule(_localctx, 26, RULE_exp_list_type_float);
		try {
			setState(187);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(183);
				match(FLOAT_LIT);
				setState(184);
				match(COMMA);
				setState(185);
				exp_list_type_float();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(186);
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
		enterRule(_localctx, 28, RULE_exp_list_type_string);
		try {
			setState(193);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(189);
				match(STRING_LIT);
				setState(190);
				match(COMMA);
				setState(191);
				exp_list_type_string();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(192);
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
		enterRule(_localctx, 30, RULE_parameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(197);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INHERIT:
				{
				setState(195);
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
			setState(201);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OUT:
				{
				setState(199);
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
			setState(203);
			match(IDENTIFIER);
			setState(204);
			match(COLON);
			setState(205);
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
		enterRule(_localctx, 32, RULE_expression);
		try {
			setState(212);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(207);
				expression_1();
				setState(208);
				match(CONCAT);
				setState(209);
				expression_1();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(211);
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
		enterRule(_localctx, 34, RULE_expression_1);
		int _la;
		try {
			setState(219);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(214);
				expression_2(0);
				setState(215);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LESS) | (1L << GREATER) | (1L << LTE) | (1L << GTE) | (1L << EQUAL_TO) | (1L << NOT_EQUAL))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(216);
				expression_2(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(218);
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
		int _startState = 36;
		enterRecursionRule(_localctx, 36, RULE_expression_2, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(222);
			expression_3(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(229);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expression_2Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expression_2);
					setState(224);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(225);
					_la = _input.LA(1);
					if ( !(_la==AND || _la==OR) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(226);
					expression_3(0);
					}
					} 
				}
				setState(231);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
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
		int _startState = 38;
		enterRecursionRule(_localctx, 38, RULE_expression_3, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(233);
			expression_4(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(240);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expression_3Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expression_3);
					setState(235);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(236);
					_la = _input.LA(1);
					if ( !(_la==PLUS || _la==MINUS) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(237);
					expression_4(0);
					}
					} 
				}
				setState(242);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
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
		int _startState = 40;
		enterRecursionRule(_localctx, 40, RULE_expression_4, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(244);
			expression_5();
			}
			_ctx.stop = _input.LT(-1);
			setState(251);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expression_4Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expression_4);
					setState(246);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(247);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << MUL) | (1L << DIV) | (1L << MOD))) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(248);
					expression_5();
					}
					} 
				}
				setState(253);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
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
		enterRule(_localctx, 42, RULE_expression_5);
		try {
			setState(257);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(254);
				match(NOT);
				setState(255);
				expression_5();
				}
				break;
			case INTEGER_LIT:
			case FLOAT_LIT:
			case STRING_LIT:
			case MINUS:
			case LB:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(256);
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
		enterRule(_localctx, 44, RULE_expression_6);
		try {
			setState(262);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MINUS:
				enterOuterAlt(_localctx, 1);
				{
				setState(259);
				match(MINUS);
				setState(260);
				expression_6();
				}
				break;
			case INTEGER_LIT:
			case FLOAT_LIT:
			case STRING_LIT:
			case LB:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(261);
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
		int _startState = 46;
		enterRecursionRule(_localctx, 46, RULE_expression_7, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(265);
			expression_8();
			}
			_ctx.stop = _input.LT(-1);
			setState(271);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expression_7Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expression_7);
					setState(267);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(268);
					factor();
					}
					} 
				}
				setState(273);
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
		enterRule(_localctx, 48, RULE_expression_8);
		try {
			setState(279);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LB:
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(274);
				match(LB);
				setState(275);
				expression();
				setState(276);
				match(RB);
				}
				}
				break;
			case INTEGER_LIT:
			case FLOAT_LIT:
			case STRING_LIT:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(278);
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
		public TerminalNode LSB() { return getToken(BKOOLParser.LSB, 0); }
		public Exp_list_type_intContext exp_list_type_int() {
			return getRuleContext(Exp_list_type_intContext.class,0);
		}
		public TerminalNode RSB() { return getToken(BKOOLParser.RSB, 0); }
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_factor);
		try {
			setState(293);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(286);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
				case 1:
					{
					setState(281);
					match(INTEGER_LIT);
					}
					break;
				case 2:
					{
					setState(282);
					match(FLOAT_LIT);
					}
					break;
				case 3:
					{
					setState(283);
					match(STRING_LIT);
					}
					break;
				case 4:
					{
					setState(284);
					match(IDENTIFIER);
					}
					break;
				case 5:
					{
					setState(285);
					function_call();
					}
					break;
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(288);
				match(IDENTIFIER);
				setState(289);
				match(LSB);
				setState(290);
				exp_list_type_int();
				setState(291);
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
		public Exp_listContext exp_list() {
			return getRuleContext(Exp_listContext.class,0);
		}
		public TerminalNode RB() { return getToken(BKOOLParser.RB, 0); }
		public Function_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_call; }
	}

	public final Function_callContext function_call() throws RecognitionException {
		Function_callContext _localctx = new Function_callContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_function_call);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(295);
			match(IDENTIFIER);
			setState(296);
			match(LB);
			setState(297);
			exp_list();
			setState(298);
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
		enterRule(_localctx, 54, RULE_exps_list);
		try {
			setState(302);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTEGER_LIT:
			case FLOAT_LIT:
			case STRING_LIT:
			case MINUS:
			case NOT:
			case LB:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(300);
				exp_list();
				}
				break;
			case EOF:
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
		enterRule(_localctx, 56, RULE_exp_list);
		try {
			setState(309);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(304);
				expression();
				setState(305);
				match(COMMA);
				setState(306);
				exp_list();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(308);
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
		enterRule(_localctx, 58, RULE_statement);
		try {
			setState(322);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,28,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(311);
				assign_stmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(312);
				if_stmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(313);
				for_stmt();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(314);
				while_stmt();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(315);
				do_while_stmt();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(316);
				block_stmt();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(317);
				return_stmt();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(318);
				continue_stmt();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(319);
				break_stmt();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(320);
				call_stmt();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(321);
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
		enterRule(_localctx, 60, RULE_assign_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(324);
			lhs();
			setState(325);
			match(EQUAL);
			setState(326);
			expression();
			setState(327);
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
		enterRule(_localctx, 62, RULE_lhs);
		try {
			setState(335);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(329);
				match(IDENTIFIER);
				setState(330);
				match(LSB);
				setState(331);
				exp_list_type_int();
				setState(332);
				match(RSB);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(334);
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
		enterRule(_localctx, 64, RULE_if_stmt);
		try {
			setState(347);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,30,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(337);
				match(IF);
				setState(338);
				expression();
				setState(339);
				statement();
				setState(340);
				match(ELSE);
				setState(341);
				statement();
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(343);
				match(IF);
				setState(344);
				expression();
				setState(345);
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
		public TerminalNode LB() { return getToken(BKOOLParser.LB, 0); }
		public Scala_valContext scala_val() {
			return getRuleContext(Scala_valContext.class,0);
		}
		public TerminalNode EQUAL() { return getToken(BKOOLParser.EQUAL, 0); }
		public Init_exprContext init_expr() {
			return getRuleContext(Init_exprContext.class,0);
		}
		public List<TerminalNode> COMMA() { return getTokens(BKOOLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKOOLParser.COMMA, i);
		}
		public Condition_exprContext condition_expr() {
			return getRuleContext(Condition_exprContext.class,0);
		}
		public Update_exprContext update_expr() {
			return getRuleContext(Update_exprContext.class,0);
		}
		public TerminalNode RB() { return getToken(BKOOLParser.RB, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public For_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_stmt; }
	}

	public final For_stmtContext for_stmt() throws RecognitionException {
		For_stmtContext _localctx = new For_stmtContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_for_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(349);
			match(LB);
			setState(350);
			scala_val();
			setState(351);
			match(EQUAL);
			setState(352);
			init_expr();
			setState(353);
			match(COMMA);
			setState(354);
			condition_expr();
			setState(355);
			match(COMMA);
			setState(356);
			update_expr();
			setState(357);
			match(RB);
			setState(358);
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

	public static class Scala_valContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(BKOOLParser.IDENTIFIER, 0); }
		public Scala_valContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scala_val; }
	}

	public final Scala_valContext scala_val() throws RecognitionException {
		Scala_valContext _localctx = new Scala_valContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_scala_val);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(360);
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

	public static class Init_exprContext extends ParserRuleContext {
		public TerminalNode INTEGER_LIT() { return getToken(BKOOLParser.INTEGER_LIT, 0); }
		public TerminalNode IDENTIFIER() { return getToken(BKOOLParser.IDENTIFIER, 0); }
		public Init_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_init_expr; }
	}

	public final Init_exprContext init_expr() throws RecognitionException {
		Init_exprContext _localctx = new Init_exprContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_init_expr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(362);
			_la = _input.LA(1);
			if ( !(_la==INTEGER_LIT || _la==IDENTIFIER) ) {
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
		enterRule(_localctx, 72, RULE_condition_expr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(364);
			match(IDENTIFIER);
			setState(365);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LESS) | (1L << GREATER) | (1L << LTE) | (1L << GTE) | (1L << EQUAL_TO) | (1L << NOT_EQUAL))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(368);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
			case 1:
				{
				setState(366);
				match(IDENTIFIER);
				}
				break;
			case 2:
				{
				setState(367);
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
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode PLUS() { return getToken(BKOOLParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(BKOOLParser.MINUS, 0); }
		public TerminalNode MUL() { return getToken(BKOOLParser.MUL, 0); }
		public TerminalNode MOD() { return getToken(BKOOLParser.MOD, 0); }
		public Update_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_update_expr; }
	}

	public final Update_exprContext update_expr() throws RecognitionException {
		Update_exprContext _localctx = new Update_exprContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_update_expr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(370);
			match(IDENTIFIER);
			setState(371);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PLUS) | (1L << MINUS) | (1L << MUL) | (1L << MOD))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(372);
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
		enterRule(_localctx, 76, RULE_while_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(374);
			match(WHILE);
			setState(375);
			match(LB);
			setState(376);
			expression();
			setState(377);
			match(RB);
			setState(378);
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
		public Do_while_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_do_while_stmt; }
	}

	public final Do_while_stmtContext do_while_stmt() throws RecognitionException {
		Do_while_stmtContext _localctx = new Do_while_stmtContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_do_while_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(380);
			match(DO);
			setState(381);
			block_stmt();
			setState(382);
			match(WHILE);
			setState(383);
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

	public static class Call_stmtContext extends ParserRuleContext {
		public Function_callContext function_call() {
			return getRuleContext(Function_callContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKOOLParser.SEMI, 0); }
		public Call_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call_stmt; }
	}

	public final Call_stmtContext call_stmt() throws RecognitionException {
		Call_stmtContext _localctx = new Call_stmtContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_call_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(385);
			function_call();
			setState(386);
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
		public TerminalNode RCB() { return getToken(BKOOLParser.RCB, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public Block_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block_stmt; }
	}

	public final Block_stmtContext block_stmt() throws RecognitionException {
		Block_stmtContext _localctx = new Block_stmtContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_block_stmt);
		int _la;
		try {
			setState(397);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LCB:
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(388);
				match(LCB);
				setState(392);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << BREAK) | (1L << RETURN) | (1L << CONTINUE) | (1L << DO) | (1L << IF) | (1L << WHILE) | (1L << LB) | (1L << LCB) | (1L << IDENTIFIER))) != 0)) {
					{
					{
					setState(389);
					statement();
					}
					}
					setState(394);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(395);
				match(RCB);
				}
				}
				break;
			case T__0:
				enterOuterAlt(_localctx, 2);
				{
				setState(396);
				match(T__0);
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
		enterRule(_localctx, 84, RULE_break_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(399);
			match(BREAK);
			setState(400);
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
		enterRule(_localctx, 86, RULE_continue_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(402);
			match(CONTINUE);
			setState(403);
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
		enterRule(_localctx, 88, RULE_return_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(405);
			match(RETURN);
			setState(406);
			expression();
			setState(407);
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
		enterRule(_localctx, 90, RULE_function_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(409);
			match(IDENTIFIER);
			setState(410);
			match(COLON);
			setState(411);
			match(FUNCTION);
			setState(412);
			return_type();
			setState(413);
			match(LB);
			setState(414);
			paramter_list();
			setState(415);
			match(RB);
			setState(416);
			inheritance();
			setState(417);
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
		enterRule(_localctx, 92, RULE_inheritance);
		try {
			setState(422);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INHERIT:
				enterOuterAlt(_localctx, 1);
				{
				setState(419);
				match(INHERIT);
				setState(420);
				function_name();
				}
				break;
			case T__0:
			case BREAK:
			case RETURN:
			case CONTINUE:
			case DO:
			case IF:
			case WHILE:
			case LB:
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
		enterRule(_localctx, 94, RULE_function_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(424);
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
		enterRule(_localctx, 96, RULE_paramter_list);
		try {
			setState(428);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OUT:
			case INHERIT:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(426);
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
		enterRule(_localctx, 98, RULE_paramter_list_term);
		try {
			setState(435);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,36,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(430);
				parameter();
				setState(431);
				match(COMMA);
				setState(432);
				paramter_list_term();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(434);
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
		enterRule(_localctx, 100, RULE_return_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(437);
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 18:
			return expression_2_sempred((Expression_2Context)_localctx, predIndex);
		case 19:
			return expression_3_sempred((Expression_3Context)_localctx, predIndex);
		case 20:
			return expression_4_sempred((Expression_4Context)_localctx, predIndex);
		case 23:
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3;\u01ba\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\3\2\7\2j\n\2\f\2\16\2m\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3v\n\3\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\5\6\u0083\n\6\3\7\3\7\3\7\3"+
		"\7\5\7\u0089\n\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\5\t\u0094\n\t\3\t"+
		"\3\t\5\t\u0098\n\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\5\n\u00a1\n\n\3\13\3\13"+
		"\3\13\3\13\3\13\5\13\u00a8\n\13\3\f\3\f\3\f\3\f\5\f\u00ae\n\f\3\r\3\r"+
		"\5\r\u00b2\n\r\3\16\3\16\3\16\3\16\5\16\u00b8\n\16\3\17\3\17\3\17\3\17"+
		"\5\17\u00be\n\17\3\20\3\20\3\20\3\20\5\20\u00c4\n\20\3\21\3\21\5\21\u00c8"+
		"\n\21\3\21\3\21\5\21\u00cc\n\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22"+
		"\3\22\5\22\u00d7\n\22\3\23\3\23\3\23\3\23\3\23\5\23\u00de\n\23\3\24\3"+
		"\24\3\24\3\24\3\24\3\24\7\24\u00e6\n\24\f\24\16\24\u00e9\13\24\3\25\3"+
		"\25\3\25\3\25\3\25\3\25\7\25\u00f1\n\25\f\25\16\25\u00f4\13\25\3\26\3"+
		"\26\3\26\3\26\3\26\3\26\7\26\u00fc\n\26\f\26\16\26\u00ff\13\26\3\27\3"+
		"\27\3\27\5\27\u0104\n\27\3\30\3\30\3\30\5\30\u0109\n\30\3\31\3\31\3\31"+
		"\3\31\3\31\7\31\u0110\n\31\f\31\16\31\u0113\13\31\3\32\3\32\3\32\3\32"+
		"\3\32\5\32\u011a\n\32\3\33\3\33\3\33\3\33\3\33\5\33\u0121\n\33\3\33\3"+
		"\33\3\33\3\33\3\33\5\33\u0128\n\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35"+
		"\5\35\u0131\n\35\3\36\3\36\3\36\3\36\3\36\5\36\u0138\n\36\3\37\3\37\3"+
		"\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0145\n\37\3 \3 \3 \3"+
		" \3 \3!\3!\3!\3!\3!\3!\5!\u0152\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\""+
		"\3\"\5\"\u015e\n\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3%\3%\3&\3&"+
		"\3&\3&\5&\u0173\n&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3"+
		"*\3*\3*\3+\3+\7+\u0189\n+\f+\16+\u018c\13+\3+\3+\5+\u0190\n+\3,\3,\3,"+
		"\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\5\60"+
		"\u01a9\n\60\3\61\3\61\3\62\3\62\5\62\u01af\n\62\3\63\3\63\3\63\3\63\3"+
		"\63\5\63\u01b6\n\63\3\64\3\64\3\64\2\6&(*\60\65\2\4\6\b\n\f\16\20\22\24"+
		"\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdf\2\n\6\2"+
		"\f\f\17\17\22\22\24\24\4\2\"%)*\3\2\'(\3\2\35\36\3\2\37!\4\2\5\5\67\67"+
		"\4\2\35\37!!\7\2\n\n\f\r\17\17\22\22\24\24\2\u01ba\2k\3\2\2\2\4u\3\2\2"+
		"\2\6w\3\2\2\2\b~\3\2\2\2\n\u0082\3\2\2\2\f\u0088\3\2\2\2\16\u008a\3\2"+
		"\2\2\20\u008f\3\2\2\2\22\u00a0\3\2\2\2\24\u00a7\3\2\2\2\26\u00ad\3\2\2"+
		"\2\30\u00b1\3\2\2\2\32\u00b7\3\2\2\2\34\u00bd\3\2\2\2\36\u00c3\3\2\2\2"+
		" \u00c7\3\2\2\2\"\u00d6\3\2\2\2$\u00dd\3\2\2\2&\u00df\3\2\2\2(\u00ea\3"+
		"\2\2\2*\u00f5\3\2\2\2,\u0103\3\2\2\2.\u0108\3\2\2\2\60\u010a\3\2\2\2\62"+
		"\u0119\3\2\2\2\64\u0127\3\2\2\2\66\u0129\3\2\2\28\u0130\3\2\2\2:\u0137"+
		"\3\2\2\2<\u0144\3\2\2\2>\u0146\3\2\2\2@\u0151\3\2\2\2B\u015d\3\2\2\2D"+
		"\u015f\3\2\2\2F\u016a\3\2\2\2H\u016c\3\2\2\2J\u016e\3\2\2\2L\u0174\3\2"+
		"\2\2N\u0178\3\2\2\2P\u017e\3\2\2\2R\u0183\3\2\2\2T\u018f\3\2\2\2V\u0191"+
		"\3\2\2\2X\u0194\3\2\2\2Z\u0197\3\2\2\2\\\u019b\3\2\2\2^\u01a8\3\2\2\2"+
		"`\u01aa\3\2\2\2b\u01ae\3\2\2\2d\u01b5\3\2\2\2f\u01b7\3\2\2\2hj\5\4\3\2"+
		"ih\3\2\2\2jm\3\2\2\2ki\3\2\2\2kl\3\2\2\2ln\3\2\2\2mk\3\2\2\2no\7\2\2\3"+
		"o\3\3\2\2\2pv\5\6\4\2qv\5\20\t\2rv\5\\/\2sv\5<\37\2tv\5\"\22\2up\3\2\2"+
		"\2uq\3\2\2\2ur\3\2\2\2us\3\2\2\2ut\3\2\2\2v\5\3\2\2\2wx\7\16\2\2xy\7\63"+
		"\2\2yz\5\n\6\2z{\7\64\2\2{|\7\30\2\2|}\5\b\5\2}\7\3\2\2\2~\177\t\2\2\2"+
		"\177\t\3\2\2\2\u0080\u0083\5\f\7\2\u0081\u0083\5\16\b\2\u0082\u0080\3"+
		"\2\2\2\u0082\u0081\3\2\2\2\u0083\13\3\2\2\2\u0084\u0085\7\5\2\2\u0085"+
		"\u0086\7-\2\2\u0086\u0089\5\f\7\2\u0087\u0089\7\5\2\2\u0088\u0084\3\2"+
		"\2\2\u0088\u0087\3\2\2\2\u0089\r\3\2\2\2\u008a\u008b\7\6\2\2\u008b\u008c"+
		"\7-\2\2\u008c\u008d\5\16\b\2\u008d\u008e\7\6\2\2\u008e\17\3\2\2\2\u008f"+
		"\u0090\5\26\f\2\u0090\u0093\7\60\2\2\u0091\u0094\5\b\5\2\u0092\u0094\5"+
		"\6\4\2\u0093\u0091\3\2\2\2\u0093\u0092\3\2\2\2\u0094\u0097\3\2\2\2\u0095"+
		"\u0098\5\22\n\2\u0096\u0098\5\24\13\2\u0097\u0095\3\2\2\2\u0097\u0096"+
		"\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\b\t\1\2\u009a\21\3\2\2\2\u009b"+
		"\u009c\7/\2\2\u009c\u009d\5\30\r\2\u009d\u009e\7.\2\2\u009e\u00a1\3\2"+
		"\2\2\u009f\u00a1\7.\2\2\u00a0\u009b\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1"+
		"\23\3\2\2\2\u00a2\u00a3\7/\2\2\u00a3\u00a4\5\66\34\2\u00a4\u00a5\7.\2"+
		"\2\u00a5\u00a8\3\2\2\2\u00a6\u00a8\7.\2\2\u00a7\u00a2\3\2\2\2\u00a7\u00a6"+
		"\3\2\2\2\u00a8\25\3\2\2\2\u00a9\u00aa\7\67\2\2\u00aa\u00ab\7-\2\2\u00ab"+
		"\u00ae\5\26\f\2\u00ac\u00ae\7\67\2\2\u00ad\u00a9\3\2\2\2\u00ad\u00ac\3"+
		"\2\2\2\u00ae\27\3\2\2\2\u00af\u00b2\5\32\16\2\u00b0\u00b2\5\34\17\2\u00b1"+
		"\u00af\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\31\3\2\2\2\u00b3\u00b4\7\5\2"+
		"\2\u00b4\u00b5\7-\2\2\u00b5\u00b8\5\32\16\2\u00b6\u00b8\7\5\2\2\u00b7"+
		"\u00b3\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8\33\3\2\2\2\u00b9\u00ba\7\6\2"+
		"\2\u00ba\u00bb\7-\2\2\u00bb\u00be\5\34\17\2\u00bc\u00be\7\6\2\2\u00bd"+
		"\u00b9\3\2\2\2\u00bd\u00bc\3\2\2\2\u00be\35\3\2\2\2\u00bf\u00c0\7\b\2"+
		"\2\u00c0\u00c1\7-\2\2\u00c1\u00c4\5\36\20\2\u00c2\u00c4\7\b\2\2\u00c3"+
		"\u00bf\3\2\2\2\u00c3\u00c2\3\2\2\2\u00c4\37\3\2\2\2\u00c5\u00c8\7\34\2"+
		"\2\u00c6\u00c8\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c6\3\2\2\2\u00c8\u00cb"+
		"\3\2\2\2\u00c9\u00cc\7\21\2\2\u00ca\u00cc\3\2\2\2\u00cb\u00c9\3\2\2\2"+
		"\u00cb\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00ce\7\67\2\2\u00ce\u00cf"+
		"\7\60\2\2\u00cf\u00d0\5\b\5\2\u00d0!\3\2\2\2\u00d1\u00d2\5$\23\2\u00d2"+
		"\u00d3\7+\2\2\u00d3\u00d4\5$\23\2\u00d4\u00d7\3\2\2\2\u00d5\u00d7\5$\23"+
		"\2\u00d6\u00d1\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7#\3\2\2\2\u00d8\u00d9"+
		"\5&\24\2\u00d9\u00da\t\3\2\2\u00da\u00db\5&\24\2\u00db\u00de\3\2\2\2\u00dc"+
		"\u00de\5&\24\2\u00dd\u00d8\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de%\3\2\2\2"+
		"\u00df\u00e0\b\24\1\2\u00e0\u00e1\5(\25\2\u00e1\u00e7\3\2\2\2\u00e2\u00e3"+
		"\f\4\2\2\u00e3\u00e4\t\4\2\2\u00e4\u00e6\5(\25\2\u00e5\u00e2\3\2\2\2\u00e6"+
		"\u00e9\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\'\3\2\2\2"+
		"\u00e9\u00e7\3\2\2\2\u00ea\u00eb\b\25\1\2\u00eb\u00ec\5*\26\2\u00ec\u00f2"+
		"\3\2\2\2\u00ed\u00ee\f\4\2\2\u00ee\u00ef\t\5\2\2\u00ef\u00f1\5*\26\2\u00f0"+
		"\u00ed\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f3\3\2"+
		"\2\2\u00f3)\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f5\u00f6\b\26\1\2\u00f6\u00f7"+
		"\5,\27\2\u00f7\u00fd\3\2\2\2\u00f8\u00f9\f\4\2\2\u00f9\u00fa\t\6\2\2\u00fa"+
		"\u00fc\5,\27\2\u00fb\u00f8\3\2\2\2\u00fc\u00ff\3\2\2\2\u00fd\u00fb\3\2"+
		"\2\2\u00fd\u00fe\3\2\2\2\u00fe+\3\2\2\2\u00ff\u00fd\3\2\2\2\u0100\u0101"+
		"\7&\2\2\u0101\u0104\5,\27\2\u0102\u0104\5.\30\2\u0103\u0100\3\2\2\2\u0103"+
		"\u0102\3\2\2\2\u0104-\3\2\2\2\u0105\u0106\7\36\2\2\u0106\u0109\5.\30\2"+
		"\u0107\u0109\5\60\31\2\u0108\u0105\3\2\2\2\u0108\u0107\3\2\2\2\u0109/"+
		"\3\2\2\2\u010a\u010b\b\31\1\2\u010b\u010c\5\62\32\2\u010c\u0111\3\2\2"+
		"\2\u010d\u010e\f\4\2\2\u010e\u0110\5\64\33\2\u010f\u010d\3\2\2\2\u0110"+
		"\u0113\3\2\2\2\u0111\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112\61\3\2\2"+
		"\2\u0113\u0111\3\2\2\2\u0114\u0115\7\61\2\2\u0115\u0116\5\"\22\2\u0116"+
		"\u0117\7\62\2\2\u0117\u011a\3\2\2\2\u0118\u011a\5\64\33\2\u0119\u0114"+
		"\3\2\2\2\u0119\u0118\3\2\2\2\u011a\63\3\2\2\2\u011b\u0121\7\5\2\2\u011c"+
		"\u0121\7\6\2\2\u011d\u0121\7\b\2\2\u011e\u0121\7\67\2\2\u011f\u0121\5"+
		"\66\34\2\u0120\u011b\3\2\2\2\u0120\u011c\3\2\2\2\u0120\u011d\3\2\2\2\u0120"+
		"\u011e\3\2\2\2\u0120\u011f\3\2\2\2\u0121\u0128\3\2\2\2\u0122\u0123\7\67"+
		"\2\2\u0123\u0124\7\63\2\2\u0124\u0125\5\32\16\2\u0125\u0126\7\64\2\2\u0126"+
		"\u0128\3\2\2\2\u0127\u0120\3\2\2\2\u0127\u0122\3\2\2\2\u0128\65\3\2\2"+
		"\2\u0129\u012a\7\67\2\2\u012a\u012b\7\61\2\2\u012b\u012c\5:\36\2\u012c"+
		"\u012d\7\62\2\2\u012d\67\3\2\2\2\u012e\u0131\5:\36\2\u012f\u0131\3\2\2"+
		"\2\u0130\u012e\3\2\2\2\u0130\u012f\3\2\2\2\u01319\3\2\2\2\u0132\u0133"+
		"\5\"\22\2\u0133\u0134\7-\2\2\u0134\u0135\5:\36\2\u0135\u0138\3\2\2\2\u0136"+
		"\u0138\5\"\22\2\u0137\u0132\3\2\2\2\u0137\u0136\3\2\2\2\u0138;\3\2\2\2"+
		"\u0139\u0145\5> \2\u013a\u0145\5B\"\2\u013b\u0145\5D#\2\u013c\u0145\5"+
		"N(\2\u013d\u0145\5P)\2\u013e\u0145\5T+\2\u013f\u0145\5Z.\2\u0140\u0145"+
		"\5X-\2\u0141\u0145\5V,\2\u0142\u0145\5R*\2\u0143\u0145\5\20\t\2\u0144"+
		"\u0139\3\2\2\2\u0144\u013a\3\2\2\2\u0144\u013b\3\2\2\2\u0144\u013c\3\2"+
		"\2\2\u0144\u013d\3\2\2\2\u0144\u013e\3\2\2\2\u0144\u013f\3\2\2\2\u0144"+
		"\u0140\3\2\2\2\u0144\u0141\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0143\3\2"+
		"\2\2\u0145=\3\2\2\2\u0146\u0147\5@!\2\u0147\u0148\7/\2\2\u0148\u0149\5"+
		"\"\22\2\u0149\u014a\7.\2\2\u014a?\3\2\2\2\u014b\u014c\7\67\2\2\u014c\u014d"+
		"\7\63\2\2\u014d\u014e\5\32\16\2\u014e\u014f\7\64\2\2\u014f\u0152\3\2\2"+
		"\2\u0150\u0152\7\67\2\2\u0151\u014b\3\2\2\2\u0151\u0150\3\2\2\2\u0152"+
		"A\3\2\2\2\u0153\u0154\7\32\2\2\u0154\u0155\5\"\22\2\u0155\u0156\5<\37"+
		"\2\u0156\u0157\7\31\2\2\u0157\u0158\5<\37\2\u0158\u015e\3\2\2\2\u0159"+
		"\u015a\7\32\2\2\u015a\u015b\5\"\22\2\u015b\u015c\5<\37\2\u015c\u015e\3"+
		"\2\2\2\u015d\u0153\3\2\2\2\u015d\u0159\3\2\2\2\u015eC\3\2\2\2\u015f\u0160"+
		"\7\61\2\2\u0160\u0161\5F$\2\u0161\u0162\7/\2\2\u0162\u0163\5H%\2\u0163"+
		"\u0164\7-\2\2\u0164\u0165\5J&\2\u0165\u0166\7-\2\2\u0166\u0167\5L\'\2"+
		"\u0167\u0168\7\62\2\2\u0168\u0169\5<\37\2\u0169E\3\2\2\2\u016a\u016b\7"+
		"\67\2\2\u016bG\3\2\2\2\u016c\u016d\t\7\2\2\u016dI\3\2\2\2\u016e\u016f"+
		"\7\67\2\2\u016f\u0172\t\3\2\2\u0170\u0173\7\67\2\2\u0171\u0173\5\"\22"+
		"\2\u0172\u0170\3\2\2\2\u0172\u0171\3\2\2\2\u0173K\3\2\2\2\u0174\u0175"+
		"\7\67\2\2\u0175\u0176\t\b\2\2\u0176\u0177\5\"\22\2\u0177M\3\2\2\2\u0178"+
		"\u0179\7\33\2\2\u0179\u017a\7\61\2\2\u017a\u017b\5\"\22\2\u017b\u017c"+
		"\7\62\2\2\u017c\u017d\5<\37\2\u017dO\3\2\2\2\u017e\u017f\7\26\2\2\u017f"+
		"\u0180\5T+\2\u0180\u0181\7\33\2\2\u0181\u0182\5\"\22\2\u0182Q\3\2\2\2"+
		"\u0183\u0184\5\66\34\2\u0184\u0185\7.\2\2\u0185S\3\2\2\2\u0186\u018a\7"+
		"\65\2\2\u0187\u0189\5<\37\2\u0188\u0187\3\2\2\2\u0189\u018c\3\2\2\2\u018a"+
		"\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u018d\3\2\2\2\u018c\u018a\3\2"+
		"\2\2\u018d\u0190\7\66\2\2\u018e\u0190\7\3\2\2\u018f\u0186\3\2\2\2\u018f"+
		"\u018e\3\2\2\2\u0190U\3\2\2\2\u0191\u0192\7\13\2\2\u0192\u0193\7.\2\2"+
		"\u0193W\3\2\2\2\u0194\u0195\7\25\2\2\u0195\u0196\7.\2\2\u0196Y\3\2\2\2"+
		"\u0197\u0198\7\20\2\2\u0198\u0199\5\"\22\2\u0199\u019a\7.\2\2\u019a[\3"+
		"\2\2\2\u019b\u019c\7\67\2\2\u019c\u019d\7\60\2\2\u019d\u019e\7\27\2\2"+
		"\u019e\u019f\5f\64\2\u019f\u01a0\7\61\2\2\u01a0\u01a1\5b\62\2\u01a1\u01a2"+
		"\7\62\2\2\u01a2\u01a3\5^\60\2\u01a3\u01a4\5<\37\2\u01a4]\3\2\2\2\u01a5"+
		"\u01a6\7\34\2\2\u01a6\u01a9\5`\61\2\u01a7\u01a9\3\2\2\2\u01a8\u01a5\3"+
		"\2\2\2\u01a8\u01a7\3\2\2\2\u01a9_\3\2\2\2\u01aa\u01ab\7\67\2\2\u01aba"+
		"\3\2\2\2\u01ac\u01af\5d\63\2\u01ad\u01af\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae"+
		"\u01ad\3\2\2\2\u01afc\3\2\2\2\u01b0\u01b1\5 \21\2\u01b1\u01b2\7-\2\2\u01b2"+
		"\u01b3\5d\63\2\u01b3\u01b6\3\2\2\2\u01b4\u01b6\5 \21\2\u01b5\u01b0\3\2"+
		"\2\2\u01b5\u01b4\3\2\2\2\u01b6e\3\2\2\2\u01b7\u01b8\t\t\2\2\u01b8g\3\2"+
		"\2\2\'ku\u0082\u0088\u0093\u0097\u00a0\u00a7\u00ad\u00b1\u00b7\u00bd\u00c3"+
		"\u00c7\u00cb\u00d6\u00dd\u00e7\u00f2\u00fd\u0103\u0108\u0111\u0119\u0120"+
		"\u0127\u0130\u0137\u0144\u0151\u015d\u0172\u018a\u018f\u01a8\u01ae\u01b5";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}