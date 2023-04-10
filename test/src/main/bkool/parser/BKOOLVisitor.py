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


    # Visit a parse tree produced by BKOOLParser#array_type.
    def visitArray_type(self, ctx:BKOOLParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#element_type.
    def visitElement_type(self, ctx:BKOOLParser.Element_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#dimesion.
    def visitDimesion(self, ctx:BKOOLParser.DimesionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#dimesion_type_int.
    def visitDimesion_type_int(self, ctx:BKOOLParser.Dimesion_type_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#dimesion_type_float.
    def visitDimesion_type_float(self, ctx:BKOOLParser.Dimesion_type_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#variable_decl.
    def visitVariable_decl(self, ctx:BKOOLParser.Variable_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_decl_no_eq.
    def visitVar_decl_no_eq(self, ctx:BKOOLParser.Var_decl_no_eqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_decl_eq.
    def visitVar_decl_eq(self, ctx:BKOOLParser.Var_decl_eqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#recursive.
    def visitRecursive(self, ctx:BKOOLParser.RecursiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_list.
    def visitArray_list(self, ctx:BKOOLParser.Array_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp_list_term.
    def visitExp_list_term(self, ctx:BKOOLParser.Exp_list_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#identifier_list.
    def visitIdentifier_list(self, ctx:BKOOLParser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression_list.
    def visitExpression_list(self, ctx:BKOOLParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp_list_type_int.
    def visitExp_list_type_int(self, ctx:BKOOLParser.Exp_list_type_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp_list_type_float.
    def visitExp_list_type_float(self, ctx:BKOOLParser.Exp_list_type_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp_list_type_string.
    def visitExp_list_type_string(self, ctx:BKOOLParser.Exp_list_type_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#parameter.
    def visitParameter(self, ctx:BKOOLParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression.
    def visitExpression(self, ctx:BKOOLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression_1.
    def visitExpression_1(self, ctx:BKOOLParser.Expression_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression_2.
    def visitExpression_2(self, ctx:BKOOLParser.Expression_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression_3.
    def visitExpression_3(self, ctx:BKOOLParser.Expression_3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression_4.
    def visitExpression_4(self, ctx:BKOOLParser.Expression_4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression_5.
    def visitExpression_5(self, ctx:BKOOLParser.Expression_5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression_6.
    def visitExpression_6(self, ctx:BKOOLParser.Expression_6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression_7.
    def visitExpression_7(self, ctx:BKOOLParser.Expression_7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression_8.
    def visitExpression_8(self, ctx:BKOOLParser.Expression_8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#factor.
    def visitFactor(self, ctx:BKOOLParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#function_call.
    def visitFunction_call(self, ctx:BKOOLParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exps_list.
    def visitExps_list(self, ctx:BKOOLParser.Exps_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp_list.
    def visitExp_list(self, ctx:BKOOLParser.Exp_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#statement.
    def visitStatement(self, ctx:BKOOLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assign_stmt.
    def visitAssign_stmt(self, ctx:BKOOLParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs.
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#if_stmt.
    def visitIf_stmt(self, ctx:BKOOLParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#for_stmt.
    def visitFor_stmt(self, ctx:BKOOLParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#scala_val.
    def visitScala_val(self, ctx:BKOOLParser.Scala_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#init_expr.
    def visitInit_expr(self, ctx:BKOOLParser.Init_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#condition_expr.
    def visitCondition_expr(self, ctx:BKOOLParser.Condition_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#update_expr.
    def visitUpdate_expr(self, ctx:BKOOLParser.Update_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#while_stmt.
    def visitWhile_stmt(self, ctx:BKOOLParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:BKOOLParser.Do_while_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#call_stmt.
    def visitCall_stmt(self, ctx:BKOOLParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#block_stmt.
    def visitBlock_stmt(self, ctx:BKOOLParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#statement_term.
    def visitStatement_term(self, ctx:BKOOLParser.Statement_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#statement_list.
    def visitStatement_list(self, ctx:BKOOLParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#break_stmt.
    def visitBreak_stmt(self, ctx:BKOOLParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#continue_stmt.
    def visitContinue_stmt(self, ctx:BKOOLParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_stmt.
    def visitReturn_stmt(self, ctx:BKOOLParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#function_decl.
    def visitFunction_decl(self, ctx:BKOOLParser.Function_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#inheritance.
    def visitInheritance(self, ctx:BKOOLParser.InheritanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#function_name.
    def visitFunction_name(self, ctx:BKOOLParser.Function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramter_list.
    def visitParamter_list(self, ctx:BKOOLParser.Paramter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramter_list_term.
    def visitParamter_list_term(self, ctx:BKOOLParser.Paramter_list_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_type.
    def visitReturn_type(self, ctx:BKOOLParser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#s_func_decl.
    def visitS_func_decl(self, ctx:BKOOLParser.S_func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#read_integer.
    def visitRead_integer(self, ctx:BKOOLParser.Read_integerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#print_integer.
    def visitPrint_integer(self, ctx:BKOOLParser.Print_integerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#read_float.
    def visitRead_float(self, ctx:BKOOLParser.Read_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#write_float.
    def visitWrite_float(self, ctx:BKOOLParser.Write_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#print_boolean.
    def visitPrint_boolean(self, ctx:BKOOLParser.Print_booleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#read_string.
    def visitRead_string(self, ctx:BKOOLParser.Read_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#print_string.
    def visitPrint_string(self, ctx:BKOOLParser.Print_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#super_.
    def visitSuper_(self, ctx:BKOOLParser.Super_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#prevent_default.
    def visitPrevent_default(self, ctx:BKOOLParser.Prevent_defaultContext):
        return self.visitChildren(ctx)



del BKOOLParser