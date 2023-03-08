# To express an arithmetic expression, there are 5 following classes:
#
# Exp: general arithmetic expression
#
# BinExp: an arithmetic expression that contains one binary operators (+,-,*,/) and two operands.
# To construct a BinExp object, you must pass parameters: first operand, operator, second operand, respectively.
#
# UnExp: an arithmetic expression that contains one unary operator (+,-) and one operand.
# To construct a UnExp object, you must pass the operator first.
#
# IntLit: an arithmetic expression that contains one integer number
#
# FloatLit: an arithmetic expression that contains one floating point number
#
# Define these classes in Python (their parents, attributes, methods) such that their
# objects can response to eval() message by returning the value of the expression. For example,
# let object x express the arithmetic expression 3 + 4 * 2.0, x.eval() must return 11.0
#
# In this exercise, we use:
#
# x1 = IntLit(1)
#
# x2 = FloatLit(2.0)
#
# x3 = BinExp(x1,"+",x1)
#
# x4 = UnExp("-",x1)
#
# x5 = BinExp(x4,"+",BinExp(IntLit(4),"*",x2))

# Extend the contents of classes Exp, BinExp, UnExp, IntLit, FloatLit such that they can response
# to printPrefix() message to return the string corresponding to the expression in prefix format.
# Note that, unary operator +/- is printed as +./-. in prefix format and there is a space after each
# operator or operand. For example, when receiving message printPrefix(), the object expressing
# the expression -4 + 3 * 2 will return the string "+ -. 4 * 3 2 "
from abc import ABC
class Exp(ABC): pass


class BinExp(Exp):
    def __init__(self, fo, operator, so):
        self.firstOperand = fo
        self.secondOperand = so
        self.operator = operator

    def eval(self):
        left = self.firstOperand.eval()
        right = self.secondOperand.eval()
        if self.operator == '+': return left + right
        elif self.operator == '-': return left - right
        elif self.operator == '*': return left * right
        elif self.operator == '/': return left / right

    def printPrefix(self):
        left = self.firstOperand.printPrefix()
        right = self.secondOperand.printPrefix()
        if self.operator == '-':
            return self.operator + "." + " " + left + " " + right
        elif self.operator == '/':
            return "." + self.operator + " " + left + " " + right
        else:
            return self.operator + " " + left + " " + right


class UnExp(Exp):
    def __init__(self, operator, o):
        self.operator = operator
        self.o = o

    def eval(self):
        value = self.o.eval()
        return -value if self.operator == '-' else value

    def printPrefix(self):
        val = self.o.printPrefix()
        if self.operator == '-':
            return self.operator + "." + " " + val
        elif self.operator == '/':
            return "." + self.operator + " " + val
        else:
            return self.operator + " " + val


class IntLit(Exp):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return self.val

    def printPrefix(self):
        return str(self.val)


class FloatLit(Exp):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return self.val

    def printPrefix(self):
        return str(self.val)

x1 = IntLit(1)
x2 = FloatLit(2.0)
x3 = BinExp(x1,"+",x1)
x4 = UnExp("-",x1)
x5 = BinExp(x4,"+",BinExp(IntLit(4),"*",x2))

print(x4.printPrefix())
print(x5.printPrefix())