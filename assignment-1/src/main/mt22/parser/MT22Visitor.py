# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decls.
    def visitDecls(self, ctx:MT22Parser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_type.
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#element_type.
    def visitElement_type(self, ctx:MT22Parser.Element_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimesion.
    def visitDimesion(self, ctx:MT22Parser.DimesionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimesion_type_int.
    def visitDimesion_type_int(self, ctx:MT22Parser.Dimesion_type_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimesion_type_float.
    def visitDimesion_type_float(self, ctx:MT22Parser.Dimesion_type_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#variable_decl.
    def visitVariable_decl(self, ctx:MT22Parser.Variable_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#equal_exp.
    def visitEqual_exp(self, ctx:MT22Parser.Equal_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#identifier_list.
    def visitIdentifier_list(self, ctx:MT22Parser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_list.
    def visitExpression_list(self, ctx:MT22Parser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_list_type_int.
    def visitExp_list_type_int(self, ctx:MT22Parser.Exp_list_type_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_list_type_float.
    def visitExp_list_type_float(self, ctx:MT22Parser.Exp_list_type_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_list_type_string.
    def visitExp_list_type_string(self, ctx:MT22Parser.Exp_list_type_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter.
    def visitParameter(self, ctx:MT22Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function_decl.
    def visitFunction_decl(self, ctx:MT22Parser.Function_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#inheritance.
    def visitInheritance(self, ctx:MT22Parser.InheritanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function_name.
    def visitFunction_name(self, ctx:MT22Parser.Function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramter_list.
    def visitParamter_list(self, ctx:MT22Parser.Paramter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramter_list_term.
    def visitParamter_list_term(self, ctx:MT22Parser.Paramter_list_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_type.
    def visitReturn_type(self, ctx:MT22Parser.Return_typeContext):
        return self.visitChildren(ctx)



del MT22Parser