from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *
from functools import reduce


def flatten(lst):
    return reduce(lambda prev, curr: prev + flatten(curr) if isinstance(curr, list) else prev + [curr], lst, [])


class ASTGeneration(MT22Visitor):
    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
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
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#arraytype.
    def visitArraytype(self, ctx: MT22Parser.ArraytypeContext):
        lst_dms = self.visit(ctx.dimension())
        typ = self.visit(ctx.eletype())
        return ArrayType(lst_dms, typ)

    # Visit a parse tree produced by MT22Parser#number.
    def visitNumber(self, ctx: MT22Parser.NumberContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#eletype.
    def visitEletype(self, ctx: MT22Parser.EletypeContext):
        if ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.AUTO():
            return AutoType()
        return BooleanType()

    # Visit a parse tree produced by MT22Parser#dimension.
    def visitDimension(self, ctx: MT22Parser.DimensionContext):
        if ctx.getChildCount() == 1:
            return [int(ctx.INTLIT().getText())]
        return [int(ctx.INTLIT().getText())] + self.visit(ctx.dimension())

    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#vardeclNoEq.
    def visitVardeclNoEq(self, ctx: MT22Parser.VardeclNoEqContext):
        idlist = self.visit(ctx.idlist())
        typ = None
        if ctx.eletype():
            typ = self.visit(ctx.eletype())
            return list(map(lambda x: VarDecl(x, typ), idlist))
        else:
            typ = self.visit(ctx.arraytype())
            return list(map(lambda x: VarDecl(x, typ), idlist))

    # Visit a parse tree produced by MT22Parser#vardeclEq.
    def visitVardeclEq(self, ctx: MT22Parser.VardeclEqContext):
        if ctx.assignment():
            ident = ctx.IDENTIFIER().getText()
            assign = self.visit(ctx.assignment())
            expr = self.visit(ctx.expr())

            # list variables, elements type and values
            lst = [ident, assign, expr]

            # flatten list
            lst_flatten = flatten(lst)

            # get index of element type
            idxType = int(len(lst_flatten)/2)
            eletype = lst_flatten[idxType]

            # get list of identifiers
            identlist = lst_flatten[0:idxType]

            # get list of values and reversed it
            val = lst_flatten[idxType + 1:]

            return list(map(lambda x, y: VarDecl(x, eletype, y), identlist, val))
        else:
            ident = ctx.IDENTIFIER().getText()
            expr = self.visit(ctx.expr())
            typ = self.visit(ctx.getChild(2))
            return VarDecl(ident, typ, expr)

    # Visit a parse tree produced by MT22Parser#assignment.
    def visitAssignment(self, ctx: MT22Parser.AssignmentContext):
        if ctx.assignment():
            return [ctx.IDENTIFIER().getText(), self.visit(ctx.assignment()), self.visit(ctx.expr())]
        return [ctx.IDENTIFIER().getText(), self.visit(ctx.getChild(2)), self.visit(ctx.expr())]

    # Visit a parse tree produced by MT22Parser#arraylit.
    def visitArraylit(self, ctx: MT22Parser.ArraylitContext):
        return ArrayLit(self.visit(ctx.exprlist()) if ctx.exprlist() else [])

    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        if ctx.getChildCount() == 1:
            return [ctx.IDENTIFIER().getText()]
        else:
            return [ctx.IDENTIFIER().getText()] + self.visit(ctx.idlist())

    # Visit a parse tree produced by MT22Parser#exprlist.
    def visitExprlist(self, ctx: MT22Parser.ExprlistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.exprlist())

    # Visit a parse tree produced by MT22Parser#parameter.
    def visitParameter(self, ctx: MT22Parser.ParameterContext):
        inherited = True if ctx.INHERIT() else False
        out = True if ctx.OUT() else False
        ident = ctx.IDENTIFIER().getText()
        eletype = self.visit(ctx.eletype()) if ctx.eletype(
        ) else self.visit(ctx.arraytype())
        return ParamDecl(ident, eletype, out, inherited)

    # Visit a parse tree produced by MT22Parser#expr.

    def visitExpr(self, ctx: MT22Parser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1(0))  # what che fuck is this here?
        left = self.visit(ctx.expr1(0))
        right = self.visit(ctx.expr1(1))
        op = ctx.CONCAT().getText()
        return BinExpr(op, left, right)

    # Visit a parse tree produced by MT22Parser#expr1.
    def visitExpr1(self, ctx: MT22Parser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2(0))
        return BinExpr(self.visit(ctx.compare()), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))

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

    # Visit a parse tree produced by MT22Parser#expr2.
    def visitExpr2(self, ctx: MT22Parser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        if ctx.AND():
            return BinExpr(ctx.AND().getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        elif ctx.OR():
            return BinExpr(ctx.OR().getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))

    # Visit a parse tree produced by MT22Parser#expr3.
    def visitExpr3(self, ctx: MT22Parser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        if ctx.PLUS():
            return BinExpr(ctx.PLUS().getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        elif ctx.MINUS():
            return BinExpr(ctx.MINUS().getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))

    # Visit a parse tree produced by MT22Parser#expr4.
    def visitExpr4(self, ctx: MT22Parser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        if ctx.MUL():
            return BinExpr(ctx.MUL().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        elif ctx.DIV():
            return BinExpr(ctx.DIV().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        return BinExpr(ctx.MOD().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))

    # Visit a parse tree produced by MT22Parser#expr5.
    def visitExpr5(self, ctx: MT22Parser.Expr5Context):
        # expr5: NOT expr5 | expr6;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr6())
        return UnExpr(ctx.NOT().getText(), self.visit(ctx.expr5()))

    # Visit a parse tree produced by MT22Parser#expr6.
    def visitExpr6(self, ctx: MT22Parser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr7())
        return UnExpr(ctx.MINUS().getText(), self.visit(ctx.expr6()))

    # Visit a parse tree produced by MT22Parser#expr7.
    def visitExpr7(self, ctx: MT22Parser.Expr7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr8())
        ident = ctx.IDENTIFIER().getText()
        exp = self.visit(ctx.exprlist())
        return ArrayCell(ident, exp)  # a[1,2,3]

    # Visit a parse tree produced by MT22Parser#expr8.

    def visitExpr8(self, ctx: MT22Parser.Expr8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.factor())
        else:
            return self.visit(ctx.expr())

    # Visit a parse tree produced by MT22Parser#factor.
    def visitFactor(self, ctx: MT22Parser.FactorContext):
        if ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            num = ctx.FLOATLIT().getText()
            if num[0] == '.' and (num[1] == 'e' or num[1] == 'E'):
                num = 0.0
            return FloatLit(float(num))
        elif ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT().getText())
        elif ctx.IDENTIFIER():
            return Id(str(ctx.IDENTIFIER().getText()))
        elif ctx.funccall():
            return self.visit(ctx.funccall())
        elif ctx.arraylit():
            return self.visit(ctx.arraylit())
        elif ctx.BOOLEANLIT():
            return BooleanLit(True if ctx.BOOLEANLIT().getText() == "true" else False)

    # Visit a parse tree produced by MT22Parser#arrayCell.
    def visitArrayCell(self, ctx: MT22Parser.ArrayCellContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#funccall.
    def visitFunccall(self, ctx: MT22Parser.FunccallContext):
        if ctx.sfuncdecl():
            ident, expr = self.visit(ctx.sfuncdecl())
            if expr is not None:
                expr = expr if isinstance(expr, list) else [expr]
            return FuncCall(ident, expr if expr is not None else [])
        return FuncCall(ctx.IDENTIFIER().getText(), self.visit(ctx.exprlist()) if ctx.exprlist() else [])

    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx: MT22Parser.StmtContext):
        # if ctx.assignStmt():
        #     return self.visit(ctx.assignStmt())
        # elif ctx.ifStmt():
        #     return self.visit(ctx.ifStmt())
        # elif ctx.forStmt():
        #     return self.visit(ctx.forStmt())
        # elif ctx.whileStmt():
        #     return self.visit(ctx.whileStmt())
        # elif ctx.doWhileStmt():
        #     return self.visit(ctx.doWhileStmt())
        # elif ctx.returnStmt():
        #     return self.visit(ctx.returnStmt())
        # elif ctx.continueStmt():
        #     return self.visit(ctx.continueStmt())
        # elif ctx.breakStmt():
        #     return self.visit(ctx.breakStmt())
        # elif ctx.callStmt():
        #     return self.visit(ctx.callStmt())
        # lst = self.visit(ctx.vardecl())
        # return lst
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#assignStmt.
    def visitAssignStmt(self, ctx: MT22Parser.AssignStmtContext):
        lhs = self.visit(ctx.lhs())
        expr = self.visit(ctx.expr())
        return AssignStmt(lhs, expr)

    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx: MT22Parser.LhsContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.IDENTIFIER().getText())
        ident = ctx.IDENTIFIER().getText()
        expr = self.visit(ctx.exprlist())
        return ArrayCell(ident, expr)

    # Visit a parse tree produced by MT22Parser#stmtlocal.
    def visitStmtlocal(self, ctx: MT22Parser.StmtlocalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#ifStmt.
    def visitIfStmt(self, ctx: MT22Parser.IfStmtContext):
        expr = self.visit(ctx.expr())

        if ctx.getChildCount() == 5:
            stmt = self.visit(ctx.stmt(0))
            return IfStmt(expr, stmt)

        left = self.visit(ctx.stmt(0))
        right = self.visit(ctx.stmt(1))
        return IfStmt(expr, left, right)

    # Visit a parse tree produced by MT22Parser#forStmt.
    def visitForStmt(self, ctx: MT22Parser.ForStmtContext):
        initexp = self.visit(ctx.initExpr())
        conditionExpr = self.visit(ctx.conditionExpr())
        updateExpr = self.visit(ctx.updateExpr())
        stmt = self.visit(ctx.stmt())
        return ForStmt(initexp, conditionExpr, updateExpr, stmt)

    # Visit a parse tree produced by MT22Parser#initExpr.
    def visitInitExpr(self, ctx: MT22Parser.InitExprContext):
        return AssignStmt(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expr()))

    # Visit a parse tree produced by MT22Parser#conditionExpr.
    def visitConditionExpr(self, ctx: MT22Parser.ConditionExprContext):
        if ctx.BOOLEANLIT():
            return BooleanLit(True if ctx.BOOLEANLIT().getText() == "true" else False)
        return BinExpr(self.visit(ctx.operator()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))

    # Visit a parse tree produced by MT22Parser#operator.
    def visitOperator(self, ctx: MT22Parser.OperatorContext):
        # LESS | GREATER | LTE | GTE | NOT_EQUAL | EQUAL_TO;
        if ctx.LESS():
            return ctx.LESS().getText()
        elif ctx.GREATER():
            return ctx.GREATER().getText()
        elif ctx.EQUAL_TO():
            return ctx.EQUAL_TO().getText()
        elif ctx.GTE():
            return ctx.GTE().getText()
        elif ctx.LTE():
            return ctx.LTE().getText()
        return ctx.NOT_EQUAL().getText()

    # Visit a parse tree produced by MT22Parser#updateExpr.
    def visitUpdateExpr(self, ctx: MT22Parser.UpdateExprContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by MT22Parser#whileStmt.
    def visitWhileStmt(self, ctx: MT22Parser.WhileStmtContext):
        # whileStmt: WHILE LB expr RB stmtlocal;
        expr = self.visit(ctx.expr())
        stmt = self.visit(ctx.stmt())
        return WhileStmt(expr, stmt)

    # Visit a parse tree produced by MT22Parser#doWhileStmt.
    def visitDoWhileStmt(self, ctx: MT22Parser.DoWhileStmtContext):
        # doWhileStmt: DO blockStmt WHILE expr SEMI;
        return DoWhileStmt(self.visit(ctx.expr()), self.visit(ctx.blockStmt()))

    # Visit a parse tree produced by MT22Parser#callStmt.
    def visitCallStmt(self, ctx: MT22Parser.CallStmtContext):
        if ctx.sfuncdecl():
            ident, expr = self.visit(ctx.sfuncdecl())
            if expr is not None:
                expr = expr if isinstance(expr, list) else [expr]
            return CallStmt(ident, expr if expr is not None else [])
        return CallStmt(ctx.IDENTIFIER().getText(), self.visit(ctx.exprlist()) if ctx.exprlist() else [])

    # Visit a parse tree produced by MT22Parser#blockStmt.
    def visitBlockStmt(self, ctx: MT22Parser.BlockStmtContext):
        return BlockStmt(self.visit(ctx.stmtTerm()))

    # Visit a parse tree produced by MT22Parser#stmtTerm.
    def visitStmtTerm(self, ctx: MT22Parser.StmtTermContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.stmtList())

    # Visit a parse tree produced by MT22Parser#stmtList.
    def visitStmtList(self, ctx: MT22Parser.StmtListContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.stmt()) if isinstance(self.visit(ctx.stmt()), list) else [self.visit(ctx.stmt())]
        local = self.visit(ctx.stmt()) if isinstance(
            self.visit(ctx.stmt()), list) else [self.visit(ctx.stmt())]
        return local + self.visit(ctx.stmtList())

    # Visit a parse tree produced by MT22Parser#breakStmt.
    def visitBreakStmt(self, ctx: MT22Parser.BreakStmtContext):
        return BreakStmt()

    # Visit a parse tree produced by MT22Parser#continueStmt.
    def visitContinueStmt(self, ctx: MT22Parser.ContinueStmtContext):
        return ContinueStmt()

    # Visit a parse tree produced by MT22Parser#returnStmt.
    def visitReturnStmt(self, ctx: MT22Parser.ReturnStmtContext):
        return ReturnStmt(self.visit(ctx.expr()) if ctx.expr() else None)

    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx: MT22Parser.FuncdeclContext):
        ident = ctx.IDENTIFIER().getText()
        rettype = self.visit(ctx.returnType())
        param_list = self.visit(ctx.paramterList())
        inherits = self.visit(ctx.inheritance()) if ctx.inheritance() else None
        blockStmt = self.visit(ctx.blockStmt())
        return FuncDecl(ident, rettype, param_list, inherits, blockStmt)

    # Visit a parse tree produced by MT22Parser#inheritance.

    def visitInheritance(self, ctx: MT22Parser.InheritanceContext):
        if ctx.getChildCount() == 0:
            return None
        return ctx.IDENTIFIER().getText()

    # Visit a parse tree produced by MT22Parser#paramterList.
    def visitParamterList(self, ctx: MT22Parser.ParamterListContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.paramterListTerm())

    # Visit a parse tree produced by MT22Parser#paramterListTerm.
    def visitParamterListTerm(self, ctx: MT22Parser.ParamterListTermContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.parameter())]
        return [self.visit(ctx.parameter())] + self.visit(ctx.paramterListTerm())

    # Visit a parse tree produced by MT22Parser#returnType.
    def visitReturnType(self, ctx: MT22Parser.ReturnTypeContext):
        if ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.AUTO():
            return AutoType()
        elif ctx.VOID():
            return VoidType()
        elif ctx.arraytype():
            return self.visit(ctx.arraytype())
        return BooleanType()

    # Visit a parse tree produced by MT22Parser#sfuncdecl.
    def visitSfuncdecl(self, ctx: MT22Parser.SfuncdeclContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MT22Parser#readInteger.
    def visitReadInteger(self, ctx: MT22Parser.ReadIntegerContext):
        # readInteger: READINTEGER LB RB;
        return ctx.READINTEGER().getText(), None

    # Visit a parse tree produced by MT22Parser#printInteger.
    def visitPrintInteger(self, ctx: MT22Parser.PrintIntegerContext):
        # printInteger: PRINTINTEGER LB expr RB;
        return ctx.PRINTINTEGER().getText(), self.visit(ctx.expr())

    # Visit a parse tree produced by MT22Parser#readFloat.
    def visitReadFloat(self, ctx: MT22Parser.ReadFloatContext):
        # readFloat: READFLOAT LB RB;
        return ctx.READFLOAT().getText(), None

    # Visit a parse tree produced by MT22Parser#writeFloat.
    def visitWriteFloat(self, ctx: MT22Parser.WriteFloatContext):
        # writeFloat: WRITEFLOAT LB expr RB;
        return ctx.WRITEFLOAT().getText(), self.visit(ctx.expr())

    # Visit a parse tree produced by MT22Parser#printBoolean.
    def visitPrintBoolean(self, ctx: MT22Parser.PrintBooleanContext):
        # printBoolean: PRINTBOOLEAN LB expr RB;
        return ctx.PRINTBOOLEAN().getText(), self.visit(ctx.expr())

    # Visit a parse tree produced by MT22Parser#readString.
    def visitReadString(self, ctx: MT22Parser.ReadStringContext):
        # readString: READSTRING LB RB;
        return ctx.READSTRING().getText(), None

    # Visit a parse tree produced by MT22Parser#printString.
    def visitPrintString(self, ctx: MT22Parser.PrintStringContext):
        # printString: PRINTSTRING LB expr RB;
        return ctx.PRINTSTRING().getText(), self.visit(ctx.expr())

    # Visit a parse tree produced by MT22Parser#superCall.
    def visitSuperCall(self, ctx: MT22Parser.SuperCallContext):
        # superCall: SUPER LB expr RB;
        return ctx.SUPER().getText(), self.visit(ctx.exprlist())

    # Visit a parse tree produced by MT22Parser#preventDefault.
    def visitPreventDefault(self, ctx: MT22Parser.PreventDefaultContext):
        # preventDefault: PREVENTDEFAULT LB RB;
        return ctx.PREVENTDEFAULT().getText(), None
