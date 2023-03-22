import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_program(self):
        input = "f : integer ;"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 801))

    def test_program_2(self):
        input = "f : integer = foo(5+2-6*1) ;"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 802))

    def test_program_3(self):
        input = "f,y : integer = foo(5+2-6*1), abc(6 == 6) ;"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 803))

    def test_program_4(self):
        input = "f : array [4,5] of integer;"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 804))

    def test_program_5(self):
        input = """x, y, z: array [2] of integer = {5e10 + "hello", -0.0e8}, "hello \\n", 123456789;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 805))

    def test_program_6(self):
        input = "f,x,t : integer = {3,4}, 5 ;"
        expect = "Error on line 1 col 27: ;"
        self.assertTrue(TestParser.test(input, expect, 806))

    def test_program_7(self):
        input = """f : array [1] of integer = {1214, 123};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 807))

    def test_program_8(self):
        input = """ f,y : integer = {"abc", "xyz"}, 1==1 ; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 808))

    def test_program_9(self):
        input = "fa : array [4,5] of integer = {};"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 809))

    def test_program_10(self):
        input = """fac: array [4] of string = {"tokyo", "newyork", "london"};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 810))

    def test_program_11(self):
        input = "f : auto = 1 + 2 -3 * 5 /10 + foo(x,z,t) ;"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 811))

    def test_program_12(self):
        """CASE : #2 202.txt"""
        input = "f : float = 124.41124e-10 ;"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 812))

    def test_program_13(self):
        input = """
            var : string = "hello world";
            main : function void(){
                do{
                    return false;
                }while(n == 0);
                var = "Lau Dai Tinh Ai" :: var;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 813))

    def test_program_14(self):
        input = """
            var : string = "hello world";
            foo : function auto () {}
            main: function void(){
                var = "Lau Dai Tinh Ai" :: var;
                return foo(123);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 814))

    def test_program_15(self):
        input = """
            main: function void(){
                var = "Bac" :: "uuu";
                for(i = 0 , i < n + 1, i = i + 1){
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 815))

    def test_program_16(self):
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
                if n == 0 {}
                else {}
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 816))

    def test_program_17(self):
        input = """
            var : string = "hello world";
            main: function void(){
                do{
                    return false;
                }while(n == 0);
                var = "Lau Dai Tinh Ai" :: var;
                for(,,) {}
                test(123, ytx, 5+2+5+5);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 817))

    def test_program_18(self):
        input = """
            var : string = "hello world";
            main: function void(){
                do{
                    return false;
                }while(n == 0);
                var = "Lau Dai Tinh Ai" :: var;
                for(,,) continue;
                test(123, ytx, 5+2+5+5);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 818))

    def test_program_19(self):
        input = """
            var : string = "hello world";
            main: function void(){
                do{
                    return false;
                }while(n == 0);
                var = "Lau Dai Tinh Ai" :: var;
                for(,,) break;
                if ( i < 1) return 1 + foo(2);
                test(123, ytx, 5+2+5+5);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 819))

    def test_program_20(self):
        input = """
            var : string = "hello world";
            main: function void(){
                do{
                    return false;
                }while(n == 0);
                var = "Lau Dai Tinh Ai" :: var;
                for(,,) {return "chac khong co tren tran gian";}
                test(123, ytx, 5+2+5+5);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 820))

    def test_program_21(self):
        input = """a, b, c, d: integer = 3, 4, 6;"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 821))

    def test_program_22(self):
        input = """
            var : string = "hello world";
            main: function void(){
                do{
                    return false;
                }while(n == 0);
                var = "Lau Dai Tinh Ai" :: var;
                for(i = a + b, i < n + 1, i = i + a *b -2 /10) {
                    return "chac khong co tren tran gian";
                }
                test(123, ytx, 5+2+5+5);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 822))

    def test_program_23(self):
        input = """
            var : string = "hello world";
            fact : function auto (alpha : string, delta : integer) {
                if(a < b) return true;
                else return 1 + fact(1 + 1 + 2);
            }
            main: function void(){
                do{
                    return false;
                }while(n == 0);
                var = "Lau Dai Tinh Ai" :: var;
                for(i = a + b, i < n + 1, i = i + a *b -2 /10) {
                    return "chac khong co tren tran gian";
                }
                test(123, ytx, 5+2+5+5);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 823))

    def test_program_24(self):
        input = """
            var : string = "hello world";
            fact : function auto (alpha : string, delta : integer) {
                if(a < b) return true;
                else return 1 + fact(1 + 1 + 2);
            }
            main: function void(){
                do{
                    a : float = 121.124e+10;
                    b : float = 1_124_141.012e-10;
                    c : float = 12_124.81E-10;
                    return false;
                }while(n == 0);
                var = "Lau Dai Tinh Ai" :: var;
                for(i = a + b, i < n + 1, i = i + a *b -2 /10) {
                    return "chac khong co tren tran gian";
                }
                test(123, ytx, 5+2+5+5);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 824))

    def test_program_25(self):
        input = """
            main: function void(){
                a : auto = 12.128431e-10;
                var = se % 10 + 10 - 1;
                while(acn > 10 + 1){
                    s = l + 1;
                    for ( i = 1, j > 0 , c = c + 1){
                        return a + fact(12);
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 825))

    def test_program_26(self):
        input = """
            main: function void(){
                a : auto = 12.128431e-10;
                var = se % 10 + 10 - 1;
                c : boolean = false;
                while(acn > 10 + 1){
                    s = l + 1;
                    for ( i = 1, j > 0 , c = c + 1){
                        return a + fact(12);
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 826))

    def test_program_27(self):
        input = """
            main: function void(){
                a : auto = 12.128431e-10;
                var = se % 10 + 10 - 1;
                a : auto = "string";
                while(acn > 10 + 1){
                    s = l + 1;
                    for ( i = 1, j > 0 , c = c + 1){
                        return a + fact(12);
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 827))

    def test_program_28(self):
        input = """
            main: function void(){
                a : auto = 12.128431e-10;
                var = se % 10 + 10 - 1;
                a : auto = "string";
                // abc yxy comment is here ??
                /* abcas uasdn uqwnsdad */
                while(acn > 10 + 1){
                    s = l + 1;
                    for ( i = 1, j > 0 , c = c + 1){
                        return a + fact(12);
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 828))

    def test_program_29(self):
        input = """
            ABNCASDH : auto ;
            main: function void(){
                a : auto = 12.128431e-10;
                var = se % 10 + 10 - 1;
                a : auto = "string";
                // abc yxy comment is here ??
                /* abcas uasdn uqwnsdad */
                while(acn > 10 + 1){
                    s = l + 1;
                    for ( i = 1, j > 0 , c = c + 1){
                        return a + fact(12);
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 829))

    def test_program_30(self):
        input = """
             ABNCASDH : auto ;
             main: function void(){
                 a : auto = 12.128431e-10;
                 var = se % 10 + 10 - 1;
                 a : auto = "string";
                 // abc yxy comment is here ??
                 /* abcas uasdn uqwnsdad */

                 var = "em oi " + "lau dai tinh ai" :: "chac khong co tren tran gian";
                 while(acn > 10 + 1){
                     s = l + 1;
                     for ( i = 1, j > 0 , c = c + 1){
                         return a + fact(12);
                     }
                 }
             }
         """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 830))

    def test_program_31(self):
        input = """
             ABNCASDH : auto ;
             main: function void(){
                do {return 0;} while(b < 9);
             }
         """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 831))

    def test_program_32(self):
        input = """
             ABNCASDH : auto ;
             main: function void(){
                do {return 0;} while(b < 9);
                for(i = 0 , i == 1-1, a = 294) return ;
             }
         """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 832))

    def test_program_33(self):
        input = """
             ABNCASDH : auto ;
             main: function void(){
                do {return 0;} while(b < 9);
                for(i = 0 , i == 1-1, a = 294) return ;

                if (a == 1 + 1) return;
                a : float = 123.124_1824e-10;
             }
         """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 833))

    def test_program_34(self):
        input = """
            a: integer = func(10);
            for(i = 3, i <= 10, i + 1) {
                sum = sum + i;
            }
            print("I Love you");
        """
        expect = "Error on line 3 col 12: for"
        self.assertTrue(TestParser.test(input, expect, 834))

    def test_program_35(self):
        input = """
            integers: array [5] of integer = {1, 2, 3, "a"};
            a = 10;
        """
        expect = "Error on line 3 col 14: ="
        self.assertTrue(TestParser.test(input, expect, 835))

    def test_program_36(self):
        input = """
            integers: array [5] of integer = {1, 2, 3, "a"};
            a = 10;
            a : integer = "hello world";
            c : float = 812.123e-10;
        """
        expect = "Error on line 3 col 14: ="
        self.assertTrue(TestParser.test(input, expect, 836))

    def test_program_37(self):
        """CASE : #2 202.txt"""
        input = """f : integer = foo(5+2-6*1), {"em dong y"};"""
        expect = "Error on line 1 col 26: ,"
        self.assertTrue(TestParser.test(input, expect, 837))

    def test_program_38(self):
        """CASE : #3 203.txt"""
        input = """float: integer = 10;"""
        expect = "Error on line 1 col 0: float"
        self.assertTrue(TestParser.test(input, expect, 838))

    def test_program_39(self):
        input = """
            {}
        """
        expect = "Error on line 2 col 12: {"
        self.assertTrue(TestParser.test(input, expect, 839))

    def test_program_40(self):
        input = """
            if (n != 0 ) return 1;
        """
        expect = "Error on line 2 col 12: if"
        self.assertTrue(TestParser.test(input, expect, 840))

    def test_program_41(self):
        input = """
            main: function boolean () {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 841))

    def test_program_42(self):
        input = """
            /* main function */
            main: function float () {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 842))

    def test_program_43(self):
        input = """
            /* main function */
            main: function float () {
                n = 10 + 132 * x / 10 == 0 + cn;
                for (i = 0 , i > n , i = i + 1) break;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 843))

    def test_program_44(self):
        input = """
            /* main function */
            main: function float () {
                n = 10 + 132 * x / 10 == 0 + cn;
                for (i = 0 , i > n , i = i + 1) break;
                while(n && a) continue;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 844))

    def test_program_45(self):
        input = """
            /* main function */
            main: function float () {
                n = 10 + 132 * x / 10 == 0 + cn;
                for (i = 0 , i > n , i = i + 1) break;
                while(n && a) continue;
                do {} while(n || a);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 845))

    def test_program_46(self):
        input = """
            /* main function */
            main: function float (a : auto, b: auto) {
                n = 10 + 132 * x / 10 == 0 + cn;
                for (i = 0 , i > n , i = i + 1) break;
                while(n && a) continue;
                do {} while(n || a);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 846))

    def test_program_47(self):
        input = """
            /* main function */
            main: function float (a : auto, b: auto) {
                n = 10 + 132 * x / 10 == 0 + cn;
                for (i = 0 , i > n , i = i + 1) break;
                while(n && a) continue;
                do {} while(n || a);
                if ( n > 0) {} else return 0;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 847))

    def test_program_48(self):
        input = """
            /* main function */
            main: function float (a : auto, b: auto) {
                n = 10 + 132 * x / 10 == 0 + cn;
                for (i = 0 , i > n , i = i + 1) break;
                while(n && a) continue;
                do {} while(n || a);
                if ( n > 0) {
                    var : string = "hello" ::  "world";
                } else return 0;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 848))

    def test_program_49(self):
        input = """
            /* main function */
            main: function float (a : auto, b: auto) {
                n = 10 + 132 * x / 10 == 0 + cn;
                for (i = 0 , i > n , i = i + 1) break;
                while(n && a) continue;
                do {} while(n || a);
                if ( n > 0) {
                    var : string = "hello" ::  "world";
                } else return 0;
                if ( n && 0 ){
                    while(n == 0){
                        return false;
                    }
                    for (,,){
                        a = 10;
                        a = a + 123 && b - 10 * 18 -19;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 849))

    def test_program_50(self):
        input = """
            /* main function */

            delta : boolean = true;
            main: function float (a : auto, b: auto) {
                n = 10 + 132 * x / 10 == 0 + cn;
                for (i = 0 , i > n , i = i + 1) break;
                while(n && a) continue;
                do {} while(n || a);
                if ( n > 0) {
                    var : string = "hello" ::  "world";
                } else return 0;
                if ( n && 0 ){
                    while(n == 0){
                        return false;
                    }
                    for (,,){
                        a = 10;
                        a = a + 123 && b - 10 * 18 -19;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 850))

    def test_program_51(self):
        input = """
            /* main function */
            main: function float () {
                a = true || false;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 851))

    def test_program_52(self):
        input = """
            /* main function */
            main: function float () {
                a = true && false;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 852))

    def test_program_53(self):
        input = """
            /* main function */
            factor : integer = 10.0;
            main: function float () {
                a = true || false;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 853))

    def test_program_54(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            main: function float () {
                a = true || false;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 854))

    def test_program_55(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            str : auto = "abc";
            main: function float () {
                a = true || false;

            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 855))

    def test_program_56(self):
        input = """
            /* main function */
            main: function float () {
                a = true || false;
                return;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 856))

    def test_program_57(self):
        input = """
            /* main function */
            main: function float () {
                a = true && false;
                return a;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 858))

    def test_program_58(self):
        input = """
            /* main function */
            factor : integer = 10.0;
            main: function float () {
                a = true || false;
                {}
                {}
                {}
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 858))

    def test_program_59(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            main: function float () {
                a = true || false;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 859))

    def test_program_60(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            str : auto = "abc";
            main: function float () {
                a = true || false;
                a[0] = 19 + 123 + 19 * 13 -10 ;

            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 860))

    def test_program_61(self):
        input = """
            /* main function */
            main: function float () {
                a = true || false;
                a = as[1] + 123 - 1 + a[a[0]];
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 861))

    def test_program_62(self):
        input = """
            /* main function */
            main: function float () {
                a = true && false;
                print(abc);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 862))

    def test_program_63(self):
        input = """
            /* main function */
            factor : integer = 10.0;
            main: function float () {
                a = true || false;
                foo(123 +13 -1 + foo(5));
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 863))

    def test_program_64(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            main: function float () {
                a = {};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 864))

    def test_program_65(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            str : auto = "abc";
            main: function float () {
                a = true || false;
                b : auto;

            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 865))

    def test_program_66(self):
        input = """
            /* main function */
            main: function float () {
                a = true || false;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 866))

    def test_program_67(self):
        input = """
            /* main function */
            main: function float () {
                n = strlen(str);
                for (i = 0, i < n / 2, i = i + 1) {
                    swap(str[i], str[n - i - 1]);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 867))

    def test_program_68(self):
        input = """
            /* main function */
            factor : integer = 10.0;
            main: function float () {
                a = true || false;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 868))

    def test_program_69(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            main: function float () {
                a = true || false;
                foo();
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 869))

    def test_program_70(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            str : auto = "abc";
            main: function float () {
                a = true || false;
                r,s : float;
                r = 2.0;
                s = r * r * myPi;
                a[0] = s;

            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 870))

    def test_program_71(self):
        input = """
            /* main function */
            main: function float () {
                return 1 + 2 + {} - myPI * foo(a[a[0]] - 10 + swap());
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 871))

    def test_program_72(self):
        input = """
            /* main function */
            main: function float (out n : integer, out i : float) {
                a = true && false;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 872))

    def test_program_73(self):
        input = """
            /* main function */
            factor : integer = 10.0;
            main: function float (inherit out a : auto) {
                a = true || false;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 873))

    def test_program_74(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            main: function float () {
                a = true || false;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 854))

    def test_program_75(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            str : auto = "abc";
            main: function float () {
                for (i = 1, i < 10, i + 1) {
                    writeInt(i);
                }
            }
        """
        expect = "Error on line 6 col 38: +"
        self.assertTrue(TestParser.test(input, expect, 875))

    def test_program_76(self):
        input = """
            /* main function */
            main: function string () {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 876))

    def test_program_77(self):
        input = """
            /* main function */
            main: function float () {{{}}{}}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 877))

    def test_program_78(self):
        input = """
            /* main function */
            factor : integer = 10.0;
            main: function float () {
                continue;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 878))

    def test_program_79(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            main: function float () {
                a = true || false;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 879))

    def test_program_80(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            str : auto = "abc";
            main: function float () {
                a = 1_23.40E+156;

            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 880))

    def test_program_81(self):
        input = """
            /* main function */
            main: function float () {
                a = 1_23.04E-56;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 881))

    def test_program_82(self):
        input = """
            /* main function */
            main: function float () {
                a = 1_23.456e-10;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 882))

    def test_program_83(self):
        input = """
            /* main function */
            factor : integer = 10.0;
            main: function float () {
                a = "@#$&\t^@$(@(ahs\\"ash\\"%%@&@\\"dsad\\"123&^@@";
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 883))

    def test_program_84(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            main: function float () {
                a = "@#$&^@$(@(ahs\\"ash\\"%%@&@\\"dsad\\"123&^@@";
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 884))

    def test_program_85(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            str : auto = "abc";
            main: function float () {
                a = "Chuoi cua ban la: \\"12345\\"";

            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 885))

    def test_program_86(self):
        input = """
            /* main function */
            main: function float () {
                a = true || false;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 886))

    def test_program_87(self):
        input = """
            /* main function */
            main: function float () {
                a = "This is Hung\'s PC";
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 887))

    def test_program_88(self):
        input = """
            /* main function */
            factor : integer = 10.0;
            main: function float () {
                a = "He asked me: \\\"Where is John?\\\"";
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 888))

    def test_program_89(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            main: function float () {
                a = 1_23_1414_214;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 889))

    def test_program_90(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            str : auto = "abc";
            main: function float () {
                a = 3200_21000_123_000;

            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 890))

    def test_program_91(self):
        input = """
            /* main function */
            main: function float () {
                a = 1_23.000456E-10;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 891))

    def test_program_92(self):
        input = """
            /* main function */
            main: function float () {
                a = 1_23.40E+156;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 892))

    def test_program_93(self):
        input = """
            /* main function */
            factor : integer = 10.0;
            main: function float () {
                /*tran khac chan nam qua xa, */ \n //ve day voi nhau hai dua dap chung men*/ abcxyz
                a = true || false;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 893))

    def test_program_94(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            main: function float () {
                /* anh muon ta ve cung mot nha, an sang va cung hat ca */ // nhung biet sao gio 
                a = true || false;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 894))

    def test_program_95(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            str : auto = "abc";
            main: function float () {
                a = true || false;

            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 855))

    def test_program_96(self):
        input = """
            /* main function */
            main: function float () {
                a = "@#$\b&^@$(@(ahs\\"ash\\"%%@&@\\"dsad\\"123&^@@";
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 896))

    def test_program_97(self):
        input = """
            func: function void () {
                if (i==1) 
                    if (i==2)
                        if (i > 3)
                            if (i>=5)
                                printString("I love you");
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 897))

    def test_program_98(self):
        input = """
            func: function void () {
                if ("i love you") 
                    if ("but")
                        if ("you don't love me")
                            if ("make")
                                printString("me and my broken heart");
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 898))

    def test_program_99(self):
        input = """
            func: function void () {
                if ("i wanna hide the truth") 
                    while("i wanna shelter you")
                        if ("but with the beast inside")
                            while("there's nowhere we can hide")
                                return "No matter what we breed";
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 899))

    def test_program_100(self):
        input = """
            /* main function */
            ac : float = 12.0e-10;
            str : auto = "abc";
            main: function float () {
                a = "don't get too close, it's dark inside" :: "it's where my demon hide";
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 900))