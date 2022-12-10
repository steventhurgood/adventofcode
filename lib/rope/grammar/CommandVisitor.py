# type: ignore
# Generated from Command.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CommandParser import CommandParser
else:
    from CommandParser import CommandParser

# This class defines a complete generic visitor for a parse tree produced by CommandParser.


class CommandVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CommandParser#commands.
    def visitCommands(self, ctx: CommandParser.CommandsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CommandParser#command.
    def visitCommand(self, ctx: CommandParser.CommandContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CommandParser#direction.
    def visitDirection(self, ctx: CommandParser.DirectionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CommandParser#count.
    def visitCount(self, ctx: CommandParser.CountContext):
        return self.visitChildren(ctx)


del CommandParser
