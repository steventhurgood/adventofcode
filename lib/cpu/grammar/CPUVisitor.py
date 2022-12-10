# Generated from CPU.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CPUParser import CPUParser
else:
    from CPUParser import CPUParser

# This class defines a complete generic visitor for a parse tree produced by CPUParser.

class CPUVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CPUParser#commands.
    def visitCommands(self, ctx:CPUParser.CommandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPUParser#command.
    def visitCommand(self, ctx:CPUParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPUParser#noop.
    def visitNoop(self, ctx:CPUParser.NoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPUParser#addx.
    def visitAddx(self, ctx:CPUParser.AddxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPUParser#count.
    def visitCount(self, ctx:CPUParser.CountContext):
        return self.visitChildren(ctx)



del CPUParser