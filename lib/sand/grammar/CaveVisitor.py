# Generated from Cave.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CaveParser import CaveParser
else:
    from CaveParser import CaveParser

# This class defines a complete generic visitor for a parse tree produced by CaveParser.

class CaveVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CaveParser#cave.
    def visitCave(self, ctx:CaveParser.CaveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaveParser#rock.
    def visitRock(self, ctx:CaveParser.RockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaveParser#pair.
    def visitPair(self, ctx:CaveParser.PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaveParser#x.
    def visitX(self, ctx:CaveParser.XContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaveParser#y.
    def visitY(self, ctx:CaveParser.YContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CaveParser#number.
    def visitNumber(self, ctx:CaveParser.NumberContext):
        return self.visitChildren(ctx)



del CaveParser