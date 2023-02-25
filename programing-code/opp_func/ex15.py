
from abc import ABC
class Exp(ABC):pass
class BinExp(Exp):
    def __init__(self,o1,op,o2):
        self.left = o1
        self.op = op
        self.right = o2
class UnExp(Exp):
    def __init__(self,op,o1):
        self.op = op
        self.operand = o1
class IntLit(Exp):
    def __init__(self,v):
        self.value = v
class FloatLit(Exp):
    def __init__(self,v):
        self.value = v


class Eval:
    def visit(self, x):
        if type(x) == IntLit:
            return x.value
        elif type(x) == FloatLit:
            return x.value
        elif type(x) == BinExp:
            left = self.visit(x.left)
            right = self.visit(x.right)
            if x.op == '+':
                return left + right
            elif x.op == '-':
                return left - right
            elif x.op == '*':
                return left * right
            elif x.op == '/':
                return left / right
        elif type(x) == UnExp:
            return 0 - self.visit(x.operand)


class PrintPrefix:
    def visit(self, x):
        if type(x) == IntLit:
            return str(x.value)
        elif type(x) == FloatLit:
            return str(x.value)
        elif type(x) == BinExp:
            left = self.visit(x.left)
            right = self.visit(x.right)
            if x.op == '-':
                return x.op + "." + " " + left + " " + right
            elif x.op == '/':
                return "." + x.op + " " + left + " " + right
            else:
                return x.op + " " + left + " " + right
        elif type(x) == UnExp:
            if x.op == '-':
                return x.op + "." + " " + self.visit(x.operand)
            elif x.op == '/':
                return "." + x.op + " " + self.visit(x.operand)
            else:
                return x.op + " " + self.visit(x.operand)
class PrintPostfix: pass



x1 = IntLit(1)
x2 = FloatLit(2.0)
x3 = BinExp(x1,"+",x1)
x4 = UnExp("-",x1)
x5 = BinExp(x4,"+",BinExp(IntLit(4),"*",x2))

v1 = Eval()
v2 = PrintPrefix()

print(v1.visit(x5))
print(v2.visit(x5))