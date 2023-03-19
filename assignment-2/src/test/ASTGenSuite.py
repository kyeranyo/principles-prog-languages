import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test1(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 301))

    def test2(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test3(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test4(self):
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test5(self):
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test6(self):
        input = """
foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

main: function void () {
     printInteger(4);
}"""
        expect = """Program([
\tFuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
\tFuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test7(self):

        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test8(self):

        input = """func: function integer () {
            preventDefault();
        }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([CallStmt(preventDefault, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test9(self):
        input_str = """
        a : integer = 10;
        func: function string () {
            a, b: integer = 12, 0;
        }
        func : function string () {
            a : integer = 10;
        }
        """
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(10))
	FuncDecl(func, StringType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(12)), VarDecl(b, IntegerType, IntegerLit(0))]))
	FuncDecl(func, StringType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(10))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 309))

    def test10(self):
        input = """alter: array [3] of integer;"""
        expect = """Program([
	VarDecl(alter, ArrayType([3], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test11(self):
        input = """alter: array[2,3,4,5] of float;"""
        expect = """Program([
	VarDecl(alter, ArrayType([2, 3, 4, 5], FloatType))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test12(self):
        input = """a, b, c: integer = 12.5, 45e10, 32;"""
        expect = """Program([
	VarDecl(a, IntegerType, FloatLit(12.5))
	VarDecl(b, IntegerType, FloatLit(450000000000.0))
	VarDecl(c, IntegerType, IntegerLit(32))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test13(self):
        input = """a: float = 12*6>3;"""
        expect = """Program([
	VarDecl(a, FloatType, BinExpr(>, BinExpr(*, IntegerLit(12), IntegerLit(6)), IntegerLit(3)))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test14(self):
        input = """chinh: string = "Xinchao rat vui duoc gap ban $$$#$@#@D haha";"""
        expect = """Program([
	VarDecl(chinh, StringType, StringLit(Xinchao rat vui duoc gap ban $$$#$@#@D haha))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test15(self):
        input = """a, b: array [3,2] of integer = {2, 3}, {"hello", 3+5};"""
        expect = """Program([
	VarDecl(a, ArrayType([3, 2], IntegerType), ArrayLit([IntegerLit(2), IntegerLit(3)]))
	VarDecl(b, ArrayType([3, 2], IntegerType), ArrayLit([StringLit(hello), BinExpr(+, IntegerLit(3), IntegerLit(5))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test16(self):
        input = """x, y, z: array [2] of integer = {5e10 + "hello", -0.0e8}, "hello \\n", 123456789;"""
        expect = """Program([
	VarDecl(x, ArrayType([2], IntegerType), ArrayLit([BinExpr(+, FloatLit(50000000000.0), StringLit(hello)), UnExpr(-, FloatLit(0.0))]))
	VarDecl(y, ArrayType([2], IntegerType), StringLit(hello \\n))
	VarDecl(z, ArrayType([2], IntegerType), IntegerLit(123456789))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test17(self):
        input = """aee123, _asdwe, _bmmwe: float;"""
        expect = """Program([
	VarDecl(aee123, FloatType)
	VarDecl(_asdwe, FloatType)
	VarDecl(_bmmwe, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test18(self):
        input = """a: integer; a: float = -12e8-1648200.2235;"""
        expect = """Program([
	VarDecl(a, IntegerType)
	VarDecl(a, FloatType, BinExpr(-, UnExpr(-, FloatLit(1200000000.0)), FloatLit(1648200.2235)))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test19(self):
        input = """bcs: integer = !12 && abc || "efgha" - .124e8 + 123456 / !"hello" % bc * e; """
        expect = """Program([
	VarDecl(bcs, IntegerType, BinExpr(||, BinExpr(&&, UnExpr(!, IntegerLit(12)), Id(abc)), BinExpr(+, BinExpr(-, StringLit(efgha), FloatLit(12400000.0)), BinExpr(*, BinExpr(%, BinExpr(/, IntegerLit(123456), UnExpr(!, StringLit(hello))), Id(bc)), Id(e)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test20(self):
        input = """isSubsequence : function boolean(s: string, t: string) {
    n = length(s);
    m = length(t);
    i = 0;
    j = 0;
    while ((i < n) && (j < m)) {
        if (s[i] == t[j]) {
            i = i + 1;
        }
        j = j + 1;
    }
    return i == n;
}
main: function void() {
    s = "abc";
    t = "ahbgdc";
    printBool(isSubsequence(s, t));
}
"""
        expect = """Program([
	FuncDecl(isSubsequence, BooleanType, [Param(s, StringType), Param(t, StringType)], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(s)])), AssignStmt(Id(m), FuncCall(length, [Id(t)])), AssignStmt(Id(i), IntegerLit(0)), AssignStmt(Id(j), IntegerLit(0)), WhileStmt(BinExpr(&&, BinExpr(<, Id(i), Id(n)), BinExpr(<, Id(j), Id(m))), BlockStmt([IfStmt(BinExpr(==, ArrayCell(s, [Id(i)]), ArrayCell(t, [Id(j)])), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))])), ReturnStmt(BinExpr(==, Id(i), Id(n)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(abc)), AssignStmt(Id(t), StringLit(ahbgdc)), CallStmt(printBool, FuncCall(isSubsequence, [Id(s), Id(t)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test21(self):
        input = """
                isSubsequence : function boolean(s: string, t: string) {
                    n = length(s);
                    m = length(t);
                    i = 0;
                    j = 0;
                    while ((i < n) && (j < m)) {
                        if (s[i] == t[j]) {
                            i = i + 1;
                        }
                        j = j + 1;
                    }
                    return i == n;
                }
                """
        expect = """Program([
	FuncDecl(isSubsequence, BooleanType, [Param(s, StringType), Param(t, StringType)], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(s)])), AssignStmt(Id(m), FuncCall(length, [Id(t)])), AssignStmt(Id(i), IntegerLit(0)), AssignStmt(Id(j), IntegerLit(0)), WhileStmt(BinExpr(&&, BinExpr(<, Id(i), Id(n)), BinExpr(<, Id(j), Id(m))), BlockStmt([IfStmt(BinExpr(==, ArrayCell(s, [Id(i)]), ArrayCell(t, [Id(j)])), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))])), ReturnStmt(BinExpr(==, Id(i), Id(n)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test22(self):
        input = """countvalue: function integer (a: array[5] of string, b:string) {
            count: string = 0;
            for (i=0, i<countlength(a), i+1) {
                if (a[i]==b) count=count+1;
            }
            return count;
        }"""
        expect = """Program([
	FuncDecl(countvalue, IntegerType, [Param(a, ArrayType([5], StringType)), Param(b, StringType)], None, BlockStmt([VarDecl(count, StringType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(countlength, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(a, [Id(i)]), Id(b)), AssignStmt(Id(count), BinExpr(+, Id(count), IntegerLit(1))))])), ReturnStmt(Id(count))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test23(self):
        input = """swap: function void(a: integer, b: integer) {
    temp = a;
    a = b;
    b = temp;
}

bubbleSort: function void (arr: array [10] of integer) {
    n = 10;
    swapped = true;
    while (swapped) {
        swapped = false;
        for (i = 0, i < n - 1, i + 1) {
            if (arr[i] > arr[i + 1]) {
                swap(arr[i], arr[i + 1]);
                swapped = true;
            }
        }
    }
}

printArray: function void (arr: array [10] of integer) {
    for (i = 0, i < 10, i + 1) {
        printInt(arr[i]);
    }
}

main: function void () {
    arr = {5, 2, 8, 4, 9, 1, 3, 7, 6, 0};
    bubbleSort(arr);
    printArray(arr);
}"""
        expect = """Program([
	FuncDecl(swap, VoidType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([AssignStmt(Id(temp), Id(a)), AssignStmt(Id(a), Id(b)), AssignStmt(Id(b), Id(temp))]))
	FuncDecl(bubbleSort, VoidType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([AssignStmt(Id(n), IntegerLit(10)), AssignStmt(Id(swapped), BooleanLit(True)), WhileStmt(Id(swapped), BlockStmt([AssignStmt(Id(swapped), BooleanLit(False)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(arr, [Id(i)]), ArrayCell(arr, [BinExpr(+, Id(i), IntegerLit(1))])), BlockStmt([CallStmt(swap, ArrayCell(arr, [Id(i)]), ArrayCell(arr, [BinExpr(+, Id(i), IntegerLit(1))])), AssignStmt(Id(swapped), BooleanLit(True))]))]))]))]))
	FuncDecl(printArray, VoidType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInt, ArrayCell(arr, [Id(i)]))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(arr), ArrayLit([IntegerLit(5), IntegerLit(2), IntegerLit(8), IntegerLit(4), IntegerLit(9), IntegerLit(1), IntegerLit(3), IntegerLit(7), IntegerLit(6), IntegerLit(0)])), CallStmt(bubbleSort, Id(arr)), CallStmt(printArray, Id(arr))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test24(self):
        input = """isSubsequence : function boolean (s : string, t : string) {
    n = length(s);
    m = length(t);
    i = 0;
    j = 0;
    while ((i < n) && (j < m)) {
        if (s[i] == t[j]) {
            i = i + 1;
        }
        j = j + 1;
    }
    return i == n;
}

main: function void () {
    s = "abc";
    t = "ahbgdc";
    printBool(isSubsequence(s, t));
}"""
        expect = """Program([
	FuncDecl(isSubsequence, BooleanType, [Param(s, StringType), Param(t, StringType)], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(s)])), AssignStmt(Id(m), FuncCall(length, [Id(t)])), AssignStmt(Id(i), IntegerLit(0)), AssignStmt(Id(j), IntegerLit(0)), WhileStmt(BinExpr(&&, BinExpr(<, Id(i), Id(n)), BinExpr(<, Id(j), Id(m))), BlockStmt([IfStmt(BinExpr(==, ArrayCell(s, [Id(i)]), ArrayCell(t, [Id(j)])), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))])), ReturnStmt(BinExpr(==, Id(i), Id(n)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(abc)), AssignStmt(Id(t), StringLit(ahbgdc)), CallStmt(printBool, FuncCall(isSubsequence, [Id(s), Id(t)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test25(self):
        input = """isPrime : function boolean(n: integer) {
    if (n < 2) {
        return false;
    }
    for (i = 2, i <= sqrt(n), i + 1) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

main: function void() {
    printBool(isPrime(17));
    printBool(isPrime(20));
}"""
        expect = """Program([
	FuncDecl(isPrime, BooleanType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(n), IntegerLit(2)), BlockStmt([ReturnStmt(BooleanLit(False))])), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), FuncCall(sqrt, [Id(n)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))]))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printBool, FuncCall(isPrime, [IntegerLit(17)])), CallStmt(printBool, FuncCall(isPrime, [IntegerLit(20)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test26(self):
        input = """romanToInt : function integer (s : string) {
    n = length(s);
    result = 0;
    for (i = 0, i < n, i + 1) {
        if ((i > 0) && (roman[s[i]] > roman[s[i - 1]])) {
            result = result + roman[s[i]] - 2 * roman[s[i - 1]];
        } else {
            result = result + roman[s[i]];
        }
    }
    return result;
}

main: function void () {
    s = "MCMXCIV";
    printInt(romanToInt(s));
}"""
        expect = """Program([
	FuncDecl(romanToInt, IntegerType, [Param(s, StringType)], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(s)])), AssignStmt(Id(result), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(&&, BinExpr(>, Id(i), IntegerLit(0)), BinExpr(>, ArrayCell(roman, [ArrayCell(s, [Id(i)])]), ArrayCell(roman, [ArrayCell(s, [BinExpr(-, Id(i), IntegerLit(1))])]))), BlockStmt([AssignStmt(Id(result), BinExpr(-, BinExpr(+, Id(result), ArrayCell(roman, [ArrayCell(s, [Id(i)])])), BinExpr(*, IntegerLit(2), ArrayCell(roman, [ArrayCell(s, [BinExpr(-, Id(i), IntegerLit(1))])]))))]), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(roman, [ArrayCell(s, [Id(i)])])))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(MCMXCIV)), CallStmt(printInt, FuncCall(romanToInt, [Id(s)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test27(self):
        input = """fibonacci : function integer(n: integer) {
    if (n == 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    } else {
        return fibonacci(n-1) + fibonacci(n-2);
    }
}

main: function void() {
    print(fibonacci(7)); // prints 13
}"""
        expect = """Program([
	FuncDecl(fibonacci, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(IntegerLit(0))]), IfStmt(BinExpr(==, Id(n), IntegerLit(1)), BlockStmt([ReturnStmt(IntegerLit(1))]), BlockStmt([ReturnStmt(BinExpr(+, FuncCall(fibonacci, [BinExpr(-, Id(n), IntegerLit(1))]), FuncCall(fibonacci, [BinExpr(-, Id(n), IntegerLit(2))])))])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(print, FuncCall(fibonacci, [IntegerLit(7)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test28(self):
        input = """sumArray : function integer(arr: array[3] of integer) {
    sum = 0;
    for (i = 0, i < length(arr), i + 1) {
        sum = sum + arr[i];
    }
    return sum;
}

main: function void() {
    a = {1, 2, 3, 4, 5};
    print(sumArray(a));
}"""
        expect = """Program([
	FuncDecl(sumArray, IntegerType, [Param(arr, ArrayType([3], IntegerType))], None, BlockStmt([AssignStmt(Id(sum), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(arr)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(arr, [Id(i)])))])), ReturnStmt(Id(sum))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), CallStmt(print, FuncCall(sumArray, [Id(a)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test29(self):
        input = """isPerfect : function boolean(n: integer) {
    sum = 0;
    for (i = 1, i < n, i + 1) {
        if (n % i == 0) {
            sum = sum + i;
        }
    }
    return sum == n;
}

main: function void() {
    printBool(isPerfect(6));
    printBool(isPerfect(10));
}"""
        expect = """Program([
	FuncDecl(isPerfect, BooleanType, [Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(sum), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(i)))]))])), ReturnStmt(BinExpr(==, Id(sum), Id(n)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printBool, FuncCall(isPerfect, [IntegerLit(6)])), CallStmt(printBool, FuncCall(isPerfect, [IntegerLit(10)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test30(self):
        input = """sortDescending : function void(arr: array[3] of integer) {
    n = length(arr);
    swapped = true;
    while (swapped) {
        swapped = false;
        for (i = 0, i < n - 1, i + 1) {
            if (arr[i] < arr[i + 1]) {
                temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
                swapped = true;
            }
        }
    }
}

main: function void() {
    a = {3, 5, 2, 8, 1};
    sortDescending(a);
    print(a);
}"""
        expect = """Program([
	FuncDecl(sortDescending, VoidType, [Param(arr, ArrayType([3], IntegerType))], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(arr)])), AssignStmt(Id(swapped), BooleanLit(True)), WhileStmt(Id(swapped), BlockStmt([AssignStmt(Id(swapped), BooleanLit(False)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(arr, [Id(i)]), ArrayCell(arr, [BinExpr(+, Id(i), IntegerLit(1))])), BlockStmt([AssignStmt(Id(temp), ArrayCell(arr, [Id(i)])), AssignStmt(ArrayCell(arr, [Id(i)]), ArrayCell(arr, [BinExpr(+, Id(i), IntegerLit(1))])), AssignStmt(ArrayCell(arr, [BinExpr(+, Id(i), IntegerLit(1))]), Id(temp)), AssignStmt(Id(swapped), BooleanLit(True))]))]))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([IntegerLit(3), IntegerLit(5), IntegerLit(2), IntegerLit(8), IntegerLit(1)])), CallStmt(sortDescending, Id(a)), CallStmt(print, Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test31(self):
        input = """sum : function integer(a: integer, b: integer) {
    return a + b;
}
main: function void() {
    print(sum(1,2));
}"""
        expect = """Program([
	FuncDecl(sum, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(print, FuncCall(sum, [IntegerLit(1), IntegerLit(2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test32(self):
        input = """foo: function void (a: auto) {
            hello(a,b[100]);
            dosth(hello(abc,said()));   
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, AutoType)], None, BlockStmt([CallStmt(hello, Id(a), ArrayCell(b, [IntegerLit(100)])), CallStmt(dosth, FuncCall(hello, [Id(abc), FuncCall(said, [])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test33(self):
        input = """foo: function integer () {
            if (a<=a[i])
                if (a["hhaha",i]==a) a=a+2;
                else if (a[hellu]<=3) a[haha]=4; 
                    else cdef=345;
            else haha=ac;
        }"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([IfStmt(BinExpr(<=, Id(a), ArrayCell(a, [Id(i)])), IfStmt(BinExpr(==, ArrayCell(a, [StringLit(hhaha), Id(i)]), Id(a)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(2))), IfStmt(BinExpr(<=, ArrayCell(a, [Id(hellu)]), IntegerLit(3)), AssignStmt(ArrayCell(a, [Id(haha)]), IntegerLit(4)), AssignStmt(Id(cdef), IntegerLit(345)))), AssignStmt(Id(haha), Id(ac)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test34(self):
        input = """isPerfectSquare: function boolean (n: integer) {
    i = 1;
    while (i * i < n) {
        i = i + 1;
    }
    return i * i == n;
}

main: function void () {
    n = 16;
    printBool(isPerfectSquare(n));
}"""
        expect = """Program([
	FuncDecl(isPerfectSquare, BooleanType, [Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(i), IntegerLit(1)), WhileStmt(BinExpr(<, BinExpr(*, Id(i), Id(i)), Id(n)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), ReturnStmt(BinExpr(==, BinExpr(*, Id(i), Id(i)), Id(n)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), IntegerLit(16)), CallStmt(printBool, FuncCall(isPerfectSquare, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test35(self):
        input = """isPrime: function boolean (n: integer) {
    if (n < 2) {
        return false;
    }
    for (i = 2, i < n, i + 1) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

main: function void () {
    n = 7;
    printBool(isPrime(n));
}"""
        expect = """Program([
	FuncDecl(isPrime, BooleanType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(n), IntegerLit(2)), BlockStmt([ReturnStmt(BooleanLit(False))])), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))]))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), IntegerLit(7)), CallStmt(printBool, FuncCall(isPrime, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test36(self):
        input = """gcd: function integer (a: integer, b: integer) {
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
}

main: function void () {
    a = 24;
    b = 36;
    print(gcd(a, b));
}"""
        expect = """Program([
	FuncDecl(gcd, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(b), IntegerLit(0)), BlockStmt([ReturnStmt(Id(a))])), ReturnStmt(FuncCall(gcd, [Id(b), BinExpr(%, Id(a), Id(b))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(24)), AssignStmt(Id(b), IntegerLit(36)), CallStmt(print, FuncCall(gcd, [Id(a), Id(b)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test37(self):
        input = """factorial: function integer (n: integer) {
    if (n == 0) {
        return 1;
    }
    return n * factorial(n - 1);
}

main: function void () {
    n = 5;
    print(factorial(n));
}"""
        expect = """Program([
	FuncDecl(factorial, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(IntegerLit(1))])), ReturnStmt(BinExpr(*, Id(n), FuncCall(factorial, [BinExpr(-, Id(n), IntegerLit(1))])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), IntegerLit(5)), CallStmt(print, FuncCall(factorial, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test38(self):
        input = """findMax: function integer (arr: array[10] of integer) {
    max = arr[0];
    for (i = 1, i < 10, i + 1) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

main: function void () {
    arr = {5, 2, 9, 1, 7, 3, 6, 8, 4, 0};
    print(findMax(arr));
}"""
        expect = """Program([
	FuncDecl(findMax, IntegerType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([AssignStmt(Id(max), ArrayCell(arr, [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(arr, [Id(i)]), Id(max)), BlockStmt([AssignStmt(Id(max), ArrayCell(arr, [Id(i)]))]))])), ReturnStmt(Id(max))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(arr), ArrayLit([IntegerLit(5), IntegerLit(2), IntegerLit(9), IntegerLit(1), IntegerLit(7), IntegerLit(3), IntegerLit(6), IntegerLit(8), IntegerLit(4), IntegerLit(0)])), CallStmt(print, FuncCall(findMax, [Id(arr)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test39(self):
        input = """isPalindrome: function boolean (s: string) {
    n = length(s);
    for (i = 0, i < n / 2, i + 1) {
        if (s[i] != s[n - i - 1]) {
            return false;
        }
    }
    return true;
}

main: function void () {
    s = "abccba";
    printBool(isPalindrome(s));
}"""
        expect = """Program([
	FuncDecl(isPalindrome, BooleanType, [Param(s, StringType)], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(s)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(/, Id(n), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(s, [Id(i)]), ArrayCell(s, [BinExpr(-, BinExpr(-, Id(n), Id(i)), IntegerLit(1))])), BlockStmt([ReturnStmt(BooleanLit(False))]))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(abccba)), CallStmt(printBool, FuncCall(isPalindrome, [Id(s)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test40(self):
        input = """sumArray: function integer(arr: array [10] of integer) {
    sum = 0;
    for (i = 0, i < 10, i + 1) {
        sum = sum + arr[i];
    }
    return sum;
}
main: function void() {
    arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    print(sumArray(arr));
}"""
        expect = """Program([
	FuncDecl(sumArray, IntegerType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([AssignStmt(Id(sum), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(arr, [Id(i)])))])), ReturnStmt(Id(sum))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(arr), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7), IntegerLit(8), IntegerLit(9), IntegerLit(10)])), CallStmt(print, FuncCall(sumArray, [Id(arr)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test41(self):
        input = """findIndex: function integer (arr: array [10] of integer, target: integer) {
    for (i = 0, i < 10, i + 1) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}

main: function void () {
    arr = {5, 2, 8, 4, 9, 1, 3, 7, 6, 0};
    index = findIndex(arr, 4);
    printInt(index);
}"""
        expect = """Program([
	FuncDecl(findIndex, IntegerType, [Param(arr, ArrayType([10], IntegerType)), Param(target, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(arr, [Id(i)]), Id(target)), BlockStmt([ReturnStmt(Id(i))]))])), ReturnStmt(UnExpr(-, IntegerLit(1)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(arr), ArrayLit([IntegerLit(5), IntegerLit(2), IntegerLit(8), IntegerLit(4), IntegerLit(9), IntegerLit(1), IntegerLit(3), IntegerLit(7), IntegerLit(6), IntegerLit(0)])), AssignStmt(Id(index), FuncCall(findIndex, [Id(arr), IntegerLit(4)])), CallStmt(printInt, Id(index))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test42(self):
        input = """minArray: function integer (arr: array [10] of integer) {
    min = arr[0];
    for (i = 1, i < 10, i + 1) {
        if (arr[i] < min) {
            min = arr[i];
        }
    }
    return min;
}

main: function void () {
    arr = {5, 2, 8, 4, 9, 1, 3, 7, 6, 0};
    minVal = minArray(arr);
    printInt(minVal);
}"""
        expect = """Program([
	FuncDecl(minArray, IntegerType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([AssignStmt(Id(min), ArrayCell(arr, [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(arr, [Id(i)]), Id(min)), BlockStmt([AssignStmt(Id(min), ArrayCell(arr, [Id(i)]))]))])), ReturnStmt(Id(min))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(arr), ArrayLit([IntegerLit(5), IntegerLit(2), IntegerLit(8), IntegerLit(4), IntegerLit(9), IntegerLit(1), IntegerLit(3), IntegerLit(7), IntegerLit(6), IntegerLit(0)])), AssignStmt(Id(minVal), FuncCall(minArray, [Id(arr)])), CallStmt(printInt, Id(minVal))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test43(self):
        input = """isAscending: function boolean (arr: array [10] of integer) {
    for (i = 0, i < 9, i + 1) {
        if (arr[i] > arr[i + 1]) {
            return false;
        }
    }
    return true;
}

main: function void () {
    arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    ascending = isAscending(arr);
    if (ascending) {
        printString("The array is in ascending order");
    } else {
        printString("The array is not in ascending order");
    }
}"""
        expect = """Program([
	FuncDecl(isAscending, BooleanType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(9)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(arr, [Id(i)]), ArrayCell(arr, [BinExpr(+, Id(i), IntegerLit(1))])), BlockStmt([ReturnStmt(BooleanLit(False))]))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(arr), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7), IntegerLit(8), IntegerLit(9), IntegerLit(10)])), AssignStmt(Id(ascending), FuncCall(isAscending, [Id(arr)])), IfStmt(Id(ascending), BlockStmt([CallStmt(printString, StringLit(The array is in ascending order))]), BlockStmt([CallStmt(printString, StringLit(The array is not in ascending order))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test44(self):
        input = """contains: function boolean (arr: array [10] of integer, target: integer) {
    for (i = 0, i < 10, i + 1) {
        if (arr[i] == target) {
            return true;
        }
    }
    return false;
}

main: function void () {
    arr = {5, 2, 8, 4, 9, 1, 3, 7, 6, 0};
    if (contains(arr, 4)) {
        printString("The array contains the target value");
    } else {
        printString("The array does not contain the target value");
    }
}"""
        expect = """Program([
	FuncDecl(contains, BooleanType, [Param(arr, ArrayType([10], IntegerType)), Param(target, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(arr, [Id(i)]), Id(target)), BlockStmt([ReturnStmt(BooleanLit(True))]))])), ReturnStmt(BooleanLit(False))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(arr), ArrayLit([IntegerLit(5), IntegerLit(2), IntegerLit(8), IntegerLit(4), IntegerLit(9), IntegerLit(1), IntegerLit(3), IntegerLit(7), IntegerLit(6), IntegerLit(0)])), IfStmt(FuncCall(contains, [Id(arr), IntegerLit(4)]), BlockStmt([CallStmt(printString, StringLit(The array contains the target value))]), BlockStmt([CallStmt(printString, StringLit(The array does not contain the target value))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test45(self):
        input = """countOccurrences: function integer (arr: array [10] of integer, target: integer) {
    count = 0;
    for (i = 0, i < 10, i + 1) {
        if (arr[i] == target) {
            count = count + 1;
        }
    }
    return count;
}

main: function void () {
    arr = {5, 2, 8, 4, 9, 1, 3, 7, 6, 0};
    numOccurrences = countOccurrences(arr, 5);
    printInt(numOccurrences);
}"""
        expect = """Program([
	FuncDecl(countOccurrences, IntegerType, [Param(arr, ArrayType([10], IntegerType)), Param(target, IntegerType)], None, BlockStmt([AssignStmt(Id(count), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(arr, [Id(i)]), Id(target)), BlockStmt([AssignStmt(Id(count), BinExpr(+, Id(count), IntegerLit(1)))]))])), ReturnStmt(Id(count))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(arr), ArrayLit([IntegerLit(5), IntegerLit(2), IntegerLit(8), IntegerLit(4), IntegerLit(9), IntegerLit(1), IntegerLit(3), IntegerLit(7), IntegerLit(6), IntegerLit(0)])), AssignStmt(Id(numOccurrences), FuncCall(countOccurrences, [Id(arr), IntegerLit(5)])), CallStmt(printInt, Id(numOccurrences))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test46(self):
        input = """sumEvenNumbers: function integer (arr: array [10] of integer) {
    sum = 0;
    for (i = 0, i < 10, i + 1) {
        if (arr[i] % 2 == 0) {
            sum = sum + arr[i];
        }
    }
    return sum;
}

main: function void () {
    arr = {5, 2, 8, 4, 9, 1, 3, 7, 6, 0};
    evenSum = sumEvenNumbers(arr);
    printInt(evenSum);
}"""
        expect = """Program([
	FuncDecl(sumEvenNumbers, IntegerType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([AssignStmt(Id(sum), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, ArrayCell(arr, [Id(i)]), IntegerLit(2)), IntegerLit(0)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(arr, [Id(i)])))]))])), ReturnStmt(Id(sum))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(arr), ArrayLit([IntegerLit(5), IntegerLit(2), IntegerLit(8), IntegerLit(4), IntegerLit(9), IntegerLit(1), IntegerLit(3), IntegerLit(7), IntegerLit(6), IntegerLit(0)])), AssignStmt(Id(evenSum), FuncCall(sumEvenNumbers, [Id(arr)])), CallStmt(printInt, Id(evenSum))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test47(self):
        input = """isSymmetric: function boolean (arr: array [10] of integer) {
    for (i = 0, i < 5, i + 1) {
        if (arr[i] != arr[9 - i]) {
            return false;
        }
    }
    return true;
}

main: function void () {
    arr1 = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1};
    arr2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    if (isSymmetric(arr1)) {
        printString("arr1 is symmetric");
    } else {
        printString("arr1 is not symmetric");
    }
    if (isSymmetric(arr2)) {
        printString("arr2 is symmetric");
    } else {
        printString("arr2 is not symmetric");
    }
}"""
        expect = """Program([
	FuncDecl(isSymmetric, BooleanType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(arr, [Id(i)]), ArrayCell(arr, [BinExpr(-, IntegerLit(9), Id(i))])), BlockStmt([ReturnStmt(BooleanLit(False))]))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(arr1), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(5), IntegerLit(4), IntegerLit(3), IntegerLit(2), IntegerLit(1)])), AssignStmt(Id(arr2), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7), IntegerLit(8), IntegerLit(9), IntegerLit(10)])), IfStmt(FuncCall(isSymmetric, [Id(arr1)]), BlockStmt([CallStmt(printString, StringLit(arr1 is symmetric))]), BlockStmt([CallStmt(printString, StringLit(arr1 is not symmetric))])), IfStmt(FuncCall(isSymmetric, [Id(arr2)]), BlockStmt([CallStmt(printString, StringLit(arr2 is symmetric))]), BlockStmt([CallStmt(printString, StringLit(arr2 is not symmetric))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test48(self):
        input = """countAboveAvg: function integer (arr: array [10] of integer) {
    sum = sumArray(arr);
    avg = sum / 10;
    count = 0;
    for (i = 0, i < 10, i + 1) {
        if (arr[i] > avg) {
            count = count + 1;
        }
    }
    return count;
}

main: function void () {
    arr = {5, 2, 8, 4, 9, 1, 3, 7, 6, 0};
    count = countAboveAvg(arr);
    printInt(count);
}"""
        expect = """Program([
	FuncDecl(countAboveAvg, IntegerType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([AssignStmt(Id(sum), FuncCall(sumArray, [Id(arr)])), AssignStmt(Id(avg), BinExpr(/, Id(sum), IntegerLit(10))), AssignStmt(Id(count), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(arr, [Id(i)]), Id(avg)), BlockStmt([AssignStmt(Id(count), BinExpr(+, Id(count), IntegerLit(1)))]))])), ReturnStmt(Id(count))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(arr), ArrayLit([IntegerLit(5), IntegerLit(2), IntegerLit(8), IntegerLit(4), IntegerLit(9), IntegerLit(1), IntegerLit(3), IntegerLit(7), IntegerLit(6), IntegerLit(0)])), AssignStmt(Id(count), FuncCall(countAboveAvg, [Id(arr)])), CallStmt(printInt, Id(count))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test49(self):
        input = """rapael: float = !true + !false -4 + -5 / 3 <= 1 && 3 + 1 - "hello" / "world";"""
        expect = """Program([
	VarDecl(rapael, FloatType, BinExpr(<=, BinExpr(+, BinExpr(-, BinExpr(+, UnExpr(!, BooleanLit(True)), UnExpr(!, BooleanLit(False))), IntegerLit(4)), BinExpr(/, UnExpr(-, IntegerLit(5)), IntegerLit(3))), BinExpr(&&, IntegerLit(1), BinExpr(-, BinExpr(+, IntegerLit(3), IntegerLit(1)), BinExpr(/, StringLit(hello), StringLit(world))))))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test50(self):
        input = """universe: function auto () {}"""
        expect = """Program([
	FuncDecl(universe, AutoType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test51(self):
        input = """axolot: function void (inherit out c: integer, b: auto) {}"""
        expect = """Program([
	FuncDecl(axolot, VoidType, [InheritOutParam(c, IntegerType), Param(b, AutoType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test52(self):
        input = """Company: function void (a: auto, c: auto, d: auto, a:auto) {}"""
        expect = """Program([
	FuncDecl(Company, VoidType, [Param(a, AutoType), Param(c, AutoType), Param(d, AutoType), Param(a, AutoType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test53(self):
        input = """foo: function integer () {
            {}
            {}        
        }"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([BlockStmt([]), BlockStmt([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test54(self):
        input = """foo: function void () {
            a[12,34]= "toi la hot boy";
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(12), IntegerLit(34)]), StringLit(toi la hot boy))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test55(self):
        input = """foo: function void () {
            if (i==true) i=i+1; else i=i+2;
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(i), BooleanLit(True)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test56(self):
        input = """foo: function void () {
            for (a=0, a<=10, a+1) {
                for (a=0, a<=10, a+1) {
                    for (a=0, a<=10, a+1) {
                    }
                }
            }
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(0)), BinExpr(<=, Id(a), IntegerLit(10)), BinExpr(+, Id(a), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(0)), BinExpr(<=, Id(a), IntegerLit(10)), BinExpr(+, Id(a), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(a), IntegerLit(0)), BinExpr(<=, Id(a), IntegerLit(10)), BinExpr(+, Id(a), IntegerLit(1)), BlockStmt([]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test57(self):
        input = """foo: function integer () {
            while (a-3>=12) 
                if (i==true) i=i+1; 
                else i=i+2;
        }"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([WhileStmt(BinExpr(>=, BinExpr(-, Id(a), IntegerLit(3)), IntegerLit(12)), IfStmt(BinExpr(==, Id(i), BooleanLit(True)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(2)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test58(self):
        input = """foo: function integer () {
            while (a-3>=12)
                for (a=0, a<=10, a+1)
                    if (i==true) i=i+1; else i=i+2;
        }"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([WhileStmt(BinExpr(>=, BinExpr(-, Id(a), IntegerLit(3)), IntegerLit(12)), ForStmt(AssignStmt(Id(a), IntegerLit(0)), BinExpr(<=, Id(a), IntegerLit(10)), BinExpr(+, Id(a), IntegerLit(1)), IfStmt(BinExpr(==, Id(i), BooleanLit(True)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(2))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test59(self):
        input = """foo: function integer () {
            while (a-3>=12)
                while (a-3>=12)
                    while (a-3>=12)
                        while (a-3>=12)
                            while (a-3>=12)
                                a=a+4;
        }"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([WhileStmt(BinExpr(>=, BinExpr(-, Id(a), IntegerLit(3)), IntegerLit(12)), WhileStmt(BinExpr(>=, BinExpr(-, Id(a), IntegerLit(3)), IntegerLit(12)), WhileStmt(BinExpr(>=, BinExpr(-, Id(a), IntegerLit(3)), IntegerLit(12)), WhileStmt(BinExpr(>=, BinExpr(-, Id(a), IntegerLit(3)), IntegerLit(12)), WhileStmt(BinExpr(>=, BinExpr(-, Id(a), IntegerLit(3)), IntegerLit(12)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(4))))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test60(self):
        input = """foo: function integer () {
            if (i==true) 
                if (i==5)
                    if (i>a)
                        if (i>=c)
                            if (i==e)i=i+1;
                
        }"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(i), BooleanLit(True)), IfStmt(BinExpr(==, Id(i), IntegerLit(5)), IfStmt(BinExpr(>, Id(i), Id(a)), IfStmt(BinExpr(>=, Id(i), Id(c)), IfStmt(BinExpr(==, Id(i), Id(e)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test61(self):
        input = """foo: function integer () {
            if (abac==true)
                if (i>abac) abac=abac+1;
                else abac=i;
            else abac=100;
        }"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(abac), BooleanLit(True)), IfStmt(BinExpr(>, Id(i), Id(abac)), AssignStmt(Id(abac), BinExpr(+, Id(abac), IntegerLit(1))), AssignStmt(Id(abac), Id(i))), AssignStmt(Id(abac), IntegerLit(100)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test62(self):
        input = """foo: function integer () {
            if (a<=a[i])
                if (a["hhaha",i]==a) a=a+2;
                else if (a[hellu]<=3) a[haha]=4; 
                    else cdef=345;
            else haha=ac;
        }"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([IfStmt(BinExpr(<=, Id(a), ArrayCell(a, [Id(i)])), IfStmt(BinExpr(==, ArrayCell(a, [StringLit(hhaha), Id(i)]), Id(a)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(2))), IfStmt(BinExpr(<=, ArrayCell(a, [Id(hellu)]), IntegerLit(3)), AssignStmt(ArrayCell(a, [Id(haha)]), IntegerLit(4)), AssignStmt(Id(cdef), IntegerLit(345)))), AssignStmt(Id(haha), Id(ac)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test63(self):
        input = """oo: function integer () {
            do {
                a: string = "My name is Chinh";
                b: float = "U are U"::"I am Me";
                i=i+1;
            }
            while (i<10);
        }"""
        expect = """Program([
	FuncDecl(oo, IntegerType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(i), IntegerLit(10)), BlockStmt([VarDecl(a, StringType, StringLit(My name is Chinh)), VarDecl(b, FloatType, BinExpr(::, StringLit(U are U), StringLit(I am Me))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test64(self):
        input = """foo: function integer () {
            do {
                do {  
                }
                while (a>=abc);
            }
            while (a<-2);
        }"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(a), UnExpr(-, IntegerLit(2))), BlockStmt([DoWhileStmt(BinExpr(>=, Id(a), Id(abc)), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test65(self):
        input = """// I hope it's true $#^@*!@#(I!)@(*)
        foo: function integer () {
            break;
            continue;
        }"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([BreakStmt(), ContinueStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def test66(self):
        input = """foo: function integer () {
            hello(a, 8, 0); 
        }"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([CallStmt(hello, Id(a), IntegerLit(8), IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test67(self):
        input = """integers: array [5] of integer = {1, 7, 3, 9, 5};
            largest_int: integer = find_largest(integers);"""
        expect = """Program([
	VarDecl(integers, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(7), IntegerLit(3), IntegerLit(9), IntegerLit(5)]))
	VarDecl(largest_int, IntegerType, FuncCall(find_largest, [Id(integers)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test68(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test69(self):
        input = """main: function void (inherit out a: auto) {}"""
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(a, AutoType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test70(self):
        input = """countvalue: function integer (a: array[5] of string, b:string) {
            count: string = 0;
            for (i=0, i<countlength(a), i+1) {
                if (a[i]==b) count=count+1;
            }
            return count;
        }"""
        expect = """Program([
	FuncDecl(countvalue, IntegerType, [Param(a, ArrayType([5], StringType)), Param(b, StringType)], None, BlockStmt([VarDecl(count, StringType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(countlength, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(a, [Id(i)]), Id(b)), AssignStmt(Id(count), BinExpr(+, Id(count), IntegerLit(1))))])), ReturnStmt(Id(count))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test71(self):
        input = """foo: function void (a: auto) {
            hello(a,b[100]);
            dosth(hello(abc,said()));   
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, AutoType)], None, BlockStmt([CallStmt(hello, Id(a), ArrayCell(b, [IntegerLit(100)])), CallStmt(dosth, FuncCall(hello, [Id(abc), FuncCall(said, [])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test72(self):
        input = """isPrime: function boolean (n: integer) {
    if (n < 2) {
        return false;
    }
    for (i = 2, i <= sqrt(n), i + 1) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

countPrimes: function integer (arr: array [10] of integer) {
    count = 0;
    for (i = 0, i < 10, i + 1) {
        if (isPrime(arr[i])) {
            count = count + 1;
        }
    }
    return count;
}"""
        expect = """Program([
	FuncDecl(isPrime, BooleanType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(n), IntegerLit(2)), BlockStmt([ReturnStmt(BooleanLit(False))])), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), FuncCall(sqrt, [Id(n)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))]))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(countPrimes, IntegerType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([AssignStmt(Id(count), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(FuncCall(isPrime, [ArrayCell(arr, [Id(i)])]), BlockStmt([AssignStmt(Id(count), BinExpr(+, Id(count), IntegerLit(1)))]))])), ReturnStmt(Id(count))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test73(self):
        input = """fibonacci: function integer (n: integer) {
    if (n == 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    } else {
        return fibonacci(n-1) + fibonacci(n-2);
    }
}"""
        expect = """Program([
	FuncDecl(fibonacci, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(IntegerLit(0))]), IfStmt(BinExpr(==, Id(n), IntegerLit(1)), BlockStmt([ReturnStmt(IntegerLit(1))]), BlockStmt([ReturnStmt(BinExpr(+, FuncCall(fibonacci, [BinExpr(-, Id(n), IntegerLit(1))]), FuncCall(fibonacci, [BinExpr(-, Id(n), IntegerLit(2))])))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test74(self):
        input = """sum2DArray: function integer (arr: array [10, 10] of integer) {
    sum = 0;
    for (i = 0, i < 10, i + 1) {
        for (j = 0, j < 10, j + 1) {
            sum = sum + arr[i, j];
        }
    }
    return sum;
}"""
        expect = """Program([
	FuncDecl(sum2DArray, IntegerType, [Param(arr, ArrayType([10, 10], IntegerType))], None, BlockStmt([AssignStmt(Id(sum), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(10)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(arr, [Id(i), Id(j)])))]))])), ReturnStmt(Id(sum))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test75(self):
        input = """findKthLargest: function integer (arr: array [10] of integer, k: integer) {
    reverseSort(arr);
    return arr[k-1];
}"""
        expect = """Program([
	FuncDecl(findKthLargest, IntegerType, [Param(arr, ArrayType([10], IntegerType)), Param(k, IntegerType)], None, BlockStmt([CallStmt(reverseSort, Id(arr)), ReturnStmt(ArrayCell(arr, [BinExpr(-, Id(k), IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test76(self):
        input = """isIncreasing: function boolean (arr: array [10] of integer) {
    for (i = 0, i < 9, i + 1) {
        if (arr[i] > arr[i + 1]) {
            return false;
        }
    }
    return true;
}"""
        expect = """Program([
	FuncDecl(isIncreasing, BooleanType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(9)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(arr, [Id(i)]), ArrayCell(arr, [BinExpr(+, Id(i), IntegerLit(1))])), BlockStmt([ReturnStmt(BooleanLit(False))]))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test77(self):
        input = """quickSort: function void (arr: array [10] of integer, left: integer, right: integer) {
    if (left < right) {
        pivot = arr[right];
        i = left - 1;
        for (j = left, j <= right - 1, j + 1) {
            if (arr[j] < pivot) {
                i = i + 1;
                swap(arr[i], arr[j]);
            }
        }
        swap(arr[i + 1], arr[right]);
        pivotIndex = i + 1;
        quickSort(arr, left, pivotIndex - 1);
        quickSort(arr, pivotIndex + 1, right);
    }
}"""
        expect = """Program([
	FuncDecl(quickSort, VoidType, [Param(arr, ArrayType([10], IntegerType)), Param(left, IntegerType), Param(right, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(left), Id(right)), BlockStmt([AssignStmt(Id(pivot), ArrayCell(arr, [Id(right)])), AssignStmt(Id(i), BinExpr(-, Id(left), IntegerLit(1))), ForStmt(AssignStmt(Id(j), Id(left)), BinExpr(<=, Id(j), BinExpr(-, Id(right), IntegerLit(1))), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(arr, [Id(j)]), Id(pivot)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), CallStmt(swap, ArrayCell(arr, [Id(i)]), ArrayCell(arr, [Id(j)]))]))])), CallStmt(swap, ArrayCell(arr, [BinExpr(+, Id(i), IntegerLit(1))]), ArrayCell(arr, [Id(right)])), AssignStmt(Id(pivotIndex), BinExpr(+, Id(i), IntegerLit(1))), CallStmt(quickSort, Id(arr), Id(left), BinExpr(-, Id(pivotIndex), IntegerLit(1))), CallStmt(quickSort, Id(arr), BinExpr(+, Id(pivotIndex), IntegerLit(1)), Id(right))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test78(self):
        input = """heapSort: function void (arr: array [10] of integer) {
    n = 10;
    for (i = n / 2 - 1, i >= 0, i - 1) {
        heapify(arr, n, i);
    }
    for (i = n - 1, i >= 0, i - 1) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}

heapify: function void (arr: array [10] of integer, n: integer, i: integer) {
    largest = i;
    l = 2 * i + 1;
    r = 2 * i + 2;
    if ((l < n) && (arr[l] > arr[largest])) {
        largest = l;
    }
    if ((r < n) && (arr[r] > arr[largest])) {
        largest = r;
    }
    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

findKthLargest: function integer (arr: array [10] of integer, k: integer) {
    heapSort(arr);
    return arr[k-1];
}"""
        expect = """Program([
	FuncDecl(heapSort, VoidType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([AssignStmt(Id(n), IntegerLit(10)), ForStmt(AssignStmt(Id(i), BinExpr(-, BinExpr(/, Id(n), IntegerLit(2)), IntegerLit(1))), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([CallStmt(heapify, Id(arr), Id(n), Id(i))])), ForStmt(AssignStmt(Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([CallStmt(swap, ArrayCell(arr, [IntegerLit(0)]), ArrayCell(arr, [Id(i)])), CallStmt(heapify, Id(arr), Id(i), IntegerLit(0))]))]))
	FuncDecl(heapify, VoidType, [Param(arr, ArrayType([10], IntegerType)), Param(n, IntegerType), Param(i, IntegerType)], None, BlockStmt([AssignStmt(Id(largest), Id(i)), AssignStmt(Id(l), BinExpr(+, BinExpr(*, IntegerLit(2), Id(i)), IntegerLit(1))), AssignStmt(Id(r), BinExpr(+, BinExpr(*, IntegerLit(2), Id(i)), IntegerLit(2))), IfStmt(BinExpr(&&, BinExpr(<, Id(l), Id(n)), BinExpr(>, ArrayCell(arr, [Id(l)]), ArrayCell(arr, [Id(largest)]))), BlockStmt([AssignStmt(Id(largest), Id(l))])), IfStmt(BinExpr(&&, BinExpr(<, Id(r), Id(n)), BinExpr(>, ArrayCell(arr, [Id(r)]), ArrayCell(arr, [Id(largest)]))), BlockStmt([AssignStmt(Id(largest), Id(r))])), IfStmt(BinExpr(!=, Id(largest), Id(i)), BlockStmt([CallStmt(swap, ArrayCell(arr, [Id(i)]), ArrayCell(arr, [Id(largest)])), CallStmt(heapify, Id(arr), Id(n), Id(largest))]))]))
	FuncDecl(findKthLargest, IntegerType, [Param(arr, ArrayType([10], IntegerType)), Param(k, IntegerType)], None, BlockStmt([CallStmt(heapSort, Id(arr)), ReturnStmt(ArrayCell(arr, [BinExpr(-, Id(k), IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test79(self):
        input = """sumArray: function integer (arr: array [10] of integer, n: integer) {
    if (n == 1) {
        return arr[0];
    } else {
        return arr[n-1] + sumArray(arr, n-1);
    }
}"""
        expect = """Program([
	FuncDecl(sumArray, IntegerType, [Param(arr, ArrayType([10], IntegerType)), Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(1)), BlockStmt([ReturnStmt(ArrayCell(arr, [IntegerLit(0)]))]), BlockStmt([ReturnStmt(BinExpr(+, ArrayCell(arr, [BinExpr(-, Id(n), IntegerLit(1))]), FuncCall(sumArray, [Id(arr), BinExpr(-, Id(n), IntegerLit(1))])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test80(self):
        input = """longestSubstring: function string (str: string) {
    n = length();
    longestSub = "";
    for (i = 0, i < n, i + 1) {
        for (j = i + 1, j <= n, j + 1) {
            subStr = substring(i, j);
            if (isPalindrome(subStr) && (length() > length())) {
                longestSub = subStr;
            }
        }
    }
    return longestSub;
}

isPalindrome: function boolean (str: string) {
    n = length();
    for (i = 0, i < n/2, i + 1) {
        if (str[i] != str[n-i-1]) {
            return false;
        }
    }
    return true;
}"""
        expect = """Program([
	FuncDecl(longestSubstring, StringType, [Param(str, StringType)], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [])), AssignStmt(Id(longestSub), StringLit()), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), BinExpr(+, Id(i), IntegerLit(1))), BinExpr(<=, Id(j), Id(n)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(Id(subStr), FuncCall(substring, [Id(i), Id(j)])), IfStmt(BinExpr(&&, FuncCall(isPalindrome, [Id(subStr)]), BinExpr(>, FuncCall(length, []), FuncCall(length, []))), BlockStmt([AssignStmt(Id(longestSub), Id(subStr))]))]))])), ReturnStmt(Id(longestSub))]))
	FuncDecl(isPalindrome, BooleanType, [Param(str, StringType)], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(/, Id(n), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(str, [Id(i)]), ArrayCell(str, [BinExpr(-, BinExpr(-, Id(n), Id(i)), IntegerLit(1))])), BlockStmt([ReturnStmt(BooleanLit(False))]))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test81(self):
        input = """evaluateMathExpression: function float (expression: string) {
    stack = createStack();
    operatorStack = createStack();
    for (i = 0, i < length(), i + 1) {
        if (expression[i] == digit) {
            numberStr = expression[i];
            while (((i + 1) < length()) && expression[i + 1] == digit) {
                i = i + 1;
                numberStr = numberStr + expression[i];
            }
            number = parseFloat(numberStr);
            push(number);
        } else if (expression[i] == operator) {
            while (!isEmpty() && hasHigherPrecedence(top(), expression[i])) {
                applyOperator(stack, pop());
            }
            push(expression[i]);
        }
    }
    while (!isEmpty()) {
        applyOperator(stack, pop());
    }
    return top();
}
"""
        expect = """Program([
	FuncDecl(evaluateMathExpression, FloatType, [Param(expression, StringType)], None, BlockStmt([AssignStmt(Id(stack), FuncCall(createStack, [])), AssignStmt(Id(operatorStack), FuncCall(createStack, [])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(expression, [Id(i)]), Id(digit)), BlockStmt([AssignStmt(Id(numberStr), ArrayCell(expression, [Id(i)])), WhileStmt(BinExpr(==, BinExpr(&&, BinExpr(<, BinExpr(+, Id(i), IntegerLit(1)), FuncCall(length, [])), ArrayCell(expression, [BinExpr(+, Id(i), IntegerLit(1))])), Id(digit)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), AssignStmt(Id(numberStr), BinExpr(+, Id(numberStr), ArrayCell(expression, [Id(i)])))])), AssignStmt(Id(number), FuncCall(parseFloat, [Id(numberStr)])), CallStmt(push, Id(number))]), IfStmt(BinExpr(==, ArrayCell(expression, [Id(i)]), Id(operator)), BlockStmt([WhileStmt(BinExpr(&&, UnExpr(!, FuncCall(isEmpty, [])), FuncCall(hasHigherPrecedence, [FuncCall(top, []), ArrayCell(expression, [Id(i)])])), BlockStmt([CallStmt(applyOperator, Id(stack), FuncCall(pop, []))])), CallStmt(push, ArrayCell(expression, [Id(i)]))])))])), WhileStmt(UnExpr(!, FuncCall(isEmpty, [])), BlockStmt([CallStmt(applyOperator, Id(stack), FuncCall(pop, []))])), ReturnStmt(FuncCall(top, []))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test82(self):
        input = """isValidMathExpression: function boolean (expression: string) {
    stack = createStack();
    for (i = 0, i < length(), i + 1) {
        if (expression[i] == digit) {
            numberStr = expression[i];
            while (((i + 1) < length()) && (expression[i + 1] == digit)) {
                i = i + 1;
                numberStr = numberStr + expression[i];
            }
            number = parseFloat(numberStr);
            push(number);
        }
    }
}"""
        expect = """Program([
	FuncDecl(isValidMathExpression, BooleanType, [Param(expression, StringType)], None, BlockStmt([AssignStmt(Id(stack), FuncCall(createStack, [])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(expression, [Id(i)]), Id(digit)), BlockStmt([AssignStmt(Id(numberStr), ArrayCell(expression, [Id(i)])), WhileStmt(BinExpr(&&, BinExpr(<, BinExpr(+, Id(i), IntegerLit(1)), FuncCall(length, [])), BinExpr(==, ArrayCell(expression, [BinExpr(+, Id(i), IntegerLit(1))]), Id(digit))), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), AssignStmt(Id(numberStr), BinExpr(+, Id(numberStr), ArrayCell(expression, [Id(i)])))])), AssignStmt(Id(number), FuncCall(parseFloat, [Id(numberStr)])), CallStmt(push, Id(number))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test83(self):
        input = """fibonacci: function integer (n: integer) {
    if (n <= 1) {
        return n;
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

main: function void () {
    n = 10;
    result = fibonacci(n);
    printInt(result);
}"""
        expect = """Program([
	FuncDecl(fibonacci, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, Id(n), IntegerLit(1)), BlockStmt([ReturnStmt(Id(n))]), BlockStmt([ReturnStmt(BinExpr(+, FuncCall(fibonacci, [BinExpr(-, Id(n), IntegerLit(1))]), FuncCall(fibonacci, [BinExpr(-, Id(n), IntegerLit(2))])))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), IntegerLit(10)), AssignStmt(Id(result), FuncCall(fibonacci, [Id(n)])), CallStmt(printInt, Id(result))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test84(self):
        input = """quadratic: function void (a: float, b: float, c: float) {
    delta = b * b - 4 * a * c;
    if (delta < 0) {
        print("The equation has no real roots.");
    } else if (delta == 0) {
        root = -b / (2 * a);
        print("The equation has one real root: ", root);
    } else {
        root1 = (-b + sqrt(delta)) / (2 * a);
        root2 = (-b - sqrt(delta)) / (2 * a);
        print("The equation has two real roots: ", root1, " and ", root2);
    }
}

main: function void () {
    a = 2;
    b = 5;
    c = -3;
    quadratic(a, b, c);
}"""
        expect = """Program([
	FuncDecl(quadratic, VoidType, [Param(a, FloatType), Param(b, FloatType), Param(c, FloatType)], None, BlockStmt([AssignStmt(Id(delta), BinExpr(-, BinExpr(*, Id(b), Id(b)), BinExpr(*, BinExpr(*, IntegerLit(4), Id(a)), Id(c)))), IfStmt(BinExpr(<, Id(delta), IntegerLit(0)), BlockStmt([CallStmt(print, StringLit(The equation has no real roots.))]), IfStmt(BinExpr(==, Id(delta), IntegerLit(0)), BlockStmt([AssignStmt(Id(root), BinExpr(/, UnExpr(-, Id(b)), BinExpr(*, IntegerLit(2), Id(a)))), CallStmt(print, StringLit(The equation has one real root: ), Id(root))]), BlockStmt([AssignStmt(Id(root1), BinExpr(/, BinExpr(+, UnExpr(-, Id(b)), FuncCall(sqrt, [Id(delta)])), BinExpr(*, IntegerLit(2), Id(a)))), AssignStmt(Id(root2), BinExpr(/, BinExpr(-, UnExpr(-, Id(b)), FuncCall(sqrt, [Id(delta)])), BinExpr(*, IntegerLit(2), Id(a)))), CallStmt(print, StringLit(The equation has two real roots: ), Id(root1), StringLit( and ), Id(root2))])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(2)), AssignStmt(Id(b), IntegerLit(5)), AssignStmt(Id(c), UnExpr(-, IntegerLit(3))), CallStmt(quadratic, Id(a), Id(b), Id(c))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test85(self):
        input = """linearSystem: function void (a11: float, a12: float, a21: float, a22: float, b1: float, b2: float) {
    determinant = a11 * a22 - a12 * a21;
    if (determinant == 0) {
        print("The system has no unique solution.");
    } else {
        x1 = (b1 * a22 - b2 * a12) / determinant;
        x2 = (a11 * b2 - a21 * b1) / determinant;
        print("The system has a unique solution: x1 = ", x1, ", x2 = ", x2);
    }
}

main: function void () {
    a11 = 2;
    a12 = 3;
    a21 = 4;
    a22 = 5;
    b1 = 1;
    b2 = 2;
    linearSystem(a11, a12, a21, a22, b1, b2);
}"""
        expect = """Program([
	FuncDecl(linearSystem, VoidType, [Param(a11, FloatType), Param(a12, FloatType), Param(a21, FloatType), Param(a22, FloatType), Param(b1, FloatType), Param(b2, FloatType)], None, BlockStmt([AssignStmt(Id(determinant), BinExpr(-, BinExpr(*, Id(a11), Id(a22)), BinExpr(*, Id(a12), Id(a21)))), IfStmt(BinExpr(==, Id(determinant), IntegerLit(0)), BlockStmt([CallStmt(print, StringLit(The system has no unique solution.))]), BlockStmt([AssignStmt(Id(x1), BinExpr(/, BinExpr(-, BinExpr(*, Id(b1), Id(a22)), BinExpr(*, Id(b2), Id(a12))), Id(determinant))), AssignStmt(Id(x2), BinExpr(/, BinExpr(-, BinExpr(*, Id(a11), Id(b2)), BinExpr(*, Id(a21), Id(b1))), Id(determinant))), CallStmt(print, StringLit(The system has a unique solution: x1 = ), Id(x1), StringLit(, x2 = ), Id(x2))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a11), IntegerLit(2)), AssignStmt(Id(a12), IntegerLit(3)), AssignStmt(Id(a21), IntegerLit(4)), AssignStmt(Id(a22), IntegerLit(5)), AssignStmt(Id(b1), IntegerLit(1)), AssignStmt(Id(b2), IntegerLit(2)), CallStmt(linearSystem, Id(a11), Id(a12), Id(a21), Id(a22), Id(b1), Id(b2))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test86(self):
        input = """diffEq2: function void (a: float, b: float, c: float) {
    delta = b * b - 4 * a * c;
    if (delta < 0) {
        print("The differential equation has no real solutions.");
    } else {
        if (delta == 0) {
            x0 = -b / (2 * a);
            y0 = f(x0);
            print("The differential equation has one real solution: y(x) = ", y0, " for x = ", x0);
        }
        else {
            x1 = (-b + sqrt(delta)) / (2 * a);
            x2 = (-b - sqrt(delta)) / (2 * a);
            y1 = f(x1);
            y2 = f(x2);
            print("The differential equation has two real solutions: y(x) = ", y1, " for x = ", x1, " and y(x) = ", y2, " for x = ", x2);
        }
    }
}
f: function float (x: float) {
        return exp(x) + exp(-x);
}
main: function void () {
    a = 1;
    b = 0;
    c = -1;
    diffEq2(a, b, c, f);
}"""
        expect = """Program([
	FuncDecl(diffEq2, VoidType, [Param(a, FloatType), Param(b, FloatType), Param(c, FloatType)], None, BlockStmt([AssignStmt(Id(delta), BinExpr(-, BinExpr(*, Id(b), Id(b)), BinExpr(*, BinExpr(*, IntegerLit(4), Id(a)), Id(c)))), IfStmt(BinExpr(<, Id(delta), IntegerLit(0)), BlockStmt([CallStmt(print, StringLit(The differential equation has no real solutions.))]), BlockStmt([IfStmt(BinExpr(==, Id(delta), IntegerLit(0)), BlockStmt([AssignStmt(Id(x0), BinExpr(/, UnExpr(-, Id(b)), BinExpr(*, IntegerLit(2), Id(a)))), AssignStmt(Id(y0), FuncCall(f, [Id(x0)])), CallStmt(print, StringLit(The differential equation has one real solution: y(x) = ), Id(y0), StringLit( for x = ), Id(x0))]), BlockStmt([AssignStmt(Id(x1), BinExpr(/, BinExpr(+, UnExpr(-, Id(b)), FuncCall(sqrt, [Id(delta)])), BinExpr(*, IntegerLit(2), Id(a)))), AssignStmt(Id(x2), BinExpr(/, BinExpr(-, UnExpr(-, Id(b)), FuncCall(sqrt, [Id(delta)])), BinExpr(*, IntegerLit(2), Id(a)))), AssignStmt(Id(y1), FuncCall(f, [Id(x1)])), AssignStmt(Id(y2), FuncCall(f, [Id(x2)])), CallStmt(print, StringLit(The differential equation has two real solutions: y(x) = ), Id(y1), StringLit( for x = ), Id(x1), StringLit( and y(x) = ), Id(y2), StringLit( for x = ), Id(x2))]))]))]))
	FuncDecl(f, FloatType, [Param(x, FloatType)], None, BlockStmt([ReturnStmt(BinExpr(+, FuncCall(exp, [Id(x)]), FuncCall(exp, [UnExpr(-, Id(x))])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(1)), AssignStmt(Id(b), IntegerLit(0)), AssignStmt(Id(c), UnExpr(-, IntegerLit(1))), CallStmt(diffEq2, Id(a), Id(b), Id(c), Id(f))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test87(self):
        input = """matrixInverse: function void (matrix: array [3,3] of float) {
    determinant = matrix[0,0] * (matrix[1,1] * matrix[2,2] - matrix[2,1] * matrix[1,2])
                - matrix[0,1] * (matrix[1,0] * matrix[2,2] - matrix[2,0] * matrix[1,2])
                + matrix[0,2] * (matrix[1,0] * matrix[2,1] - matrix[2,0] * matrix[1,1]);
    if (determinant == 0) {
        print("The matrix has no inverse.");
    } else {
        inverseMatrix : array [3,3] of float;
        inverseMatrix[0,0] = (matrix[1,1] * matrix[2,2] - matrix[2,1] * matrix[1,2]) / determinant;
        inverseMatrix[0,1] = (matrix[0,2] * matrix[2,1] - matrix[0,1] * matrix[2,2]) / determinant;
        inverseMatrix[0,2] = (matrix[0,1] * matrix[1,2] - matrix[0,2] * matrix[1,1]) / determinant;
        inverseMatrix[1,0] = (matrix[1,2] * matrix[2,0] - matrix[1,0] * matrix[2,2]) / determinant;
        inverseMatrix[1,1] = (matrix[0,0] * matrix[2,2] - matrix[0,2] * matrix[2,0]) / determinant;
        inverseMatrix[1,2] = (matrix[1,0] * matrix[0,2] - matrix[0,0] * matrix[1,2]) / determinant;
        inverseMatrix[2,0] = (matrix[1,0] * matrix[2,1] - matrix[2,0] * matrix[1,1]) / determinant;
        inverseMatrix[2,1] = (matrix[2,0] * matrix[0,1] - matrix[0,0] * matrix[2,1]) / determinant;
        inverseMatrix[2,2] = (matrix[0,0] * matrix[1,1] - matrix[1,0] * matrix[0,1]) / determinant;
        print("The inverse matrix is:");
        for (i = 0, i < 3, i + 1) {
            for (j = 0, j < 3, j + 1) {
                printFloat(inverseMatrix[i,j]);
            }
        }
    }
}

main: function void () {
    matrix = {{3.0, 1.0, 2.0}, {4.0, 0.0, 2.0}, {1.0, 5.0, 6.0}};
    matrixInverse(matrix);
}"""
        expect = """Program([
	FuncDecl(matrixInverse, VoidType, [Param(matrix, ArrayType([3, 3], FloatType))], None, BlockStmt([AssignStmt(Id(determinant), BinExpr(+, BinExpr(-, BinExpr(*, ArrayCell(matrix, [IntegerLit(0), IntegerLit(0)]), BinExpr(-, BinExpr(*, ArrayCell(matrix, [IntegerLit(1), IntegerLit(1)]), ArrayCell(matrix, [IntegerLit(2), IntegerLit(2)])), BinExpr(*, ArrayCell(matrix, [IntegerLit(2), IntegerLit(1)]), ArrayCell(matrix, [IntegerLit(1), IntegerLit(2)])))), BinExpr(*, ArrayCell(matrix, [IntegerLit(0), IntegerLit(1)]), BinExpr(-, BinExpr(*, ArrayCell(matrix, [IntegerLit(1), IntegerLit(0)]), ArrayCell(matrix, [IntegerLit(2), IntegerLit(2)])), BinExpr(*, ArrayCell(matrix, [IntegerLit(2), IntegerLit(0)]), ArrayCell(matrix, [IntegerLit(1), IntegerLit(2)]))))), BinExpr(*, ArrayCell(matrix, [IntegerLit(0), IntegerLit(2)]), BinExpr(-, BinExpr(*, ArrayCell(matrix, [IntegerLit(1), IntegerLit(0)]), ArrayCell(matrix, [IntegerLit(2), IntegerLit(1)])), BinExpr(*, ArrayCell(matrix, [IntegerLit(2), IntegerLit(0)]), ArrayCell(matrix, [IntegerLit(1), IntegerLit(1)])))))), IfStmt(BinExpr(==, Id(determinant), IntegerLit(0)), BlockStmt([CallStmt(print, StringLit(The matrix has no inverse.))]), BlockStmt([VarDecl(inverseMatrix, ArrayType([3, 3], FloatType)), AssignStmt(ArrayCell(inverseMatrix, [IntegerLit(0), IntegerLit(0)]), BinExpr(/, BinExpr(-, BinExpr(*, ArrayCell(matrix, [IntegerLit(1), IntegerLit(1)]), ArrayCell(matrix, [IntegerLit(2), IntegerLit(2)])), BinExpr(*, ArrayCell(matrix, [IntegerLit(2), IntegerLit(1)]), ArrayCell(matrix, [IntegerLit(1), IntegerLit(2)]))), Id(determinant))), AssignStmt(ArrayCell(inverseMatrix, [IntegerLit(0), IntegerLit(1)]), BinExpr(/, BinExpr(-, BinExpr(*, ArrayCell(matrix, [IntegerLit(0), IntegerLit(2)]), ArrayCell(matrix, [IntegerLit(2), IntegerLit(1)])), BinExpr(*, ArrayCell(matrix, [IntegerLit(0), IntegerLit(1)]), ArrayCell(matrix, [IntegerLit(2), IntegerLit(2)]))), Id(determinant))), AssignStmt(ArrayCell(inverseMatrix, [IntegerLit(0), IntegerLit(2)]), BinExpr(/, BinExpr(-, BinExpr(*, ArrayCell(matrix, [IntegerLit(0), IntegerLit(1)]), ArrayCell(matrix, [IntegerLit(1), IntegerLit(2)])), BinExpr(*, ArrayCell(matrix, [IntegerLit(0), IntegerLit(2)]), ArrayCell(matrix, [IntegerLit(1), IntegerLit(1)]))), Id(determinant))), AssignStmt(ArrayCell(inverseMatrix, [IntegerLit(1), IntegerLit(0)]), BinExpr(/, BinExpr(-, BinExpr(*, ArrayCell(matrix, [IntegerLit(1), IntegerLit(2)]), ArrayCell(matrix, [IntegerLit(2), IntegerLit(0)])), BinExpr(*, ArrayCell(matrix, [IntegerLit(1), IntegerLit(0)]), ArrayCell(matrix, [IntegerLit(2), IntegerLit(2)]))), Id(determinant))), AssignStmt(ArrayCell(inverseMatrix, [IntegerLit(1), IntegerLit(1)]), BinExpr(/, BinExpr(-, BinExpr(*, ArrayCell(matrix, [IntegerLit(0), IntegerLit(0)]), ArrayCell(matrix, [IntegerLit(2), IntegerLit(2)])), BinExpr(*, ArrayCell(matrix, [IntegerLit(0), IntegerLit(2)]), ArrayCell(matrix, [IntegerLit(2), IntegerLit(0)]))), Id(determinant))), AssignStmt(ArrayCell(inverseMatrix, [IntegerLit(1), IntegerLit(2)]), BinExpr(/, BinExpr(-, BinExpr(*, ArrayCell(matrix, [IntegerLit(1), IntegerLit(0)]), ArrayCell(matrix, [IntegerLit(0), IntegerLit(2)])), BinExpr(*, ArrayCell(matrix, [IntegerLit(0), IntegerLit(0)]), ArrayCell(matrix, [IntegerLit(1), IntegerLit(2)]))), Id(determinant))), AssignStmt(ArrayCell(inverseMatrix, [IntegerLit(2), IntegerLit(0)]), BinExpr(/, BinExpr(-, BinExpr(*, ArrayCell(matrix, [IntegerLit(1), IntegerLit(0)]), ArrayCell(matrix, [IntegerLit(2), IntegerLit(1)])), BinExpr(*, ArrayCell(matrix, [IntegerLit(2), IntegerLit(0)]), ArrayCell(matrix, [IntegerLit(1), IntegerLit(1)]))), Id(determinant))), AssignStmt(ArrayCell(inverseMatrix, [IntegerLit(2), IntegerLit(1)]), BinExpr(/, BinExpr(-, BinExpr(*, ArrayCell(matrix, [IntegerLit(2), IntegerLit(0)]), ArrayCell(matrix, [IntegerLit(0), IntegerLit(1)])), BinExpr(*, ArrayCell(matrix, [IntegerLit(0), IntegerLit(0)]), ArrayCell(matrix, [IntegerLit(2), IntegerLit(1)]))), Id(determinant))), AssignStmt(ArrayCell(inverseMatrix, [IntegerLit(2), IntegerLit(2)]), BinExpr(/, BinExpr(-, BinExpr(*, ArrayCell(matrix, [IntegerLit(0), IntegerLit(0)]), ArrayCell(matrix, [IntegerLit(1), IntegerLit(1)])), BinExpr(*, ArrayCell(matrix, [IntegerLit(1), IntegerLit(0)]), ArrayCell(matrix, [IntegerLit(0), IntegerLit(1)]))), Id(determinant))), CallStmt(print, StringLit(The inverse matrix is:)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(3)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(printFloat, ArrayCell(inverseMatrix, [Id(i), Id(j)]))]))]))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(matrix), ArrayLit([ArrayLit([FloatLit(3.0), FloatLit(1.0), FloatLit(2.0)]), ArrayLit([FloatLit(4.0), FloatLit(0.0), FloatLit(2.0)]), ArrayLit([FloatLit(1.0), FloatLit(5.0), FloatLit(6.0)])])), CallStmt(matrixInverse, Id(matrix))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test88(self):
        input = """computeAverage: function void(arr: array[10] of integer) {
    n = 10;
    sum = 0;
    for (i = 0, i < n, i + 1) {
        sum = sum + arr[i];
    }
    avg = sum / n;
    print("Average is: ", avg);
}

// Main function
main: function void() {
    arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    computeAverage(arr);
}"""
        expect = """Program([
	FuncDecl(computeAverage, VoidType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([AssignStmt(Id(n), IntegerLit(10)), AssignStmt(Id(sum), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(arr, [Id(i)])))])), AssignStmt(Id(avg), BinExpr(/, Id(sum), Id(n))), CallStmt(print, StringLit(Average is: ), Id(avg))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(arr), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7), IntegerLit(8), IntegerLit(9), IntegerLit(10)])), CallStmt(computeAverage, Id(arr))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test89(self):
        input = """
fibonacci: function integer(n: integer) {
    if (n <= 1) {
        return n;
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

// Main function
main: function void() {

    print("Enter n: ");
    n = readInt();

    print("Fibonacci number at position ", n, " is: ", fibonacci(n));
}"""
        expect = """Program([
	FuncDecl(fibonacci, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, Id(n), IntegerLit(1)), BlockStmt([ReturnStmt(Id(n))]), BlockStmt([ReturnStmt(BinExpr(+, FuncCall(fibonacci, [BinExpr(-, Id(n), IntegerLit(1))]), FuncCall(fibonacci, [BinExpr(-, Id(n), IntegerLit(2))])))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(print, StringLit(Enter n: )), AssignStmt(Id(n), FuncCall(readInt, [])), CallStmt(print, StringLit(Fibonacci number at position ), Id(n), StringLit( is: ), FuncCall(fibonacci, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test90(self):
        input = """
coinChange: function void(coins: array[4] of integer, n: integer) {
    dp: array[100] of integer;
    for (i = 1, i <= n, i + 1) {
        dp[i] = INF;
    }
    
    for (i = 1, i <= n, i + 1) {
        for (j = 0, j < 4, j + 1) {
            if ((coins[j] <= i) && ((dp[i - coins[j]] + 1) < dp[i])) {
                dp[i] = dp[i - coins[j]] + 1;
            }
        }
    }
    
    print("Minimum number of coins required to make change for ", n, " is: ", dp[n]);
}

main: function void() {
    coins = {1, 3, 5, 7};
    n = 12;

    coinChange(coins, n);
}"""
        expect = """Program([
	FuncDecl(coinChange, VoidType, [Param(coins, ArrayType([4], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(dp, ArrayType([100], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(dp, [Id(i)]), Id(INF))])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(4)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(&&, BinExpr(<=, ArrayCell(coins, [Id(j)]), Id(i)), BinExpr(<, BinExpr(+, ArrayCell(dp, [BinExpr(-, Id(i), ArrayCell(coins, [Id(j)]))]), IntegerLit(1)), ArrayCell(dp, [Id(i)]))), BlockStmt([AssignStmt(ArrayCell(dp, [Id(i)]), BinExpr(+, ArrayCell(dp, [BinExpr(-, Id(i), ArrayCell(coins, [Id(j)]))]), IntegerLit(1)))]))]))])), CallStmt(print, StringLit(Minimum number of coins required to make change for ), Id(n), StringLit( is: ), ArrayCell(dp, [Id(n)]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(coins), ArrayLit([IntegerLit(1), IntegerLit(3), IntegerLit(5), IntegerLit(7)])), AssignStmt(Id(n), IntegerLit(12)), CallStmt(coinChange, Id(coins), Id(n))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test91(self):
        input = """fibonacciSum: function integer(n: integer) {
    if (n <= 0) {
        return 0;
    } 
    else {
        if (n == 1) {
            return 1;
        }
        else {
            prev1 = 0;
            prev2 = 1;
            sum = 1;
            for (i = 2, i <= n, i+1) {
                current = prev1 + prev2;
                sum = sum + current;
                prev1 = prev2;
                prev2 = current;
            }
            return sum;
        }
    }
}

main: function void() {
    n = 10;
    result = fibonacciSum(n);
    print("The sum of the first " + n + " Fibonacci numbers is " + result);
}"""
        expect = """Program([
	FuncDecl(fibonacciSum, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(IntegerLit(0))]), BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(1)), BlockStmt([ReturnStmt(IntegerLit(1))]), BlockStmt([AssignStmt(Id(prev1), IntegerLit(0)), AssignStmt(Id(prev2), IntegerLit(1)), AssignStmt(Id(sum), IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(current), BinExpr(+, Id(prev1), Id(prev2))), AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(current))), AssignStmt(Id(prev1), Id(prev2)), AssignStmt(Id(prev2), Id(current))])), ReturnStmt(Id(sum))]))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), IntegerLit(10)), AssignStmt(Id(result), FuncCall(fibonacciSum, [Id(n)])), CallStmt(print, BinExpr(+, BinExpr(+, BinExpr(+, StringLit(The sum of the first ), Id(n)), StringLit( Fibonacci numbers is )), Id(result)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test92(self):
        input = """insertionSort: function void(arr: array[10] of integer) {
    for (i = 1, i < 10, i+1) {
        key = arr[i];
        j = i - 1;
        while ((j >= 0) && (arr[j] > key)) {
            arr[j+1] = arr[j];
            j = j - 1;
        }
        arr[j+1] = key;
    }
}

printArray: function void(arr: array[10] of integer) {
    for (i = 0, i < 10, i+1) {
        printInt(arr[i]);
        print(" ");
    }
    print("\\n");
}

main: function void() {
    arr = {5, 2, 8, 4, 9, 1, 3, 7, 6, 0};
    print("Original array: ");
    printArray(arr);
    insertionSort(arr);
    print("Sorted array: ");
    printArray(arr);
}"""
        expect = """Program([
	FuncDecl(insertionSort, VoidType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(key), ArrayCell(arr, [Id(i)])), AssignStmt(Id(j), BinExpr(-, Id(i), IntegerLit(1))), WhileStmt(BinExpr(&&, BinExpr(>=, Id(j), IntegerLit(0)), BinExpr(>, ArrayCell(arr, [Id(j)]), Id(key))), BlockStmt([AssignStmt(ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))]), ArrayCell(arr, [Id(j)])), AssignStmt(Id(j), BinExpr(-, Id(j), IntegerLit(1)))])), AssignStmt(ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))]), Id(key))]))]))
	FuncDecl(printArray, VoidType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInt, ArrayCell(arr, [Id(i)])), CallStmt(print, StringLit( ))])), CallStmt(print, StringLit(\\n))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(arr), ArrayLit([IntegerLit(5), IntegerLit(2), IntegerLit(8), IntegerLit(4), IntegerLit(9), IntegerLit(1), IntegerLit(3), IntegerLit(7), IntegerLit(6), IntegerLit(0)])), CallStmt(print, StringLit(Original array: )), CallStmt(printArray, Id(arr)), CallStmt(insertionSort, Id(arr)), CallStmt(print, StringLit(Sorted array: )), CallStmt(printArray, Id(arr))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test93(self):
        input = """combination: function integer (n: integer, k: integer) {
    if ((k == 0) || (k == n)) {
        return 1;
    } else {
        return combination(n - 1, k - 1) + combination(n - 1, k);
    }
}

main: function void () {
    n = 5;
    k = 3;
    result = combination(n, k);
    printInt(result);
}"""
        expect = """Program([
	FuncDecl(combination, IntegerType, [Param(n, IntegerType), Param(k, IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(==, Id(k), IntegerLit(0)), BinExpr(==, Id(k), Id(n))), BlockStmt([ReturnStmt(IntegerLit(1))]), BlockStmt([ReturnStmt(BinExpr(+, FuncCall(combination, [BinExpr(-, Id(n), IntegerLit(1)), BinExpr(-, Id(k), IntegerLit(1))]), FuncCall(combination, [BinExpr(-, Id(n), IntegerLit(1)), Id(k)])))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), IntegerLit(5)), AssignStmt(Id(k), IntegerLit(3)), AssignStmt(Id(result), FuncCall(combination, [Id(n), Id(k)])), CallStmt(printInt, Id(result))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test94(self):
        input = """solveQuadratic: function void (a: float, b: float, c: float) {
    delta = b * b - 4 * a * c;
    if (delta < 0) {
        printString("No real roots");
    } else {
        if (delta == 0) {
            x = -b / (2 * a);
            printString("One real root: ");
            printFloat(x);
        }
        else {
            x1 = (-b + sqrt(delta)) / (2 * a);
            x2 = (-b - sqrt(delta)) / (2 * a);
            printString("Two real roots: ");
            printFloat(x1);
            printString(", ");
            printFloat(x2);
        }
    }
}

main: function void () {
    a = 2;
    b = -3;
    c = -4;
    solveQuadratic(a, b, c);
}"""
        expect = """Program([
	FuncDecl(solveQuadratic, VoidType, [Param(a, FloatType), Param(b, FloatType), Param(c, FloatType)], None, BlockStmt([AssignStmt(Id(delta), BinExpr(-, BinExpr(*, Id(b), Id(b)), BinExpr(*, BinExpr(*, IntegerLit(4), Id(a)), Id(c)))), IfStmt(BinExpr(<, Id(delta), IntegerLit(0)), BlockStmt([CallStmt(printString, StringLit(No real roots))]), BlockStmt([IfStmt(BinExpr(==, Id(delta), IntegerLit(0)), BlockStmt([AssignStmt(Id(x), BinExpr(/, UnExpr(-, Id(b)), BinExpr(*, IntegerLit(2), Id(a)))), CallStmt(printString, StringLit(One real root: )), CallStmt(printFloat, Id(x))]), BlockStmt([AssignStmt(Id(x1), BinExpr(/, BinExpr(+, UnExpr(-, Id(b)), FuncCall(sqrt, [Id(delta)])), BinExpr(*, IntegerLit(2), Id(a)))), AssignStmt(Id(x2), BinExpr(/, BinExpr(-, UnExpr(-, Id(b)), FuncCall(sqrt, [Id(delta)])), BinExpr(*, IntegerLit(2), Id(a)))), CallStmt(printString, StringLit(Two real roots: )), CallStmt(printFloat, Id(x1)), CallStmt(printString, StringLit(, )), CallStmt(printFloat, Id(x2))]))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(2)), AssignStmt(Id(b), UnExpr(-, IntegerLit(3))), AssignStmt(Id(c), UnExpr(-, IntegerLit(4))), CallStmt(solveQuadratic, Id(a), Id(b), Id(c))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test95(self):
        input = """binarySearch: function integer (arr: array [10] of integer, target: integer) {
    left = 0;
    right = 9;
    while (left <= right) {
        mid = (left + right) / 2;
        if (arr[mid] == target) {
            return mid;
        } else {
            if (arr[mid] < target) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }
    }
    return -1;
}"""
        expect = """Program([
	FuncDecl(binarySearch, IntegerType, [Param(arr, ArrayType([10], IntegerType)), Param(target, IntegerType)], None, BlockStmt([AssignStmt(Id(left), IntegerLit(0)), AssignStmt(Id(right), IntegerLit(9)), WhileStmt(BinExpr(<=, Id(left), Id(right)), BlockStmt([AssignStmt(Id(mid), BinExpr(/, BinExpr(+, Id(left), Id(right)), IntegerLit(2))), IfStmt(BinExpr(==, ArrayCell(arr, [Id(mid)]), Id(target)), BlockStmt([ReturnStmt(Id(mid))]), BlockStmt([IfStmt(BinExpr(<, ArrayCell(arr, [Id(mid)]), Id(target)), BlockStmt([AssignStmt(Id(left), BinExpr(+, Id(mid), IntegerLit(1)))]), BlockStmt([AssignStmt(Id(right), BinExpr(-, Id(mid), IntegerLit(1)))]))]))])), ReturnStmt(UnExpr(-, IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test96(self):
        input = """complex: array[1,2,3] of integer = CountPP[1,a[2,b[3,c[4],d[5]]]];"""
        expect = """Program([
	VarDecl(complex, ArrayType([1, 2, 3], IntegerType), ArrayCell(CountPP, [IntegerLit(1), ArrayCell(a, [IntegerLit(2), ArrayCell(b, [IntegerLit(3), ArrayCell(c, [IntegerLit(4)]), ArrayCell(d, [IntegerLit(5)])])])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test97(self):
        input = """a, b, c, d, e: integer = a[1], b[2,3,4], c[5], d[12], e[18,22,"haha"];"""
        expect = """Program([
	VarDecl(a, IntegerType, ArrayCell(a, [IntegerLit(1)]))
	VarDecl(b, IntegerType, ArrayCell(b, [IntegerLit(2), IntegerLit(3), IntegerLit(4)]))
	VarDecl(c, IntegerType, ArrayCell(c, [IntegerLit(5)]))
	VarDecl(d, IntegerType, ArrayCell(d, [IntegerLit(12)]))
	VarDecl(e, IntegerType, ArrayCell(e, [IntegerLit(18), IntegerLit(22), StringLit(haha)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test98(self):
        input = """matrix: array [4, 4] of integer = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
        diag_sum: integer = 0;
        main: function void(){
            for (i = 0, i < 4, i + 1) {
                diag_sum = diag_sum + matrix[i, i];
            }
            printf("The sum of the elements on the main diagonal is %d.\\n", diag_sum);
        }"""
        expect = """Program([
	VarDecl(matrix, ArrayType([4, 4], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]), ArrayLit([IntegerLit(5), IntegerLit(6), IntegerLit(7), IntegerLit(8)]), ArrayLit([IntegerLit(9), IntegerLit(10), IntegerLit(11), IntegerLit(12)]), ArrayLit([IntegerLit(13), IntegerLit(14), IntegerLit(15), IntegerLit(16)])]))
	VarDecl(diag_sum, IntegerType, IntegerLit(0))
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(diag_sum), BinExpr(+, Id(diag_sum), ArrayCell(matrix, [Id(i), Id(i)])))])), CallStmt(printf, StringLit(The sum of the elements on the main diagonal is %d.\\n), Id(diag_sum))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def test99(self):
        input = """main: function void() {
            // Declare and initialize variables.
            float_: array [10] of integer;
            fib_nums: array [10] of integer;
            for (i = 0, i < 10, i + 1) {
                fib_nums[i] = fibonacci(i);
            }

            matrix: array [3, 3] of integer;

            // Find the largest Fibonacci number.
            largest_fib: integer = find_largest(fib_nums);

            // Find the row with the largest sum in the matrix.
            largest_sum: integer = 0;
            largest_sum_row: integer = -1;

            // Output the results.
            printf("The largest Fibonacci number is %d.\\n", largest_fib);
            printf("The row with the largest sum in the matrix is row %d, with a sum of %d.\\n", largest_sum_row, largest_sum);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(float_, ArrayType([10], IntegerType)), VarDecl(fib_nums, ArrayType([10], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(fib_nums, [Id(i)]), FuncCall(fibonacci, [Id(i)]))])), VarDecl(matrix, ArrayType([3, 3], IntegerType)), VarDecl(largest_fib, IntegerType, FuncCall(find_largest, [Id(fib_nums)])), VarDecl(largest_sum, IntegerType, IntegerLit(0)), VarDecl(largest_sum_row, IntegerType, UnExpr(-, IntegerLit(1))), CallStmt(printf, StringLit(The largest Fibonacci number is %d.\\n), Id(largest_fib)), CallStmt(printf, StringLit(The row with the largest sum in the matrix is row %d, with a sum of %d.\\n), Id(largest_sum_row), Id(largest_sum))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))

    def test100(self):
        input = """foo: function integer (a: integer) {
            ab[3]={"hello", "see you later"};
            a: integer = {abce, 123} - {"haha"};
        }
        """
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(a, IntegerType)], None, BlockStmt([AssignStmt(ArrayCell(ab, [IntegerLit(3)]), ArrayLit([StringLit(hello), StringLit(see you later)])), VarDecl(a, IntegerType, BinExpr(-, ArrayLit([Id(abce), IntegerLit(123)]), ArrayLit([StringLit(haha)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))
