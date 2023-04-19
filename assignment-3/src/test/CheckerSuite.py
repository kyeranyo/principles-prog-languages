import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_undeclared_function1(self):
        """Simple program: int main() {} """
        input = """f : integer = "abc";"""
        expect = "Type mismatch in Variable Declaration: VarDecl(f, IntegerType, StringLit(abc))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_undeclared_function2(self):
        """Simple program: int main() {} """
        input = """
            var : string = 123;
            main: function void(){}"""
        expect = "Type mismatch in Variable Declaration: VarDecl(var, StringType, IntegerLit(123))"
        self.assertTrue(TestChecker.test(input,expect,101))

    def test_undeclared_function3(self):
        """Simple program: int main() {} """
        input = """
            var : string = "abc";
            main: function void(){}
            main: function void(){}
            """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,102))

    def test_undeclared_function4(self):
        """Simple program: int main() {} """
        input = """
            var : string = "abc";
            main: function void(){}
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,103))

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
        self.assertTrue(TestChecker.test(input,expect,104))

    def test_undeclared_function6(self):
        """Simple program: int main() {} """
        input = """
            var : auto = "abc";
            func: function void(alpha : string, delta : integer){
            }
            main: function void(){}
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,105))

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
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,106))

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
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,107))

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
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,108))

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
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,109))

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
        self.assertTrue(TestChecker.test(input,expect,110))

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
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,111))

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
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,112))

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
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,113))

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
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,114))

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
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,115))

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
        self.assertTrue(TestChecker.test(input,expect,116))

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
        self.assertTrue(TestChecker.test(input,expect,117))

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
        self.assertTrue(TestChecker.test(input,expect,118))

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
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,119))

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
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,120))

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
        self.assertTrue(TestChecker.test(input,expect,121))

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
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 122))

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
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 123))

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
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 124))

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
        self.assertTrue(TestChecker.test(input, expect, 125))

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
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 126))

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
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 127))

    def test_undeclared_function29(self):
        """Simple program: int main() inherit func2 {} """
        input = """
            //var : string = foo(1.0, 2);
            foo : function auto (inherit out z : auto, t:auto) inherit func{
                z = 5;
                return z + t;
            }
            a : auto = foo(2.0, 2);
            b : auto = foo(3.0, 1);
            c : float = a + b;
            main : function void() {}
            func : function void() {}
            """
        expect = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input, expect, 128))
