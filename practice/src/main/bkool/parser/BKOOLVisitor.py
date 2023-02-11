# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#decls.
    def visitDecls(self, ctx:BKOOLParser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#decl.
    def visitDecl(self, ctx:BKOOLParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardecl.
    def visitVardecl(self, ctx:BKOOLParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#funcdecl.
    def visitFuncdecl(self, ctx:BKOOLParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp.
    def visitExp(self, ctx:BKOOLParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#term.
    def visitTerm(self, ctx:BKOOLParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#factor.
    def visitFactor(self, ctx:BKOOLParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assign_stmt.
    def visitAssign_stmt(self, ctx:BKOOLParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_stmt.
    def visitReturn_stmt(self, ctx:BKOOLParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#call_stmt.
    def visitCall_stmt(self, ctx:BKOOLParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param_call_stmt.
    def visitParam_call_stmt(self, ctx:BKOOLParser.Param_call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramdecl.
    def visitParamdecl(self, ctx:BKOOLParser.ParamdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramterm.
    def visitParamterm(self, ctx:BKOOLParser.ParamtermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param.
    def visitParam(self, ctx:BKOOLParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#idlist.
    def visitIdlist(self, ctx:BKOOLParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#typ.
    def visitTyp(self, ctx:BKOOLParser.TypContext):
        return self.visitChildren(ctx)



del BKOOLParser