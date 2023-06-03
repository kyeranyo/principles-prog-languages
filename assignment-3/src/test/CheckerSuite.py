import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_static1(self):
        input_str = """delta: integer = fact(3);"""
        except_str = "Undeclared Function: fact"
        self.assertTrue(TestChecker.test(input_str, except_str, 400))

    def test_static2(self):
        input_str = """x, y, z: float = 1, 2, 3;"""
        except_str = "No entry point"
        self.assertTrue(TestChecker.test(input_str, except_str, 401))

    def test_static3(self):
        input_str = """main: function void () {
            printInteger(4);
        }"""
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 402))

    def test_static4(self):
        input_str = """x: integer = 65;
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            a, b: integer = 1, 2;
            inc(x, delta);
            printInteger(x);
        }"""
        except_str = "Undeclared Identifier: delta"
        self.assertTrue(TestChecker.test(input_str, except_str, 403))

    def test_static5(self):
        input_str = """program: function void() {
            b : string = "Hello";
            a : string = "World";
            c : auto = b :: a;
        }"""
        except_str = "No entry point"
        self.assertTrue(TestChecker.test(input_str, except_str, 404))

    def test_static6(self):
        input_str = """
            multiply: function integer (x: integer, y: integer) {
                return x * y;
            }
            square: function integer (inherit out x: integer) {
                return x * x;
            }
            main: function void () inherit multiply {
                super(1212+2,31);
                a : integer = 5;
                b : integer = square(a);
            }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 405))

    def test_static7(self):
        input_str = """
        length: function integer (s: string) {
            return 2;
        }
        isPalindrome : function boolean (s : string) {
            i : integer;
            for (i = 0, i < length(s) / 2, i + 1) {
            }
            return true;
        }
        main: function void () {
            s : string= "racecar";
            if (isPalindrome(s)) {
                printString("s is a palindrome.");
            } else {
                printString("s is not a palindrome.");
            }
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 406))

    def test_static8(self):
        input_str = """
        length: function integer (s: string) {
            return 2;
        }
        reverse : function string (s : string) {
            result : string = "";
            i : integer;
            for (i = length(s) - 1, i >= 0, i - 1) {
                result = result :: "c";
            }
            return result;
        }
        main: function void () {
            s : string = "Hello world!";
            printString(reverse(s));
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 407))

    def test_static9(self):
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
        except_str = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input_str, except_str, 408))

    def test_static10(self):
        input_str = """
        isArmstrong : function boolean (n : integer) {
            sum : integer = 0;
            temp : integer = n;
            while (temp > 0) {
                digit : integer = temp % 10;
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
            n : integer = 153;
            if (isArmstrong(n)) {
                printString("n is an Armstrong number.");
            } else {
                printString("n is not an Armstrong number.");
            }
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 409))

    def test_static11(self):
        input_str = """
        main: function void () {
            a : integer = 5;
            b : integer = 6;
            if (a > b) {
                printString("a is greater than b.");
            } else if (a < b) {
                printString("a is less than b.");
            } else {
                printString("a is equal to b.");
            }
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 410))

    def test_static12(self):
        input_str = """
        length : function integer (nums : array[5] of integer) {
            return 5;
        }
        searchInsert : function integer (nums : array[5] of integer, target : integer) {
            i : integer;
            for (i = 0, i < length(nums), i + 1) {
                if (nums[i] >= target) {
                    return i;
                }
            }
            return length(nums);
        }
        main: function void () {
            nums : array[5] of integer = {1, 3, 5, 6};
            target : integer = 5;
            printInteger(searchInsert(nums, target));
        }
        """
        except_str = "Type mismatch in Variable Declaration: VarDecl(nums, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(3), IntegerLit(5), IntegerLit(6)]))"
        self.assertTrue(TestChecker.test(input_str, except_str, 411))

    def test_static13(self):
        input_str = """
        lowestCommonAncestor : function integer (root : integer, p : integer, q : integer) {
            if ((p < root) && (q < root)) {
                rootLeft : integer = root - 1;
                return lowestCommonAncestor(rootLeft, p, q);
            } else if ((p > root) && (q > root)) {
                rootRight : integer = root + 1;
                return lowestCommonAncestor(rootRight, p, q);
            } else {
                return root;
            }
        }
        main: function void () {
            root : integer = 6;
            p : integer = 2;
            q : integer = 8;
            printInteger(lowestCommonAncestor(root, p, q));
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 412))

    def test_static14(self):
        input_str = """
        sumOfLeftLeaves : function integer (root : integer) {
            if (root == 0) {
                return 0;
            }
            rootLeft : integer = root - 1;
            rootLeftLeft : integer = rootLeft - 1;
            rootLeftRight : integer = rootLeft + 1;
            rootRight : integer = root + 1;
            if ((rootLeft != 0) && (rootLeftLeft == 0) && (rootLeftRight == 0)) {
                rootLeftVal : integer = rootLeft;
                return rootLeftVal + sumOfLeftLeaves(rootRight);
            }
            return sumOfLeftLeaves(rootLeft) + sumOfLeftLeaves(rootRight);
        }
        main: function void () {
            root : integer = 3;
            printInteger(sumOfLeftLeaves(root));
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 413))

    def test_static15(self):
        input_str = """
        reverseList : function integer (head : auto) {
            prev : integer = 0;
            curr : integer = head;
            while (curr != null) {
                nextTemp : integer = currNext;
                currNext = prev;
                prev = curr;
                curr = nextTemp;
            }
            return prev;
        }
        main: function void () {
            head : integer = 1;
            printInteger (reverseList(head));
        }
        """
        except_str = "Undeclared Identifier: null"
        self.assertTrue(TestChecker.test(input_str, except_str, 414))

    def test_static16(self):
        input_str = """
        sqrt : function integer (x : integer) {
            if (x == 0) {
                return 0;
            }
            if (x < 0) {
                return -1;
            }
            left : integer  = 1;
            right  : integer  = x;
            while (left <= right) {
                mid : integer = (left + right) / 2;
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
            x : integer = 8;
            printFloat(sqrt(x));
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 415))

    def test_static17(self):
        input_str = """
        climbStairs : function integer (n : integer) {
            if (n == 1) {
                return 1;
            }
            first : integer = 1;
            second : integer = 2;
            i : integer;
            for (i = 3, i <= n, i + 1) {
                third : integer = first + second;
                first = second;
                second = third;
            }
            return second;
        }
        main: function void () {
            n : integer = 4;
            printInteger(climbStairs(n));
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 416))

    def test_static18(self):
        input_str = """
        countPrimes : function integer (n : integer) {
            if (n < 2) {
                return 0;
            }
            count : integer = 0;
            i : integer;
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
            i : integer;
            for (i = 2, i * i <= n, i + 1) {
                if (n % i == 0) {
                    return false;
                }
            }
            return true;
        }
        main: function void () {
            n : integer = 10;
            printInteger(countPrimes(n));
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 417))

    def test_static19(self):
        input_str = """
        numDecodings : function integer (s : string) {
            n : integer = 6;
            dp : array[6] of integer;
            dp[0] = 1;
            dp[1] = 1;
            i : integer;
            for (i = 2, i <= n, i + 1) {
                dp[i] = dp[i - 1];
                dp[i] = dp[i] + dp[i - 2];
            }
            return dp[n];
        }
        main: function void () {
            s : string = "226";
            printInteger(numDecodings(s));
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 418))

    def test_static20(self):
        input_str = """
            foo : function integer (a : integer) inherit goo {
                super(a);
            }
            goo : function integer (inherit a : integer) {}
            main: function void () {}
        """
        except_str = "Invalid Parameter: a"
        self.assertTrue(TestChecker.test(input_str, except_str, 419))

    def test_static21(self):
        input_str = """
            foo : function auto (a : auto) inherit goo {
                super(2);
                return a + b;
            }
            goo : function integer (inherit b : integer) {}
            main: function void () {
                printInteger(foo(2));
            }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 420))

    def test_static22(self):
        input_str = """
            main: function void () {
                foo(2);
            }
            foo : function auto (a : auto) {
                return a;
            }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 421))

    def test_static23(self):
        input_str = """
            main: function void () {
                a : auto;
            }
        """
        except_str = "Invalid Variable: a"
        self.assertTrue(TestChecker.test(input_str, except_str, 422))

    def test_static24(self):
        input_str = """
            main: function void () {
                a : auto = 2;
                printInteger(a);
            }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 423))

    def test_static25(self):
        input_str = """
            f : function auto (a : auto, b : integer) {
                return a + b;
            }
            main: function void (){
                f("abc", 2);
            }
        """
        except_str = "Type mismatch in statement: CallStmt(f, StringLit(abc), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input_str, except_str, 424))

    def test_static26(self):
        input_str = """
            f : function auto (a : auto, b : integer) {
                return a + b;
            }
            main: function void (){
                printInteger(f(2, 2));
            }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 425))

    def test_static27(self):
        input_str = """
            a: integer;
            foo: function integer (p: boolean) {}
            bar: function integer () inherit foo {
                super();                                              // line 4
            }
        """
        except_str = "Type mismatch in expression: "
        self.assertTrue(TestChecker.test(input_str, except_str, 426))

    def test_static28(self):
        input_str = """
            goo: function void(a: auto, a: auto) inherit foo{}
        """
        except_str = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input_str, except_str, 427))

    def test_static29(self):
        input_str = """
        M: function void (a: integer) inherit N {
            super(a);
        } 
        N: function void (inherit a: integer) {}
        """
        except_str = "Invalid Parameter: a"
        self.assertTrue(TestChecker.test(input_str, except_str, 428))

    def test_static30(self):
        input_str = """
        M: function void (a: integer) inherit N {
            super(a);
        } 
        N: function void (inherit a: integer) {}
        """
        except_str = "Invalid Parameter: a"
        self.assertTrue(TestChecker.test(input_str, except_str, 429))

    def test_static31(self):
        input_str = """
        secondHighest : function array[5] of integer (salary : array[5] of integer) {
                result : array[5] of integer;
                i : integer;
                for (i = 0, i < 5, i + 1) {
                    if (salary[i] > 100) {
                        break;
                    }
                }
                return result;
            }
            main: function void () {
                salary : array [5] of integer = {1, 2, 3, 4, 5};
                secondHighest(salary);
            }
            """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 430))

    def test_static32(self):
        input_str = """
         main: function void () {
            arr : array [10] of integer = {1, 2, {3, 4}, 5, 6};
         }
        """
        except_str = "Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(2), ArrayLit([IntegerLit(3), IntegerLit(4)]), IntegerLit(5), IntegerLit(6)])"
        self.assertTrue(TestChecker.test(input_str, except_str, 431))

    def test_static33(self):
        input_str = """
        b : function void() {}
        a : integer = b;
        """
        except_str = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, Id(b))"
        self.assertTrue(TestChecker.test(input_str, except_str, 432))

    def test_static34(self):
        input_str = """
        a : integer;
        a : function void() {}
        """
        except_str = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input_str, except_str, 433))

    def test_static35(self):
        input_str = """
        a : integer;
        a : integer;
        """
        except_str = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input_str, except_str, 434))

    def test_static36(self):
        input_str = """
        foo: function auto() {
            return 1;
        }
        goo: function auto() {
            return 2;
        }
        main: function void () {
            a : array [2] of integer = {foo(), goo()};
            printInteger(a[0]);
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 435))

    def test_static37(self):
        input_str = """
        inc : function void (out n : integer, a: float) inherit foo{} //1
        foo : function auto (inherit n: float, b: integer){} //2
        """
        except_str = "Invalid statement in function: inc"
        self.assertTrue(TestChecker.test(input_str, except_str, 436))

    def test_static38(self):
        input_str = """
        inc : function void (out n : integer, a: float) inherit foo{} //1
        foo : function auto (inherit n: float, n: integer){} //2
        """
        except_str = "Redeclared Parameter: n"
        self.assertTrue(TestChecker.test(input_str, except_str, 437))

    def test_static39(self):
        input_str = """
        arr: array [2,2,2,2] of integer = {
                {
                    { {1, 2}, {3, 4} },
                    { {5, 6}, {7, 8} }
                },
                {
                    { {9, 10}, {11, 12} },
                    { {13, 14}, {15, 16} }
                }
            };
            m: integer;
            n: float = readInteger();
            foo1: function auto (c: integer, d: integer) inherit foo {
                super(2.0,512);
                printInteger(1);
                if (b == 1) return 1;
                a = readFloat();
                a = a + b;
                arraycell : integer;
                arraycell = arr[0,0,0,0];
                return arraycell;
            } 
            foo: function auto (inherit a: float, inherit b: integer) {
                return a;
            }   
            main : function void () {}
            """
        expect_str = ""
        self.assertTrue(TestChecker.test(input_str, expect_str, 438))

    def test_static40(self):
        input_str = """
            foo: function integer() {
                return 1;
                return 1+"2";
            }
        """
        except_str = "No entry point"
        self.assertTrue(TestChecker.test(input_str, except_str, 439))

    def test_static41(self):
        input_str = """
        foo: function void (inherit a: integer, a: float) inherit bar {}
        """
        except_str = "Undeclared Function: bar"
        self.assertTrue(TestChecker.test(input_str, except_str, 440))

    def test_static42(self):
        input_str = """
        bar: function void (inherit a: integer){}
        foo: function void (a: integer) inherit bar {
            preventDefault();
        }
        """
        except_str = "No entry point"
        self.assertTrue(TestChecker.test(input_str, except_str, 441))

    def test_static43(self):
        input_str = """
        bar: function void (inherit a: integer){}
        foo: function void () inherit bar {
            preventDefault();
            a:integer=1;
        }
        main : function void(a : integer) {}
        """
        except_str = "No entry point"
        self.assertTrue(TestChecker.test(input_str, except_str, 442))

    def test_static44(self):
        input_str = """
        foo: function void() inherit foo1{
            super("HCMUT",true);
            x = 7;
        }
        foo1: function void (inherit x: string, inherit b:boolean){}
        main : function string() {}
        """
        except_str = "Type mismatch in statement: AssignStmt(Id(x), IntegerLit(7))"
        self.assertTrue(TestChecker.test(input_str, except_str, 443))

    def test_static45(self):
        input_str = """
        main : function void() {
            x: auto = x+10;
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 444))

    def test_static46(self):
        input_str = """
        a : float = foo(1,2);
        foo : function integer (a : auto, b: auto) {
            a = "abc";
            b = "bcd";
            return a + b;
        }
        """
        except_str = "Type mismatch in statement: AssignStmt(Id(a), StringLit(abc))"
        self.assertTrue(TestChecker.test(input_str, except_str, 445))

    def test_static47(self):
        input_str = """
        main : function void() {
            preventDefault();
        }
        """
        except_str = "Invalid statement in function: main"
        self.assertTrue(TestChecker.test(input_str, except_str, 446))

    def test_static48(self):
        input_str = """
        main : function void() {
            a : integer = 1;
            b : float = 2.0;
            c : string = "abc";
            if (a == 1) {
                a : float = 1.0;
                printFloat(a);
            }
            else {
                b : string = "bcd";
                printString(b);
                c : integer = 1;
                printInteger(c);
                if (c == 1) {
                    a : string = "abc";
                    printString(a);
                    i  : integer = 1;
                    for (i = 1, i < 10, i + 1) {
                        a : boolean = true;
                        printBoolean(a);
                    }
                }
            }
            printFloat(a);
            printString(c);
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 447))

    def test_static49(self):
        input_str = """
        foo : function float (a : integer, b : integer,c:auto) {
                x : integer ;
                return c;
            }
        goo : function auto (x : integer, y : integer) {}
        """
        expect_str = "No entry point"
        self.assertTrue(TestChecker.test(input_str, expect_str, 448))

    def test_static50(self):
        input_str = """
        foo : function auto (a : auto, b : auto) {
            x : integer = readInteger();
            if (x == 1) {
                return a + x;
            }
            else {
                return b + x;
            }
        }
        main : function void() {
            c : integer = foo(1,2);
            printFloat(c);
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 449))

    def test_static51(self):
        input_str = """
        goo : function float (a : integer, b : integer) {
                x : integer ;
                return gau(4 , 1.3) ;
            }
        gau : function auto (x : integer, y : integer) {}
        """
        expect_str = "Type mismatch in expression: FuncCall(gau, [IntegerLit(4), FloatLit(1.3)])"
        self.assertTrue(TestChecker.test(input_str, expect_str, 450))

    def test_static52(self):
        input_str = """
        main: function void () {
            a: integer = 1;
            b: integer = 2;
            while (a <= 10) {
                b = b * 2;
                printInteger(b);
                a = a + 1;
            }
            return;
        }"""
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 451))

    def test_static53(self):
        input_str = """
            readInt: function void () {
                a : integer = 2 + readInteger();
            }
        """
        self.assertTrue(TestChecker.test(input_str, "No entry point", 452))

    def test_static54(self):
        input_str = """
        length: function integer (s : array[4] of integer) {
            return 4;
        }
        plusOne : function array[4] of integer (digits : array[4] of integer) {
            n : integer = length(digits);
            i : integer;
            for (i = n - 1, i >= 0, i - 1) {
                if (digits[i] < 9) {
                    digits[i] = digits[i] + 1;
                    return digits;
                }
                digits[i] = 0;
            }
            for (i = 1, i < n, i + 1) {
                digits[i] = 0;
            }
            return digits;
        }
        main: function void () {
            digits : array[4] of integer = {1, 2, 3, 4};
            printInteger(plusOne(digits));
        }
        """
        except_str = "Type mismatch in statement: CallStmt(printInteger, FuncCall(plusOne, [Id(digits)]))"
        self.assertTrue(TestChecker.test(input_str, except_str, 453))

    def test_static55(self):
        input_str = """
        x: function void() {}
        main: function void() inherit x {
            super(); //?
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 454))

    def test_static56(self):
        input_str = """program: function void() {
            a: integer = 1;
            b: integer = 2;
            c: integer = 3;
            d: integer = 4;
            e: integer = 5;
            arr: array [5] of integer = {a, b, c, d, e};
            i : float;
            for (i = 0, i < 5, 1) {
                if (arr[i] % 2 == 0) {
                    printString("even");
                }
                else {
                    printString("odd");
                }
            }
        }"""
        except_str = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), IntegerLit(1), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, ArrayCell(arr, [Id(i)]), IntegerLit(2)), IntegerLit(0)), BlockStmt([CallStmt(printString, StringLit(even))]), BlockStmt([CallStmt(printString, StringLit(odd))]))]))"
        self.assertTrue(TestChecker.test(input_str, except_str, 455))

    def test_static57(self):
        input_str = """
            main: function void () {
                a: integer = 10;
                b: float = 3.14e-7;
                c: boolean = true;
                d , e : array[2] of integer = {1, 2}, {3, 4};
            }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 456))

    def test_static58(self):
        input_str = """
        double : function array[5] of integer (input : array[5] of integer) {
            i : integer;
            for (i = 0, i < 5, i + 1) {
                input[i] = input[i] * 2;
            }
            return input;
        }
        main: function void () {
            a : array[5] of integer = {1, 2, 3, 4, 5};
            b : array[5] of integer = double(a);
            i : integer;
            for (i = 0, i < 5, i + 1) {
                printInteger(b[i]);
            }
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 457))

    def test_static59(self):
        input_str = """
        a : integer = -1 + 2;
        """
        except_str = "No entry point"
        self.assertTrue(TestChecker.test(input_str, except_str, 458))

    def test_static60(self):
        input_str = """
        foo: function integer() {
            arr: array[5] of integer = {3, 7, 9, 2, 4};
            target: integer = 9;
            n: integer = 5;
            found: boolean = false;
            index: integer = -1;
            i : integer;
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
        main: function void() {
            printInteger(foo());
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 459))

    def test_static61(self):
        input_str = """
        sortColors : function void (nums : array[4] of integer) {
            red : integer = 0;
            white : integer = 0;
            blue : integer = 0;
            i : integer;
            for (i = 0, i < 4, i + 1) {
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
            for (i = red + white, i < 4, i + 1) {
                nums[i] = 2;
            }
        }
        main: function void () {
            nums : array[4] of integer = {2, 0, 2, 1, 1, 0};
            sortColors(nums);
            printInt(nums);
        }
        """
        except_str = "Type mismatch in Variable Declaration: VarDecl(nums, ArrayType([4], IntegerType), ArrayLit([IntegerLit(2), IntegerLit(0), IntegerLit(2), IntegerLit(1), IntegerLit(1), IntegerLit(0)]))"
        self.assertTrue(TestChecker.test(input_str, except_str, 460))

    def test_static62(self):
        input_str = """
        climateChange : function void (arr : array[4] of integer) {
            n : integer = 4;
            i : integer;
            for (i = 0, i < n - 1, i + 1) {
                j : integer;
                for (j = 0, j < n - i - 1, j + 1) {
                    if (arr[j] > arr[j + 1]) {
                        temp : integer = arr[j];
                        arr[j] = arr[j + 1];
                        arr[j + 1] = temp;
                    }
                }
            }
        }
        main: function void () {
            arr : array[4] of integer= {64, 34, 25, 12};
            climateChange(arr);
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 461))

    def test_static63(self):
        input_str = """
        main: function void () {
            a : integer = foo(2.0,"abc");
            printInteger(foo(2.0,"abc"));
        }
        foo : function auto (a : auto, b : auto) {
            return "abc";
        }
        """
        except_str = "Type mismatch in statement: ReturnStmt(StringLit(abc))"
        self.assertTrue(TestChecker.test(input_str, except_str, 462))

    def test_static64(self):
        input_str = """
        findPeakElement : function integer (nums : array[6] of integer) {
            n : integer = 6;
            if (n == 1) {
                return 0;
            }
            if (nums[0] > nums[1]) {
                return 0;
            }
            if (nums[n - 1] > nums[n - 2]) {
                return n - 1;
            }
            i : integer;
            for (i = 1, i < n - 1, i + 1) {
                if ((nums[i] > nums[i - 1]) && (nums[i] > nums[i + 1])) {
                    return i;
                }
            }
            return -1;
        }
        main: function void () {
            nums : array[6] of integer = {1, 2, 3, 1 , 4, 5};
            printInteger(findPeakElement(nums));
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 463))

    def test_static65(self):
        input_str = """
        length : function integer (arr : array[5] of integer) {
            return 5;
        }
        moveZeroes : function void (nums : array[5] of integer) {
            n : integer = length(nums);
            lastNonZeroFoundAt : integer = 0;
            i : integer;
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
            nums : array [5] of integer = {0, 1, 0, 3, 12};
            moveZeroes(nums);
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 464))

    def test_static66(self):
        input_str = """
        islandPerimeter : function integer (grid : array[4,4] of integer) {
            n : integer = 4;
            m : integer = 4;
            result : integer = 0;
            i : integer;
            for (i = 0, i < n, i + 1) {
                j : integer;
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
            printInteger(islandPerimeter(grid));
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 465))

    def test_static67(self):
        input_str = """ n : array [1,2] of integer ; m : integer = n[6, 3, 5] ;"""
        expect_str = "Type mismatch in expression: ArrayCell(n, [IntegerLit(6), IntegerLit(3), IntegerLit(5)])"
        self.assertTrue(TestChecker.test(input_str, expect_str, 466))

    def test_static68(self):
        input_str = """ arrays : array [3, 2] of integer = {{{1}, {2}}, {{2}, {3}}, {{3}, {3, 3}}} ; """
        expect_str = "Illegal array literal: ArrayLit([ArrayLit([ArrayLit([IntegerLit(1)]), ArrayLit([IntegerLit(2)])]), ArrayLit([ArrayLit([IntegerLit(2)]), ArrayLit([IntegerLit(3)])]), ArrayLit([ArrayLit([IntegerLit(3)]), ArrayLit([IntegerLit(3), IntegerLit(3)])])])"
        self.assertTrue(TestChecker.test(input_str, expect_str, 467))

    def test_static69(self):
        input_str = """
        sort: function void (arr: array [10] of integer, low: integer, high: integer) {
            if (low < high) {
                pi : integer = partition(arr, low, high);
                sort(arr, low, pi - 1);
                sort(arr, pi + 1, high);
            }
        }

        partition: function integer (arr: array [10] of integer, low: integer, high: integer) {
            pivot : integer = arr[high];
            i : integer = low - 1;
            j : integer;
            for (j = low, j < high, j + 1) {
                if (arr[j] < pivot) {
                    i = i + 1;
                    temp : integer = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
            temp : integer = arr[i + 1];
            arr[i + 1] = arr[high];
            arr[high] = temp;
            return i + 1;
        }
        """
        except_str = "No entry point"
        self.assertTrue(TestChecker.test(input_str, except_str, 468))

    def test_static70(self):
        input_str = """
        transpose : function array[4,4] of integer (A : array[4,4] of integer) {
            result : array[4,4] of integer;
            i : integer;
            for (i = 0, i < 4, i + 1) {
                j : integer;
                for (j = 0, j < 4, j + 1) {
                    result[j,i] = A[i,j];
                }
            }
            return result;
        }
        main: function void () {
            A : array [4,4] of integer = {
                {1, 2, 3, 4},
                {5, 6, 7, 8},
                {9, 10, 11, 12},
                {13, 14, 15, 16}
            };
            transpose(A);
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 469))

    def test_static71(self):
        input_str = """
         threeSum : function array[2] of integer (nums : array[6] of integer) {
            n : integer = 6;
            result : array [2] of integer = {1,2};
            i : integer;
            for (i = 0, i < n, i + 1) {
                if ((i > 0) && (nums[i] == nums[i - 1])) {
                    continue;
                }
                target : integer = -nums[i];
                left : integer = i + 1;
                right : integer = n - 1;
                while (left < right) {
                    if ((nums[left] + nums[right]) == target) {
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
            nums : array[6] of integer = {-1, 0, 1, 2, -1, -4};
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 470))

    def test_static72(self):
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
        except_str = "Undeclared Function: parseNumber"
        self.assertTrue(TestChecker.test(input_str, except_str, 471))

    def test_static73(self):
        input_str = """
            main : function void() {
                b : float = readFloat();
                if ((b >= 2.0) && (b <= 3.0)) {
                    printString("b is between 2.0 and 3.0, inclusive.\\n");
                } else {
                    printString("b is not between 2.0 and 3.0, inclusive.\\n");
                }
            }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 472))

    def test_static74(self):
        input_str = """
        findCelebrity : function integer (n : integer) {
            candidate : integer = 0;
            i : integer;
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
        except_str = "Undeclared Function: knows"
        self.assertTrue(TestChecker.test(input_str, except_str, 473))

    def test_static75(self):
        input_str = """
        climbStairs : function integer (n : integer) {
            if (n == 1) {
                return 1;
            }
            first : integer= 1;
            second : integer = 2;
            i : integer;
            for (i = 3, i <= n, i + 1) {
                third : integer = first + second;
                first = second;
                second = third;
            }
            return second;
        }
        main: function void () {
            n : integer = 4;
            printInteger(climbStairs(n));
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 474))

    def test_static76(self):
        input_str = """
        a: integer = 1;
        foo: function void (b: integer) inherit a {}
        a: function string (inherit c: string) {}
        """
        expect_str = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input_str, expect_str, 475))

    def test_static77(self):
        input_str = """
        a: float = foo(1, 2) + 1.5;
        foo: function auto(a: integer, b: integer) {
            return a + b;
        }
        main: function void() {
            printInteger(a);
        }
        """
        except_str = "Type mismatch in statement: CallStmt(printInteger, Id(a))"
        self.assertTrue(TestChecker.test(input_str, except_str, 476))

    def test_static78(self):
        input_str = """
        x : auto={4,5,6};
        y:  auto=x[1,2];
        """
        except_str = "Type mismatch in expression: ArrayCell(x, [IntegerLit(1), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input_str, except_str, 477))

    def test_static79(self):
        input_str = """
        a: array[2,2] of integer;
        b: array[2] of integer = a[0];
        """
        except_str = "No entry point"
        self.assertTrue(TestChecker.test(input_str, except_str, 478))

    def test_static80(self):
        input_str = """
            arr: array [2,2,2,2] of integer = {
                {
                    { {1, 2}, {3, 4} },
                    { {5, 6}, {7, 8} }
                },
                {
                    { {9, 10}, {11, 12} },
                    { {13, 14}, {15, 16} }
                }
            };
            a : array[2] of integer = arr[0,3,1];
        """
        except_str = "No entry point"
        self.assertTrue(TestChecker.test(input_str, except_str, 479))

    def test_static81(self):
        input_str = """
        foo: function integer(a:auto, b:auto){
            x:integer = a + 1;
            y:string = b :: "abc";
            return x + 1;
        }
        main:function void(){
            foo(1, 2);
            foo2("abc", "abc");
        }
        foo2: function integer(a:auto, b:auto){
            x:integer = a + 1;
            y:string = b :: "abc";
        }
        """
        except_str = "Type mismatch in statement: CallStmt(foo, IntegerLit(1), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input_str, except_str, 480))

    def test_static82(self):
        input_str = """
        func: function integer() {
            a: integer = 12;
            return 3;
            a: float = 14;
        }
        """
        except_str = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input_str, except_str, 481))

    def test_static83(self):
        input_str = """
        func: function integer(a: integer) {
            if (a < 13) return 16;
            else a = a + 1;
            a: float = 12; 
            return 10;
        }
        """
        except_str = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input_str, except_str, 482))

    def test_static84(self):
        # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8953
        input_str = """
        foo: function integer(){}
        main: function void(){
            foo: integer = 3;
            a: integer;
            a = foo(); // line 5
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 483))

    def test_static85(self):
        input_str = """
        bar: function void (inherit a: integer){}
        foo: function void (a: integer) inherit bar {
            super(a);
        }
        """
        except_str = "Invalid Parameter: a"
        self.assertTrue(TestChecker.test(input_str, except_str, 484))

    def test_static86(self):
        input_str = """
        a: integer = 1;
        foo: function void (b: integer) inherit a {}
        a: function string (inherit c: string) {}
        """
        except_str = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input_str, except_str, 485))

    def test_static87(self):
        input_str = """
        a: float;
        main: function integer (n: integer) {
            a: integer;
            printInteger(a);
            {
                a: boolean;
                printBoolean(a);
                {
                    a: string;
                    printString(a);
                    {
                        printString(a);
                    }
                }
            }
        }
        """
        expect_str = "No entry point"
        self.assertTrue(TestChecker.test(input_str, expect_str, 486))

    def test_static88(self):
        input_str = """
            main: function void () {
            a : integer;
            b : integer;
            if (a > 10) {
                if (b > 10) {
                    printFloat(1.2);
                }
                else {
                    readString();
                }
            }
            else {
                s : string = "Hello";
                printString(s);
            }
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 487))

    def test_static89(self):
        input_str = """
            binarySearch: function integer (arr: array [10] of integer, target: integer) {
                low : integer = 0;
                high : integer = 9;
                while (low <= high) {
                    mid : integer = (low + high) / 2;
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
        except_str = "No entry point"
        self.assertTrue(TestChecker.test(input_str, except_str, 488))

    def test_static90(self):
        input_str = """
        rotate : function void (nums : array[7] of integer, k : integer) {
            n : integer = 7;
            k = k % n;
            if (k == 0) {
                return;
            }
            reverse(nums, 0, n - 1);
            reverse(nums, 0, k - 1);
            reverse(nums, k, n - 1);
        }
        main: function void () {
            nums : array [7] of integer = {1, 2, 3, 4, 5, 6, 7};
            k : integer = 3;
            rotate(nums, k);
        }
        """
        except_str = "Undeclared Function: reverse"
        self.assertTrue(TestChecker.test(input_str, except_str, 489))

    def test_static91(self):
        input_str = """
        main : function void() {
            do {
                printString("Hello");
            }
            while (true);
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 490))

    def test_static92(self):
        input_str = """
        strings: array [2,3,2] of string = {{{"1","2"},{"1","2"},{"1","1"}},{{"1","1"},{"1","1"},{"1","1"}}};
        main : function void() {}
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 491))

    def test_static93(self):
        input_str = """
        main : function void() {
            a : integer = foo() + 2;
            b : float = goo() + 2.3;
        }
        foo : function auto() {
            return 1;
        }
        goo : function auto() {
            return "2";
        }
        """
        except_str = "Type mismatch in statement: ReturnStmt(StringLit(2))"
        self.assertTrue(TestChecker.test(input_str, except_str, 492))

    def test_static94(self):
        input_str = """
        foo : function auto() {
            return 1;
        }
        goo : function auto() {
            return "2";
        }
        main : function void() {
            a : float = foo() + 2.3;
            b : string = goo() :: "a";
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 493))

    def test_static95(self):
        input_str = """
        foo : function auto() {
            if (true) {
                return 1;
            }
            else return 2;
            return 1;
            return "asfasF";
        }
        goo : function auto() {
            return "2";
        }
        main : function void() {
            a : float = foo() + 2.3;
            b : string = goo() :: "a";
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 494))

    def test_static96(self):
        input_str = """
        x : auto = 2 + 3.4;
        main : function void() {
            {
                x : string = "a";
                printString(x);
            }
            printFloat(x);
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 495))

    def test_static96(self):
        input_str = """
        main : function void() {
            i : integer ; 
            for (i = 0 , i < 10 , i +1 ) {
                continue;
            }
            break;
        }
        """
        except_str = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input_str, except_str, 496))

    def test_static97(self):
        input_str = """
        main : function void() {
            i : integer ; 
            for (i = 0 , i < 10 , i +1 ) {
                if (i == 5) {
                    break;
                    if (true) {
                        continue;
                    }
                }
            }
        }
        """
        except_str = ""
        self.assertTrue(TestChecker.test(input_str, except_str, 497))

    def test_static98(self):
        input = """a : array[2] of integer = {1,2,3};"""
        except_str = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"
        self.assertTrue(TestChecker.test(input, except_str, 498))

    def test_static99(self):
        input_str = """
        a : array[2,3] of integer = {{1,2,3},{4,5,6}};
        b : array[3] of integer = a[1.0];
        """
        except_str = "Type mismatch in expression: ArrayCell(a, [FloatLit(1.0)])"
        self.assertTrue(TestChecker.test(input_str, except_str, 499))

    def test_static100(self):
        input_str = """
        a : array[2,3] of integer = {{1,2,3},{4,5,6}};
        b : integer = a[1,2.0];
        """
        except_str = "Type mismatch in expression: ArrayCell(a, [IntegerLit(1), FloatLit(2.0)])"
        self.assertTrue(TestChecker.test(input_str, except_str, 500))

    def test_static101(self):
        input_str = """
        foo : function auto() {}
        main : function string() {
            printString("ab");
            return foo();
            x: string = foo();
        }
        """
        except_str = "No entry point"
        self.assertTrue(TestChecker.test(input_str, except_str, 501))

    def test_static102(self):
        input_str = """
        foo : function string() {
            if (true) {
                return goo();
            }
            else return "b";
            return "a";
        }
        main : function string() {
            printString(goo());
        }
        goo : function auto() {
            return 2;
        }
        """
        except_str = "Type mismatch in statement: ReturnStmt(IntegerLit(2))"
        self.assertTrue(TestChecker.test(input_str, except_str, 502))
