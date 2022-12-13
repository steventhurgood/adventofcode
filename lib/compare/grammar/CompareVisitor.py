# Generated from Compare.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CompareParser import CompareParser
else:
    from CompareParser import CompareParser

# This class defines a complete generic visitor for a parse tree produced by CompareParser.

class CompareVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CompareParser#pairs.
    def visitPairs(self, ctx:CompareParser.PairsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompareParser#pair.
    def visitPair(self, ctx:CompareParser.PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompareParser#left.
    def visitLeft(self, ctx:CompareParser.LeftContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompareParser#right.
    def visitRight(self, ctx:CompareParser.RightContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompareParser#list_or_int.
    def visitList_or_int(self, ctx:CompareParser.List_or_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompareParser#number.
    def visitNumber(self, ctx:CompareParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompareParser#list.
    def visitList(self, ctx:CompareParser.ListContext):
        return self.visitChildren(ctx)



del CompareParser