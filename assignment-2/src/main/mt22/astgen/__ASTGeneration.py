from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *

# from src.main.mt22.utils.AST import Program


class ASTGeneration(MT22Visitor):
    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        """
        :param ctx: MT22Parser.ProgramContext
        :return: Program
        """
        decl_list = []
        for x in ctx.decls():
            decl = self.visitDecls(x)
            if type(decl) == list:
                decl_list.extend(decl if decl else [])
            else:
                decl_list.append(decl)
        return Program(decl_list)

    # Visit a parse tree produced by MT22Parser#decls.
    def visitDecls(self, ctx: MT22Parser.DeclsContext):
        """
        visitChildren() iterates over all child nodes of a given node
        and triggers the accept method for each of them. Look in
        your generated parser to see what the accept method does. 
        Normally it calls the visit function of the next child in 
        the chain or simply visits over its own children 
        by calling again visitChildren (which has basically the 
        same effect, just in a more general way).

        :param ctx: MT22Parser.DeclsContext
        :return: Children
        """
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#arraytype.
    def visitArraytype(self, ctx: MT22Parser.ArraytypeContext):
        dimesion = self.visit(ctx.dimesion())
        typ = self.visit(ctx.eletype())
        return ArrayType(dimesion, typ)

    # Visit a parse tree produced by MT22Parser#number.
    def visitNumber(self, ctx: MT22Parser.NumberContext):
        if ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        else:
            return FloatLit(float(ctx.FLOATLIT().getText()))

    # Visit a parse tree produced by MT22Parser#eletype.
    def visitEletype(self, ctx: MT22Parser.EletypeContext):
        if ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        return BooleanType()

    # Visit a parse tree produced by MT22Parser#dimesion.
    def visitDimesion(self, ctx: MT22Parser.DimesionContext):
        if ctx.getChildCount() == 1:
            dimesion_list = []
            dimesion_list.append(self.visit(ctx.number()))
            return dimesion_list
        else:
            return [self.visit(ctx.number())] + self.visit(ctx.dimesion())

    # Visit a parse tree produced by MT22Parser#vardecl.

    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        if ctx.vardeclNoEq():
            return self.visit(ctx.vardeclNoEq())
        return self.visit(ctx.vardeclEq())

    # Visit a parse tree produced by MT22Parser#vardeclNoEq.
    def visitVardeclNoEq(self, ctx: MT22Parser.VardeclNoEqContext):
        idlist = self.visit(ctx.idlist())
        if ctx.eletype():
            typ = self.visit(ctx.eletype())
            return list(map(lambda x: VarDecl(str(x), typ), idlist))
        typ = self.visit(ctx.arraytype())
        return list(map(lambda x: VarDecl(str(x), typ), idlist))


    # Visit a parse tree produced by MT22Parser#vardeclEq.
    def visitVardeclEq(self, ctx: MT22Parser.VardeclEqContext):
        if ctx.assignRecur():
            return 1
        ident = ctx.IDENTIFIER().getText()
        typ = self.visit(ctx.eletype())
        exp = self.visit(ctx.expr())
        # return VarDecl(ident, typ, exp)
        return exp
            

    # Visit a parse tree produced by MT22Parser#assignRecur.
    def visitAssignRecur(self, ctx: MT22Parser.AssignRecurContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#arraylist.
    def visitArraylist(self, ctx: MT22Parser.ArraylistContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#explistTerm.
    def visitExplistTerm(self, ctx: MT22Parser.ExplistTermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        if ctx.idlist():
            return [ctx.IDENTIFIER()] + self.visit(ctx.idlist())
        else: return [ctx.IDENTIFIER()]


    # Visit a parse tree produced by MT22Parser#exprlist.
    def visitExprlist(self, ctx: MT22Parser.ExprlistContext):
        return [self.visit(x) for x in ctx.expr()]

    # Visit a parse tree produced by MT22Parser#parameter.
    def visitParameter(self, ctx: MT22Parser.ParameterContext):
        return self.visit(ctx)

    # Visit a parse tree produced by MT22Parser#compare.
    def visitCompare(self, ctx: MT22Parser.CompareContext):
        if ctx.EQUAL_TO():
            return ctx.EQUAL_TO().getText()
        elif ctx.NOT_EQUAL():
            return ctx.NOT_EQUAL().getText()
        elif ctx.LESS():
            return ctx.LESS().getText()
        elif ctx.GREATER():
            return ctx.GREATER().getText()
        elif ctx.LTE():
            return ctx.LTE().getText()
        elif ctx.GTE():
            return ctx.GTE().getText()

    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx: MT22Parser.ExprContext):
        if ctx.CONCAT():
            return BinExpr(ctx.CONCAT().getText(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))
        return self.visit(ctx.expr1())

    # Visit a parse tree produced by MT22Parser#expr1.
    def visitExpr1(self, ctx: MT22Parser.Expr1Context):
            return 1

        # return BinExpr(op, self.visitExpr2(ctx.expr2(0)), self.visitExpr2(ctx.expr2(1)))


    # Visit a parse tree produced by MT22Parser#expr2.
    def visitExpr2(self, ctx: MT22Parser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visitExpr3(ctx.expr3())
        if ctx.AND():
            return BinExpr(ctx.AND().getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        return BinExpr(ctx.OR().getText(), self.visitExpr2(ctx.expr2()), self.visit(ctx.expr3()))

    # Visit a parse tree produced by MT22Parser#expr3.
    def visitExpr3(self, ctx: MT22Parser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visitExpr4(ctx.expr4())
        if ctx.PLUS():
            return BinExpr(ctx.PLUS().getText(), self.visitExpr3(ctx.expr3()), self.visitExpr4(ctx.expr4()))
        return BinExpr(ctx.MINUS().getText(), self.visitExpr3(ctx.expr3()), self.visitExpr4(ctx.expr4()))

    # Visit a parse tree produced by MT22Parser#expr4.
    def visitExpr4(self, ctx: MT22Parser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visitExpr5(ctx.expr5())
        if ctx.DIV():
            return BinExpr(ctx.DIV().getText(), self.visitExpr4(ctx.expr4()), self.visitExpr5(ctx.expr5()))
        elif ctx.MUL():
            return BinExpr(ctx.MUL().getText(), self.visitExpr4(ctx.expr4()), self.visitExpr5(ctx.expr5()))
        return BinExpr(ctx.MOD().getText(), self.visitExpr4(ctx.expr4()), self.visitExpr5(ctx.expr5()))

    # Visit a parse tree produced by MT22Parser#expr5.
    def visitExpr5(self, ctx: MT22Parser.Expr5Context):
        if ctx.getChildCount() == 1:
            return self.visitExpr6(ctx.expr6())
        return UnExpr(ctx.NOT().getText(), self.visitExpr5(ctx.expr5()))

    # Visit a parse tree produced by MT22Parser#expr6.
    def visitExpr6(self, ctx: MT22Parser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visitExpr7(ctx.expr7())
        return UnExpr(ctx.MINUS().getText(), self.visitExpr6(ctx.expr6()))

    # Visit a parse tree produced by MT22Parser#expr7.
    def visitExpr7(self, ctx: MT22Parser.Expr7Context):
        if ctx.getChildCount() == 1:
            return self.visitExpr8(ctx.expr8())
        else:
            ident = ctx.IDENTIFIER().getText()
            expr = self.visitExpr8(ctx.expr8())
            return ArrayCell(ident, expr)

    # Visit a parse tree produced by MT22Parser#expr8.
    def visitExpr8(self, ctx: MT22Parser.Expr8Context):
        if ctx.getChildCount() == 1:
            return self.visitFactor(ctx.factor())
        return self.visitExpr(ctx.expr())

    # Visit a parse tree produced by MT22Parser#factor.
    def visitFactor(self, ctx: MT22Parser.FactorContext):
        if ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLit(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLit(str(ctx.STRINGLIT().getText()))
        elif ctx.IDENTIFIER():
            return Id(str(ctx.IDENTIFIER().getText()))
        elif ctx.funccall():
            return self.visitFunccall(ctx.funccall())
        elif ctx.arraylist():
            return self.visitArraylist(ctx.arraylist())
        elif ctx.BOOLEANLIT():
            return BooleanLit(True if ctx.BOOLEANLIT().getText() == "true" else False)

    # Visit a parse tree produced by MT22Parser#arrayCell.
    def visitArrayCell(self, ctx: MT22Parser.ArrayCellContext):
        ident = ctx.IDENTIFIER().getText()
        cell = self.visitExprlist(ctx.exprlist())
        return ArrayCell(ident, cell)

    # Visit a parse tree produced by MT22Parser#funccall.
    def visitFunccall(self, ctx: MT22Parser.FunccallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx: MT22Parser.StmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#assignStmt.
    def visitAssignStmt(self, ctx: MT22Parser.AssignStmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx: MT22Parser.LhsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#ifStmt.
    def visitIfStmt(self, ctx: MT22Parser.IfStmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#forStmt.
    def visitForStmt(self, ctx: MT22Parser.ForStmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#initExpr.
    def visitInitExpr(self, ctx: MT22Parser.InitExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#conditionExpr.
    def visitConditionExpr(self, ctx: MT22Parser.ConditionExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#updateExpr.
    def visitUpdateExpr(self, ctx: MT22Parser.UpdateExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#whileStmt.
    def visitWhileStmt(self, ctx: MT22Parser.WhileStmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#doWhileStmt.
    def visitDoWhileStmt(self, ctx: MT22Parser.DoWhileStmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#callStmt.
    def visitCallStmt(self, ctx: MT22Parser.CallStmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#blockStmt.
    def visitBlockStmt(self, ctx: MT22Parser.BlockStmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#stmtTerm.
    def visitStmtTerm(self, ctx: MT22Parser.StmtTermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#stmtList.
    def visitStmtList(self, ctx: MT22Parser.StmtListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#breakStmt.
    def visitBreakStmt(self, ctx: MT22Parser.BreakStmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#continueStmt.
    def visitContinueStmt(self, ctx: MT22Parser.ContinueStmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#returnStmt.
    def visitReturnStmt(self, ctx: MT22Parser.ReturnStmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx: MT22Parser.FuncdeclContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#inheritance.
    def visitInheritance(self, ctx: MT22Parser.InheritanceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#function_name.
    def visitFunction_name(self, ctx: MT22Parser.Function_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#paramterList.
    def visitParamterList(self, ctx: MT22Parser.ParamterListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#paramterListTerm.
    def visitParamterListTerm(self, ctx: MT22Parser.ParamterListTermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#returnType.
    def visitReturnType(self, ctx: MT22Parser.ReturnTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#sfuncdecl.
    def visitSfuncdecl(self, ctx: MT22Parser.SfuncdeclContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#read_integer.
    def visitRead_integer(self, ctx: MT22Parser.Read_integerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#print_integer.
    def visitPrint_integer(self, ctx: MT22Parser.Print_integerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#read_float.
    def visitRead_float(self, ctx: MT22Parser.Read_floatContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#write_float.
    def visitWrite_float(self, ctx: MT22Parser.Write_floatContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#print_boolean.
    def visitPrint_boolean(self, ctx: MT22Parser.Print_booleanContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#read_string.
    def visitRead_string(self, ctx: MT22Parser.Read_stringContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#print_string.
    def visitPrint_string(self, ctx: MT22Parser.Print_stringContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#super_.
    def visitSuper_(self, ctx: MT22Parser.Super_Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#prevent_default.
    def visitPrevent_default(self, ctx: MT22Parser.Prevent_defaultContext):
        return self.visitChildren(ctx)
