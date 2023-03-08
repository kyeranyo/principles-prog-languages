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



del BKOOLParser