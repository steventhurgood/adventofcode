# Generated from CPU.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CPUParser import CPUParser
else:
    from CPUParser import CPUParser

# This class defines a complete listener for a parse tree produced by CPUParser.
class CPUListener(ParseTreeListener):

    # Enter a parse tree produced by CPUParser#commands.
    def enterCommands(self, ctx:CPUParser.CommandsContext):
        pass

    # Exit a parse tree produced by CPUParser#commands.
    def exitCommands(self, ctx:CPUParser.CommandsContext):
        pass


    # Enter a parse tree produced by CPUParser#command.
    def enterCommand(self, ctx:CPUParser.CommandContext):
        pass

    # Exit a parse tree produced by CPUParser#command.
    def exitCommand(self, ctx:CPUParser.CommandContext):
        pass


    # Enter a parse tree produced by CPUParser#noop.
    def enterNoop(self, ctx:CPUParser.NoopContext):
        pass

    # Exit a parse tree produced by CPUParser#noop.
    def exitNoop(self, ctx:CPUParser.NoopContext):
        pass


    # Enter a parse tree produced by CPUParser#addx.
    def enterAddx(self, ctx:CPUParser.AddxContext):
        pass

    # Exit a parse tree produced by CPUParser#addx.
    def exitAddx(self, ctx:CPUParser.AddxContext):
        pass


    # Enter a parse tree produced by CPUParser#count.
    def enterCount(self, ctx:CPUParser.CountContext):
        pass

    # Exit a parse tree produced by CPUParser#count.
    def exitCount(self, ctx:CPUParser.CountContext):
        pass



del CPUParser