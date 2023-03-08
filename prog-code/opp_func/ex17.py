from abc import ABC
class Exp(ABC):pass
class BinExp(Exp):
    def __init__(self,o1,op,o2):
        self.left = o1
        self.op = op
        self.right = o2
    def accept(self,v):
        return v.visitBinExp(self)
class UnExp(Exp):
    def __init__(self,op,o1):
        self.op = op
        self.operand = o1
    def accept(self,v):
        return v.visitUnExp(self)
class IntLit(Exp):
    def __init__(self,v):
        self.value = v
    def accept(self,v):
        return v.visitIntLit(self)
class FloatLit(Exp):
    def __init__(self,v):
        self.value = v
    def accept(self,v):
        return v.visitFloatLit(self)


class Eval:
    def visit(self,x):
        return x.accept(self)

    def visitIntLit(self, int):
        return int.value

    def visitFloatLit(self, f):
        return f.value
    def visitBinExp(self, b):
        left = self.visit(b.left)
        right = self.visit(b.right)
        if b.op == '+':
            return left + right
        elif b.op == '-':
            return left - right
        elif b.op == '*':
            return left * right
        elif b.op == '/':
            return left / right

    def visitUnExp(self, u):
        return 0 - self.visit(u.operand)

class PrintPrefix:
    def visit(self, x):
        return x.accept(self)
    def visitIntLit(self, i):
        return str(i.value)
    def visitFloatLit(self, f):
        return str(f.value)
    def visitUnExp(self, u):
        return '-. ' + self.visit(u.operand)
    def visitBinExp(self, b):
        left = self.visit(b.left)
        right = self.visit(b.right)
        if b.op == '-':
            return b.op + "." + " " + left + " " + right
        elif b.op == '/':
            return "." + b.op + " " + left + " " + right
        else:
            return b.op + " " + left + " " + right

class PrintPostfix:
    def visit(self, x):
        return x.accept(self)

    def visitIntLit(self, i):
        return str(i.value)

    def visitFloatLit(self, f):
        return str(f.value)

    def visitUnExp(self, u):
        return self.visit(u.operand) + ' -.'

    def visitBinExp(self, b):
        left = self.visit(b.left)
        right = self.visit(b.right)
        if b.op == '-':
            return left + " " + right + " " + b.op + "."
        elif b.op == '/':
            return left + " " + right + " " +  "." + b.op
        else:
            return left + " " + right + " " +  b.op


x1 = IntLit(1)
x2 = FloatLit(2.0)
x3 = BinExp(x1,"+",x1)
x4 = UnExp("-",x1)
x5 = BinExp(x4,"+",BinExp(IntLit(4),"*",x2))

v1 = Eval()
v2 = PrintPrefix()
v3 = PrintPostfix()
print(v1.visit(x5))
print(v2.visit(x5))
print(v3.visit(x5))
