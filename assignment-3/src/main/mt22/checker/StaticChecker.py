from Visitor import Visitor
from AST import *
from StaticError import *


class StaticChecker(Visitor):

    def visitIntegerType(self, ast, param): 
        return IntegerType()
    
    def visitFloatType(self, ast, param): 
        return FloatType()

    def visitBooleanType(self, ast, param):
        return BooleanType()
    
    def visitStringType(self, ast, param):
        return StringType()
    
    def visitArrayType(self, ast, param): 
        return ArrayType()
    
    def visitAutoType(self, ast, param):
        return AutoType()
    
    def visitVoidType(self, ast, param):
        return VoidType()



    def visitBinExpr(self, ast, param): pass
    def visitUnExpr(self, ast, param): pass
    def visitId(self, ast, param): pass
    def visitArrayCell(self, ast, param): pass
    def visitIntegerLit(self, ast, param): pass
    def visitFloatLit(self, ast, param): pass
    def visitStringLit(self, ast, param): pass
    def visitBooleanLit(self, ast, param): pass
    def visitArrayLit(self, ast, param): pass
    def visitFuncCall(self, ast, param): pass

    def visitAssignStmt(self, ast, param): pass
    def visitBlockStmt(self, ast, param): pass
    def visitIfStmt(self, ast, param): pass
    def visitForStmt(self, ast, param): pass
    def visitWhileStmt(self, ast, param): pass
    def visitDoWhileStmt(self, ast, param): pass
    def visitBreakStmt(self, ast, param): pass
    def visitContinueStmt(self, ast, param): pass
    def visitReturnStmt(self, ast, param): pass
    def visitCallStmt(self, ast, param): pass

    def visitVarDecl(self, ast, param):
        param[0] += [VarDecl(ast.name, ast.typ, ast.init)]
        raise TypeMismatchInStatement(ast)

    def visitParamDecl(self, ast, param): pass
    def visitFuncDecl(self, ast, param): pass

    def visitProgram(self, ast, param):
        param = [[]]
        for decl in ast.decls:
            self.visit(decl, param)

        
