# Generated from Monkey.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MonkeyParser import MonkeyParser
else:
    from MonkeyParser import MonkeyParser

# This class defines a complete generic visitor for a parse tree produced by MonkeyParser.

class MonkeyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MonkeyParser#monkeys.
    def visitMonkeys(self, ctx:MonkeyParser.MonkeysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#monkey.
    def visitMonkey(self, ctx:MonkeyParser.MonkeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#identifier.
    def visitIdentifier(self, ctx:MonkeyParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#number.
    def visitNumber(self, ctx:MonkeyParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#items.
    def visitItems(self, ctx:MonkeyParser.ItemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#itemlist.
    def visitItemlist(self, ctx:MonkeyParser.ItemlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#operation.
    def visitOperation(self, ctx:MonkeyParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#expr.
    def visitExpr(self, ctx:MonkeyParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#mul_old_expr.
    def visitMul_old_expr(self, ctx:MonkeyParser.Mul_old_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#mul_num_expr.
    def visitMul_num_expr(self, ctx:MonkeyParser.Mul_num_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#sum_old_expr.
    def visitSum_old_expr(self, ctx:MonkeyParser.Sum_old_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#sum_num_expr.
    def visitSum_num_expr(self, ctx:MonkeyParser.Sum_num_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#test.
    def visitTest(self, ctx:MonkeyParser.TestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#iftrue.
    def visitIftrue(self, ctx:MonkeyParser.IftrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MonkeyParser#iffalse.
    def visitIffalse(self, ctx:MonkeyParser.IffalseContext):
        return self.visitChildren(ctx)



del MonkeyParser