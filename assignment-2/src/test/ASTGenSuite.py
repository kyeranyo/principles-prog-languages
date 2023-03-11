import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input = """x,y,z: array [2_34_5,4,2,5] of integer;"""
        expect = """Program([
	VarDecl(x, ArrayType([2345, 4, 2, 5], IntegerType))
	VarDecl(y, ArrayType([2345, 4, 2, 5], IntegerType))
	VarDecl(z, ArrayType([2345, 4, 2, 5], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_short_vardecl2(self):
        input = """x,y,z: integer;"""
        expect = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, IntegerType)
	VarDecl(z, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_full_vardecl(self):
        input = """x,y,z: auto = 1,2,3;"""
        expect = """Program([
	VarDecl(x, AutoType, IntegerLit(1))
	VarDecl(y, AutoType, IntegerLit(2))
	VarDecl(z, AutoType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_vardecls(self):
        input = """x,y,z: integer = 1,2,3;
        a, b: float;
        n : array [1,3,4,2] of integer;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
	VarDecl(n, ArrayType([1, 3, 4, 2], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_simple_program(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_more_complex_program(self):
        """More complex program"""
        input = """
        in : function void () {
                for( i = 0, i < 1, i = i + 1){
                        for( j = 0, j < 1 + 1, j = j + 1){}
                }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_more_complex_program2(self):
        """More complex program"""
        input = """
        in : function void () {
                while (true) {}
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_more_complex_program3(self):
        """More complex program"""
        input = """
        in : function void () {
                while (true) {
                        continue;
                        break;
                        return a + b - c * d + e * f + 999999;
                        return;
                }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_more_complex_program4(self):
        """More complex program"""
        input ="""
foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

main: function void () {
     printInteger(4);
}
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))
