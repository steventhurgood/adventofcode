# Generated from Monkey.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MonkeyParser import MonkeyParser
else:
    from MonkeyParser import MonkeyParser

# This class defines a complete listener for a parse tree produced by MonkeyParser.
class MonkeyListener(ParseTreeListener):

    # Enter a parse tree produced by MonkeyParser#monkeys.
    def enterMonkeys(self, ctx:MonkeyParser.MonkeysContext):
        pass

    # Exit a parse tree produced by MonkeyParser#monkeys.
    def exitMonkeys(self, ctx:MonkeyParser.MonkeysContext):
        pass


    # Enter a parse tree produced by MonkeyParser#monkey.
    def enterMonkey(self, ctx:MonkeyParser.MonkeyContext):
        pass

    # Exit a parse tree produced by MonkeyParser#monkey.
    def exitMonkey(self, ctx:MonkeyParser.MonkeyContext):
        pass


    # Enter a parse tree produced by MonkeyParser#identifier.
    def enterIdentifier(self, ctx:MonkeyParser.IdentifierContext):
        pass

    # Exit a parse tree produced by MonkeyParser#identifier.
    def exitIdentifier(self, ctx:MonkeyParser.IdentifierContext):
        pass


    # Enter a parse tree produced by MonkeyParser#number.
    def enterNumber(self, ctx:MonkeyParser.NumberContext):
        pass

    # Exit a parse tree produced by MonkeyParser#number.
    def exitNumber(self, ctx:MonkeyParser.NumberContext):
        pass


    # Enter a parse tree produced by MonkeyParser#items.
    def enterItems(self, ctx:MonkeyParser.ItemsContext):
        pass

    # Exit a parse tree produced by MonkeyParser#items.
    def exitItems(self, ctx:MonkeyParser.ItemsContext):
        pass


    # Enter a parse tree produced by MonkeyParser#itemlist.
    def enterItemlist(self, ctx:MonkeyParser.ItemlistContext):
        pass

    # Exit a parse tree produced by MonkeyParser#itemlist.
    def exitItemlist(self, ctx:MonkeyParser.ItemlistContext):
        pass


    # Enter a parse tree produced by MonkeyParser#operation.
    def enterOperation(self, ctx:MonkeyParser.OperationContext):
        pass

    # Exit a parse tree produced by MonkeyParser#operation.
    def exitOperation(self, ctx:MonkeyParser.OperationContext):
        pass


    # Enter a parse tree produced by MonkeyParser#expr.
    def enterExpr(self, ctx:MonkeyParser.ExprContext):
        pass

    # Exit a parse tree produced by MonkeyParser#expr.
    def exitExpr(self, ctx:MonkeyParser.ExprContext):
        pass


    # Enter a parse tree produced by MonkeyParser#mul_old_expr.
    def enterMul_old_expr(self, ctx:MonkeyParser.Mul_old_exprContext):
        pass

    # Exit a parse tree produced by MonkeyParser#mul_old_expr.
    def exitMul_old_expr(self, ctx:MonkeyParser.Mul_old_exprContext):
        pass


    # Enter a parse tree produced by MonkeyParser#mul_num_expr.
    def enterMul_num_expr(self, ctx:MonkeyParser.Mul_num_exprContext):
        pass

    # Exit a parse tree produced by MonkeyParser#mul_num_expr.
    def exitMul_num_expr(self, ctx:MonkeyParser.Mul_num_exprContext):
        pass


    # Enter a parse tree produced by MonkeyParser#sum_old_expr.
    def enterSum_old_expr(self, ctx:MonkeyParser.Sum_old_exprContext):
        pass

    # Exit a parse tree produced by MonkeyParser#sum_old_expr.
    def exitSum_old_expr(self, ctx:MonkeyParser.Sum_old_exprContext):
        pass


    # Enter a parse tree produced by MonkeyParser#sum_num_expr.
    def enterSum_num_expr(self, ctx:MonkeyParser.Sum_num_exprContext):
        pass

    # Exit a parse tree produced by MonkeyParser#sum_num_expr.
    def exitSum_num_expr(self, ctx:MonkeyParser.Sum_num_exprContext):
        pass


    # Enter a parse tree produced by MonkeyParser#test.
    def enterTest(self, ctx:MonkeyParser.TestContext):
        pass

    # Exit a parse tree produced by MonkeyParser#test.
    def exitTest(self, ctx:MonkeyParser.TestContext):
        pass


    # Enter a parse tree produced by MonkeyParser#iftrue.
    def enterIftrue(self, ctx:MonkeyParser.IftrueContext):
        pass

    # Exit a parse tree produced by MonkeyParser#iftrue.
    def exitIftrue(self, ctx:MonkeyParser.IftrueContext):
        pass


    # Enter a parse tree produced by MonkeyParser#iffalse.
    def enterIffalse(self, ctx:MonkeyParser.IffalseContext):
        pass

    # Exit a parse tree produced by MonkeyParser#iffalse.
    def exitIffalse(self, ctx:MonkeyParser.IffalseContext):
        pass



del MonkeyParser