// Generated from c:\Users\84865\Documents\HCMUT-cse20\CSE-PPL\practice\src\test\gui\BKOOL.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class BKOOLLexer extends Lexer {
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
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "COMMENT", "SingleLineComment", "MultiLineComment", "INTEGER_LIT", 
			"UNDERSCORE", "FLOAT_LIT", "DECPART", "EXPPART", "BOOLEAN_LIT", "FALSE", 
			"TRUE", "STRING_LIT", "SUBSTRING", "ARRAY_LIT", "EXPS", "INT_TYPE", "FLOAT_TYPE", 
			"STRINGLIST", "Escape_Sequence", "DUO_QUOTE", "SINGLE_QUOTE", "BackSpace", 
			"FormFeed", "CarriageReturn", "NewLine", "SingleQuote", "BackSlash", 
			"Dou_quote", "AUTO", "BREAK", "INTEGER", "VOID", "ARRAY", "FLOAT", "RETURN", 
			"OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", "FUNCTION", "OF", 
			"ELSE", "IF", "WHILE", "INHERIT", "PLUS", "MINUS", "MUL", "DIV", "MOD", 
			"LESS", "GREATER", "LTE", "GTE", "NOT", "AND", "OR", "EQUAL_TO", "NOT_EQUAL", 
			"CONCAT", "PERIOD", "COMMA", "SEMI", "EQUAL", "COLON", "LB", "RB", "LSB", 
			"RSB", "LCB", "RCB", "IDENTIFIER", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
			"ILLEGAL_ESCAPE"
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


	public BKOOLLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "BKOOL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;\u021a\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\3\2\3\2\3\2\3\3\3\3\5\3"+
		"\u00a7\n\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u00af\n\4\f\4\16\4\u00b2\13\4\3"+
		"\5\3\5\3\5\3\5\7\5\u00b8\n\5\f\5\16\5\u00bb\13\5\3\5\3\5\3\5\3\6\3\6\3"+
		"\6\7\6\u00c3\n\6\f\6\16\6\u00c6\13\6\3\6\3\6\6\6\u00ca\n\6\r\6\16\6\u00cb"+
		"\7\6\u00ce\n\6\f\6\16\6\u00d1\13\6\5\6\u00d3\n\6\3\7\3\7\3\b\3\b\5\b\u00d9"+
		"\n\b\3\t\3\t\3\t\6\t\u00de\n\t\r\t\16\t\u00df\3\t\3\t\7\t\u00e4\n\t\f"+
		"\t\16\t\u00e7\13\t\5\t\u00e9\n\t\3\n\6\n\u00ec\n\n\r\n\16\n\u00ed\3\n"+
		"\3\n\3\n\6\n\u00f3\n\n\r\n\16\n\u00f4\3\13\3\13\5\13\u00f9\n\13\3\f\3"+
		"\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\7\16\u0109\n\16"+
		"\f\16\16\16\u010c\13\16\3\16\3\16\3\17\3\17\3\17\3\17\7\17\u0114\n\17"+
		"\f\17\16\17\u0117\13\17\3\17\3\17\3\17\3\20\3\20\5\20\u011e\n\20\3\20"+
		"\3\20\3\21\3\21\3\21\5\21\u0125\n\21\3\22\3\22\3\22\3\22\3\22\5\22\u012c"+
		"\n\22\3\23\3\23\3\23\3\23\3\23\5\23\u0133\n\23\3\24\3\24\3\24\3\24\3\24"+
		"\5\24\u013a\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u0143\n\25\3"+
		"\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3"+
		"\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!"+
		"\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3"+
		"$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3"+
		"\'\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3"+
		"+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\3.\3.\3.\3.\3.\3/\3/\3/\3\60\3\60"+
		"\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62"+
		"\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\39\3:\3"+
		":\3:\3;\3;\3<\3<\3<\3=\3=\3=\3>\3>\3>\3?\3?\3?\3@\3@\3@\3A\3A\3B\3B\3"+
		"C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3L\6L\u0204\nL\r"+
		"L\16L\u0205\3L\7L\u0209\nL\fL\16L\u020c\13L\3M\6M\u020f\nM\rM\16M\u0210"+
		"\3M\3M\3N\3N\3O\3O\3P\3P\5\u00b9\u010a\u0115\2Q\3\3\5\4\7\2\t\2\13\5\r"+
		"\2\17\6\21\2\23\2\25\7\27\2\31\2\33\b\35\2\37\t!\2#\2%\2\'\2)\2+\2-\2"+
		"/\2\61\2\63\2\65\2\67\29\2;\2=\n?\13A\fC\rE\16G\17I\20K\21M\22O\23Q\24"+
		"S\25U\26W\27Y\30[\31]\32_\33a\34c\35e\36g\37i k!m\"o#q$s%u&w\'y({)}*\177"+
		"+\u0081,\u0083-\u0085.\u0087/\u0089\60\u008b\61\u008d\62\u008f\63\u0091"+
		"\64\u0093\65\u0095\66\u0097\67\u00998\u009b9\u009d:\u009f;\3\2\21\4\2"+
		"\f\f\17\17\3\2\63;\3\2\62;\4\2GGgg\4\2$$^^\3\2$$\3\2))\3\2\n\n\3\2\16"+
		"\16\3\2\17\17\3\2\f\f\3\2^^\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\""+
		"\"\2\u0223\2\3\3\2\2\2\2\5\3\2\2\2\2\13\3\2\2\2\2\17\3\2\2\2\2\25\3\2"+
		"\2\2\2\33\3\2\2\2\2\37\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2"+
		"\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2"+
		"\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]"+
		"\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2"+
		"\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2"+
		"\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2"+
		"\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2"+
		"\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093"+
		"\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2"+
		"\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\3\u00a1\3\2\2\2\5\u00a6\3\2\2\2\7\u00aa"+
		"\3\2\2\2\t\u00b3\3\2\2\2\13\u00d2\3\2\2\2\r\u00d4\3\2\2\2\17\u00d8\3\2"+
		"\2\2\21\u00da\3\2\2\2\23\u00eb\3\2\2\2\25\u00f8\3\2\2\2\27\u00fa\3\2\2"+
		"\2\31\u0100\3\2\2\2\33\u0105\3\2\2\2\35\u010f\3\2\2\2\37\u011b\3\2\2\2"+
		"!\u0124\3\2\2\2#\u012b\3\2\2\2%\u0132\3\2\2\2\'\u0139\3\2\2\2)\u0142\3"+
		"\2\2\2+\u0144\3\2\2\2-\u0146\3\2\2\2/\u0148\3\2\2\2\61\u014a\3\2\2\2\63"+
		"\u014c\3\2\2\2\65\u014e\3\2\2\2\67\u0150\3\2\2\29\u0152\3\2\2\2;\u0154"+
		"\3\2\2\2=\u0157\3\2\2\2?\u015c\3\2\2\2A\u0162\3\2\2\2C\u016a\3\2\2\2E"+
		"\u016f\3\2\2\2G\u0175\3\2\2\2I\u017b\3\2\2\2K\u0182\3\2\2\2M\u0186\3\2"+
		"\2\2O\u018e\3\2\2\2Q\u0192\3\2\2\2S\u0199\3\2\2\2U\u01a2\3\2\2\2W\u01a5"+
		"\3\2\2\2Y\u01ae\3\2\2\2[\u01b1\3\2\2\2]\u01b6\3\2\2\2_\u01b9\3\2\2\2a"+
		"\u01bf\3\2\2\2c\u01c7\3\2\2\2e\u01c9\3\2\2\2g\u01cb\3\2\2\2i\u01cd\3\2"+
		"\2\2k\u01cf\3\2\2\2m\u01d1\3\2\2\2o\u01d3\3\2\2\2q\u01d5\3\2\2\2s\u01d8"+
		"\3\2\2\2u\u01db\3\2\2\2w\u01dd\3\2\2\2y\u01e0\3\2\2\2{\u01e3\3\2\2\2}"+
		"\u01e6\3\2\2\2\177\u01e9\3\2\2\2\u0081\u01ec\3\2\2\2\u0083\u01ee\3\2\2"+
		"\2\u0085\u01f0\3\2\2\2\u0087\u01f2\3\2\2\2\u0089\u01f4\3\2\2\2\u008b\u01f6"+
		"\3\2\2\2\u008d\u01f8\3\2\2\2\u008f\u01fa\3\2\2\2\u0091\u01fc\3\2\2\2\u0093"+
		"\u01fe\3\2\2\2\u0095\u0200\3\2\2\2\u0097\u0203\3\2\2\2\u0099\u020e\3\2"+
		"\2\2\u009b\u0214\3\2\2\2\u009d\u0216\3\2\2\2\u009f\u0218\3\2\2\2\u00a1"+
		"\u00a2\7}\2\2\u00a2\u00a3\7\177\2\2\u00a3\4\3\2\2\2\u00a4\u00a7\5\7\4"+
		"\2\u00a5\u00a7\5\t\5\2\u00a6\u00a4\3\2\2\2\u00a6\u00a5\3\2\2\2\u00a7\u00a8"+
		"\3\2\2\2\u00a8\u00a9\b\3\2\2\u00a9\6\3\2\2\2\u00aa\u00ab\7\61\2\2\u00ab"+
		"\u00ac\7\61\2\2\u00ac\u00b0\3\2\2\2\u00ad\u00af\n\2\2\2\u00ae\u00ad\3"+
		"\2\2\2\u00af\u00b2\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1"+
		"\b\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3\u00b4\7\61\2\2\u00b4\u00b5\7,\2\2"+
		"\u00b5\u00b9\3\2\2\2\u00b6\u00b8\13\2\2\2\u00b7\u00b6\3\2\2\2\u00b8\u00bb"+
		"\3\2\2\2\u00b9\u00ba\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba\u00bc\3\2\2\2\u00bb"+
		"\u00b9\3\2\2\2\u00bc\u00bd\7,\2\2\u00bd\u00be\7\61\2\2\u00be\n\3\2\2\2"+
		"\u00bf\u00d3\7\62\2\2\u00c0\u00c4\t\3\2\2\u00c1\u00c3\t\4\2\2\u00c2\u00c1"+
		"\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5"+
		"\u00cf\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c7\u00c9\5\r\7\2\u00c8\u00ca\t\4"+
		"\2\2\u00c9\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb"+
		"\u00cc\3\2\2\2\u00cc\u00ce\3\2\2\2\u00cd\u00c7\3\2\2\2\u00ce\u00d1\3\2"+
		"\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d3\3\2\2\2\u00d1"+
		"\u00cf\3\2\2\2\u00d2\u00bf\3\2\2\2\u00d2\u00c0\3\2\2\2\u00d3\f\3\2\2\2"+
		"\u00d4\u00d5\7a\2\2\u00d5\16\3\2\2\2\u00d6\u00d9\5\23\n\2\u00d7\u00d9"+
		"\5\21\t\2\u00d8\u00d6\3\2\2\2\u00d8\u00d7\3\2\2\2\u00d9\20\3\2\2\2\u00da"+
		"\u00db\5\13\6\2\u00db\u00dd\5\u0081A\2\u00dc\u00de\t\4\2\2\u00dd\u00dc"+
		"\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0"+
		"\u00e8\3\2\2\2\u00e1\u00e5\t\5\2\2\u00e2\u00e4\t\4\2\2\u00e3\u00e2\3\2"+
		"\2\2\u00e4\u00e7\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6"+
		"\u00e9\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e8\u00e1\3\2\2\2\u00e8\u00e9\3\2"+
		"\2\2\u00e9\22\3\2\2\2\u00ea\u00ec\t\4\2\2\u00eb\u00ea\3\2\2\2\u00ec\u00ed"+
		"\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef"+
		"\u00f0\t\5\2\2\u00f0\u00f2\5e\63\2\u00f1\u00f3\t\4\2\2\u00f2\u00f1\3\2"+
		"\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5"+
		"\24\3\2\2\2\u00f6\u00f9\5\27\f\2\u00f7\u00f9\5\31\r\2\u00f8\u00f6\3\2"+
		"\2\2\u00f8\u00f7\3\2\2\2\u00f9\26\3\2\2\2\u00fa\u00fb\7h\2\2\u00fb\u00fc"+
		"\7c\2\2\u00fc\u00fd\7n\2\2\u00fd\u00fe\7u\2\2\u00fe\u00ff\7g\2\2\u00ff"+
		"\30\3\2\2\2\u0100\u0101\7v\2\2\u0101\u0102\7t\2\2\u0102\u0103\7w\2\2\u0103"+
		"\u0104\7g\2\2\u0104\32\3\2\2\2\u0105\u010a\5+\26\2\u0106\u0109\n\6\2\2"+
		"\u0107\u0109\5\35\17\2\u0108\u0106\3\2\2\2\u0108\u0107\3\2\2\2\u0109\u010c"+
		"\3\2\2\2\u010a\u010b\3\2\2\2\u010a\u0108\3\2\2\2\u010b\u010d\3\2\2\2\u010c"+
		"\u010a\3\2\2\2\u010d\u010e\5+\26\2\u010e\34\3\2\2\2\u010f\u0110\7^\2\2"+
		"\u0110\u0111\7$\2\2\u0111\u0115\3\2\2\2\u0112\u0114\13\2\2\2\u0113\u0112"+
		"\3\2\2\2\u0114\u0117\3\2\2\2\u0115\u0116\3\2\2\2\u0115\u0113\3\2\2\2\u0116"+
		"\u0118\3\2\2\2\u0117\u0115\3\2\2\2\u0118\u0119\7^\2\2\u0119\u011a\7$\2"+
		"\2\u011a\36\3\2\2\2\u011b\u011d\5\u0093J\2\u011c\u011e\5!\21\2\u011d\u011c"+
		"\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0120\5\u0095K"+
		"\2\u0120 \3\2\2\2\u0121\u0125\5#\22\2\u0122\u0125\5%\23\2\u0123\u0125"+
		"\5\'\24\2\u0124\u0121\3\2\2\2\u0124\u0122\3\2\2\2\u0124\u0123\3\2\2\2"+
		"\u0125\"\3\2\2\2\u0126\u0127\5\13\6\2\u0127\u0128\5\u0083B\2\u0128\u0129"+
		"\5#\22\2\u0129\u012c\3\2\2\2\u012a\u012c\5\13\6\2\u012b\u0126\3\2\2\2"+
		"\u012b\u012a\3\2\2\2\u012c$\3\2\2\2\u012d\u012e\5\17\b\2\u012e\u012f\5"+
		"\u0083B\2\u012f\u0130\5%\23\2\u0130\u0133\3\2\2\2\u0131\u0133\5\17\b\2"+
		"\u0132\u012d\3\2\2\2\u0132\u0131\3\2\2\2\u0133&\3\2\2\2\u0134\u0135\5"+
		"\33\16\2\u0135\u0136\5\u0083B\2\u0136\u0137\5\'\24\2\u0137\u013a\3\2\2"+
		"\2\u0138\u013a\5\33\16\2\u0139\u0134\3\2\2\2\u0139\u0138\3\2\2\2\u013a"+
		"(\3\2\2\2\u013b\u0143\5/\30\2\u013c\u0143\5\61\31\2\u013d\u0143\5\63\32"+
		"\2\u013e\u0143\5\65\33\2\u013f\u0143\5\67\34\2\u0140\u0143\5;\36\2\u0141"+
		"\u0143\59\35\2\u0142\u013b\3\2\2\2\u0142\u013c\3\2\2\2\u0142\u013d\3\2"+
		"\2\2\u0142\u013e\3\2\2\2\u0142\u013f\3\2\2\2\u0142\u0140\3\2\2\2\u0142"+
		"\u0141\3\2\2\2\u0143*\3\2\2\2\u0144\u0145\t\7\2\2\u0145,\3\2\2\2\u0146"+
		"\u0147\t\b\2\2\u0147.\3\2\2\2\u0148\u0149\t\t\2\2\u0149\60\3\2\2\2\u014a"+
		"\u014b\t\n\2\2\u014b\62\3\2\2\2\u014c\u014d\t\13\2\2\u014d\64\3\2\2\2"+
		"\u014e\u014f\t\f\2\2\u014f\66\3\2\2\2\u0150\u0151\7)\2\2\u01518\3\2\2"+
		"\2\u0152\u0153\t\r\2\2\u0153:\3\2\2\2\u0154\u0155\7^\2\2\u0155\u0156\7"+
		"$\2\2\u0156<\3\2\2\2\u0157\u0158\7c\2\2\u0158\u0159\7w\2\2\u0159\u015a"+
		"\7v\2\2\u015a\u015b\7q\2\2\u015b>\3\2\2\2\u015c\u015d\7d\2\2\u015d\u015e"+
		"\7t\2\2\u015e\u015f\7g\2\2\u015f\u0160\7c\2\2\u0160\u0161\7m\2\2\u0161"+
		"@\3\2\2\2\u0162\u0163\7k\2\2\u0163\u0164\7p\2\2\u0164\u0165\7v\2\2\u0165"+
		"\u0166\7g\2\2\u0166\u0167\7i\2\2\u0167\u0168\7g\2\2\u0168\u0169\7t\2\2"+
		"\u0169B\3\2\2\2\u016a\u016b\7x\2\2\u016b\u016c\7q\2\2\u016c\u016d\7k\2"+
		"\2\u016d\u016e\7f\2\2\u016eD\3\2\2\2\u016f\u0170\7c\2\2\u0170\u0171\7"+
		"t\2\2\u0171\u0172\7t\2\2\u0172\u0173\7c\2\2\u0173\u0174\7{\2\2\u0174F"+
		"\3\2\2\2\u0175\u0176\7h\2\2\u0176\u0177\7n\2\2\u0177\u0178\7q\2\2\u0178"+
		"\u0179\7c\2\2\u0179\u017a\7v\2\2\u017aH\3\2\2\2\u017b\u017c\7t\2\2\u017c"+
		"\u017d\7g\2\2\u017d\u017e\7v\2\2\u017e\u017f\7w\2\2\u017f\u0180\7t\2\2"+
		"\u0180\u0181\7p\2\2\u0181J\3\2\2\2\u0182\u0183\7q\2\2\u0183\u0184\7w\2"+
		"\2\u0184\u0185\7v\2\2\u0185L\3\2\2\2\u0186\u0187\7d\2\2\u0187\u0188\7"+
		"q\2\2\u0188\u0189\7q\2\2\u0189\u018a\7n\2\2\u018a\u018b\7g\2\2\u018b\u018c"+
		"\7c\2\2\u018c\u018d\7p\2\2\u018dN\3\2\2\2\u018e\u018f\7h\2\2\u018f\u0190"+
		"\7q\2\2\u0190\u0191\7t\2\2\u0191P\3\2\2\2\u0192\u0193\7u\2\2\u0193\u0194"+
		"\7v\2\2\u0194\u0195\7t\2\2\u0195\u0196\7k\2\2\u0196\u0197\7p\2\2\u0197"+
		"\u0198\7i\2\2\u0198R\3\2\2\2\u0199\u019a\7e\2\2\u019a\u019b\7q\2\2\u019b"+
		"\u019c\7p\2\2\u019c\u019d\7v\2\2\u019d\u019e\7k\2\2\u019e\u019f\7p\2\2"+
		"\u019f\u01a0\7w\2\2\u01a0\u01a1\7g\2\2\u01a1T\3\2\2\2\u01a2\u01a3\7f\2"+
		"\2\u01a3\u01a4\7q\2\2\u01a4V\3\2\2\2\u01a5\u01a6\7h\2\2\u01a6\u01a7\7"+
		"w\2\2\u01a7\u01a8\7p\2\2\u01a8\u01a9\7e\2\2\u01a9\u01aa\7v\2\2\u01aa\u01ab"+
		"\7k\2\2\u01ab\u01ac\7q\2\2\u01ac\u01ad\7p\2\2\u01adX\3\2\2\2\u01ae\u01af"+
		"\7q\2\2\u01af\u01b0\7h\2\2\u01b0Z\3\2\2\2\u01b1\u01b2\7g\2\2\u01b2\u01b3"+
		"\7n\2\2\u01b3\u01b4\7u\2\2\u01b4\u01b5\7g\2\2\u01b5\\\3\2\2\2\u01b6\u01b7"+
		"\7k\2\2\u01b7\u01b8\7h\2\2\u01b8^\3\2\2\2\u01b9\u01ba\7y\2\2\u01ba\u01bb"+
		"\7j\2\2\u01bb\u01bc\7k\2\2\u01bc\u01bd\7n\2\2\u01bd\u01be\7g\2\2\u01be"+
		"`\3\2\2\2\u01bf\u01c0\7k\2\2\u01c0\u01c1\7p\2\2\u01c1\u01c2\7j\2\2\u01c2"+
		"\u01c3\7g\2\2\u01c3\u01c4\7t\2\2\u01c4\u01c5\7k\2\2\u01c5\u01c6\7v\2\2"+
		"\u01c6b\3\2\2\2\u01c7\u01c8\7-\2\2\u01c8d\3\2\2\2\u01c9\u01ca\7/\2\2\u01ca"+
		"f\3\2\2\2\u01cb\u01cc\7,\2\2\u01cch\3\2\2\2\u01cd\u01ce\7\61\2\2\u01ce"+
		"j\3\2\2\2\u01cf\u01d0\7\'\2\2\u01d0l\3\2\2\2\u01d1\u01d2\7>\2\2\u01d2"+
		"n\3\2\2\2\u01d3\u01d4\7@\2\2\u01d4p\3\2\2\2\u01d5\u01d6\7>\2\2\u01d6\u01d7"+
		"\7?\2\2\u01d7r\3\2\2\2\u01d8\u01d9\7@\2\2\u01d9\u01da\7?\2\2\u01dat\3"+
		"\2\2\2\u01db\u01dc\7#\2\2\u01dcv\3\2\2\2\u01dd\u01de\7(\2\2\u01de\u01df"+
		"\7(\2\2\u01dfx\3\2\2\2\u01e0\u01e1\7~\2\2\u01e1\u01e2\7~\2\2\u01e2z\3"+
		"\2\2\2\u01e3\u01e4\7?\2\2\u01e4\u01e5\7?\2\2\u01e5|\3\2\2\2\u01e6\u01e7"+
		"\7#\2\2\u01e7\u01e8\7?\2\2\u01e8~\3\2\2\2\u01e9\u01ea\7<\2\2\u01ea\u01eb"+
		"\7<\2\2\u01eb\u0080\3\2\2\2\u01ec\u01ed\7\60\2\2\u01ed\u0082\3\2\2\2\u01ee"+
		"\u01ef\7.\2\2\u01ef\u0084\3\2\2\2\u01f0\u01f1\7=\2\2\u01f1\u0086\3\2\2"+
		"\2\u01f2\u01f3\7?\2\2\u01f3\u0088\3\2\2\2\u01f4\u01f5\7<\2\2\u01f5\u008a"+
		"\3\2\2\2\u01f6\u01f7\7*\2\2\u01f7\u008c\3\2\2\2\u01f8\u01f9\7+\2\2\u01f9"+
		"\u008e\3\2\2\2\u01fa\u01fb\7]\2\2\u01fb\u0090\3\2\2\2\u01fc\u01fd\7_\2"+
		"\2\u01fd\u0092\3\2\2\2\u01fe\u01ff\7}\2\2\u01ff\u0094\3\2\2\2\u0200\u0201"+
		"\7\177\2\2\u0201\u0096\3\2\2\2\u0202\u0204\t\16\2\2\u0203\u0202\3\2\2"+
		"\2\u0204\u0205\3\2\2\2\u0205\u0203\3\2\2\2\u0205\u0206\3\2\2\2\u0206\u020a"+
		"\3\2\2\2\u0207\u0209\t\17\2\2\u0208\u0207\3\2\2\2\u0209\u020c\3\2\2\2"+
		"\u020a\u0208\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u0098\3\2\2\2\u020c\u020a"+
		"\3\2\2\2\u020d\u020f\t\20\2\2\u020e\u020d\3\2\2\2\u020f\u0210\3\2\2\2"+
		"\u0210\u020e\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u0213"+
		"\bM\2\2\u0213\u009a\3\2\2\2\u0214\u0215\13\2\2\2\u0215\u009c\3\2\2\2\u0216"+
		"\u0217\13\2\2\2\u0217\u009e\3\2\2\2\u0218\u0219\13\2\2\2\u0219\u00a0\3"+
		"\2\2\2\35\2\u00a6\u00b0\u00b9\u00c4\u00cb\u00cf\u00d2\u00d8\u00df\u00e5"+
		"\u00e8\u00ed\u00f4\u00f8\u0108\u010a\u0115\u011d\u0124\u012b\u0132\u0139"+
		"\u0142\u0205\u020a\u0210\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}