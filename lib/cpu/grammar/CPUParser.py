# Generated from CPU.g4 by ANTLR 4.11.1
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
        4,1,5,33,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,0,1,0,1,1,1,1,3,1,20,8,1,1,1,3,1,23,8,1,1,2,1,2,1,
        3,1,3,1,3,1,3,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,0,30,0,11,1,0,0,0,2,
        19,1,0,0,0,4,24,1,0,0,0,6,26,1,0,0,0,8,30,1,0,0,0,10,12,3,2,1,0,
        11,10,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,15,1,
        0,0,0,15,16,5,0,0,1,16,1,1,0,0,0,17,20,3,4,2,0,18,20,3,6,3,0,19,
        17,1,0,0,0,19,18,1,0,0,0,20,22,1,0,0,0,21,23,5,4,0,0,22,21,1,0,0,
        0,22,23,1,0,0,0,23,3,1,0,0,0,24,25,5,1,0,0,25,5,1,0,0,0,26,27,5,
        2,0,0,27,28,5,5,0,0,28,29,3,8,4,0,29,7,1,0,0,0,30,31,5,3,0,0,31,
        9,1,0,0,0,3,13,19,22
    ]

class CPUParser ( Parser ):

    grammarFileName = "CPU.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'noop'", "'addx'", "<INVALID>", "'\\n'", 
                     "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "INT", "NL", 
                      "WS" ]

    RULE_commands = 0
    RULE_command = 1
    RULE_noop = 2
    RULE_addx = 3
    RULE_count = 4

    ruleNames =  [ "commands", "command", "noop", "addx", "count" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    INT=3
    NL=4
    WS=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CommandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CPUParser.EOF, 0)

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPUParser.CommandContext)
            else:
                return self.getTypedRuleContext(CPUParser.CommandContext,i)


        def getRuleIndex(self):
            return CPUParser.RULE_commands

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommands" ):
                listener.enterCommands(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommands" ):
                listener.exitCommands(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommands" ):
                return visitor.visitCommands(self)
            else:
                return visitor.visitChildren(self)




    def commands(self):

        localctx = CPUParser.CommandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_commands)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.command()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==2):
                    break

            self.state = 15
            self.match(CPUParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def noop(self):
            return self.getTypedRuleContext(CPUParser.NoopContext,0)


        def addx(self):
            return self.getTypedRuleContext(CPUParser.AddxContext,0)


        def NL(self):
            return self.getToken(CPUParser.NL, 0)

        def getRuleIndex(self):
            return CPUParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = CPUParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 17
                self.noop()
                pass
            elif token in [2]:
                self.state = 18
                self.addx()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 21
                self.match(CPUParser.NL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CPUParser.RULE_noop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNoop" ):
                listener.enterNoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNoop" ):
                listener.exitNoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoop" ):
                return visitor.visitNoop(self)
            else:
                return visitor.visitChildren(self)




    def noop(self):

        localctx = CPUParser.NoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_noop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(CPUParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WS(self):
            return self.getToken(CPUParser.WS, 0)

        def count(self):
            return self.getTypedRuleContext(CPUParser.CountContext,0)


        def getRuleIndex(self):
            return CPUParser.RULE_addx

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddx" ):
                listener.enterAddx(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddx" ):
                listener.exitAddx(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddx" ):
                return visitor.visitAddx(self)
            else:
                return visitor.visitChildren(self)




    def addx(self):

        localctx = CPUParser.AddxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_addx)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(CPUParser.T__1)
            self.state = 27
            self.match(CPUParser.WS)
            self.state = 28
            self.count()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CountContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CPUParser.INT, 0)

        def getRuleIndex(self):
            return CPUParser.RULE_count

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCount" ):
                listener.enterCount(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCount" ):
                listener.exitCount(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCount" ):
                return visitor.visitCount(self)
            else:
                return visitor.visitChildren(self)




    def count(self):

        localctx = CPUParser.CountContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_count)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(CPUParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





