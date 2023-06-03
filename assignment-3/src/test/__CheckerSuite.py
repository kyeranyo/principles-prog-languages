import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_undeclared_function1(self):
        """Simple program: int main() {} """
        input = """f : integer = "abc";"""
        expect = "Type mismatch in Variable Declaration: VarDecl(f, IntegerType, StringLit(abc))"
        self.assertTrue(TestChecker.test(input,expect,101))

    def test_undeclared_function2(self):
        """Simple program: int main() {} """
        input = """
            var : string = 123;
            main: function void(){}"""
        expect = "Type mismatch in Variable Declaration: VarDecl(var, StringType, IntegerLit(123))"
        self.assertTrue(TestChecker.test(input,expect,102))

    def test_undeclared_function3(self):
        """Simple program: int main() {} """
        input = """
            var : string = "abc";
            main: function void(){}
            main: function void(){}
            """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,103))

    def test_undeclared_function4(self):
        """Simple program: int main() {} """
        input = """
            var : string = "abc";
            main: function void(){}
            """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,104))

    def test_undeclared_function5(self):
        """Simple program: int main() {} """
        input = """
            var : auto = "abc";
            func: function void(alpha : string, delta : integer){
                alpha : string;
            }
            main: function void(){}
            """
        expect = "Redeclared Variable: alpha"
        self.assertTrue(TestChecker.test(input,expect,105))

    def test_undeclared_function6(self):
        """Simple program: int main() {} """
        input = """
            var : auto = "abc";
            func: function void(alpha : string, delta : integer){
            }
            main: function void(){}
            """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,106))

    def test_undeclared_function7(self):
        """Simple program: int main() {} """
        input = """
            var : auto = "abc";
            func: function void(alpha : string, delta : integer){
                func2();
                func3();
            }
            main: function void(){}
            func2 : function void (){}
            func3 : function void () {}
            """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,107))

    def test_undeclared_function8(self):
        """Simple program: int main() {} """
        input = """
            var : auto = "abc";
            func: function void(alpha : string, delta : integer){
                var = "abc";
                func("123", 11);
            }
            main: function void(){}
            func2 : function void (alpha : string, delta : integer){}
            func3 : function void (alpha : string, delta : integer) {}
            """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,108))

    def test_undeclared_function9(self):
        """Simple program: int main() {} """
        input = """
            var : auto = "abc";
            a : integer = 1;
            func: function void(alpha : string, delta : integer){
                a = a + 1;
            }
            main: function void(){}
            func2 : function void (alpha : string, delta : integer){}
            func3 : function void (alpha : string, delta : integer) {}
            """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,109))

    def test_undeclared_function10(self):
        """Simple program: int main() {} """
        input = """
            var : auto = "abc";
            a : integer = 1;
            func: function void(alpha : string, delta : integer){
                b : auto = "abc";
                b = var;
                
            }
            main: function void(){}
            func2 : function void (alpha : string, delta : integer){}
            func3 : function void (alpha : string, delta : integer) {}
            """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,110))

    def test_undeclared_function11(self):
        """Simple program: int main() {} """
        input = """
            v : auto = 1;
            c : auto = 1.0;
            e : auto = "abc";
            func: function void(alpha : string, delta : integer){
                b : string;
                b = v + c + e;
                
            }
            main: function void(){}
            func2 : function void (alpha : string, delta : integer){}
            func3 : function void (alpha : string, delta : integer) {}
            """
        expect = "Type mismatch in expression: BinExpr(+, BinExpr(+, Id(v), Id(c)), Id(e))"
        self.assertTrue(TestChecker.test(input,expect,111))

    def test_undeclared_function12(self):
        """Simple program: int main() {} """
        input = """
            a : string = "123";
            b : integer = 123;
            c : boolean = true;
            d : integer = 123;
            e : auto = 1;
            f : auto = 2;
            func: function void(alpha : string, delta : integer){
                i : auto = 1;
                k: auto = 2;

                g : auto = 1 + b;
                
            }
            main: function void(){}
            func2 : function void (alpha : string, delta : integer){
                //func2(alpha, a);
            }
            func3 : function void (alpha : string) {}
            """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,112))

    def test_undeclared_function13(self):
        """Simple program: int main() {} """
        input = """

            func: function void(alpha : string, delta : integer){
                k: auto = "123";
                g : auto = alpha :: k;
                
            }
            main: function void(){}
            func2 : function void (alpha : string, delta : integer){
                //func2(alpha, a);
            }
            func3 : function void (alpha : string) {}
            """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,113))

    def test_undeclared_function14(self):
        """Simple program: int main() {} """
        input = """
            a : string = "123";
            b : integer = 123;
            c : boolean = true;
            d : integer = 123;
            e : auto = true;
            f : auto = false;
            func: function void(alpha : string, delta : integer){
                i : auto = 1;
                k: auto = "123";
                e = false;
                g : auto = alpha :: k;
                m : auto = b + delta;

                z : string = g :: a;

                f = e && c;
                f = f || e;
                l : auto = f && !c;
                
            }
            main: function void(){}
            func2 : function void (alpha : string, delta : integer){
                //func2(alpha, a);
            }
            func3 : function void (alpha : string) {}
            """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,114))

    def test_undeclared_function15(self):
        """Simple program: int main() {} """
        input = """
            var : auto = "abc";
            func: function void(alpha : string, delta : integer){
                func2();
                c : string;
                b : integer;
                a : auto = func3(c,b);
                a = func3(func3(a, b), b);
                a = func2() :: func3(a, b);
            }
            main: function void(){}
            func2 : function string (){}
            func3 : function string (a : string, b : integer) {}
            """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,115))

    def test_undeclared_function16(self):
        """Simple program: int main() {} """
        input = """
            var : auto = "abc";
            func: function void(alpha : string, delta : integer){
                func2();
                c : string;
                b : integer;
                a : auto = func3(c,b);
                a = func3(func3(a, b), b);
                a = func2() :: func3(a, b);
            }
            main: function void(){}
            func2 : function string (){}
            func3 : function string (a : string, b : integer) {}
            """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,116))

    def test_undeclared_function17(self):
        """Simple program: int main() {} """
        input = """
            var : auto = "abc";
            func: function void(alpha : string, delta : integer){
                A : array [2,3,4,5] of integer;
                B : integer;
                i : auto = 12;
                A[i,1,2,4] = 1;
                F : string = func(var, B);
            }
            main: function void(){}
            """
        expect = "Type mismatch in Variable Declaration: VarDecl(F, StringType, FuncCall(func, [Id(var), Id(B)]))"
        self.assertTrue(TestChecker.test(input,expect,117))

    def test_undeclared_function18(self):
        """Simple program: int main() {} """
        input = """
            var : auto = "abc";
            func: function void(alpha : string, delta : integer){
                A : array [1] of integer = {1};
                B : integer;
                i : auto = 12;
                A[i] = 1;
                F : string = func(var, B);
            }
            main: function void(){}
            """
        expect = "Type mismatch in Variable Declaration: VarDecl(F, StringType, FuncCall(func, [Id(var), Id(B)]))"
        self.assertTrue(TestChecker.test(input,expect,118))

    def test_undeclared_function19(self):
        """Simple program: int main() {} """
        input = """
            var : auto = "abc";
            func: function void(alpha : string, delta : integer){
                break;
            }
            main: function void(){}
            """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input,expect,119))

    def test_undeclared_function20(self):
        """Simple program: int main() {} """
        input = """
            var : auto = "abc";
            B : auto = 1;
            func: function void(alpha : string, delta : integer){
                if(B > 0){
                    B = 0;
                    //continue;
                } else {
                    B = 1;
                }
            }
            main: function void(){}
            """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,120))

    def test_undeclared_function21(self):
        """Simple program: int main() {} """
        input = """
            var : auto = "abc";
            B : auto = 1;
            func: function void(alpha : string, delta : integer){
                if(B > 0){
                    B = 0;
                } else {
                    B = 1;
                }
                i : integer;
                for (i = 0, i < 10 , i + 1){
                    var : auto = "abc";
                    c : auto = 12314;
                    var = var :: "abc";
                    break;
                    continue;
                }
                z : integer;
                return;
            }
            main: function void(){}
            """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,121))

    def test_undeclared_function22(self):
        """Simple program: int main() {} """
        input = """
            var : auto = "abc";
            B : auto = 1;
            func: function string(alpha : string, delta : integer){
                continue;
                return 1;
            }
            main: function void(){}
            func2 : function string(alpha : string, delta : integer){}
            func3 : function string(alpha : string, delta : integer){}
            """
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input,expect,122))

    def test_undeclared_function23(self):
        """Simple program: int main() {} """
        input = """
            var : auto = "abc";
            B : auto = 1;
            integers: array [2,3,1] of auto = {{{"a"},{"1"},{"1"}},{{"1"},{"1"},{"1"}}};
            a : string = "hello world";
            c : float = 812.123e-10;
            func: function string(alpha : string, delta : integer){
                integers[0,0,0] = "abc";
                i : integer;
                if (i==1) 
                    if (i==2)
                        if (i > 3)
                            if (i>=5)
                                return "No matter what we breed";
                            else {
                                a = "abc";
                                j : auto = 1;
                            }
                return "";
            }
            main: function void(){}
            func2 : function string(alpha : string, delta : integer){}
            func3 : function string(alpha : string, delta : integer){}
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 123))

    def test_undeclared_function24(self):
        """Simple program: int main() {} """
        input = """
            var : auto = "abc";
            B : auto = 1;
            integers: array [2,3,1] of auto = {{{"a"},{"1"},{"1"}},{{"1"},{"1"},{"1"}}};
            a : string = "hello world";
            c : float = 812.123e-10;
            func: function string(alpha : string, delta : integer){
                integers[0,0,0] = "abc";
                i : integer;
                if (i==1) 
                    if (i==2)
                        if (i > 3)
                            if (i>=5)
                                return "No matter what we breed";
                            else {
                                a = "abc";
                                j : auto = 1;
                                integers[0,0,0] = "abc";
                            }
                for (i = 0, i < B, i + 1){
                    integers[0,0,0] = "abc";
                    if (false || true){
                        i = 2;
                        integers[0,0,0] = "abc";
                        break;
                    }
                    else if (false || true){
                        i = 9;
                        var : array [2,2] of auto = {{1,2},{3,4}};
                        a = "abc";
                        continue;
                    }
                    else break;
                }
                return "";
            }
            main: function void(){}
            func2 : function string(alpha : string, delta : integer){}
            func3 : function string(alpha : string, delta : integer){}
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 124))

    def test_undeclared_function25(self):
        """Simple program: int main() {} """
        input = """
            var : auto = "abc";
            B : auto = 1;
            integers: array [2,3,1] of auto = {{{"a"},{"1"},{"1"}},{{"1"},{"1"},{"1"}}};
            a : string = "hello world";
            c : float = 812.123e-10;
            func: function string(alpha : string, delta : integer){
                integers[0,0,0] = "abc";
                i : integer;
                if (i==1) 
                    if (i==2)
                        if (i > 3)
                            if (i>=5)
                                return "No matter what we breed";
                            else {
                                a = "abc";
                                j : auto = 1;
                                integers[0,0,0] = "abc";
                            }
                for (i = 0, i < B, i + 1){
                    integers[0,0,0] = "abc";
                    if (false || true){
                        i = 2;
                        integers[0,0,0] = "abc";
                        break;
                    }
                    else if (false || true){
                        i = 9;
                        var : array [2,2] of auto = {{1,2},{3,4}};
                        a = "abc";
                        continue;
                    }
                    else break;
                }
                return "";
                do{
                    integers[0,0,0] = "abc";
                }
                while(i == 0);
            }
            main: function void(){}
            func2 : function string(alpha : string, delta : integer){}
            func3 : function string(alpha : string, delta : integer){}
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 125))

    def test_undeclared_function26(self):
        """Simple program: int main() {} """
        input = """
            var : auto = 1;
            func: function string(alpha : string, delta : integer){
                var : auto = func2("123", 1) + 123;
                var = var - func2("123", 2);
                b : auto = 1;
                c : integer = delta + b;

            }
            //main: function void(){}
            func2 : function auto (alpha : string, delta : integer){}
            func3 : function string(alpha : string, delta : integer){}
            """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 126))

    def test_undeclared_function27(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            var : auto = 1;
            func: function string(alpha : string, delta : integer) inherit func3{
                super(1,2);
                var : auto = func2("123", 1) + 123;
                var = var - func2("123", 2);
                b : auto = 1;
                c : integer = delta + b;

            }
            main: function void(){}
            func2 : function auto (alpha : string, delta : integer){}
            func3 : function string(){}
            """
        expect = "Type mismatch in expression: IntegerLit(1)"
        self.assertTrue(TestChecker.test(input, expect, 127))

    def test_undeclared_function28(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            var : auto = 1;
            func: function string(alpha : string, delta : integer){
                x, y: integer = 1, foo(1, 2, 3);  //1
                x, y: string;                     //2
            }
            main: function void(){}
            func2 : function auto (alpha : string, delta : integer){}
            func3 : function string(){}
            foo: function integer (x: integer, y: integer, y:integer){}   //3
            """
        expect = "Redeclared Parameter: y"
        self.assertTrue(TestChecker.test(input, expect, 128))

    def test_undeclared_function29(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            //var : string = foo(1.0, 2);
            foo : function auto (inherit z : auto, t:auto) inherit func{
                super(1,2);
                z = 5;
                return z + t;
            }
            a : auto = foo(2.0, 2);
            b : auto = foo(3.0, 1);
            c : float = a + b;
            main : function void() {}
            func : function void(inherit a : auto, t:auto) {}
            """
        expect = "Type mismatch in expression: FuncCall(foo, [FloatLit(2.0), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 129))

    def test_undeclared_function30(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            //var : string = foo(1.0, 2);
            foo : function auto (inherit z : auto, t:auto) inherit func{
                preventDefault();
                z = 5;
                return z + t;
            }
            a : auto = foo(2.0, 2);
            b : auto = foo(3.0, 1);
            c : float = a + b;
            main : function void() {}
            func : function void() {}
            """
        expect = "Type mismatch in expression: FuncCall(foo, [FloatLit(2.0), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 130))

    def test_undeclared_function31(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            func : function void() {}
            func2 : function void(inherit a : auto, inherit b:auto) inherit func {
                super();
            }
            main : function void(){}
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 131))

    def test_undeclared_function32(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            func : function void() {}
            a : auto = 1;
            b : auto = 2;
            c : auto = 3;
            d : auto = 4;
            func2 : function void(inherit a : auto, inherit b:auto) inherit func {
                super();
                if ( c == 1){
                    b = a + b * c * d - c / 3;
                }
            }
            func3 : function void(inherit c : auto, inherit d:auto) inherit func2 {
                super(1,2);
            }
            func4 : function void(inherit j : auto, inherit f:auto) inherit func3 {
                super(1,2);
                d = b :: "abc";
                a : string;
            }
            main : function void(){}
            """
        expect = "Type mismatch in expression: BinExpr(::, Id(b), StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 132))

    def test_undeclared_function33(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            func : function auto (a : float, b : integer){
                return a;
            }
            c : integer = func(1,3);
            """
        expect = "Type mismatch in Variable Declaration: VarDecl(c, IntegerType, FuncCall(func, [IntegerLit(1), IntegerLit(3)]))"
        self.assertTrue(TestChecker.test(input, expect, 133))

    def test_undeclared_function34(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            func : function auto (a : float, b : integer){
                c : auto = 1;
                if (c == b){
                    return c;
                } 
                else {
                    return b;
                }
                return b;
                return "abc";
            }
            c : integer = func(1,3);
            """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 134))

    def test_undeclared_function35(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            func : function auto (a : float, b : integer){
                c : auto = 1;
                if (c == b){
                    readInteger();
                    return c;
                } 
                else {
                    readFloat();
                    return b;
                }
                return b;
                return "abc";
                
            }
            c : integer = func(1,3);
            """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 135))

    def test_undeclared_function36(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            func : function auto (a : float, b : integer){
                c : auto = 1;
                if (c == b){
                    readInteger();
                    printFloat(a);
                    return c;
                } 
                else {
                    readFloat();
                    return b;
                }
                return b;
                return "abc";
                
            }
            c : integer = func(1,3);
            """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 136))

    def test_undeclared_function37(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            func : function auto (a : float, b : integer){
                c : auto = 1;
                if (c == b){
                    readInteger();
                    printFloat(a);
                    return c;
                } 
                else {
                    readFloat();
                    return b;
                }
                return b;
                return "abc";
                
            }
            c : integer = func(1,3);
            """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 137))

    def test_undeclared_function38(self):
        """Simple program: int main() inherit func2 {} """
        input= """
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
        expect = "Type mismatch in statement: ReturnStmt(StringLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 138))

    def test_undeclared_function39(self):
        """Simple program: int main() inherit func2 {} """
        input = """
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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 139))

    def test_undeclared_function40(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            var : string = "hello world";
            sub : function boolean(var : string, delta : boolean) {
                str = "wtf r u doing here !!!";
            }
            main: function void(){
                do{
                    return false;
                }while(n == 0);
                var = "Lau Dai Tinh Ai" :: var;
                if (n == 0) {}
                else {}
            }
        """
        expect = "Undeclared Identifier: str"
        self.assertTrue(TestChecker.test(input, expect, 140))

    def test_undeclared_function41(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            var : string = "hello world";
            main: function void(){
                var : integer = 1;
                if (a > 0) var2 : integer = 2;
                do{
                    return false;
                }while(n == 0);
                var = "Lau Dai Tinh Ai" :: var;
                for(i = 0, i < n, i + 1) {}
                test(123, ytx, 5+2+5+5);
            }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 141))

    def test_undeclared_function42(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            var : string = "hello world";
            main : function void(){
                do{
                    return false;
                }while(n == 0);
                var = "Lau Dai Tinh Ai" :: var;
            }
        """
        expect = "Undeclared Identifier: n"
        self.assertTrue(TestChecker.test(input, expect, 142))

    def test_undeclared_function43(self):
        """Simple program: int main() inherit func2 {} """
        input = """
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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 143))

    def test_undeclared_function44(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            /* main function */
            ac : float = 12.0e-10;
            main: function float () {
                a = true || false;
            }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 144))

    def test_undeclared_function45(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            /* main function */
            ac : float = 12.0e-10;
            str : auto = "abc";
            main: function float () {
                a = true || false;
                a[0] = 19 + 123 + 19 * 13 -10 ;
            }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 145))

    def test_undeclared_function46(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            /* main function */
            main: function float () {
                a = true || false;
                a = as[1] + 123 - 1 + a[a[0]];
            }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 146))

    def test_undeclared_function47(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            /* main function */
            factor : integer = 10.0;
            main: function float () {
                a = true || false;
                foo(123 +13 -1 + foo(5));
            }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(factor, IntegerType, FloatLit(10.0))"
        self.assertTrue(TestChecker.test(input, expect, 147))

    def test_undeclared_function48(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            /* main function */
            ac : float = 12.0e-10;
            main: function float () {
                a = {};
            }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 148))

    def test_undeclared_function49(self):
        """Simple program: int main() inherit func2 {} """
        input = """
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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 143))

    def test_undeclared_function50(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            foo : function integer (a : integer) inherit goo {
                super(a);

            }
            goo : function integer (inherit a : integer) {}
            main: function void () {}
        """
        expect = "Invalid Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 150))

    def test_undeclared_function51(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            /* main function */

            delta : boolean = true;
            main: function float (a : auto, b: auto) {
                n = 10 + 132 * x / 10 == 0 + cn;
                for (i = 0 , i > n , i + 1) break;
                while(n && a) continue;
                do {} while(n || a);
                if ( n > 0) {
                    var : string = "hello" ::  "world";
                } else return 0;
                if ( n && 0 ){
                    while(n == 0){
                        return false;
                    }
                    for (i = 0, i < 5, i +1 ){
                        a = 10;
                        a = a + 123 && b - 10 * 18 -19;
                    }
                }
            }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 151))

    def test_undeclared_function52(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            /* main function */
            main: function float () {
                a = true && false;
            }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 152))

    def test_undeclared_function53(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            /* main function */
            /* main function */
            ac : float = 12.0e-10;
            str : auto = "abc";
            main: function float () {
                a = "don't get too close, it's dark inside" :: "it's where my demon hide";
            }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 153))

    def test_undeclared_function54(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            func: function void () {
                if ("i wanna hide the truth") 
                    while("i wanna shelter you")
                        if ("but with the beast inside")
                            while("there's nowhere we can hide")
                                return "No matter what we breed";
            }
        """
        expect = "Type mismatch in statement: IfStmt(StringLit(i wanna hide the truth), WhileStmt(StringLit(i wanna shelter you), IfStmt(StringLit(but with the beast inside), WhileStmt(StringLit(there's nowhere we can hide), ReturnStmt(StringLit(No matter what we breed))))))"
        self.assertTrue(TestChecker.test(input, expect, 154))

    def test_undeclared_function55(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            func: function void () {
                if ("i love you") 
                    if ("but")
                        if ("you don't love me")
                            if ("make")
                                printString("me and my broken heart");
            }
        """
        expect = "Type mismatch in statement: IfStmt(StringLit(i love you), IfStmt(StringLit(but), IfStmt(StringLit(you don't love me), IfStmt(StringLit(make), CallStmt(printString, StringLit(me and my broken heart))))))"
        self.assertTrue(TestChecker.test(input, expect, 155))

    def test_undeclared_function56(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            func: function void () {
                i : auto = 1;
                if (i==1) 
                    if (i==2)
                        if (i > 3)
                            if (i>=5)
                                printString("I love you");
            }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 156))

    def test_undeclared_function57(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            ac : float = 12.0e-10;
            str : auto = "abc";
            main: function float () {
                a = true || false;

            }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 157))

    def test_undeclared_function58(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            /* main function */
            ac : float = 12.0e-10;
            main: function float () {
                /* anh muon ta ve cung mot nha, an sang va cung hat ca */ // nhung biet sao gio 
                a = true || false;
            }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 158))

    def test_undeclared_function59(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            /* main function */
            factor : integer = 10.0;
            main: function float () {
                /*tran khac chan nam qua xa, */ \n //ve day voi nhau hai dua dap chung men*/ abcxyz
                a = true || false;
            }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(factor, IntegerType, FloatLit(10.0))"
        self.assertTrue(TestChecker.test(input, expect, 159))

    def test_undeclared_function60(self):
        """Simple program: int main() inherit func2 {} """
        input = """
             /* main function */
            main: function float () {
                a = 1_23.40E+156;
            }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 160))

    def test_undeclared_function61(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            /* main function */
            ac : float = 12.0e-10;
            str : auto = "abc";
            a : auto = 1;
            main: function float () {
                a = 3200_21000_123_000;

            }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 161))

    def test_undeclared_function62(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            /* main function */
            ac : float = 12.0e-10;
            a : auto = 1;
            main: function float () {
                a = 1_23_1414_214;
            }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 162))

    def test_undeclared_function63(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            /* main function */
            /* main function */
            factor : integer = 10.0;
            main: function float () {
                a : auto = "He asked me: \\\"Where is John?\\\"";
            }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(factor, IntegerType, FloatLit(10.0))"
        self.assertTrue(TestChecker.test(input, expect, 163))

    def test_undeclared_function64(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            main: function float () {
                n = strlen(str);
                for (i = 0, i < n / 2,  i + 1) {
                    swap(str[i], str[n - i - 1]);
                }
            }
        """
        expect = "Undeclared Function: strlen"
        self.assertTrue(TestChecker.test(input, expect, 164))

    def test_undeclared_function65(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            /* main function */
            ac : float = 12.0e-10;
            str : auto = "abc";
            main: function float () {
                a : auto = true || false;
                b : auto;
            }
        """
        expect = "Invalid Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 165))

    def test_undeclared_function66(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            main:function void() inherit foo{
                super(12);
                x:auto = foo(1);
                foo2();
                arr:array[2,2] of integer = {{1,2}, {1,2}};
                arr[1,2,3] = 1;
            }
            foo:function float(x:integer){
                return x + 1.2;
            }
            foo2: function void(){}
        """
        expect = "Type mismatch in expression: ArrayCell(arr, [IntegerLit(1), IntegerLit(2), IntegerLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 166))

    def test_undeclared_function67(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            var : auto = 1;
            func: function string(alpha : string, delta : integer) inherit func3{
                super(51,2);
                var : auto = func2("123", 1) + 123;
                var = var - func2("123", 2);
                b : auto = 1;
                c : integer = delta + b;

            }
            main: function void(){}
            func2 : function auto (alpha : string, delta : integer){}
            func3 : function string(){}
        """
        expect = "Type mismatch in expression: IntegerLit(51)"
        self.assertTrue(TestChecker.test(input, expect, 167))

    def test_undeclared_function68(self):
        """Simple program: int main() inherit func2 {} """
        input = """
        foo: function integer(inherit x: integer) inherit bar
        {
            super(2);
        }
        bar: function integer(inherit y: integer) inherit foo2 
        {
            super("Hi");
        }
        foo2: function integer(inherit z: float)
        {

        }
        """
        expect = "Type mismatch in expression: StringLit(Hi)"
        self.assertTrue(TestChecker.test(input, expect, 168))

    def test_undeclared_function69(self):
        """Simple program: int main() inherit func2 {} """
        input = """
        a: integer = 1;
        foo: function void (b: integer) inherit a {}
        a: function string (inherit c: string) {}
        """
        expect = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input, expect, 169))

    def test_undeclared_function70(self):
        """Simple program: int main() inherit func2 {} """
        input = """
        foo1: function void(inherit a: integer, inherit b: integer) {}
        foo2: function void(a: integer, x: float) inherit foo1 {
            preventDefault();
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 170))

    def test_undeclared_function71(self):
        """Simple program: int main() inherit func2 {} """
        input = """
        f,y : integer = {"abc", "xyz"}, 1==1 ;
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(f, IntegerType, ArrayLit([StringLit(abc), StringLit(xyz)]))"
        self.assertTrue(TestChecker.test(input, expect, 171))

    def test_undeclared_function72(self):
        """Simple program: int main() inherit func2 {} """
        input = """
        f,y : integer = {"abc", "xyz"}, 1==1 ;
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(f, IntegerType, ArrayLit([StringLit(abc), StringLit(xyz)]))"
        self.assertTrue(TestChecker.test(input, expect, 172))

    def test_undeclared_function73(self):
        """Simple program: int main() inherit func2 {} """
        input = """
        fac: array [4] of string = {"tokyo", "newyork", "london"};
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(fac, ArrayType([4], StringType), ArrayLit([StringLit(tokyo), StringLit(newyork), StringLit(london)]))"
        self.assertTrue(TestChecker.test(input, expect, 173))

    def test_undeclared_function74(self):
        """Simple program: int main() inherit func2 {} """
        input = """
        f : auto = 1 + 2 -3 * 5 /10 + foo(x,z,t) ;
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 174))

    def test_undeclared_function75(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            a: integer = func(10);
            main: function string () {
                for(i = 3, i <= 10, i + 1) {
                    sum = sum + i;
                }
                print("I Love you");
            }
        """
        expect = "Undeclared Function: func"
        self.assertTrue(TestChecker.test(input, expect, 175))

    def test_undeclared_function76(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            a: integer = func(10);
            main: function string () {
                for(i = 3, i <= 10, i + 1) {
                    sum = sum + i;
                }
                print("I Love you");
            }
        """
        expect = "Undeclared Function: func"
        self.assertTrue(TestChecker.test(input, expect, 176))

    def test_undeclared_function77(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            ABNCASDH : auto ;
            main: function void(){
                a : auto = 2.128431e-3;
                var = se % 10 + 10 - 1;
                a : auto = "string";
                // abc yxy comment is here ??
                /* abcas uasdn uqwnsdad */
                while(acn > 10 + 1){
                    s = l + 1;
                    for ( i = 1, j > 0 , c + 1){
                        return a + fact(12);
                    }
                }
            }
        """
        expect = "Invalid Variable: ABNCASDH"
        self.assertTrue(TestChecker.test(input, expect, 177))

    def test_undeclared_function78(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            main: function void(){
                a : auto = 12.128431e-10;
                var = se % 10 + 10 - 1;
                a : auto = "string";
                // abc yxy comment is here ??
                /* abcas uasdn uqwnsdad */
                while(acn > 10 + 1){
                    s = l + 1;
                    for ( i = 1, j > 0 ,  c + 1){
                        return a + fact(12);
                    }
                }
            }
        """
        expect = "Undeclared Identifier: se"
        self.assertTrue(TestChecker.test(input, expect, 178))

    def test_undeclared_function79(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            main: function void(){
                a : auto = 12.128431e-10;
                var = se % 10 + 10 - 1;
                a : auto = "string";
                while(acn > 10 + 1){
                    s = l + 1;
                    for ( i = 1, j > 0 ,  c + 1){
                        return a + fact(12);
                    }
                }
            }
        """
        expect = "Undeclared Identifier: se"
        self.assertTrue(TestChecker.test(input, expect, 179))

    def test_undeclared_function80(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            main: function void(){
                a : auto = 12.128431e-10;
                var = se % 10 + 10 - 1;
                c : boolean = false;
                while(acn > 10 + 1){
                    s = l + 1;
                    for ( i = 1, j > 0 , c + 1){
                        return a + fact(12);
                    }
                }
            }
        """
        expect = "Undeclared Identifier: se"
        self.assertTrue(TestChecker.test(input, expect, 180))

    def test_undeclared_function81(self):
        """Simple program: int main() inherit func2 {} """
        input = """
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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 181))

    def test_undeclared_function82(self):
        """Simple program: int main() inherit func2 {} """
        input = """
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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 182))

    def test_undeclared_function83(self):
        """Simple program: int main() inherit func2 {} """
        input = """
        main : function void() {
            i : integer ; 
            for (i = 0 , i < 10 , i +1 ) {
                continue;
            }
            break;
        }
        """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 183))

    def test_undeclared_function84(self):
        """Simple program: int main() inherit func2 {} """
        input = """
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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 184))

    def test_undeclared_function85(self):
        """Simple program: int main() inherit func2 {} """
        input = """
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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 185))

    def test_undeclared_function86(self):
        """Simple program: int main() inherit func2 {} """
        input = """
        inc : function void (out n : integer, a: float) inherit foo {} //1
        foo : function auto (inherit m: float, n: integer){} //2
        """
        expect = "Invalid statement in function: inc"
        self.assertTrue(TestChecker.test(input, expect, 186))

    def test_undeclared_function87(self):
        """Simple program: int main() inherit func2 {} """
        input = """
        foo: function auto () { return 1; }
        main: function void () {
            x: integer = goo() + foo();
        }
        goo: function auto () { 
            if (something) return 1; 
            else return true; 
        }
        """
        expect = "Undeclared Identifier: something"
        self.assertTrue(TestChecker.test(input, expect, 187))

    def test_undeclared_function88(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            binarySearch: function integer (arr: array [10] of integer, target: integer) {
            left: integer = 0;
            right: integer = 9;
            while (left <= right) {
                mid: integer = (left + right) / 2;
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
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 188))

    def test_undeclared_function89(self):
        """Simple program: int main() inherit func2 {} """
        input = """
        main: function void() {
            arr: auto = {5, 2, 8, 4, 9, 1, 3, 7, 6, 0};
            print("Original array: ");
            printArray(arr);
            insertionSort(arr);
            print("Sorted array: ");
            printArray(arr);
        }
        printArray: function void(arr: array[10] of integer) {
            for (i = 0, i < 10, i+1) {
                printInt(arr[i]);
                print(" ");
            }
            print("\\n");
        }
        insertionSort: function void(arr: array[10] of integer) {
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
        """
        expect = "Undeclared Function: print"
        self.assertTrue(TestChecker.test(input, expect, 189))

    def test_undeclared_function90(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            delta : float = 1.9;
            quadratic: function void (a: float, b: float, c: float) {
            delta = b * b - 4 * a * c;
            if (delta < 0) {
                printString("The equation has no real roots.");
            } else if (delta == 0) {
                root = -b / (2 * a);
                printString("The equation has one real root: ");
            } else {
                root1 = (-b + sqrt(delta)) / (2 * a);
                root2 = (-b - sqrt(delta)) / (2 * a);
                printString("The equation has two real roots: ");
            }
        }

        main: function void () {
            a = 2;
            b = 5;
            c = -3;
            quadratic(a, b, c);
        }
        """
        expect = "Type mismatch in expression: BinExpr(==, Id(delta), IntegerLit(0))"
        self.assertTrue(TestChecker.test(input, expect, 190))

    def test_undeclared_function91(self):
        """Simple program: int main() inherit func2 {} """
        input = """
             main: function void(){
                 a : auto = 12.128431e-10;
                 var = se % 10 + 10 - 1;
                 a : auto = "string";
                 // abc yxy comment is here ??
                 /* abcas uasdn uqwnsdad */

                 var = "em oi " + "lau dai tinh ai" :: "chac khong co tren tran gian";
                 while(acn > 10 + 1){
                     s = l + 1;
                     for ( i = 1, j > 0 , c + 1){
                         return a + fact(12);
                     }
                 }
             }
        """
        expect = "Undeclared Identifier: se"
        self.assertTrue(TestChecker.test(input, expect, 191))

    def test_undeclared_function92(self):
        """Simple program: int main() inherit func2 {} """
        input = """
             main: function void(){
                do {return 0;} while(b < 9);
             }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 192))

    def test_undeclared_function93(self):
        """Simple program: int main() inherit func2 {} """
        input = """
             main: function void(){
                do {return 0;} while(b < 9);
                for(i = 0 , i == 1-1, a *3) return ;
             }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 193))

    def test_undeclared_function94(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            integers: array [5] of integer = {1, 2, 3, "a"};
            a : integer = "hello world";
            c : float = 812.123e-10;
        """
        expect = "Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), StringLit(a)])"
        self.assertTrue(TestChecker.test(input, expect, 194))

    def test_undeclared_function95(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            f : integer = {"em dong y"};
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(f, IntegerType, ArrayLit([StringLit(em dong y)]))"
        self.assertTrue(TestChecker.test(input, expect, 195))

    def test_undeclared_function96(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            flot: integer = 10;
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 196))

    def test_undeclared_function97(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            main : function void (inherit out delta : integer){
                {}
            }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 197))

    def test_undeclared_function98(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            main : function void (inherit out delta : integer){
                if (n != 0 ) return 1;
            }
        """
        expect = "Undeclared Identifier: n"
        self.assertTrue(TestChecker.test(input, expect, 198))

    def test_undeclared_function99(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            main: function float () {}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 199))

    def test_undeclared_function100(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            main: function float () {
                n = 10 + 132 * x / 10 == 0 + cn;
                for (i = 0 , i > n , i + 1) break;
            }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 200))
