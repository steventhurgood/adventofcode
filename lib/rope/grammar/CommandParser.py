# type: ignore
# Generated from Command.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4, 1, 7, 26, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 2, 3, 7, 3, 1, 0, 4, 0, 10, 8, 0, 11, 0, 12,
        0, 11, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 20, 8, 1, 1, 2, 1, 2, 1, 3, 1, 3, 1, 3, 0, 0,
        4, 0, 2, 4, 6, 0, 1, 1, 0, 1, 4, 23, 0, 9, 1, 0, 0, 0, 2, 15, 1, 0, 0, 0, 4, 21, 1, 0, 0, 0, 6,
        23, 1, 0, 0, 0, 8, 10, 3, 2, 1, 0, 9, 8, 1, 0, 0, 0, 10, 11, 1, 0, 0, 0, 11, 9, 1, 0, 0, 0, 11,
        12, 1, 0, 0, 0, 12, 13, 1, 0, 0, 0, 13, 14, 5, 0, 0, 1, 14, 1, 1, 0, 0, 0, 15, 16, 3, 4, 2,
        0, 16, 17, 5, 6, 0, 0, 17, 19, 3, 6, 3, 0, 18, 20, 5, 7, 0, 0, 19, 18, 1, 0, 0, 0, 19, 20,
        1, 0, 0, 0, 20, 3, 1, 0, 0, 0, 21, 22, 7, 0, 0, 0, 22, 5, 1, 0, 0, 0, 23, 24, 5, 5, 0, 0, 24,
        7, 1, 0, 0, 0, 2, 11, 19
    ]


class CommandParser (Parser):

    grammarFileName = "Command.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'U'", "'D'", "'L'", "'R'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "INT", "WHITESPACE", "NEWLINE"]

    RULE_commands = 0
    RULE_command = 1
    RULE_direction = 2
    RULE_count = 3

    ruleNames = ["commands", "command", "direction", "count"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    INT = 5
    WHITESPACE = 6
    NEWLINE = 7

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class CommandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CommandParser.EOF, 0)

        def command(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(CommandParser.CommandContext)
            else:
                return self.getTypedRuleContext(CommandParser.CommandContext, i)

        def getRuleIndex(self):
            return CommandParser.RULE_commands

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterCommands"):
                listener.enterCommands(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitCommands"):
                listener.exitCommands(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitCommands"):
                return visitor.visitCommands(self)
            else:
                return visitor.visitChildren(self)

    def commands(self):

        localctx = CommandParser.CommandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_commands)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.command()
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0):
                    break

            self.state = 13
            self.match(CommandParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def direction(self):
            return self.getTypedRuleContext(CommandParser.DirectionContext, 0)

        def WHITESPACE(self):
            return self.getToken(CommandParser.WHITESPACE, 0)

        def count(self):
            return self.getTypedRuleContext(CommandParser.CountContext, 0)

        def NEWLINE(self):
            return self.getToken(CommandParser.NEWLINE, 0)

        def getRuleIndex(self):
            return CommandParser.RULE_command

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterCommand"):
                listener.enterCommand(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitCommand"):
                listener.exitCommand(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitCommand"):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)

    def command(self):

        localctx = CommandParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.direction()
            self.state = 16
            self.match(CommandParser.WHITESPACE)
            self.state = 17
            self.count()
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 7:
                self.state = 18
                self.match(CommandParser.NEWLINE)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DirectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return CommandParser.RULE_direction

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterDirection"):
                listener.enterDirection(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitDirection"):
                listener.exitDirection(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitDirection"):
                return visitor.visitDirection(self)
            else:
                return visitor.visitChildren(self)

    def direction(self):

        localctx = CommandParser.DirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_direction)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CountContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CommandParser.INT, 0)

        def getRuleIndex(self):
            return CommandParser.RULE_count

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterCount"):
                listener.enterCount(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitCount"):
                listener.exitCount(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitCount"):
                return visitor.visitCount(self)
            else:
                return visitor.visitChildren(self)

    def count(self):

        localctx = CommandParser.CountContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_count)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(CommandParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
