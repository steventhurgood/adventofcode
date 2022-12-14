# Generated from Cave.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CaveParser import CaveParser
else:
    from CaveParser import CaveParser

# This class defines a complete listener for a parse tree produced by CaveParser.
class CaveListener(ParseTreeListener):

    # Enter a parse tree produced by CaveParser#cave.
    def enterCave(self, ctx:CaveParser.CaveContext):
        pass

    # Exit a parse tree produced by CaveParser#cave.
    def exitCave(self, ctx:CaveParser.CaveContext):
        pass


    # Enter a parse tree produced by CaveParser#rock.
    def enterRock(self, ctx:CaveParser.RockContext):
        pass

    # Exit a parse tree produced by CaveParser#rock.
    def exitRock(self, ctx:CaveParser.RockContext):
        pass


    # Enter a parse tree produced by CaveParser#pair.
    def enterPair(self, ctx:CaveParser.PairContext):
        pass

    # Exit a parse tree produced by CaveParser#pair.
    def exitPair(self, ctx:CaveParser.PairContext):
        pass


    # Enter a parse tree produced by CaveParser#x.
    def enterX(self, ctx:CaveParser.XContext):
        pass

    # Exit a parse tree produced by CaveParser#x.
    def exitX(self, ctx:CaveParser.XContext):
        pass


    # Enter a parse tree produced by CaveParser#y.
    def enterY(self, ctx:CaveParser.YContext):
        pass

    # Exit a parse tree produced by CaveParser#y.
    def exitY(self, ctx:CaveParser.YContext):
        pass


    # Enter a parse tree produced by CaveParser#number.
    def enterNumber(self, ctx:CaveParser.NumberContext):
        pass

    # Exit a parse tree produced by CaveParser#number.
    def exitNumber(self, ctx:CaveParser.NumberContext):
        pass



del CaveParser