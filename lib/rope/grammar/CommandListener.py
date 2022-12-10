# Generated from Command.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CommandParser import CommandParser
else:
    from CommandParser import CommandParser

# This class defines a complete listener for a parse tree produced by CommandParser.
class CommandListener(ParseTreeListener):

    # Enter a parse tree produced by CommandParser#commands.
    def enterCommands(self, ctx:CommandParser.CommandsContext):
        pass

    # Exit a parse tree produced by CommandParser#commands.
    def exitCommands(self, ctx:CommandParser.CommandsContext):
        pass


    # Enter a parse tree produced by CommandParser#command.
    def enterCommand(self, ctx:CommandParser.CommandContext):
        pass

    # Exit a parse tree produced by CommandParser#command.
    def exitCommand(self, ctx:CommandParser.CommandContext):
        pass


    # Enter a parse tree produced by CommandParser#direction.
    def enterDirection(self, ctx:CommandParser.DirectionContext):
        pass

    # Exit a parse tree produced by CommandParser#direction.
    def exitDirection(self, ctx:CommandParser.DirectionContext):
        pass


    # Enter a parse tree produced by CommandParser#count.
    def enterCount(self, ctx:CommandParser.CountContext):
        pass

    # Exit a parse tree produced by CommandParser#count.
    def exitCount(self, ctx:CommandParser.CountContext):
        pass



del CommandParser