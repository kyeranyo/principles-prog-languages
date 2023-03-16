import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_ast_1(self):
        input_str = """delta: integer = fact(3);"""
        expect = """Program([
	VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 300))

    def test_ast_2(self):
        input_str = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 301))

    def test_ast_3(self):
        input_str = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input_str, expect, 302))

    def test_ast_4(self):
        """Simple program"""
        input_str = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 303))

    def test_ast_5(self):
        """More complex program"""
        input_str = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 304))

    def test_ast_6(self):
        """More complex program"""
        input_str = """x: integer = 65;
         inc: function void(out n: integer, delta: integer) {
             n = n + delta;
         }
         main: function void() {
             a, b: integer = 1, 2;
             inc(x, delta);
             printInteger(x);
         }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(2)), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 305))

    def test_ast_7(self):
        input_str = """a, b, c: integer = 3, 4, 6;"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(3))
	VarDecl(b, IntegerType, IntegerLit(4))
	VarDecl(c, IntegerType, IntegerLit(6))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 306))

    def test_ast_8(self):
        input_str = """a, b, c: integer = 3, 4, 6;
        d, e, f: float;"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(3))
	VarDecl(b, IntegerType, IntegerLit(4))
	VarDecl(c, IntegerType, IntegerLit(6))
	VarDecl(d, FloatType)
	VarDecl(e, FloatType)
	VarDecl(f, FloatType)
])"""
        self.assertTrue(TestAST.test(input_str, expect, 307))

    def test_ast_9(self):
        input_str = """
        a : integer = 3;
        program: function void () {
            a, b, c: integer;
            d, e, f: float;
            g: boolean;
        }"""
        expect_str = """Program([
	VarDecl(a, IntegerType, IntegerLit(3))
	FuncDecl(program, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), VarDecl(b, IntegerType), VarDecl(c, IntegerType), VarDecl(d, FloatType), VarDecl(e, FloatType), VarDecl(f, FloatType), VarDecl(g, BooleanType)]))
])"""
        self.assertTrue(TestAST.test(input_str, expect_str, 308))

    def test_ast_10(self):
        input_str = """
        program: function void (arr: array [10,12] of integer, left: integer, right: integer) {
            if (left < right) {
                mid = (left + right)/2;
                sort(arr, left, mid);
                sort(arr, mid + 1, right);
                merge(arr, left, mid, right);
            }
        }
        merge: function void (arr: array [10] of integer, left: integer, mid: integer, right: integer) {
            n1 = mid - left + 1;
            n2 = right - mid;
            left_arr : array [10] of integer;
            right_arr : array [10] of integer;
            for (i = 0, i < n1, i + 1) {
                left_arr[i] = arr[left + i];
            }
            for (j = 0, j < n2, j + 1) {
                right_arr[j] = arr[mid + 1 + j];
            }

            i = 0;
            j = 0;
            k = left;

            while ((i < n1) && (j < n2)) {
                if (left_arr[i] <= right_arr[j]) {
                    arr[k] = left_arr[i];
                    i = i + 1;
                }
                else {
                    arr[k] = right_arr[j];
                    j = j + 1;
                }
                k = k + 1;
            }

            while (i < n1) {
                arr[k] = left_arr[i];
                i = i + 1;
                k = k + 1;
            }

            while (j < n2) {
                arr[k] = right_arr[j];
                j = j + 1;
                k = k + 1;
            }
        }
        """
        expect = """Program([
	FuncDecl(program, VoidType, [Param(arr, ArrayType([10, 12], IntegerType)), Param(left, IntegerType), Param(right, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(left), Id(right)), BlockStmt([AssignStmt(Id(mid), BinExpr(/, BinExpr(+, Id(left), Id(right)), IntegerLit(2))), CallStmt(sort, Id(arr), Id(left), Id(mid)), CallStmt(sort, Id(arr), BinExpr(+, Id(mid), IntegerLit(1)), Id(right)), CallStmt(merge, Id(arr), Id(left), Id(mid), Id(right))]))]))
	FuncDecl(merge, VoidType, [Param(arr, ArrayType([10], IntegerType)), Param(left, IntegerType), Param(mid, IntegerType), Param(right, IntegerType)], None, BlockStmt([AssignStmt(Id(n1), BinExpr(+, BinExpr(-, Id(mid), Id(left)), IntegerLit(1))), AssignStmt(Id(n2), BinExpr(-, Id(right), Id(mid))), VarDecl(left_arr, ArrayType([10], IntegerType)), VarDecl(right_arr, ArrayType([10], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n1)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(left_arr, [Id(i)]), ArrayCell(arr, [BinExpr(+, Id(left), Id(i))]))])), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(n2)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(right_arr, [Id(j)]), ArrayCell(arr, [BinExpr(+, BinExpr(+, Id(mid), IntegerLit(1)), Id(j))]))])), AssignStmt(Id(i), IntegerLit(0)), AssignStmt(Id(j), IntegerLit(0)), AssignStmt(Id(k), Id(left)), WhileStmt(BinExpr(&&, BinExpr(<, Id(i), Id(n1)), BinExpr(<, Id(j), Id(n2))), BlockStmt([IfStmt(BinExpr(<=, ArrayCell(left_arr, [Id(i)]), ArrayCell(right_arr, [Id(j)])), BlockStmt([AssignStmt(ArrayCell(arr, [Id(k)]), ArrayCell(left_arr, [Id(i)])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]), BlockStmt([AssignStmt(ArrayCell(arr, [Id(k)]), ArrayCell(right_arr, [Id(j)])), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))])), AssignStmt(Id(k), BinExpr(+, Id(k), IntegerLit(1)))])), WhileStmt(BinExpr(<, Id(i), Id(n1)), BlockStmt([AssignStmt(ArrayCell(arr, [Id(k)]), ArrayCell(left_arr, [Id(i)])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), AssignStmt(Id(k), BinExpr(+, Id(k), IntegerLit(1)))])), WhileStmt(BinExpr(<, Id(j), Id(n2)), BlockStmt([AssignStmt(ArrayCell(arr, [Id(k)]), ArrayCell(right_arr, [Id(j)])), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1))), AssignStmt(Id(k), BinExpr(+, Id(k), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 309))

    def test_ast_11(self):
        input_str = """
            program: function void (arr: array [10] of integer) {
            n = 10;
            for (i = 0, i < n - 1, i + 1) {
                for (j = 0, j < n - i - 1, j + 1) {
                    if (arr[j] > arr[j + 1]) {
                        temp = arr[j];
                        arr[j] = arr[j + 1];
                        arr[j + 1] = temp;
                    }
                }
            }
        }"""
        expect = """Program([
	FuncDecl(program, VoidType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([AssignStmt(Id(n), IntegerLit(10)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), BinExpr(-, BinExpr(-, Id(n), Id(i)), IntegerLit(1))), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(arr, [Id(j)]), ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))])), BlockStmt([AssignStmt(Id(temp), ArrayCell(arr, [Id(j)])), AssignStmt(ArrayCell(arr, [Id(j)]), ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))])), AssignStmt(ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))]), Id(temp))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 310))

    def test_ast_12(self):
        input_str = """program: function void() {
            a = ("a" :: "b") :: "c";
        }"""
        expect = """Program([
	FuncDecl(program, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(::, BinExpr(::, StringLit(a), StringLit(b)), StringLit(c)))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 311))

    def test_ast_13(self):
        """Testing for inheritance"""
        input_str = """
            multiply: function integer (x: integer, y: integer) {
                return x * y;
            }
            square: function integer (inherit out x: integer) {
                return x * x;
            }
            main: function void () inherit multiply {
                a = super(1212+2,31);
                b = square(a);
            }
        """
        expect = """Program([
	FuncDecl(multiply, IntegerType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(*, Id(x), Id(y)))]))
	FuncDecl(square, IntegerType, [InheritOutParam(x, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(*, Id(x), Id(x)))]))
	FuncDecl(main, VoidType, [], multiply, BlockStmt([AssignStmt(Id(a), FuncCall(super, [BinExpr(+, IntegerLit(1212), IntegerLit(2)), IntegerLit(31)])), AssignStmt(Id(b), FuncCall(square, [Id(a)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 312))

    def test_ast_14(self):
        input_str = """
        program: function void (arr: array [10] of integer) {
            n = 10;
            swapped = true;
            while (swapped) {
                swapped = false;
                for (i = 0, i < n - 1, i + 1) {
                    if (arr[i] > arr[i + 1]) {
                        temp = arr[i];
                        arr[i] = arr[i + 1];
                        arr[i + 1] = temp;
                        swapped = true;
                    }
                }
            }
        }
        """
        expect = """Program([
	FuncDecl(program, VoidType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([AssignStmt(Id(n), IntegerLit(10)), AssignStmt(Id(swapped), BooleanLit(True)), WhileStmt(Id(swapped), BlockStmt([AssignStmt(Id(swapped), BooleanLit(False)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(arr, [Id(i)]), ArrayCell(arr, [BinExpr(+, Id(i), IntegerLit(1))])), BlockStmt([AssignStmt(Id(temp), ArrayCell(arr, [Id(i)])), AssignStmt(ArrayCell(arr, [Id(i)]), ArrayCell(arr, [BinExpr(+, Id(i), IntegerLit(1))])), AssignStmt(ArrayCell(arr, [BinExpr(+, Id(i), IntegerLit(1))]), Id(temp)), AssignStmt(Id(swapped), BooleanLit(True))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 313))

    def test_ast_15(self):
        input_str = """
         isPalindrome : function boolean (s : string) {
             for (i = 0, i < length(s) / 2, i + 1) {
                 if (s[i] != s[length(s) - i - 1]) {
                     return false;
                 }
             }
             return true;
         }
         main: function void () {
             s = "racecar";
             if (isPalindrome(s)) {
                 printString("s is a palindrome.");
             } else {
                 printString("s is not a palindrome.");
             }
         }
         """
        expect = """Program([
	FuncDecl(isPalindrome, BooleanType, [Param(s, StringType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(/, FuncCall(length, [Id(s)]), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(s, [Id(i)]), ArrayCell(s, [BinExpr(-, BinExpr(-, FuncCall(length, [Id(s)]), Id(i)), IntegerLit(1))])), BlockStmt([ReturnStmt(BooleanLit(False))]))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(racecar)), IfStmt(FuncCall(isPalindrome, [Id(s)]), BlockStmt([CallStmt(printString, StringLit(s is a palindrome.))]), BlockStmt([CallStmt(printString, StringLit(s is not a palindrome.))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 314))

    def test_ast_16(self):
        """Reverse string function"""
        input_str = """
         reverse : function string (s : string) {
             result = "";
             for (i = length(s) - 1, i >= 0, i - 1) {
                 result = result + s[i];
             }
             return result;
         }
         main: function void () {
             s = "Hello world!";
             printString(reverse(s));
         }
         """
        expect = """Program([
	FuncDecl(reverse, StringType, [Param(s, StringType)], None, BlockStmt([AssignStmt(Id(result), StringLit()), ForStmt(AssignStmt(Id(i), BinExpr(-, FuncCall(length, [Id(s)]), IntegerLit(1))), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(s, [Id(i)])))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(Hello world!)), CallStmt(printString, FuncCall(reverse, [Id(s)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 315))

    def test_ast_17(self):
        """Reverse int function"""
        input_str = """
         reverse : function integer (n : integer) {
             result = 0;
             while (n > 0) {
                 result = result * 10 + n % 10;
                 n = n / 10;
             }
             return result;
         }
         main: function void () {
             n = 12345;
             printInt(reverse(n));
         }
         """
        expect = """Program([
	FuncDecl(reverse, IntegerType, [Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(result), IntegerLit(0)), WhileStmt(BinExpr(>, Id(n), IntegerLit(0)), BlockStmt([AssignStmt(Id(result), BinExpr(+, BinExpr(*, Id(result), IntegerLit(10)), BinExpr(%, Id(n), IntegerLit(10)))), AssignStmt(Id(n), BinExpr(/, Id(n), IntegerLit(10)))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), IntegerLit(12345)), CallStmt(printInt, FuncCall(reverse, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 316))

    def test_ast_18(self):
        """Search insert position function"""
        input_str = """
         searchInsert : function integer (nums : array[5] of integer, target : integer) {
             for (i = 0, i < length(nums), i + 1) {
                 if (nums[i] >= target) {
                     return i;
                 }
             }
             return length(nums);
         }
         main: function void () {
             nums = 21;
             target = 5;
             printInt(searchInsert(nums, target));
         }
         """
        expect = """Program([
	FuncDecl(searchInsert, IntegerType, [Param(nums, ArrayType([5], IntegerType)), Param(target, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(nums)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>=, ArrayCell(nums, [Id(i)]), Id(target)), BlockStmt([ReturnStmt(Id(i))]))])), ReturnStmt(FuncCall(length, [Id(nums)]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(nums), IntegerLit(21)), AssignStmt(Id(target), IntegerLit(5)), CallStmt(printInt, FuncCall(searchInsert, [Id(nums), Id(target)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 317))

    def test_ast_19(self):
        input_str = """
        main: function void () {
            if (x > 0) {
                printString("x is positive!");
            }
            else if (x < 0) {
                printString("x is negative!");
            }
            else {
                printString("x is zero!");
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(x), IntegerLit(0)), BlockStmt([CallStmt(printString, StringLit(x is positive!))]), IfStmt(BinExpr(<, Id(x), IntegerLit(0)), BlockStmt([CallStmt(printString, StringLit(x is negative!))]), BlockStmt([CallStmt(printString, StringLit(x is zero!))])))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 318))

    def test_ast_20(self):
        input_str = """
                 isArmstrong : function boolean (n : integer) {
             sum = 0;
             temp = n;
             while (temp > 0) {
                 digit = temp % 10;
                 sum = sum + digit * digit * digit;
                 temp = temp / 10;
             }
             if (sum == n) {
                 return true;
             } else {
                 return false;
             }
         }
         main: function void () {
             n = 153;
             if (isArmstrong(n)) {
                 printString("n is an Armstrong number.");
             } else {
                 printString("n is not an Armstrong number.");
             }
         }
         """
        expect = """Program([
	FuncDecl(isArmstrong, BooleanType, [Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(sum), IntegerLit(0)), AssignStmt(Id(temp), Id(n)), WhileStmt(BinExpr(>, Id(temp), IntegerLit(0)), BlockStmt([AssignStmt(Id(digit), BinExpr(%, Id(temp), IntegerLit(10))), AssignStmt(Id(sum), BinExpr(+, Id(sum), BinExpr(*, BinExpr(*, Id(digit), Id(digit)), Id(digit)))), AssignStmt(Id(temp), BinExpr(/, Id(temp), IntegerLit(10)))])), IfStmt(BinExpr(==, Id(sum), Id(n)), BlockStmt([ReturnStmt(BooleanLit(True))]), BlockStmt([ReturnStmt(BooleanLit(False))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), IntegerLit(153)), IfStmt(FuncCall(isArmstrong, [Id(n)]), BlockStmt([CallStmt(printString, StringLit(n is an Armstrong number.))]), BlockStmt([CallStmt(printString, StringLit(n is not an Armstrong number.))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 319))

    def test_ast_21(self):
        """is anaGram function"""
        input_str = """
         isAnaGram : function boolean (s1 : string, s2 : string) {
             if (length(s1) != length(s2)) {
                 return false;
             }
             for (i = 0, i < length(s1), i + 1) {
                 if (s1[i] != s2[length(s2) - i - 1]) {
                     return false;
                 }
             }
             return true;
         }
         main: function void () {
             s1 = "racecar";
             s2 = "racecar";
             if (isAnaGram(s1, s2)) {
                 printString("s1 and s2 are anagrams.");
             } else {
                 printString("s1 and s2 are not anagrams.");
             }
         }
         """
        expect = """Program([
	FuncDecl(isAnaGram, BooleanType, [Param(s1, StringType), Param(s2, StringType)], None, BlockStmt([IfStmt(BinExpr(!=, FuncCall(length, [Id(s1)]), FuncCall(length, [Id(s2)])), BlockStmt([ReturnStmt(BooleanLit(False))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(s1)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(s1, [Id(i)]), ArrayCell(s2, [BinExpr(-, BinExpr(-, FuncCall(length, [Id(s2)]), Id(i)), IntegerLit(1))])), BlockStmt([ReturnStmt(BooleanLit(False))]))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s1), StringLit(racecar)), AssignStmt(Id(s2), StringLit(racecar)), IfStmt(FuncCall(isAnaGram, [Id(s1), Id(s2)]), BlockStmt([CallStmt(printString, StringLit(s1 and s2 are anagrams.))]), BlockStmt([CallStmt(printString, StringLit(s1 and s2 are not anagrams.))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 320))

    def test_ast_22(self):
        input_str = """
         lowestCommonAncestor : function integer (root : integer, p : integer, q : integer) {
             if ((p < root) && (q < root)) {
                 return lowestCommonAncestor(rootLeft, p, q);
             } else if ((p > root) && (q > root)) {
                 return lowestCommonAncestor(rootRight, p, q);
             } else {
                 return root;
             }
         }
         main: function void () {
             root = 6;
             p = 2;
             q = 8;
             printInt(lowestCommonAncestor(root, p, q));
         }
         """
        expect = """Program([
	FuncDecl(lowestCommonAncestor, IntegerType, [Param(root, IntegerType), Param(p, IntegerType), Param(q, IntegerType)], None, BlockStmt([IfStmt(BinExpr(&&, BinExpr(<, Id(p), Id(root)), BinExpr(<, Id(q), Id(root))), BlockStmt([ReturnStmt(FuncCall(lowestCommonAncestor, [Id(rootLeft), Id(p), Id(q)]))]), IfStmt(BinExpr(&&, BinExpr(>, Id(p), Id(root)), BinExpr(>, Id(q), Id(root))), BlockStmt([ReturnStmt(FuncCall(lowestCommonAncestor, [Id(rootRight), Id(p), Id(q)]))]), BlockStmt([ReturnStmt(Id(root))])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(root), IntegerLit(6)), AssignStmt(Id(p), IntegerLit(2)), AssignStmt(Id(q), IntegerLit(8)), CallStmt(printInt, FuncCall(lowestCommonAncestor, [Id(root), Id(p), Id(q)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 321))

    def test_ast_23(self):
        """Sum of left leaves function"""
        input_str = """
         sumOfLeftLeaves : function integer (root : integer) {
             if (root == null) {
                 return 0;
             }
             if ((rootLeft != null) && (rootLeftLeft == null) && (rootLeftRight == null)) {
                 return rootLeftVal + sumOfLeftLeaves(rootRight);
             }
             return sumOfLeftLeaves(rootLeft) + sumOfLeftLeaves(rootRight);
         }
         main: function void () {
             root = 3;
             printInt(sumOfLeftLeaves(root));
         }
         """
        expect = """Program([
	FuncDecl(sumOfLeftLeaves, IntegerType, [Param(root, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(root), Id(null)), BlockStmt([ReturnStmt(IntegerLit(0))])), IfStmt(BinExpr(&&, BinExpr(&&, BinExpr(!=, Id(rootLeft), Id(null)), BinExpr(==, Id(rootLeftLeft), Id(null))), BinExpr(==, Id(rootLeftRight), Id(null))), BlockStmt([ReturnStmt(BinExpr(+, Id(rootLeftVal), FuncCall(sumOfLeftLeaves, [Id(rootRight)])))])), ReturnStmt(BinExpr(+, FuncCall(sumOfLeftLeaves, [Id(rootLeft)]), FuncCall(sumOfLeftLeaves, [Id(rootRight)])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(root), IntegerLit(3)), CallStmt(printInt, FuncCall(sumOfLeftLeaves, [Id(root)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 322))

    def test_ast_24(self):
        """Reverse Linked List function"""
        input_str = """
         reverseList : function integer (head : integer) {
             prev = null;
             curr = head;
             while (curr != null) {
                 nextTemp = currNext;
                 currNext = prev;
                 prev = curr;
                 curr = nextTemp;
             }
             return prev;
         }
         main: function void () {
             head = 1;
             printInt(reverseList(head));
         }
         """
        expect = """Program([
	FuncDecl(reverseList, IntegerType, [Param(head, IntegerType)], None, BlockStmt([AssignStmt(Id(prev), Id(null)), AssignStmt(Id(curr), Id(head)), WhileStmt(BinExpr(!=, Id(curr), Id(null)), BlockStmt([AssignStmt(Id(nextTemp), Id(currNext)), AssignStmt(Id(currNext), Id(prev)), AssignStmt(Id(prev), Id(curr)), AssignStmt(Id(curr), Id(nextTemp))])), ReturnStmt(Id(prev))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(head), IntegerLit(1)), CallStmt(printInt, FuncCall(reverseList, [Id(head)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 323))

    def test_ast_25(self):
        """Valid Parentheses function"""
        input_str = """
         isValid : function boolean (s : string) {
             if (length(s) % 2 != 0) {
                 return false;
             }
             for (i = 0, i < length(s), i + 1) {
                 if (s[i] == "(") {
                     push(s[i]);
                 } else if (s[i] == ")") {
                     if (top() == "(") {
                         pop();
                     } else {
                         return false;
                     }
                 }
             }
             if (isEmpty()) {
                 return true;
             } else {
                 return false;
             }
         }
         main: function void () {
             s = "((()))";
             if (isValid(s)) {
                 printString("s is valid.");
             } else {
                 printString("s is not valid.");
             }
         }
         """
        expect = """Program([
	FuncDecl(isValid, BooleanType, [Param(s, StringType)], None, BlockStmt([IfStmt(BinExpr(!=, BinExpr(%, FuncCall(length, [Id(s)]), IntegerLit(2)), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(s)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(s, [Id(i)]), StringLit(()), BlockStmt([CallStmt(push, ArrayCell(s, [Id(i)]))]), IfStmt(BinExpr(==, ArrayCell(s, [Id(i)]), StringLit())), BlockStmt([IfStmt(BinExpr(==, FuncCall(top, []), StringLit(()), BlockStmt([CallStmt(pop, )]), BlockStmt([ReturnStmt(BooleanLit(False))]))])))])), IfStmt(FuncCall(isEmpty, []), BlockStmt([ReturnStmt(BooleanLit(True))]), BlockStmt([ReturnStmt(BooleanLit(False))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(((())))), IfStmt(FuncCall(isValid, [Id(s)]), BlockStmt([CallStmt(printString, StringLit(s is valid.))]), BlockStmt([CallStmt(printString, StringLit(s is not valid.))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 324))

    def test_ast_26(self):
        """Square Root function"""
        input_str = """
         sqrt : function float (x : float) {
             if (x == 0) {
                 return 0;
             }
             if (x < 0) {
                 return -1;
             }
             left = 1;
             right = x;
             while (left <= right) {
                 mid = (left + right) / 2;
                 if (mid * mid == x) {
                     return mid;
                 } else if (mid * mid < x) {
                     left = mid + 1;
                 } else {
                     right = mid - 1;
                 }
             }
             return right;
         }
         main: function void () {
             x = 8;
             printFloat(sqrt(x));
         }
         """
        expected = """Program([
	FuncDecl(sqrt, FloatType, [Param(x, FloatType)], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(0)), BlockStmt([ReturnStmt(IntegerLit(0))])), IfStmt(BinExpr(<, Id(x), IntegerLit(0)), BlockStmt([ReturnStmt(UnExpr(-, IntegerLit(1)))])), AssignStmt(Id(left), IntegerLit(1)), AssignStmt(Id(right), Id(x)), WhileStmt(BinExpr(<=, Id(left), Id(right)), BlockStmt([AssignStmt(Id(mid), BinExpr(/, BinExpr(+, Id(left), Id(right)), IntegerLit(2))), IfStmt(BinExpr(==, BinExpr(*, Id(mid), Id(mid)), Id(x)), BlockStmt([ReturnStmt(Id(mid))]), IfStmt(BinExpr(<, BinExpr(*, Id(mid), Id(mid)), Id(x)), BlockStmt([AssignStmt(Id(left), BinExpr(+, Id(mid), IntegerLit(1)))]), BlockStmt([AssignStmt(Id(right), BinExpr(-, Id(mid), IntegerLit(1)))])))])), ReturnStmt(Id(right))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), IntegerLit(8)), CallStmt(printFloat, FuncCall(sqrt, [Id(x)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 325))

    def test_ast_27(self):
        """Climbing Stairs function"""
        input_str = """
         climbStairs : function integer (n : integer) {
             if (n == 1) {
                 return 1;
             }
             first = 1;
             second = 2;
             for (i = 3, i <= n, i + 1) {
                 third = first + second;
                 first = second;
                 second = third;
             }
             return second;
         }
         main: function void () {
             n = 4;
             printInt(climbStairs(n));
         }
         """
        expected = """Program([
	FuncDecl(climbStairs, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(1)), BlockStmt([ReturnStmt(IntegerLit(1))])), AssignStmt(Id(first), IntegerLit(1)), AssignStmt(Id(second), IntegerLit(2)), ForStmt(AssignStmt(Id(i), IntegerLit(3)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(third), BinExpr(+, Id(first), Id(second))), AssignStmt(Id(first), Id(second)), AssignStmt(Id(second), Id(third))])), ReturnStmt(Id(second))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), IntegerLit(4)), CallStmt(printInt, FuncCall(climbStairs, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 326))

    def test_ast_28(self):
        """Count Primes function"""
        input_str = """
         countPrimes : function integer (n : integer) {
             if (n < 2) {
                 return 0;
             }
             count = 0;
             for (i = 2, i < n, i + 1) {
                 if (isPrime(i)) {
                     count = count + 1;
                 }
             }
             return count;
         }
         isPrime : function boolean (n : integer) {
             if (n < 2) {
                 return false;
             }
             for (i = 2, i * i <= n, i + 1) {
                 if (n % i == 0) {
                     return false;
                 }
             }
             return true;
         }
         main: function void () {
             n = 10;
             printInt(countPrimes(n));
         }
         """
        expected = """Program([
	FuncDecl(countPrimes, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(n), IntegerLit(2)), BlockStmt([ReturnStmt(IntegerLit(0))])), AssignStmt(Id(count), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(FuncCall(isPrime, [Id(i)]), BlockStmt([AssignStmt(Id(count), BinExpr(+, Id(count), IntegerLit(1)))]))])), ReturnStmt(Id(count))]))
	FuncDecl(isPrime, BooleanType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(n), IntegerLit(2)), BlockStmt([ReturnStmt(BooleanLit(False))])), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, BinExpr(*, Id(i), Id(i)), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), BlockStmt([ReturnStmt(BooleanLit(False))]))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), IntegerLit(10)), CallStmt(printInt, FuncCall(countPrimes, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 327))

    def test_ast_29(self):
        """Decode Ways function"""
        input_str = """
         numDecodings : function integer (s : string) {
             if (s == "") {
                 return 0;
             }
             n = length(s);
             dp : array[6] of integer;
             dp[0] = 1;
             dp[1] = 1;
             for (i = 2, i <= n, i + 1) {
                 if (s[i - 1] != "0") {
                     dp[i] = dp[i - 1];
                 }
                 if ((s[i - 2] == "1") || ((s[i - 2] == "2") && (s[i - 1] < "7"))) {
                     dp[i] = dp[i] + dp[i - 2];
                 }
             }
             return dp[n];
         }
         main: function void () {
             s = "226";
             printInt(numDecodings(s));
         }
         """
        expected = """Program([
	FuncDecl(numDecodings, IntegerType, [Param(s, StringType)], None, BlockStmt([IfStmt(BinExpr(==, Id(s), StringLit()), BlockStmt([ReturnStmt(IntegerLit(0))])), AssignStmt(Id(n), FuncCall(length, [Id(s)])), VarDecl(dp, ArrayType([6], IntegerType)), AssignStmt(ArrayCell(dp, [IntegerLit(0)]), IntegerLit(1)), AssignStmt(ArrayCell(dp, [IntegerLit(1)]), IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(s, [BinExpr(-, Id(i), IntegerLit(1))]), StringLit(0)), BlockStmt([AssignStmt(ArrayCell(dp, [Id(i)]), ArrayCell(dp, [BinExpr(-, Id(i), IntegerLit(1))]))])), IfStmt(BinExpr(||, BinExpr(==, ArrayCell(s, [BinExpr(-, Id(i), IntegerLit(2))]), StringLit(1)), BinExpr(&&, BinExpr(==, ArrayCell(s, [BinExpr(-, Id(i), IntegerLit(2))]), StringLit(2)), BinExpr(<, ArrayCell(s, [BinExpr(-, Id(i), IntegerLit(1))]), StringLit(7)))), BlockStmt([AssignStmt(ArrayCell(dp, [Id(i)]), BinExpr(+, ArrayCell(dp, [Id(i)]), ArrayCell(dp, [BinExpr(-, Id(i), IntegerLit(2))])))]))])), ReturnStmt(ArrayCell(dp, [Id(n)]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(226)), CallStmt(printInt, FuncCall(numDecodings, [Id(s)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 328))

    def test_ast_30(self):
        """Delete Node in a Linked List function"""
        input_str = """
         deleteNode : function void (node : integer) {
             nodeVal = nodeVal;
             nodeNext = nodeNext;
         }
         main: function void () {
             node = 5;
             deleteNode(node);
         }
         """
        expected = """Program([
	FuncDecl(deleteNode, VoidType, [Param(node, IntegerType)], None, BlockStmt([AssignStmt(Id(nodeVal), Id(nodeVal)), AssignStmt(Id(nodeNext), Id(nodeNext))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(node), IntegerLit(5)), CallStmt(deleteNode, Id(node))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 329))

    def test_ast_31(self):
        """Merge Two Sorted Lists function"""
        input_str = """
         mergeTwoLists : function integer (l1 : integer, l2 : integer) {
             if (l1 == null) {
                 return l2;
             }
             if (l2 == null) {
                 return l1;
             }
             if (l1Val < l2Val) {
                 l1Next = mergeTwoLists(l1Next, l2);
                 return l1;
             } else {
                 l2Next = mergeTwoLists(l1, l2Next);
                 return l2;
             }
         }
         main: function void () {
             l1 = 1;
             l2 = 2;
             printInt(mergeTwoLists(l1, l2));
         }
         """
        expected = """Program([
	FuncDecl(mergeTwoLists, IntegerType, [Param(l1, IntegerType), Param(l2, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(l1), Id(null)), BlockStmt([ReturnStmt(Id(l2))])), IfStmt(BinExpr(==, Id(l2), Id(null)), BlockStmt([ReturnStmt(Id(l1))])), IfStmt(BinExpr(<, Id(l1Val), Id(l2Val)), BlockStmt([AssignStmt(Id(l1Next), FuncCall(mergeTwoLists, [Id(l1Next), Id(l2)])), ReturnStmt(Id(l1))]), BlockStmt([AssignStmt(Id(l2Next), FuncCall(mergeTwoLists, [Id(l1), Id(l2Next)])), ReturnStmt(Id(l2))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(l1), IntegerLit(1)), AssignStmt(Id(l2), IntegerLit(2)), CallStmt(printInt, FuncCall(mergeTwoLists, [Id(l1), Id(l2)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 330))

    def test_ast_32(self):
        """Find the index of the first occurrence of a substring function"""
        input_str = """
         find : function integer (str : string, sub : string) {
             for (i = 0, i < length(str), i + 1) {
                 for (j = 0, j < length(sub), j + 1) {
                     if (str[i + j] != sub[j]) {
                         break;
                     }
                 }
                 if (j == length(sub)) {
                     return i;
                 }
             }
             return -1;
         }
         main: function void () {
             str = "Hello World!";
             sub = "World";
             printInt(find(str, sub));
         }
         """
        expected = """Program([
	FuncDecl(find, IntegerType, [Param(str, StringType), Param(sub, StringType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(str)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), FuncCall(length, [Id(sub)])), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(str, [BinExpr(+, Id(i), Id(j))]), ArrayCell(sub, [Id(j)])), BlockStmt([BreakStmt()]))])), IfStmt(BinExpr(==, Id(j), FuncCall(length, [Id(sub)])), BlockStmt([ReturnStmt(Id(i))]))])), ReturnStmt(UnExpr(-, IntegerLit(1)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(str), StringLit(Hello World!)), AssignStmt(Id(sub), StringLit(World)), CallStmt(printInt, FuncCall(find, [Id(str), Id(sub)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 331))

    def test_ast_33(self):
        """Put the first letter of each word in uppercase function"""
        input_str = """
         capitalize : function string (str : string) {
             str[0] = toUpper(str[0]);
             for (i = 1, i < length(str), i + 1) {
                 if (str[i - 1] == " ") {
                     str[i] = toUpper(str[i]);
                 }
             }
             return str;
         }
         main: function void () {
             str = "hello world!";
             printStr(capitalize(str));
         }
         """
        expected = """Program([
	FuncDecl(capitalize, StringType, [Param(str, StringType)], None, BlockStmt([AssignStmt(ArrayCell(str, [IntegerLit(0)]), FuncCall(toUpper, [ArrayCell(str, [IntegerLit(0)])])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), FuncCall(length, [Id(str)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(str, [BinExpr(-, Id(i), IntegerLit(1))]), StringLit( )), BlockStmt([AssignStmt(ArrayCell(str, [Id(i)]), FuncCall(toUpper, [ArrayCell(str, [Id(i)])]))]))])), ReturnStmt(Id(str))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(str), StringLit(hello world!)), CallStmt(printStr, FuncCall(capitalize, [Id(str)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 332))

    def test_ast_34(self):
        """Find the first non-repeating character function"""
        input_str = """
         firstNonRepeating : function string (str : string) {
             for (i = 0, i < length(str), i + 1) {
                 found = false;
                 for (j = 0, j < length(str), j + 1) {
                     if ((i != j) && (str[i] == str[j])) {
                         found = true;
                         break;
                     }
                 }
                 if (!found) {
                     return str[i];
                 }
             }
             return "";
         }
         main: function void () {
             str = "Hello World!";
             printStr(firstNonRepeating(str));
         }
         """
        expected = """Program([
	FuncDecl(firstNonRepeating, StringType, [Param(str, StringType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(str)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(found), BooleanLit(False)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), FuncCall(length, [Id(str)])), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(&&, BinExpr(!=, Id(i), Id(j)), BinExpr(==, ArrayCell(str, [Id(i)]), ArrayCell(str, [Id(j)]))), BlockStmt([AssignStmt(Id(found), BooleanLit(True)), BreakStmt()]))])), IfStmt(UnExpr(!, Id(found)), BlockStmt([ReturnStmt(ArrayCell(str, [Id(i)]))]))])), ReturnStmt(StringLit())]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(str), StringLit(Hello World!)), CallStmt(printStr, FuncCall(firstNonRepeating, [Id(str)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 333))

    def test_ast_35(self):
        """Isomorphic Strings function"""
        input_str = """
         isIsomorphic : function boolean (s : string, t : string) {
             n = length(s);
             if (n != length(t)) {
                 return false;
             }
             map : array [256] of integer= {};
             for (i = 0, i < n, i + 1) {
                 if (map[s[i]] == 0) {
                     map[s[i]] = t[i];
                 } else {
                     if (map[s[i]] != t[i]) {
                         return false;
                     }
                 }
             }
             return true;
         }
         main: function void () {
             s = "egg";
             t = "add";
             printBool(isIsomorphic(s, t));
         }
         """
        expected = """Program([
	FuncDecl(isIsomorphic, BooleanType, [Param(s, StringType), Param(t, StringType)], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(s)])), IfStmt(BinExpr(!=, Id(n), FuncCall(length, [Id(t)])), BlockStmt([ReturnStmt(BooleanLit(False))])), VarDecl(map, ArrayType([256], IntegerType), ArrayLit([])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(map, [ArrayCell(s, [Id(i)])]), IntegerLit(0)), BlockStmt([AssignStmt(ArrayCell(map, [ArrayCell(s, [Id(i)])]), ArrayCell(t, [Id(i)]))]), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(map, [ArrayCell(s, [Id(i)])]), ArrayCell(t, [Id(i)])), BlockStmt([ReturnStmt(BooleanLit(False))]))]))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(egg)), AssignStmt(Id(t), StringLit(add)), CallStmt(printBool, FuncCall(isIsomorphic, [Id(s), Id(t)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 334))

    def test_ast_36(self):
        """Is Subsequence function"""
        input_str = """
         isSubsequence : function boolean (s : string, t : string) {
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
         }
         """
        expected = """Program([
	FuncDecl(isSubsequence, BooleanType, [Param(s, StringType), Param(t, StringType)], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(s)])), AssignStmt(Id(m), FuncCall(length, [Id(t)])), AssignStmt(Id(i), IntegerLit(0)), AssignStmt(Id(j), IntegerLit(0)), WhileStmt(BinExpr(&&, BinExpr(<, Id(i), Id(n)), BinExpr(<, Id(j), Id(m))), BlockStmt([IfStmt(BinExpr(==, ArrayCell(s, [Id(i)]), ArrayCell(t, [Id(j)])), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))])), ReturnStmt(BinExpr(==, Id(i), Id(n)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(abc)), AssignStmt(Id(t), StringLit(ahbgdc)), CallStmt(printBool, FuncCall(isSubsequence, [Id(s), Id(t)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 335))

    def test_ast_37(self):
        """Find the Difference function"""
        input_str = """
         findTheDifference : function string (s : string, t : string) {
             n = length(s);
             m = length(t);
             sum = 0;
             for (i = 0, i < n, i + 1) {
                 sum = sum + ord(s[i]);
             }
             for (i = 0, i < m, i + 1) {
                 sum = sum - ord(t[i]);
             }
             return chr(-sum);
         }
         main: function void () {
             s = "abcd";
             t = "abcde";
             printString(findTheDifference(s, t));
         }
         """
        expected = """Program([
	FuncDecl(findTheDifference, StringType, [Param(s, StringType), Param(t, StringType)], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(s)])), AssignStmt(Id(m), FuncCall(length, [Id(t)])), AssignStmt(Id(sum), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), FuncCall(ord, [ArrayCell(s, [Id(i)])])))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(m)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(-, Id(sum), FuncCall(ord, [ArrayCell(t, [Id(i)])])))])), ReturnStmt(FuncCall(chr, [UnExpr(-, Id(sum))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(abcd)), AssignStmt(Id(t), StringLit(abcde)), CallStmt(printString, FuncCall(findTheDifference, [Id(s), Id(t)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 336))

    def test_ast_38(self):
        """Find the Celebrity function"""
        input_str = """
         findCelebrity : function integer (n : integer) {
             candidate = 0;
             for (i = 1, i < n, i + 1) {
                 if (knows(candidate, i)) {
                     candidate = i;
                 }
             }
             for (i = 0, i < n, i + 1) {
                 if ((i != candidate) && ((knows(candidate, i)) || (!knows(i, candidate)))) {
                     return -1;
                 }
             }
             return candidate;
         }
         main: function void () {
             n = 2;
             printInt(findCelebrity(n));
         }
         """
        expected = """Program([
	FuncDecl(findCelebrity, IntegerType, [Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(candidate), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(FuncCall(knows, [Id(candidate), Id(i)]), BlockStmt([AssignStmt(Id(candidate), Id(i))]))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(&&, BinExpr(!=, Id(i), Id(candidate)), BinExpr(||, FuncCall(knows, [Id(candidate), Id(i)]), UnExpr(!, FuncCall(knows, [Id(i), Id(candidate)])))), BlockStmt([ReturnStmt(UnExpr(-, IntegerLit(1)))]))])), ReturnStmt(Id(candidate))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(n), IntegerLit(2)), CallStmt(printInt, FuncCall(findCelebrity, [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 337))

    def test_ast_39(self):
        """Roman to Integer function"""
        input_str = """
         romanToInt : function integer (s : string) {
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
         }
         """
        expected = """Program([
	FuncDecl(romanToInt, IntegerType, [Param(s, StringType)], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(s)])), AssignStmt(Id(result), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(&&, BinExpr(>, Id(i), IntegerLit(0)), BinExpr(>, ArrayCell(roman, [ArrayCell(s, [Id(i)])]), ArrayCell(roman, [ArrayCell(s, [BinExpr(-, Id(i), IntegerLit(1))])]))), BlockStmt([AssignStmt(Id(result), BinExpr(-, BinExpr(+, Id(result), ArrayCell(roman, [ArrayCell(s, [Id(i)])])), BinExpr(*, IntegerLit(2), ArrayCell(roman, [ArrayCell(s, [BinExpr(-, Id(i), IntegerLit(1))])]))))]), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(roman, [ArrayCell(s, [Id(i)])])))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(MCMXCIV)), CallStmt(printInt, FuncCall(romanToInt, [Id(s)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 338))

    def test_ast_40(self):
        """Length of Last Word function"""
        input_str = """
         lengthOfLastWord : function integer (s : string) {
             n : integer = length(s);
             result : integer = 0;
             for (i = n - 1, i >= 0, i - 1) {
                 if (s[i] != " ") {
                     result = result + 1;
                 } else {
                     if (result > 0) {
                         break;
                     }
                 }
             }
             return result;
         }
         main: function void () {
             s = "Hello World";
             printInt(lengthOfLastWord(s));
         }
         """
        expected = """Program([
	FuncDecl(lengthOfLastWord, IntegerType, [Param(s, StringType)], None, BlockStmt([VarDecl(n, IntegerType, FuncCall(length, [Id(s)])), VarDecl(result, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(s, [Id(i)]), StringLit( )), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), IntegerLit(1)))]), BlockStmt([IfStmt(BinExpr(>, Id(result), IntegerLit(0)), BlockStmt([BreakStmt()]))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(Hello World)), CallStmt(printInt, FuncCall(lengthOfLastWord, [Id(s)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 339))

    def test_ast_41(self):
        input_str = """
            main : function void() {
                if ((b >= 2.0) && (b <= 3.0)) {
                    printf("b is between 2.0 and 3.0, inclusive.\\n");
                } else {
                    printf("b is not between 2.0 and 3.0, inclusive.\\n");
                }
            }
        """
        expected = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(&&, BinExpr(>=, Id(b), FloatLit(2.0)), BinExpr(<=, Id(b), FloatLit(3.0))), BlockStmt([CallStmt(printf, StringLit(b is between 2.0 and 3.0, inclusive.\\n))]), BlockStmt([CallStmt(printf, StringLit(b is not between 2.0 and 3.0, inclusive.\\n))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 340))

    def test_ast_42(self):
        input_str = """
        main: function integer () {
            n = parseNumber("5");
            result : integer = 1;
            for (i = 1, i <= n, i + 1) {
                result = result * i;
            }
            return result;
        }
        """
        expected = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(n), FuncCall(parseNumber, [StringLit(5)])), VarDecl(result, IntegerType, IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(result), BinExpr(*, Id(result), Id(i)))])), ReturnStmt(Id(result))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 341))

    def test_ast_43(self):
        input_str = """
        main: function void () {
            algorithm = "binary tree traversal (inorder)";
            root : integer = parseTree("(3 (1 () (2)) (4 () (5)))");
            result : array[5] of integer = {};
            inorder(root, result);
        }
        """
        expected = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(algorithm), StringLit(binary tree traversal (inorder))), VarDecl(root, IntegerType, FuncCall(parseTree, [StringLit((3 (1 () (2)) (4 () (5))))])), VarDecl(result, ArrayType([5], IntegerType), ArrayLit([])), CallStmt(inorder, Id(root), Id(result))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 342))

    def test_ast_44(self):
        input_str = """
                main: function void () {
            if (a > 10) {
                if (b > 10) {
                    printFloat(1.2);
                }
                else {
                    readString();
                }
            }
            else {
                s = "Hello";
                printString(s);
            }
        }
        """
        expected = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(10)), BlockStmt([IfStmt(BinExpr(>, Id(b), IntegerLit(10)), BlockStmt([CallStmt(printFloat, FloatLit(1.2))]), BlockStmt([CallStmt(readString, )]))]), BlockStmt([AssignStmt(Id(s), StringLit(Hello)), CallStmt(printString, Id(s))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 343))

    def test_ast_45(self):
        input_str = """
        main: function void () {
            if (a > 10) {
                if (b > 10) {
                    printString("Both a and b are greater than 10");
                }
                else {
                    printString("Only a is greater than 10");
                }
            }
            else {
                printString("Neither a nor b is greater than 10");
            }
        }
        """
        expected = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(10)), BlockStmt([IfStmt(BinExpr(>, Id(b), IntegerLit(10)), BlockStmt([CallStmt(printString, StringLit(Both a and b are greater than 10))]), BlockStmt([CallStmt(printString, StringLit(Only a is greater than 10))]))]), BlockStmt([CallStmt(printString, StringLit(Neither a nor b is greater than 10))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 344))

    def test_ast_46(self):
        """Bubble sort"""
        input_str = """
        program: function void (arr: array [10] of integer) {
            n = 10;
            for (i = 0, i < n - 1, i + 1) {
                for (j = 0, j < n - i - 1, j + 1) {
                    if (arr[j] > arr[j + 1]) {
                        temp = arr[j];
                        arr[j] = arr[j + 1];
                        arr[j + 1] = temp;
                    }
                }
            }
        }
        """
        expected = """Program([
	FuncDecl(program, VoidType, [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([AssignStmt(Id(n), IntegerLit(10)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), BinExpr(-, BinExpr(-, Id(n), Id(i)), IntegerLit(1))), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(arr, [Id(j)]), ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))])), BlockStmt([AssignStmt(Id(temp), ArrayCell(arr, [Id(j)])), AssignStmt(ArrayCell(arr, [Id(j)]), ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))])), AssignStmt(ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))]), Id(temp))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 345))

    def test_ast_47(self):
        """Binary Search"""
        input_str = """
            binarySearch: function integer (arr: array [10] of integer, target: integer) {
                low = 0;
                high = 9;
                while (low <= high) {
                    mid = (low + high) / 2;
                    if (arr[mid] == target) {
                        return mid;
                    } else if (arr[mid] < target) {
                        low = mid + 1;
                    } else {
                        high = mid - 1;
                    }
                }
                return -1;
            }
        """
        expected = """Program([
	FuncDecl(binarySearch, IntegerType, [Param(arr, ArrayType([10], IntegerType)), Param(target, IntegerType)], None, BlockStmt([AssignStmt(Id(low), IntegerLit(0)), AssignStmt(Id(high), IntegerLit(9)), WhileStmt(BinExpr(<=, Id(low), Id(high)), BlockStmt([AssignStmt(Id(mid), BinExpr(/, BinExpr(+, Id(low), Id(high)), IntegerLit(2))), IfStmt(BinExpr(==, ArrayCell(arr, [Id(mid)]), Id(target)), BlockStmt([ReturnStmt(Id(mid))]), IfStmt(BinExpr(<, ArrayCell(arr, [Id(mid)]), Id(target)), BlockStmt([AssignStmt(Id(low), BinExpr(+, Id(mid), IntegerLit(1)))]), BlockStmt([AssignStmt(Id(high), BinExpr(-, Id(mid), IntegerLit(1)))])))])), ReturnStmt(UnExpr(-, IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 346))

    def test_ast_48(self):
        """Loop through array"""
        input_str = """
        a : integer = 3;
        program: function void () {
            a, b, c: integer;
            d, e, f: float;
            g: boolean;
        }"""
        expected = """Program([
	VarDecl(a, IntegerType, IntegerLit(3))
	FuncDecl(program, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), VarDecl(b, IntegerType), VarDecl(c, IntegerType), VarDecl(d, FloatType), VarDecl(e, FloatType), VarDecl(f, FloatType), VarDecl(g, BooleanType)]))
])"""
        self.assertTrue(TestAST.test(input_str, expected, 347))

    def test_ast_49(self):
        input_str = """
        program: function void () {
            a: integer = 1;
            b: integer = 2;
            while (a <= 10) {
                b = b * 2;
                printInteger(b);
                a = a + 1;
            }
            return;
        }
        """
        expect = """Program([
	FuncDecl(program, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(2)), WhileStmt(BinExpr(<=, Id(a), IntegerLit(10)), BlockStmt([AssignStmt(Id(b), BinExpr(*, Id(b), IntegerLit(2))), CallStmt(printInteger, Id(b)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 348))

    def test_ast_50(self):
        """Testing return statement:"""
        input_str = """
            factorial: function integer (n: integer) {
                if ((n == 0) || (n==1)) return 1;
                else return n * factorial(n - 1);
            }

            program: function void () {
                a: integer = factorial(5);
                return;
            }
        """
        expect = """Program([
	FuncDecl(factorial, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(==, Id(n), IntegerLit(0)), BinExpr(==, Id(n), IntegerLit(1))), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(factorial, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(program, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, FuncCall(factorial, [IntegerLit(5)])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 349))

    def test_ast_51(self):
        input_str = """
            readInt: function void () {
                a : integer = 2 + readInteger();
            }
        """
        expect = """Program([
	FuncDecl(readInt, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, BinExpr(+, IntegerLit(2), FuncCall(readInteger, [])))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 350))

    def test_ast_52(self):
        """Plus One function"""
        input_str = """
         plusOne : function array[4] of integer (digits : array[4] of integer) {
             n = length(digits);
             for (i = n - 1, i >= 0, i - 1) {
                 if (digits[i] < 9) {
                     digits[i] = digits[i] + 1;
                     return digits;
                 }
                 digits[i] = 0;
             }
             digits = {1};
             for (i = 1, i < n, i + 1) {
                 digits[i] = 0;
             }
             return digits;
         }
         main: function void () {
             digits = {1, 2, 3};
             printInt(plusOne(digits));
         }
         """
        expect = """Program([
	FuncDecl(plusOne, ArrayType([4], IntegerType), [Param(digits, ArrayType([4], IntegerType))], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(digits)])), ForStmt(AssignStmt(Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(digits, [Id(i)]), IntegerLit(9)), BlockStmt([AssignStmt(ArrayCell(digits, [Id(i)]), BinExpr(+, ArrayCell(digits, [Id(i)]), IntegerLit(1))), ReturnStmt(Id(digits))])), AssignStmt(ArrayCell(digits, [Id(i)]), IntegerLit(0))])), AssignStmt(Id(digits), ArrayLit([IntegerLit(1)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(digits, [Id(i)]), IntegerLit(0))])), ReturnStmt(Id(digits))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(digits), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), CallStmt(printInt, FuncCall(plusOne, [Id(digits)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 351))

    def test_ast_53(self):
        input_str = """program: function void() {
            a: integer = 1;
            b: integer = 2;
            c: integer = 3;
            d: integer = 4;
            e: integer = 5;
            arr: array [5] of integer = {a, b, c, d, e};
            for (i = 0, i < 5, 1) {
                if (arr[i] % 2 == 0) {
                    print("even");
                }
                else {
                    print("odd");
                }
            }
        }"""
        expect = """Program([
	FuncDecl(program, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(2)), VarDecl(c, IntegerType, IntegerLit(3)), VarDecl(d, IntegerType, IntegerLit(4)), VarDecl(e, IntegerType, IntegerLit(5)), VarDecl(arr, ArrayType([5], IntegerType), ArrayLit([Id(a), Id(b), Id(c), Id(d), Id(e)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), IntegerLit(1), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, ArrayCell(arr, [Id(i)]), IntegerLit(2)), IntegerLit(0)), BlockStmt([CallStmt(print, StringLit(even))]), BlockStmt([CallStmt(print, StringLit(odd))]))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 352))

    def test_ast_54(self):
        input_str = """program: function void() {
            a: integer = 1;
            b: integer = 2;
            c: integer = 3;
            d: integer = 4;
            e: integer = 5;
            arr: array [5] of integer = {a, b, c, d, e};
            for (i = 0, i < 5, 1) {
                if (arr[i] % 2 == 0) {
                    print("even");
                }
                else {
                    print("odd");
                }
            }
        }"""
        expect = """Program([
	FuncDecl(program, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(2)), VarDecl(c, IntegerType, IntegerLit(3)), VarDecl(d, IntegerType, IntegerLit(4)), VarDecl(e, IntegerType, IntegerLit(5)), VarDecl(arr, ArrayType([5], IntegerType), ArrayLit([Id(a), Id(b), Id(c), Id(d), Id(e)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), IntegerLit(1), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, ArrayCell(arr, [Id(i)]), IntegerLit(2)), IntegerLit(0)), BlockStmt([CallStmt(print, StringLit(even))]), BlockStmt([CallStmt(print, StringLit(odd))]))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 353))

    def test_ast_55(self):
        input_str = """
            main: function array[1] of boolean (cd: auto, temp: string) {
            a=c[d[e[s["string"]]]];
            b=b[1,2,3];
            return b;
        }"""
        expect = """Program([
	FuncDecl(main, ArrayType([1], BooleanType), [Param(cd, AutoType), Param(temp, StringType)], None, BlockStmt([AssignStmt(Id(a), ArrayCell(c, [ArrayCell(d, [ArrayCell(e, [ArrayCell(s, [StringLit(string)])])])])), AssignStmt(Id(b), ArrayCell(b, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])), ReturnStmt(Id(b))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 354))

    def test_ast_56(self):
        """Testing variable declaration with initial values:"""
        input_str = """
            program: function void () {
                a: integer = 10;
                b: float = 3.14e-7;
                c: boolean = true;
                d , e : array[2] of integer = {1, 2}, {3, 4};
            }
        """
        expect = """Program([
	FuncDecl(program, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(10)), VarDecl(b, FloatType, FloatLit(3.14e-07)), VarDecl(c, BooleanType, BooleanLit(True)), VarDecl(d, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)])), VarDecl(e, ArrayType([2], IntegerType), ArrayLit([IntegerLit(3), IntegerLit(4)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 355))

    def test_ast_57(self):
        input_str = """
        a,b,c : array[10] of integer = {1,2,3,4*12,5,6,7,8,9,10}, {12,31} , {321+21, 321-21};
        """
        expect = """Program([
	VarDecl(a, ArrayType([10], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), BinExpr(*, IntegerLit(4), IntegerLit(12)), IntegerLit(5), IntegerLit(6), IntegerLit(7), IntegerLit(8), IntegerLit(9), IntegerLit(10)]))
	VarDecl(b, ArrayType([10], IntegerType), ArrayLit([IntegerLit(12), IntegerLit(31)]))
	VarDecl(c, ArrayType([10], IntegerType), ArrayLit([BinExpr(+, IntegerLit(321), IntegerLit(21)), BinExpr(-, IntegerLit(321), IntegerLit(21))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 356))

    def test_ast_58(self):
        input_str = """
        program: function void () {
            a: array[3] of integer = {1, 2, 3};
            b: array[2,2] of integer = {{1, 2}, {3, 4}};
            c: array[4] of float;
        }
        """
        expect = """Program([
	FuncDecl(program, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), VarDecl(b, ArrayType([2, 2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(3), IntegerLit(4)])])), VarDecl(c, ArrayType([4], FloatType))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 357))

    def test_ast_59(self):
        """Matrix"""
        input_str = """
            main : function void() {
                a : array[6,6] of integer = 
                {{1, 2, 3, 4, 5, 6},
                {7, 8, 9, 10, 11, 12},
                {13, 14, 15, 16, 17, 18},
                {19, 20, 21, 22, 23, 24},
                {25, 26, 27, 28, 29, 30},
                {31, 32, 33, 34, 35, 36}};
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([6, 6], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6)]), ArrayLit([IntegerLit(7), IntegerLit(8), IntegerLit(9), IntegerLit(10), IntegerLit(11), IntegerLit(12)]), ArrayLit([IntegerLit(13), IntegerLit(14), IntegerLit(15), IntegerLit(16), IntegerLit(17), IntegerLit(18)]), ArrayLit([IntegerLit(19), IntegerLit(20), IntegerLit(21), IntegerLit(22), IntegerLit(23), IntegerLit(24)]), ArrayLit([IntegerLit(25), IntegerLit(26), IntegerLit(27), IntegerLit(28), IntegerLit(29), IntegerLit(30)]), ArrayLit([IntegerLit(31), IntegerLit(32), IntegerLit(33), IntegerLit(34), IntegerLit(35), IntegerLit(36)])]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 358))

    def test_ast_60(self):
        input_str = """
         double : function array[5] of integer (input : array[5] of integer) {
             for (i = 0, i < 5, i + 1) {
                 input[i] = input[i] * 2;
             }
             return input;
         }
         main: function void () {
             a : array[5] of integer = {1, 2, 3, 4, 5};
             a = double(a);
             for (i = 0, i < 5, i + 1) {
                 printInt(a[i]);
             }
         }
         """
        expect = """Program([
	FuncDecl(double, ArrayType([5], IntegerType), [Param(input, ArrayType([5], IntegerType))], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(input, [Id(i)]), BinExpr(*, ArrayCell(input, [Id(i)]), IntegerLit(2)))])), ReturnStmt(Id(input))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), AssignStmt(Id(a), FuncCall(double, [Id(a)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInt, ArrayCell(a, [Id(i)]))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 359))

    def test_ast_61(self):
        input_str = """
        a : integer = -1 + 2;
        """
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(+, UnExpr(-, IntegerLit(1)), IntegerLit(2)))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 360))

    def test_ast_62(self):
        """Search insert position function"""
        input_str = """
         searchInsert : function integer (nums : array[5] of integer, target : integer) {
             for (i = 0, i < length(nums), i + 1) {
                 if (nums[i] >= target) {
                     return i;
                 }
             }
             return length(nums);
         }
         main: function void () {
             nums = {1, 3, 5, 6};
             target = 5;
             printInt(searchInsert(nums, target));
         }
         """
        expect = """Program([
	FuncDecl(searchInsert, IntegerType, [Param(nums, ArrayType([5], IntegerType)), Param(target, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(nums)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>=, ArrayCell(nums, [Id(i)]), Id(target)), BlockStmt([ReturnStmt(Id(i))]))])), ReturnStmt(FuncCall(length, [Id(nums)]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(nums), ArrayLit([IntegerLit(1), IntegerLit(3), IntegerLit(5), IntegerLit(6)])), AssignStmt(Id(target), IntegerLit(5)), CallStmt(printInt, FuncCall(searchInsert, [Id(nums), Id(target)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 361))

    def test_ast_63(self):
        """Remove duplicates function"""
        input_str = """
         removeDuplicates : function integer (nums : array[5] of integer) {
             if (length(nums) == 0) {
                 return 0;
             }
             i = 0;
             for (j = 1, j < length(nums), j + 1) {
                 if (nums[j] != nums[i]) {
                     i = i + 1;
                     nums[i] = nums[j];
                 }
             }
             return i + 1;
         }
         main: function void () {
             nums = {1, 1, 2};
             printInt(removeDuplicates(nums));
         }
         """
        expect = """Program([
	FuncDecl(removeDuplicates, IntegerType, [Param(nums, ArrayType([5], IntegerType))], None, BlockStmt([IfStmt(BinExpr(==, FuncCall(length, [Id(nums)]), IntegerLit(0)), BlockStmt([ReturnStmt(IntegerLit(0))])), AssignStmt(Id(i), IntegerLit(0)), ForStmt(AssignStmt(Id(j), IntegerLit(1)), BinExpr(<, Id(j), FuncCall(length, [Id(nums)])), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(nums, [Id(j)]), ArrayCell(nums, [Id(i)])), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), AssignStmt(ArrayCell(nums, [Id(i)]), ArrayCell(nums, [Id(j)]))]))])), ReturnStmt(BinExpr(+, Id(i), IntegerLit(1)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(nums), ArrayLit([IntegerLit(1), IntegerLit(1), IntegerLit(2)])), CallStmt(printInt, FuncCall(removeDuplicates, [Id(nums)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 362))

    def test_ast_64(self):
        input_str = """
                main: function integer() {
            arr: array[5] of integer = {3, 7, 9, 2, 4};
            target: integer = 9;
            n: integer = 5;
            found: boolean = false;
            index: integer = -1;
            for (i = 0, i < n, i + 1) {
                if (arr[i] == target) {
                    found = true;
                    index = i;
                    break;
                }
            }
            if (found) {
                return index;
            }
            else {
                return -1;
            }
        }
        """
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(arr, ArrayType([5], IntegerType), ArrayLit([IntegerLit(3), IntegerLit(7), IntegerLit(9), IntegerLit(2), IntegerLit(4)])), VarDecl(target, IntegerType, IntegerLit(9)), VarDecl(n, IntegerType, IntegerLit(5)), VarDecl(found, BooleanType, BooleanLit(False)), VarDecl(index, IntegerType, UnExpr(-, IntegerLit(1))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(arr, [Id(i)]), Id(target)), BlockStmt([AssignStmt(Id(found), BooleanLit(True)), AssignStmt(Id(index), Id(i)), BreakStmt()]))])), IfStmt(Id(found), BlockStmt([ReturnStmt(Id(index))]), BlockStmt([ReturnStmt(UnExpr(-, IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 363))

    def test_ast_65(self):
        """Sort Colors function"""
        input_str = """
         sortColors : function void (nums : array[4] of integer) {
             red = 0;
             white = 0;
             blue = 0;
             for (i = 0, i < length(nums), i + 1) {
                 if (nums[i] == 0) {
                     red = red + 1;
                 } else if (nums[i] == 1) {
                     white = white + 1;
                 } else {
                     blue = blue + 1;
                 }
             }
             for (i = 0, i < red, i + 1) {
                 nums[i] = 0;
             }
             for (i = red, i < red + white, i + 1) {
                 nums[i] = 1;
             }
             for (i = red + white, i < length(nums), i + 1) {
                 nums[i] = 2;
             }
         }
         main: function void () {
             nums = {2, 0, 2, 1, 1, 0};
             sortColors(nums);
             printInt(nums);
         }
        """
        expect = """Program([
	FuncDecl(sortColors, VoidType, [Param(nums, ArrayType([4], IntegerType))], None, BlockStmt([AssignStmt(Id(red), IntegerLit(0)), AssignStmt(Id(white), IntegerLit(0)), AssignStmt(Id(blue), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(nums)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(nums, [Id(i)]), IntegerLit(0)), BlockStmt([AssignStmt(Id(red), BinExpr(+, Id(red), IntegerLit(1)))]), IfStmt(BinExpr(==, ArrayCell(nums, [Id(i)]), IntegerLit(1)), BlockStmt([AssignStmt(Id(white), BinExpr(+, Id(white), IntegerLit(1)))]), BlockStmt([AssignStmt(Id(blue), BinExpr(+, Id(blue), IntegerLit(1)))])))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(red)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(nums, [Id(i)]), IntegerLit(0))])), ForStmt(AssignStmt(Id(i), Id(red)), BinExpr(<, Id(i), BinExpr(+, Id(red), Id(white))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(nums, [Id(i)]), IntegerLit(1))])), ForStmt(AssignStmt(Id(i), BinExpr(+, Id(red), Id(white))), BinExpr(<, Id(i), FuncCall(length, [Id(nums)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(nums, [Id(i)]), IntegerLit(2))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(nums), ArrayLit([IntegerLit(2), IntegerLit(0), IntegerLit(2), IntegerLit(1), IntegerLit(1), IntegerLit(0)])), CallStmt(sortColors, Id(nums)), CallStmt(printInt, Id(nums))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 364))

    def test_ast_66(self):
        """Climate Change function"""
        input_str = """
         climateChange : function void (arr : array[4] of integer) {
             n = length(arr);
             for (i = 0, i < n - 1, i + 1) {
                 for (j = 0, j < n - i - 1, j + 1) {
                     if (arr[j] > arr[j + 1]) {
                         temp = arr[j];
                         arr[j] = arr[j + 1];
                         arr[j + 1] = temp;
                     }
                 }
             }
         }
         main: function void () {
             arr = {64, 34, 25, 12, 22, 11, 90};
             climateChange(arr);
             printInt(arr);
         }
         """
        expect = """Program([
	FuncDecl(climateChange, VoidType, [Param(arr, ArrayType([4], IntegerType))], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(arr)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), BinExpr(-, BinExpr(-, Id(n), Id(i)), IntegerLit(1))), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(arr, [Id(j)]), ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))])), BlockStmt([AssignStmt(Id(temp), ArrayCell(arr, [Id(j)])), AssignStmt(ArrayCell(arr, [Id(j)]), ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))])), AssignStmt(ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))]), Id(temp))]))]))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(arr), ArrayLit([IntegerLit(64), IntegerLit(34), IntegerLit(25), IntegerLit(12), IntegerLit(22), IntegerLit(11), IntegerLit(90)])), CallStmt(climateChange, Id(arr)), CallStmt(printInt, Id(arr))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 365))

    def test_ast_67(self):
        """Coin Change function"""
        input_str = """
         coinChange : function integer (coins : array[4] of integer, amount : integer) {
             if (amount == 0) {
                 return 0;
             }
             if (amount < 0) {
                 return -1;
             }
             min = 999999999;
             for (i = 0, i < length(coins), i + 1) {
                 res = coinChange(coins, amount - coins[i]);
                 if ((res != -1) && (res < min)) {
                     min = res + 1;
                 }
             }
             if (min == 999999999) {
                 return -1;
             } else {
                 return min;
             }
         }
         main: function void () {
             coins = {1, 2, 5};
             amount = 11;
             printInt(coinChange(coins, amount));
         }
         """
        expect = """Program([
	FuncDecl(coinChange, IntegerType, [Param(coins, ArrayType([4], IntegerType)), Param(amount, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(amount), IntegerLit(0)), BlockStmt([ReturnStmt(IntegerLit(0))])), IfStmt(BinExpr(<, Id(amount), IntegerLit(0)), BlockStmt([ReturnStmt(UnExpr(-, IntegerLit(1)))])), AssignStmt(Id(min), IntegerLit(999999999)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(coins)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(res), FuncCall(coinChange, [Id(coins), BinExpr(-, Id(amount), ArrayCell(coins, [Id(i)]))])), IfStmt(BinExpr(&&, BinExpr(!=, Id(res), UnExpr(-, IntegerLit(1))), BinExpr(<, Id(res), Id(min))), BlockStmt([AssignStmt(Id(min), BinExpr(+, Id(res), IntegerLit(1)))]))])), IfStmt(BinExpr(==, Id(min), IntegerLit(999999999)), BlockStmt([ReturnStmt(UnExpr(-, IntegerLit(1)))]), BlockStmt([ReturnStmt(Id(min))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(coins), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(5)])), AssignStmt(Id(amount), IntegerLit(11)), CallStmt(printInt, FuncCall(coinChange, [Id(coins), Id(amount)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 366))

    def test_ast_68(self):
        """Coin Change 2 function"""
        input_str = """
         change : function integer (amount : integer, coins : array[4] of integer) {
             dp : array[5] of integer;
             dp[0] = 1;
             for (i = 0, i < length(coins), i + 1) {
                 for (j = coins[i], j <= amount, j + 1) {
                     dp[j] = dp[j] + dp[j - coins[i]];
                 }
             }
             return dp[amount];
         }
         main: function void () {
             amount = 5;
             coins = {1, 2, 5};
             printInt(change(amount, coins));
         }
         """
        expect = """Program([
	FuncDecl(change, IntegerType, [Param(amount, IntegerType), Param(coins, ArrayType([4], IntegerType))], None, BlockStmt([VarDecl(dp, ArrayType([5], IntegerType)), AssignStmt(ArrayCell(dp, [IntegerLit(0)]), IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(coins)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), ArrayCell(coins, [Id(i)])), BinExpr(<=, Id(j), Id(amount)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(dp, [Id(j)]), BinExpr(+, ArrayCell(dp, [Id(j)]), ArrayCell(dp, [BinExpr(-, Id(j), ArrayCell(coins, [Id(i)]))])))]))])), ReturnStmt(ArrayCell(dp, [Id(amount)]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(amount), IntegerLit(5)), AssignStmt(Id(coins), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(5)])), CallStmt(printInt, FuncCall(change, [Id(amount), Id(coins)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 367))

    def test_ast_69(self):
        """Find Peak Element function"""
        input_str = """
         findPeakElement : function integer (nums : array[6] of integer) {
             n = length(nums);
             if (n == 1) {
                 return 0;
             }
             if (nums[0] > nums[1]) {
                 return 0;
             }
             if (nums[n - 1] > nums[n - 2]) {
                 return n - 1;
             }
             for (i = 1, i < n - 1, i + 1) {
                 if ((nums[i] > nums[i - 1]) && (nums[i] > nums[i + 1])) {
                     return i;
                 }
             }
             return -1;
         }
         main: function void () {
             nums = {1, 2, 3, 1};
             printInt(findPeakElement(nums));
         }
         """
        expect = """Program([
	FuncDecl(findPeakElement, IntegerType, [Param(nums, ArrayType([6], IntegerType))], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(nums)])), IfStmt(BinExpr(==, Id(n), IntegerLit(1)), BlockStmt([ReturnStmt(IntegerLit(0))])), IfStmt(BinExpr(>, ArrayCell(nums, [IntegerLit(0)]), ArrayCell(nums, [IntegerLit(1)])), BlockStmt([ReturnStmt(IntegerLit(0))])), IfStmt(BinExpr(>, ArrayCell(nums, [BinExpr(-, Id(n), IntegerLit(1))]), ArrayCell(nums, [BinExpr(-, Id(n), IntegerLit(2))])), BlockStmt([ReturnStmt(BinExpr(-, Id(n), IntegerLit(1)))])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(&&, BinExpr(>, ArrayCell(nums, [Id(i)]), ArrayCell(nums, [BinExpr(-, Id(i), IntegerLit(1))])), BinExpr(>, ArrayCell(nums, [Id(i)]), ArrayCell(nums, [BinExpr(+, Id(i), IntegerLit(1))]))), BlockStmt([ReturnStmt(Id(i))]))])), ReturnStmt(UnExpr(-, IntegerLit(1)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(nums), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(1)])), CallStmt(printInt, FuncCall(findPeakElement, [Id(nums)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 368))

    def test_ast_70(self):
        input_str = """
         rotate : function void (nums : array[7] of integer, k : integer) {
             n = length(nums);
             k = k % n;
             if (k == 0) {
                 return;
             }
             reverse(nums, 0, n - 1);
             reverse(nums, 0, k - 1);
             reverse(nums, k, n - 1);
         }
         main: function void () {
             nums = {1, 2, 3, 4, 5, 6, 7};
             k = 3;
             rotate(nums, k);
             printInt(nums);
         }
         """
        expect = """Program([
	FuncDecl(rotate, VoidType, [Param(nums, ArrayType([7], IntegerType)), Param(k, IntegerType)], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(nums)])), AssignStmt(Id(k), BinExpr(%, Id(k), Id(n))), IfStmt(BinExpr(==, Id(k), IntegerLit(0)), BlockStmt([ReturnStmt()])), CallStmt(reverse, Id(nums), IntegerLit(0), BinExpr(-, Id(n), IntegerLit(1))), CallStmt(reverse, Id(nums), IntegerLit(0), BinExpr(-, Id(k), IntegerLit(1))), CallStmt(reverse, Id(nums), Id(k), BinExpr(-, Id(n), IntegerLit(1)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(nums), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7)])), AssignStmt(Id(k), IntegerLit(3)), CallStmt(rotate, Id(nums), Id(k)), CallStmt(printInt, Id(nums))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 369))

    def test_ast_71(self):
        input_str = """
         majorityElement : function integer (nums : array[7] of integer) {
             n = length(nums);
             count = 0;
             for (i = 0, i < n, i + 1) {
                 if (count == 0) {
                     candidate = nums[i];
                 }
                 if (nums[i] == candidate) {
                     count = count + 1;
                 } else {
                     count = count - 1;
                 }
             }
             return candidate;
         }
         main: function void () {
             nums = {2, 2, 1, 1, 1, 2, 2};
             printInt(majorityElement(nums));
         }
         """
        expect = """Program([
	FuncDecl(majorityElement, IntegerType, [Param(nums, ArrayType([7], IntegerType))], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(nums)])), AssignStmt(Id(count), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(count), IntegerLit(0)), BlockStmt([AssignStmt(Id(candidate), ArrayCell(nums, [Id(i)]))])), IfStmt(BinExpr(==, ArrayCell(nums, [Id(i)]), Id(candidate)), BlockStmt([AssignStmt(Id(count), BinExpr(+, Id(count), IntegerLit(1)))]), BlockStmt([AssignStmt(Id(count), BinExpr(-, Id(count), IntegerLit(1)))]))])), ReturnStmt(Id(candidate))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(nums), ArrayLit([IntegerLit(2), IntegerLit(2), IntegerLit(1), IntegerLit(1), IntegerLit(1), IntegerLit(2), IntegerLit(2)])), CallStmt(printInt, FuncCall(majorityElement, [Id(nums)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 370))

    def test_ast_72(self):
        """Contains Duplicate function"""
        input_str = """
         containsDuplicate : function boolean (nums : array[5] of integer) {
             n = length(nums);
             for (i = 0, i < n, i + 1) {
                 for (j = i + 1, j < n, j + 1) {
                     if (nums[i] == nums[j]) {
                         return true;
                     }
                 }
             }
             return false;
         }
         main: function void () {
             nums = {1, 2, 3, 1};
             printBool(containsDuplicate(nums));
         }
         """
        expect = """Program([
	FuncDecl(containsDuplicate, BooleanType, [Param(nums, ArrayType([5], IntegerType))], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(nums)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), BinExpr(+, Id(i), IntegerLit(1))), BinExpr(<, Id(j), Id(n)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(nums, [Id(i)]), ArrayCell(nums, [Id(j)])), BlockStmt([ReturnStmt(BooleanLit(True))]))]))])), ReturnStmt(BooleanLit(False))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(nums), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(1)])), CallStmt(printBool, FuncCall(containsDuplicate, [Id(nums)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 371))

    def test_ast_73(self):
        """Two Sum function"""
        input_str = """
         twoSum : function array[2] of integer (nums : array[4] of integer, target : integer) {
             n = length(nums);
             for (i = 0, i < n, i + 1) {
                 for (j = i + 1, j < n, j + 1) {
                     if (nums[i] + nums[j] == target) {
                         return {i, j};
                     }
                 }
             }
             return {-1, -1};
         }
         main: function void () {
             nums = {2, 7, 11, 15};
             target = 9;
             printInt(twoSum(nums, target));
         }
         """
        expect = """Program([
	FuncDecl(twoSum, ArrayType([2], IntegerType), [Param(nums, ArrayType([4], IntegerType)), Param(target, IntegerType)], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(nums)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), BinExpr(+, Id(i), IntegerLit(1))), BinExpr(<, Id(j), Id(n)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(+, ArrayCell(nums, [Id(i)]), ArrayCell(nums, [Id(j)])), Id(target)), BlockStmt([ReturnStmt(ArrayLit([Id(i), Id(j)]))]))]))])), ReturnStmt(ArrayLit([UnExpr(-, IntegerLit(1)), UnExpr(-, IntegerLit(1))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(nums), ArrayLit([IntegerLit(2), IntegerLit(7), IntegerLit(11), IntegerLit(15)])), AssignStmt(Id(target), IntegerLit(9)), CallStmt(printInt, FuncCall(twoSum, [Id(nums), Id(target)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 372))

    def test_ast_74(self):
        """Missing Number function"""
        input_str = """
         missingNumber : function integer (nums : array[4] of integer) {
             n = length(nums);
             sum = 0;
             for (i = 0, i < n, i + 1) {
                 sum = sum + nums[i];
             }
             return (n * (n + 1)) / 2 - sum;
         }
         main: function void () {
             nums = {3, 0, 1};
             printInt(missingNumber(nums));
         }
         """
        expect = """Program([
	FuncDecl(missingNumber, IntegerType, [Param(nums, ArrayType([4], IntegerType))], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(nums)])), AssignStmt(Id(sum), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(nums, [Id(i)])))])), ReturnStmt(BinExpr(-, BinExpr(/, BinExpr(*, Id(n), BinExpr(+, Id(n), IntegerLit(1))), IntegerLit(2)), Id(sum)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(nums), ArrayLit([IntegerLit(3), IntegerLit(0), IntegerLit(1)])), CallStmt(printInt, FuncCall(missingNumber, [Id(nums)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 373))

    def test_ast_75(self):
        """Intersection of Two Arrays II function"""
        input_str = """
         intersect : function array[2] of integer (nums1 : array[4] of integer, nums2 : array[2] of integer) {
             n1 = length(nums1);
             n2 = length(nums2);
             result : array [2] of integer= {};
             for (i = 0, i < n1, i + 1) {
                 for (j = 0, j < n2, j + 1) {
                     if (nums1[i] == nums2[j]) {
                         result = append(result, nums1[i]);
                         nums2[j] = -1;
                         break;
                     }
                 }
             }
             return result;
         }
         main: function void () {
             nums1 = {1, 2, 2, 1};
             nums2 = {2, 2};
             printInt(intersect(nums1, nums2));
         }
         """
        expect = """Program([
	FuncDecl(intersect, ArrayType([2], IntegerType), [Param(nums1, ArrayType([4], IntegerType)), Param(nums2, ArrayType([2], IntegerType))], None, BlockStmt([AssignStmt(Id(n1), FuncCall(length, [Id(nums1)])), AssignStmt(Id(n2), FuncCall(length, [Id(nums2)])), VarDecl(result, ArrayType([2], IntegerType), ArrayLit([])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n1)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(n2)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(nums1, [Id(i)]), ArrayCell(nums2, [Id(j)])), BlockStmt([AssignStmt(Id(result), FuncCall(append, [Id(result), ArrayCell(nums1, [Id(i)])])), AssignStmt(ArrayCell(nums2, [Id(j)]), UnExpr(-, IntegerLit(1))), BreakStmt()]))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(nums1), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(2), IntegerLit(1)])), AssignStmt(Id(nums2), ArrayLit([IntegerLit(2), IntegerLit(2)])), CallStmt(printInt, FuncCall(intersect, [Id(nums1), Id(nums2)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 374))

    def test_ast_76(self):
        """Find All Numbers Disappeared in an Array function"""
        input_str = """
         findDisappearedNumbers : function array[2] of integer (nums : array[4] of integer) {
             n = length(nums);
             result : array [2] of integer= {};
             for (i = 0, i < n, i + 1) {
                 index = abs(nums[i]) - 1;
                 if (nums[index] > 0) {
                     nums[index] = -nums[index];
                 }
             }
             for (i = 0, i < n, i + 1) {
                 if (nums[i] > 0) {
                     result = append(result, i + 1);
                 }
             }
             return result;
         }
         main: function void () {
             nums = {4, 3, 2, 7, 8, 2, 3, 1};
             printInt(findDisappearedNumbers(nums));
         }
         """
        expect = """Program([
	FuncDecl(findDisappearedNumbers, ArrayType([2], IntegerType), [Param(nums, ArrayType([4], IntegerType))], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(nums)])), VarDecl(result, ArrayType([2], IntegerType), ArrayLit([])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(index), BinExpr(-, FuncCall(abs, [ArrayCell(nums, [Id(i)])]), IntegerLit(1))), IfStmt(BinExpr(>, ArrayCell(nums, [Id(index)]), IntegerLit(0)), BlockStmt([AssignStmt(ArrayCell(nums, [Id(index)]), UnExpr(-, ArrayCell(nums, [Id(index)])))]))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(nums, [Id(i)]), IntegerLit(0)), BlockStmt([AssignStmt(Id(result), FuncCall(append, [Id(result), BinExpr(+, Id(i), IntegerLit(1))]))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(nums), ArrayLit([IntegerLit(4), IntegerLit(3), IntegerLit(2), IntegerLit(7), IntegerLit(8), IntegerLit(2), IntegerLit(3), IntegerLit(1)])), CallStmt(printInt, FuncCall(findDisappearedNumbers, [Id(nums)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 375))

    def test_ast_77(self):
        """Find All Duplicates in an Array function"""
        input_str = """
         findDuplicates : function array[2] of integer (nums : array[8] of integer) {
             n = length(nums);
             result : array [2] of integer= {};
             for (i = 0, i < n, i + 1) {
                 index = abs(nums[i]) - 1;
                 if (nums[index] < 0) {
                     result = append(result, abs(nums[i]));
                 }
                 nums[index] = -nums[index];
             }
             return result;
         }
         main: function void () {
             nums = {4, 3, 2, 7, 8, 2, 3, 1};
             printInt(findDuplicates(nums));
         }
         """
        expect = """Program([
	FuncDecl(findDuplicates, ArrayType([2], IntegerType), [Param(nums, ArrayType([8], IntegerType))], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(nums)])), VarDecl(result, ArrayType([2], IntegerType), ArrayLit([])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(index), BinExpr(-, FuncCall(abs, [ArrayCell(nums, [Id(i)])]), IntegerLit(1))), IfStmt(BinExpr(<, ArrayCell(nums, [Id(index)]), IntegerLit(0)), BlockStmt([AssignStmt(Id(result), FuncCall(append, [Id(result), FuncCall(abs, [ArrayCell(nums, [Id(i)])])]))])), AssignStmt(ArrayCell(nums, [Id(index)]), UnExpr(-, ArrayCell(nums, [Id(index)])))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(nums), ArrayLit([IntegerLit(4), IntegerLit(3), IntegerLit(2), IntegerLit(7), IntegerLit(8), IntegerLit(2), IntegerLit(3), IntegerLit(1)])), CallStmt(printInt, FuncCall(findDuplicates, [Id(nums)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 376))

    def test_ast_78(self):
        """Find the Duplicate Number function"""
        input_str = """
         findDuplicate : function integer (nums : array[5] of integer) {
             n = length(nums);
             slow = nums[0];
             fast = nums[nums[0]];
             while (slow != fast) {
                 slow = nums[slow];
                 fast = nums[nums[fast]];
             }
             fast = 0;
             while (slow != fast) {
                 slow = nums[slow];
                 fast = nums[fast];
             }
             return slow;
         }
         main: function void () {
             nums = {1, 3, 4, 2, 2};
             printInt(findDuplicate(nums));
         }
         """
        expect = """Program([
	FuncDecl(findDuplicate, IntegerType, [Param(nums, ArrayType([5], IntegerType))], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(nums)])), AssignStmt(Id(slow), ArrayCell(nums, [IntegerLit(0)])), AssignStmt(Id(fast), ArrayCell(nums, [ArrayCell(nums, [IntegerLit(0)])])), WhileStmt(BinExpr(!=, Id(slow), Id(fast)), BlockStmt([AssignStmt(Id(slow), ArrayCell(nums, [Id(slow)])), AssignStmt(Id(fast), ArrayCell(nums, [ArrayCell(nums, [Id(fast)])]))])), AssignStmt(Id(fast), IntegerLit(0)), WhileStmt(BinExpr(!=, Id(slow), Id(fast)), BlockStmt([AssignStmt(Id(slow), ArrayCell(nums, [Id(slow)])), AssignStmt(Id(fast), ArrayCell(nums, [Id(fast)]))])), ReturnStmt(Id(slow))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(nums), ArrayLit([IntegerLit(1), IntegerLit(3), IntegerLit(4), IntegerLit(2), IntegerLit(2)])), CallStmt(printInt, FuncCall(findDuplicate, [Id(nums)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 377))

    def test_ast_79(self):
        """3 Sum function"""
        input_str = """
         threeSum : function array[2] of integer (nums : array[6] of integer) {
             n = length(nums);
             sort(nums);
             result : array [2] of integer= {};
             for (i = 0, i < n, i + 1) {
                 if ((i > 0) && (nums[i] == nums[i - 1])) {
                     continue;
                 }
                 target : integer = -nums[i];
                 left : integer = i + 1;
                 right : integer = n - 1;
                 while (left < right) {
                     if ((nums[left] + nums[right]) == target) {
                         result = append(result, {nums[i], nums[left], nums[right]});
                         left = left + 1;
                         while ((left < right) && (nums[left] == nums[left - 1])) {
                             left = left + 1;
                         }
                         right = right - 1;
                         while ((left < right) && (nums[right] == nums[right + 1])) {
                             right = right - 1;
                         }
                     } else {
                         if ((nums[left] + nums[right]) < target) {
                             left = left + 1;
                         } else {
                             right = right - 1;
                         }
                     }
                 }
             }
             return result;
         }
         main: function void () {
             nums = {-1, 0, 1, 2, -1, -4};
             printInt(threeSum(nums));
         }
         """
        expect = """Program([
	FuncDecl(threeSum, ArrayType([2], IntegerType), [Param(nums, ArrayType([6], IntegerType))], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(nums)])), CallStmt(sort, Id(nums)), VarDecl(result, ArrayType([2], IntegerType), ArrayLit([])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(&&, BinExpr(>, Id(i), IntegerLit(0)), BinExpr(==, ArrayCell(nums, [Id(i)]), ArrayCell(nums, [BinExpr(-, Id(i), IntegerLit(1))]))), BlockStmt([ContinueStmt()])), VarDecl(target, IntegerType, UnExpr(-, ArrayCell(nums, [Id(i)]))), VarDecl(left, IntegerType, BinExpr(+, Id(i), IntegerLit(1))), VarDecl(right, IntegerType, BinExpr(-, Id(n), IntegerLit(1))), WhileStmt(BinExpr(<, Id(left), Id(right)), BlockStmt([IfStmt(BinExpr(==, BinExpr(+, ArrayCell(nums, [Id(left)]), ArrayCell(nums, [Id(right)])), Id(target)), BlockStmt([AssignStmt(Id(result), FuncCall(append, [Id(result), ArrayLit([ArrayCell(nums, [Id(i)]), ArrayCell(nums, [Id(left)]), ArrayCell(nums, [Id(right)])])])), AssignStmt(Id(left), BinExpr(+, Id(left), IntegerLit(1))), WhileStmt(BinExpr(&&, BinExpr(<, Id(left), Id(right)), BinExpr(==, ArrayCell(nums, [Id(left)]), ArrayCell(nums, [BinExpr(-, Id(left), IntegerLit(1))]))), BlockStmt([AssignStmt(Id(left), BinExpr(+, Id(left), IntegerLit(1)))])), AssignStmt(Id(right), BinExpr(-, Id(right), IntegerLit(1))), WhileStmt(BinExpr(&&, BinExpr(<, Id(left), Id(right)), BinExpr(==, ArrayCell(nums, [Id(right)]), ArrayCell(nums, [BinExpr(+, Id(right), IntegerLit(1))]))), BlockStmt([AssignStmt(Id(right), BinExpr(-, Id(right), IntegerLit(1)))]))]), BlockStmt([IfStmt(BinExpr(<, BinExpr(+, ArrayCell(nums, [Id(left)]), ArrayCell(nums, [Id(right)])), Id(target)), BlockStmt([AssignStmt(Id(left), BinExpr(+, Id(left), IntegerLit(1)))]), BlockStmt([AssignStmt(Id(right), BinExpr(-, Id(right), IntegerLit(1)))]))]))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(nums), ArrayLit([UnExpr(-, IntegerLit(1)), IntegerLit(0), IntegerLit(1), IntegerLit(2), UnExpr(-, IntegerLit(1)), UnExpr(-, IntegerLit(4))])), CallStmt(printInt, FuncCall(threeSum, [Id(nums)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 378))

    def test_ast_80(self):
        """Reverse Words in a String function"""
        input_str = """
         reverseWords : function string (s : string) {
             n : integer = length(s);
             result : integer = "";
             i : integer = 0;
             while (i < n) {
                 while ((i < n) && (s[i] == " ")) {
                     i = i + 1;
                 }
                 if (i >= n) {
                     break;
                 }
                 start = i;
                 while ((i < n) && (s[i] != " ")) {
                     i = i + 1;
                 }
                 sub = substring(s, start, i - start);
                 if (result == "") {
                     result = sub;
                 } else {
                     result = sub + " " + result;
                 }
             }
             return result;
         }
         main: function void () {
             s = "the sky is blue";
             printString(reverseWords(s));
         }
         """
        expect = """Program([
	FuncDecl(reverseWords, StringType, [Param(s, StringType)], None, BlockStmt([VarDecl(n, IntegerType, FuncCall(length, [Id(s)])), VarDecl(result, IntegerType, StringLit()), VarDecl(i, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(<, Id(i), Id(n)), BlockStmt([WhileStmt(BinExpr(&&, BinExpr(<, Id(i), Id(n)), BinExpr(==, ArrayCell(s, [Id(i)]), StringLit( ))), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), IfStmt(BinExpr(>=, Id(i), Id(n)), BlockStmt([BreakStmt()])), AssignStmt(Id(start), Id(i)), WhileStmt(BinExpr(&&, BinExpr(<, Id(i), Id(n)), BinExpr(!=, ArrayCell(s, [Id(i)]), StringLit( ))), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), AssignStmt(Id(sub), FuncCall(substring, [Id(s), Id(start), BinExpr(-, Id(i), Id(start))])), IfStmt(BinExpr(==, Id(result), StringLit()), BlockStmt([AssignStmt(Id(result), Id(sub))]), BlockStmt([AssignStmt(Id(result), BinExpr(+, BinExpr(+, Id(sub), StringLit( )), Id(result)))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(the sky is blue)), CallStmt(printString, FuncCall(reverseWords, [Id(s)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 379))

    def test_ast_81(self):
        """Move Zeroes function"""
        input_str = """
         moveZeroes : function void (nums : array[5] of integer) {
             n = length(nums);
             lastNonZeroFoundAt = 0;
             for (i = 0, i < n, i + 1) {
                 if (nums[i] != 0) {
                     nums[lastNonZeroFoundAt] = nums[i];
                     lastNonZeroFoundAt = lastNonZeroFoundAt + 1;
                 }
             }
             for (i = lastNonZeroFoundAt, i < n, i + 1) {
                 nums[i] = 0;
             }
         }
         main: function void () {
             nums = {0, 1, 0, 3, 12};
             moveZeroes(nums);
             printInt(nums);
         }
         """
        expect = """Program([
	FuncDecl(moveZeroes, VoidType, [Param(nums, ArrayType([5], IntegerType))], None, BlockStmt([AssignStmt(Id(n), FuncCall(length, [Id(nums)])), AssignStmt(Id(lastNonZeroFoundAt), IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(nums, [Id(i)]), IntegerLit(0)), BlockStmt([AssignStmt(ArrayCell(nums, [Id(lastNonZeroFoundAt)]), ArrayCell(nums, [Id(i)])), AssignStmt(Id(lastNonZeroFoundAt), BinExpr(+, Id(lastNonZeroFoundAt), IntegerLit(1)))]))])), ForStmt(AssignStmt(Id(i), Id(lastNonZeroFoundAt)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(nums, [Id(i)]), IntegerLit(0))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(nums), ArrayLit([IntegerLit(0), IntegerLit(1), IntegerLit(0), IntegerLit(3), IntegerLit(12)])), CallStmt(moveZeroes, Id(nums)), CallStmt(printInt, Id(nums))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 380))

    def test_ast_82(self):
        """islandPerimeter function"""
        input_str = """
         islandPerimeter : function integer (grid : array[4,4] of integer) {
             n : integer = length(grid);
             m : integer = length(grid[0]);
             result : integer = 0;
             for (i = 0, i < n, i + 1) {
                 for (j = 0, j < m, j + 1) {
                     if (grid[i,j] == 1) {
                         result = result + 4;
                         if ((i > 0) && (grid[i - 1,j] == 1)) {
                             result = result - 2;
                         }
                         if ((j > 0) && (grid[i,j - 1] == 1)) {
                             result = result - 2;
                         }
                     }
                 }
             }
             return result;
         }
         main: function void () {
             grid : array [4,4] of integer = {{0, 1, 0, 0},
                     {1, 1, 1, 0},
                     {0, 1, 0, 0},
                     {1, 1, 0, 0}};
             printInt(islandPerimeter(grid));
         }
         """
        expect = """Program([
	FuncDecl(islandPerimeter, IntegerType, [Param(grid, ArrayType([4, 4], IntegerType))], None, BlockStmt([VarDecl(n, IntegerType, FuncCall(length, [Id(grid)])), VarDecl(m, IntegerType, FuncCall(length, [ArrayCell(grid, [IntegerLit(0)])])), VarDecl(result, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(m)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(grid, [Id(i), Id(j)]), IntegerLit(1)), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), IntegerLit(4))), IfStmt(BinExpr(&&, BinExpr(>, Id(i), IntegerLit(0)), BinExpr(==, ArrayCell(grid, [BinExpr(-, Id(i), IntegerLit(1)), Id(j)]), IntegerLit(1))), BlockStmt([AssignStmt(Id(result), BinExpr(-, Id(result), IntegerLit(2)))])), IfStmt(BinExpr(&&, BinExpr(>, Id(j), IntegerLit(0)), BinExpr(==, ArrayCell(grid, [Id(i), BinExpr(-, Id(j), IntegerLit(1))]), IntegerLit(1))), BlockStmt([AssignStmt(Id(result), BinExpr(-, Id(result), IntegerLit(2)))]))]))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(grid, ArrayType([4, 4], IntegerType), ArrayLit([ArrayLit([IntegerLit(0), IntegerLit(1), IntegerLit(0), IntegerLit(0)]), ArrayLit([IntegerLit(1), IntegerLit(1), IntegerLit(1), IntegerLit(0)]), ArrayLit([IntegerLit(0), IntegerLit(1), IntegerLit(0), IntegerLit(0)]), ArrayLit([IntegerLit(1), IntegerLit(1), IntegerLit(0), IntegerLit(0)])])), CallStmt(printInt, FuncCall(islandPerimeter, [Id(grid)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 381))

    def test_ast_83(self):
        """Median of Two Sorted Arrays function"""
        input_str = """
         findMedianSortedArrays : function float (nums1 : array[5] of integer, nums2 : array[5] of integer) {
             n1 : integer = length(nums1);
             n2 : integer = length(nums2);
             if (n1 > n2) {
                 return findMedianSortedArrays(nums2, nums1);
             }
             k : integer = (n1 + n2 + 1) / 2;
             l : integer = 0;
             r : integer = n1;
             while (l < r) {
                 m1 : integer = l + (r - l) / 2;
                 m2 : integer = k - m1;
                 if (nums1[m1] < nums2[m2 - 1]) {
                     l = m1 + 1;
                 } else {
                     r = m1;
                 }
             }
         }
         main: function void () {
             nums1 : array [5] of integer = {1, 3};
             nums2 : array [5] of integer = {2};
             printFloat(findMedianSortedArrays(nums1, nums2));
         }
         """
        expect = """Program([
	FuncDecl(findMedianSortedArrays, FloatType, [Param(nums1, ArrayType([5], IntegerType)), Param(nums2, ArrayType([5], IntegerType))], None, BlockStmt([VarDecl(n1, IntegerType, FuncCall(length, [Id(nums1)])), VarDecl(n2, IntegerType, FuncCall(length, [Id(nums2)])), IfStmt(BinExpr(>, Id(n1), Id(n2)), BlockStmt([ReturnStmt(FuncCall(findMedianSortedArrays, [Id(nums2), Id(nums1)]))])), VarDecl(k, IntegerType, BinExpr(/, BinExpr(+, BinExpr(+, Id(n1), Id(n2)), IntegerLit(1)), IntegerLit(2))), VarDecl(l, IntegerType, IntegerLit(0)), VarDecl(r, IntegerType, Id(n1)), WhileStmt(BinExpr(<, Id(l), Id(r)), BlockStmt([VarDecl(m1, IntegerType, BinExpr(+, Id(l), BinExpr(/, BinExpr(-, Id(r), Id(l)), IntegerLit(2)))), VarDecl(m2, IntegerType, BinExpr(-, Id(k), Id(m1))), IfStmt(BinExpr(<, ArrayCell(nums1, [Id(m1)]), ArrayCell(nums2, [BinExpr(-, Id(m2), IntegerLit(1))])), BlockStmt([AssignStmt(Id(l), BinExpr(+, Id(m1), IntegerLit(1)))]), BlockStmt([AssignStmt(Id(r), Id(m1))]))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(nums1, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(3)])), VarDecl(nums2, ArrayType([5], IntegerType), ArrayLit([IntegerLit(2)])), CallStmt(printFloat, FuncCall(findMedianSortedArrays, [Id(nums1), Id(nums2)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 382))

    def test_ast_84(self):
        """Flatten array function"""
        input_str = """
         flatten : function array[10] of integer (arr : array[10] of integer) {
             result : array[10] of integer;
             for (i = 0, i < length(arr), i + 1) {
                 if (typeof(arr[i]) == "array") {
                     result = result + flatten(arr[i]);
                 } else {
                     result = result + arr[i];
                 }
             }
             return result;
         }
         main: function void () {
             arr : array [10] of integer = {1, 2, {3, 4}, 5, 6};
             print(flatten(arr));
         }
         """
        expect = """Program([
	FuncDecl(flatten, ArrayType([10], IntegerType), [Param(arr, ArrayType([10], IntegerType))], None, BlockStmt([VarDecl(result, ArrayType([10], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(arr)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, FuncCall(typeof, [ArrayCell(arr, [Id(i)])]), StringLit(array)), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), FuncCall(flatten, [ArrayCell(arr, [Id(i)])])))]), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(arr, [Id(i)])))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([10], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), ArrayLit([IntegerLit(3), IntegerLit(4)]), IntegerLit(5), IntegerLit(6)])), CallStmt(print, FuncCall(flatten, [Id(arr)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 383))

    def test_ast_85(self):
        """Transpose matrix function"""
        input_str = """
         transpose : function array[4,4] of integer (A : array[4,4] of integer) {
             result : array[4,4] of integer;
             for (i = 0, i < length(A), i + 1) {
                 for (j = 0, j < length(A[i]), j + 1) {
                     result[j,i] = A[i,j];
                 }
             }
             return result;
         }
         main: function void () {
             A : array [4,4] of integer = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
             print(transpose(A));
         }
         """
        expect = """Program([
	FuncDecl(transpose, ArrayType([4, 4], IntegerType), [Param(A, ArrayType([4, 4], IntegerType))], None, BlockStmt([VarDecl(result, ArrayType([4, 4], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(A)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), FuncCall(length, [ArrayCell(A, [Id(i)])])), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(result, [Id(j), Id(i)]), ArrayCell(A, [Id(i), Id(j)]))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(A, ArrayType([4, 4], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)]), ArrayLit([IntegerLit(7), IntegerLit(8), IntegerLit(9)])])), CallStmt(print, FuncCall(transpose, [Id(A)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 384))

    def test_ast_86(self):
        """Combine two tables function"""
        input_str = """
         combine : function array[5] of integer (table1 : array[5] of integer, table2 : array[5] of integer) {
             result : array[5] of integer;
             for (i = 0, i < length(table1), i + 1) {
                 result[i] = table1[i] + table2[i];
             }
             return result;
         }
         main: function void () {
             table1 : array [5] of integer = {{1, 2}, {3, 4}, {5, 6}};
             table2 : array [5] of integer = {{7, 8}, {9, 10}, {11, 12}};
             print(combine(table1, table2));
         }
         """
        expect = """Program([
	FuncDecl(combine, ArrayType([5], IntegerType), [Param(table1, ArrayType([5], IntegerType)), Param(table2, ArrayType([5], IntegerType))], None, BlockStmt([VarDecl(result, ArrayType([5], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(table1)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(result, [Id(i)]), BinExpr(+, ArrayCell(table1, [Id(i)]), ArrayCell(table2, [Id(i)])))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(table1, ArrayType([5], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(3), IntegerLit(4)]), ArrayLit([IntegerLit(5), IntegerLit(6)])])), VarDecl(table2, ArrayType([5], IntegerType), ArrayLit([ArrayLit([IntegerLit(7), IntegerLit(8)]), ArrayLit([IntegerLit(9), IntegerLit(10)]), ArrayLit([IntegerLit(11), IntegerLit(12)])])), CallStmt(print, FuncCall(combine, [Id(table1), Id(table2)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 385))

    def test_ast_87(self):
        """Big countries function"""
        input_str = """
         bigCountries : function array[5] of integer (name : array[5] of string, population : array[5] of integer, area : array[5] of integer) {
             result : array[5] of integer;
             for (i = 0, i < length(name), i + 1) {
                 if ((population[i] > 25000000) || (area[i] > 3000000)) {
                     result = result + name[i];
                 }
             }
             return result;
         }
         main: function void () {
             name : array [5] of string = {"China", "India", "USA", "Indonesia", "Pakistan"};
             population : array [5] of integer = {1403500365, 1339180127, 324459463, 263991379, 205095217};
             area : array [5] of integer = {9706961, 3287590, 9372610, 1904569, 881912};
             print(bigCountries(name, population, area));
         }
         """
        expect = """Program([
	FuncDecl(bigCountries, ArrayType([5], IntegerType), [Param(name, ArrayType([5], StringType)), Param(population, ArrayType([5], IntegerType)), Param(area, ArrayType([5], IntegerType))], None, BlockStmt([VarDecl(result, ArrayType([5], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(name)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(||, BinExpr(>, ArrayCell(population, [Id(i)]), IntegerLit(25000000)), BinExpr(>, ArrayCell(area, [Id(i)]), IntegerLit(3000000))), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(name, [Id(i)])))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(name, ArrayType([5], StringType), ArrayLit([StringLit(China), StringLit(India), StringLit(USA), StringLit(Indonesia), StringLit(Pakistan)])), VarDecl(population, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1403500365), IntegerLit(1339180127), IntegerLit(324459463), IntegerLit(263991379), IntegerLit(205095217)])), VarDecl(area, ArrayType([5], IntegerType), ArrayLit([IntegerLit(9706961), IntegerLit(3287590), IntegerLit(9372610), IntegerLit(1904569), IntegerLit(881912)])), CallStmt(print, FuncCall(bigCountries, [Id(name), Id(population), Id(area)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 386))

    def test_ast_88(self):
        """Not Boring Movies function"""
        input_str = """
         notBoringMovies : function array[5] of integer (id : array[5] of integer, duration : array[5] of integer) {
             result : array[5] of integer;
             for (i = 0, i < length(id), i + 1) {
                 if (duration[i] % 2 == 1) {
                     result = result + id[i];
                 }
             }
             return result;
         }
         main: function void () {
             id : array [5] of integer = {1, 2, 3, 4, 5};
             duration : array [5] of integer = {120, 90, 90, 120, 120};
             print(notBoringMovies(id, duration));
         }
         """
        expect = """Program([
	FuncDecl(notBoringMovies, ArrayType([5], IntegerType), [Param(id, ArrayType([5], IntegerType)), Param(duration, ArrayType([5], IntegerType))], None, BlockStmt([VarDecl(result, ArrayType([5], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(id)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, ArrayCell(duration, [Id(i)]), IntegerLit(2)), IntegerLit(1)), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(id, [Id(i)])))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(id, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), VarDecl(duration, ArrayType([5], IntegerType), ArrayLit([IntegerLit(120), IntegerLit(90), IntegerLit(90), IntegerLit(120), IntegerLit(120)])), CallStmt(print, FuncCall(notBoringMovies, [Id(id), Id(duration)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 387))

    def test_ast_89(self):
        """Top K Frequent Elements function"""
        input_str = """
         topKFrequent : function array[5] of integer (nums : array[5] of integer, k : integer) {
             result : array[5] of integer;
             for (i = 0, i < length(nums), i + 1) {
                 if (nums[i] > k) {
                     result = result + nums[i];
                 }
             }
             return result;
         }
         main: function void () {
             nums : array [5] of integer = {1, 1, 1, 2, 2, 3};
             k : integer = 2;
             print(topKFrequent(nums, k));
         }
         """
        expect = """Program([
	FuncDecl(topKFrequent, ArrayType([5], IntegerType), [Param(nums, ArrayType([5], IntegerType)), Param(k, IntegerType)], None, BlockStmt([VarDecl(result, ArrayType([5], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(nums)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(nums, [Id(i)]), Id(k)), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(nums, [Id(i)])))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(nums, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(1), IntegerLit(1), IntegerLit(2), IntegerLit(2), IntegerLit(3)])), VarDecl(k, IntegerType, IntegerLit(2)), CallStmt(print, FuncCall(topKFrequent, [Id(nums), Id(k)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 388))

    def test_ast_90(self):
        """Find team size function"""
        input_str = """
         findTeamSize : function array[5] of integer (scores : array[5] of integer, ages : array[5] of integer) {
             result : array[5] of integer;
             for (i = 0, i < length(scores), i + 1) {
                 if ((scores[i] > 5) && (ages[i] < 10)) {
                     result = result + 1;
                 }
             }
             return result;
         }
         main: function void () {
             scores : array [5] of integer = {3, 5, 10, 3, 5};
             ages : array [5] of integer = {5, 8, 9, 10, 5};
             print(findTeamSize(scores, ages));
         }
         """
        expect = """Program([
	FuncDecl(findTeamSize, ArrayType([5], IntegerType), [Param(scores, ArrayType([5], IntegerType)), Param(ages, ArrayType([5], IntegerType))], None, BlockStmt([VarDecl(result, ArrayType([5], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(scores)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(&&, BinExpr(>, ArrayCell(scores, [Id(i)]), IntegerLit(5)), BinExpr(<, ArrayCell(ages, [Id(i)]), IntegerLit(10))), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), IntegerLit(1)))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(scores, ArrayType([5], IntegerType), ArrayLit([IntegerLit(3), IntegerLit(5), IntegerLit(10), IntegerLit(3), IntegerLit(5)])), VarDecl(ages, ArrayType([5], IntegerType), ArrayLit([IntegerLit(5), IntegerLit(8), IntegerLit(9), IntegerLit(10), IntegerLit(5)])), CallStmt(print, FuncCall(findTeamSize, [Id(scores), Id(ages)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 389))

    def test_ast_91(self):
        """WAres function"""
        input_str = """
         WAres : function array[5] of integer (A : array[5] of integer, B : array[5] of integer) {
             result : array[5] of integer;
             for (i = 0, i < length(A), i + 1) {
                 if (A[i] != B[i]) {
                     result = result + i;
                 }
             }
             return result;
         }
         main: function void () {
             A : array [5] of integer = {1, 2, 3, 4};
             B : array [5] of integer = {1, 3, 5, 4};
             print(WAres(A, B));
         }
         """
        expect = """Program([
	FuncDecl(WAres, ArrayType([5], IntegerType), [Param(A, ArrayType([5], IntegerType)), Param(B, ArrayType([5], IntegerType))], None, BlockStmt([VarDecl(result, ArrayType([5], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(A)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(A, [Id(i)]), ArrayCell(B, [Id(i)])), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), Id(i)))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(A, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), VarDecl(B, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(3), IntegerLit(5), IntegerLit(4)])), CallStmt(print, FuncCall(WAres, [Id(A), Id(B)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 390))

    def test_ast_92(self):
        """Average times function"""
        input_str = """
         averageTimes : function array[5] of integer (times : array[5] of integer) {
             result : array[5] of integer;
             for (i = 0, i < length(times), i + 1) {
                 if (times[i] > 0) {
                     result = result + times[i];
                 }
             }
             return result / length(times);
         }
         main: function void () {
             times : array [5] of integer = {1, 2, 3, 4, 5};
             print(averageTimes(times));
         }
         """
        expect = """Program([
	FuncDecl(averageTimes, ArrayType([5], IntegerType), [Param(times, ArrayType([5], IntegerType))], None, BlockStmt([VarDecl(result, ArrayType([5], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(times)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(times, [Id(i)]), IntegerLit(0)), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(times, [Id(i)])))]))])), ReturnStmt(BinExpr(/, Id(result), FuncCall(length, [Id(times)])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(times, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), CallStmt(print, FuncCall(averageTimes, [Id(times)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 391))

    def test_ast_93(self):
        """Sort old books function"""
        input_str = """
         sortOldBooks : function array[5] of integer (books : array[5] of integer) {
             result : array[5] of integer;
             for (i = 0, i < length(books), i + 1) {
                 if (books[i] > 100) {
                     result = result + books[i];
                 }
             }
             return result;
         }
         main: function void () {
             books : array [5] of integer = {1, 2, 3, 4, 5};
             print(sortOldBooks(books));
         }
         """
        expect = """Program([
	FuncDecl(sortOldBooks, ArrayType([5], IntegerType), [Param(books, ArrayType([5], IntegerType))], None, BlockStmt([VarDecl(result, ArrayType([5], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(books)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(books, [Id(i)]), IntegerLit(100)), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(books, [Id(i)])))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(books, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), CallStmt(print, FuncCall(sortOldBooks, [Id(books)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 392))

    def test_ast_94(self):
        """Concatenated words function"""
        input_str = """
         findAllConcatenatedWordsInADict : function array[5] of integer (words : array[5] of string) {
             result : array[5] of integer;
             for (i = 0, i < length(words), i + 1) {
                 if (words[i] != "") {
                     result = result + words[i];
                     break;
                 }
             }
             return result;
         }
         main: function void () {
             words : array [5] of string = {"cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"};
             print(findAllConcatenatedWordsInADict(words));
         }
         """
        expect = """Program([
	FuncDecl(findAllConcatenatedWordsInADict, ArrayType([5], IntegerType), [Param(words, ArrayType([5], StringType))], None, BlockStmt([VarDecl(result, ArrayType([5], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(words)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(words, [Id(i)]), StringLit()), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(words, [Id(i)]))), BreakStmt()]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(words, ArrayType([5], StringType), ArrayLit([StringLit(cat), StringLit(cats), StringLit(catsdogcats), StringLit(dog), StringLit(dogcatsdog), StringLit(hippopotamuses), StringLit(rat), StringLit(ratcatdogcat)])), CallStmt(print, FuncCall(findAllConcatenatedWordsInADict, [Id(words)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 393))

    def test_ast_95(self):
        """Weather type in each country function"""
        input_str = """
         countWeatherType : function array[5] of integer (weather : array[5] of string, country : array[5] of string) {
             result : array[5] of integer;
             for (i = 0, i < length(weather), i + 1) {
                 if ((weather[i] == "sunny") || (weather[i] == "cloudy")) {
                     result = result + country[i];
                 }
             }
             return result;
         }
         main: function void () {
             weather : array [5] of string = {"sunny", "cloudy", "rainy"};
             country : array [5] of string = {"Vietnam", "Thailand", "Malaysia"};
             print(countWeatherType(weather, country));
         }
         """
        expect = """Program([
	FuncDecl(countWeatherType, ArrayType([5], IntegerType), [Param(weather, ArrayType([5], StringType)), Param(country, ArrayType([5], StringType))], None, BlockStmt([VarDecl(result, ArrayType([5], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(weather)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(||, BinExpr(==, ArrayCell(weather, [Id(i)]), StringLit(sunny)), BinExpr(==, ArrayCell(weather, [Id(i)]), StringLit(cloudy))), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(country, [Id(i)])))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(weather, ArrayType([5], StringType), ArrayLit([StringLit(sunny), StringLit(cloudy), StringLit(rainy)])), VarDecl(country, ArrayType([5], StringType), ArrayLit([StringLit(Vietnam), StringLit(Thailand), StringLit(Malaysia)])), CallStmt(print, FuncCall(countWeatherType, [Id(weather), Id(country)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 394))

    def test_ast_96(self):
        """Delete duplicate emails function"""
        input_str = """
            deleteDuplicateEmails : function array[5] of integer (emails : array[5] of string) {
                result : array[5] of integer;
                for (i = 0, i < length(emails), i + 1) {
                    if (emails[i] != "") {
                        result = result + emails[i];
                    }
                }
                return result;
            }
            main: function void () {
                emails : array [5] of string = {"cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"};

                print(deleteDuplicateEmails(emails));
            }
            """
        expect = """Program([
	FuncDecl(deleteDuplicateEmails, ArrayType([5], IntegerType), [Param(emails, ArrayType([5], StringType))], None, BlockStmt([VarDecl(result, ArrayType([5], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(emails)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(emails, [Id(i)]), StringLit()), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(emails, [Id(i)])))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(emails, ArrayType([5], StringType), ArrayLit([StringLit(cat), StringLit(cats), StringLit(catsdogcats), StringLit(dog), StringLit(dogcatsdog), StringLit(hippopotamuses), StringLit(rat), StringLit(ratcatdogcat)])), CallStmt(print, FuncCall(deleteDuplicateEmails, [Id(emails)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 395))

    def test_ast_97(self):
        """Unpolluted cities function"""
        input_str = """
            unpollutedCities : function array[5] of integer (cities : array[5] of string, pollution : array[5] of integer) {
                result : array[5] of integer;
                for (i = 0, i < length(cities), i + 1) {
                    if (pollution[i] < 100) {
                        result = result + cities[i];
                    }
                }
                return result;
            }
            main: function void () {
                cities : array [5] of string = {"Hanoi", "Ho Chi Minh", "Da Nang", "Haiphong", "Can Tho"};
                pollution : array [5] of integer = {10, 20, 30, 40, 50};
                print(unpollutedCities(cities, pollution));
            }
            """
        expect = """Program([
	FuncDecl(unpollutedCities, ArrayType([5], IntegerType), [Param(cities, ArrayType([5], StringType)), Param(pollution, ArrayType([5], IntegerType))], None, BlockStmt([VarDecl(result, ArrayType([5], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(cities)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(pollution, [Id(i)]), IntegerLit(100)), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(cities, [Id(i)])))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(cities, ArrayType([5], StringType), ArrayLit([StringLit(Hanoi), StringLit(Ho Chi Minh), StringLit(Da Nang), StringLit(Haiphong), StringLit(Can Tho)])), VarDecl(pollution, ArrayType([5], IntegerType), ArrayLit([IntegerLit(10), IntegerLit(20), IntegerLit(30), IntegerLit(40), IntegerLit(50)])), CallStmt(print, FuncCall(unpollutedCities, [Id(cities), Id(pollution)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 396))

    def test_ast_98(self):
        """Find the most common word function"""
        input_str = """
            mostCommonWord : function array[5] of integer (paragraph : array[5] of string, banned : array[5] of string) {
                result : array[5] of integer;
                for (i = 0, i < length(paragraph), i + 1) {
                    if (paragraph[i] != "") {
                        result = result + paragraph[i];
                        continue;
                    }
                }
                return result;
            }
            main: function void () {
                paragraph : array [5] of string = {"Bob hit a ball, the hit BALL flew far after it was hit."};
                banned : array [5] of string = {"hit"};
                print(mostCommonWord(paragraph, banned));
            }
            """
        expect = """Program([
	FuncDecl(mostCommonWord, ArrayType([5], IntegerType), [Param(paragraph, ArrayType([5], StringType)), Param(banned, ArrayType([5], StringType))], None, BlockStmt([VarDecl(result, ArrayType([5], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(paragraph)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(paragraph, [Id(i)]), StringLit()), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(paragraph, [Id(i)]))), ContinueStmt()]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(paragraph, ArrayType([5], StringType), ArrayLit([StringLit(Bob hit a ball, the hit BALL flew far after it was hit.)])), VarDecl(banned, ArrayType([5], StringType), ArrayLit([StringLit(hit)])), CallStmt(print, FuncCall(mostCommonWord, [Id(paragraph), Id(banned)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 397))

    def test_ast_99(self):
        """Second-highest salary function"""
        input_str = """
            secondHighest : function array[5] of integer (salary : array[5] of integer) {
                result : array[5] of integer;
                for (i = 0, i < length(salary), i + 1) {
                    if (salary[i] > 100) {
                        result = result + salary[i];
                        break;
                    }
                }
                return result;
            }
            main: function void () {
                salary : array [5] of integer = {1, 2, 3, 4, 5};
                print(secondHighest(salary));
            }
            """
        expect = """Program([
	FuncDecl(secondHighest, ArrayType([5], IntegerType), [Param(salary, ArrayType([5], IntegerType))], None, BlockStmt([VarDecl(result, ArrayType([5], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [Id(salary)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(salary, [Id(i)]), IntegerLit(100)), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(salary, [Id(i)]))), BreakStmt()]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(salary, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), CallStmt(print, FuncCall(secondHighest, [Id(salary)]))]))
])"""
        self.assertTrue(TestAST.test(input_str, expect, 398))

    def test_ast_100(self):
        input_string = """
        program: function void (arr: array [10] of integer, low: integer, high: integer) {
            if (low < high) {
                pi = partition(arr, low, high);
                sort(arr, low, pi - 1);
                sort(arr, pi + 1, high);
            }
        }

        partition: function integer (arr: array [10] of integer, low: integer, high: integer) {
            pivot = arr[high];
            i = low - 1;
            for (j = low, j < high, j + 1) {
                if (arr[j] < pivot) {
                    i = i + 1;
                    temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
            temp = arr[i + 1];
            arr[i + 1] = arr[high];
            arr[high] = temp;
            return i + 1;
        }
        """
        expect = """Program([
	FuncDecl(program, VoidType, [Param(arr, ArrayType([10], IntegerType)), Param(low, IntegerType), Param(high, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(low), Id(high)), BlockStmt([AssignStmt(Id(pi), FuncCall(partition, [Id(arr), Id(low), Id(high)])), CallStmt(sort, Id(arr), Id(low), BinExpr(-, Id(pi), IntegerLit(1))), CallStmt(sort, Id(arr), BinExpr(+, Id(pi), IntegerLit(1)), Id(high))]))]))
	FuncDecl(partition, IntegerType, [Param(arr, ArrayType([10], IntegerType)), Param(low, IntegerType), Param(high, IntegerType)], None, BlockStmt([AssignStmt(Id(pivot), ArrayCell(arr, [Id(high)])), AssignStmt(Id(i), BinExpr(-, Id(low), IntegerLit(1))), ForStmt(AssignStmt(Id(j), Id(low)), BinExpr(<, Id(j), Id(high)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(arr, [Id(j)]), Id(pivot)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), AssignStmt(Id(temp), ArrayCell(arr, [Id(i)])), AssignStmt(ArrayCell(arr, [Id(i)]), ArrayCell(arr, [Id(j)])), AssignStmt(ArrayCell(arr, [Id(j)]), Id(temp))]))])), AssignStmt(Id(temp), ArrayCell(arr, [BinExpr(+, Id(i), IntegerLit(1))])), AssignStmt(ArrayCell(arr, [BinExpr(+, Id(i), IntegerLit(1))]), ArrayCell(arr, [Id(high)])), AssignStmt(ArrayCell(arr, [Id(high)]), Id(temp)), ReturnStmt(BinExpr(+, Id(i), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input_string, expect, 399))
