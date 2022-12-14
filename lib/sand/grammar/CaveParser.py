# Generated from Cave.g4 by ANTLR 4.11.1
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
        4,1,5,41,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,0,
        14,8,0,11,0,12,0,15,1,0,3,0,19,8,0,1,1,1,1,1,1,5,1,24,8,1,10,1,12,
        1,27,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,5,0,0,
        6,0,2,4,6,8,10,0,0,37,0,13,1,0,0,0,2,20,1,0,0,0,4,30,1,0,0,0,6,34,
        1,0,0,0,8,36,1,0,0,0,10,38,1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,14,
        15,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,18,1,0,0,0,17,19,5,0,0,
        1,18,17,1,0,0,0,18,19,1,0,0,0,19,1,1,0,0,0,20,25,3,4,2,0,21,22,5,
        1,0,0,22,24,3,4,2,0,23,21,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,
        26,1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,28,29,5,3,0,0,29,3,1,0,0,
        0,30,31,3,6,3,0,31,32,5,2,0,0,32,33,3,8,4,0,33,5,1,0,0,0,34,35,3,
        10,5,0,35,7,1,0,0,0,36,37,3,10,5,0,37,9,1,0,0,0,38,39,5,4,0,0,39,
        11,1,0,0,0,3,15,18,25
    ]

class CaveParser ( Parser ):

    grammarFileName = "Cave.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'->'", "','", "'\\n'", "<INVALID>", "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "NL", "INT", 
                      "WS" ]

    RULE_cave = 0
    RULE_rock = 1
    RULE_pair = 2
    RULE_x = 3
    RULE_y = 4
    RULE_number = 5

    ruleNames =  [ "cave", "rock", "pair", "x", "y", "number" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    NL=3
    INT=4
    WS=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CaveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CaveParser.RockContext)
            else:
                return self.getTypedRuleContext(CaveParser.RockContext,i)


        def EOF(self):
            return self.getToken(CaveParser.EOF, 0)

        def getRuleIndex(self):
            return CaveParser.RULE_cave

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCave" ):
                listener.enterCave(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCave" ):
                listener.exitCave(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCave" ):
                return visitor.visitCave(self)
            else:
                return visitor.visitChildren(self)




    def cave(self):

        localctx = CaveParser.CaveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_cave)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.rock()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==4):
                    break

            self.state = 18
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 17
                self.match(CaveParser.EOF)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CaveParser.PairContext)
            else:
                return self.getTypedRuleContext(CaveParser.PairContext,i)


        def NL(self):
            return self.getToken(CaveParser.NL, 0)

        def getRuleIndex(self):
            return CaveParser.RULE_rock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRock" ):
                listener.enterRock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRock" ):
                listener.exitRock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRock" ):
                return visitor.visitRock(self)
            else:
                return visitor.visitChildren(self)




    def rock(self):

        localctx = CaveParser.RockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_rock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.pair()
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 21
                self.match(CaveParser.T__0)
                self.state = 22
                self.pair()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(CaveParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def x(self):
            return self.getTypedRuleContext(CaveParser.XContext,0)


        def y(self):
            return self.getTypedRuleContext(CaveParser.YContext,0)


        def getRuleIndex(self):
            return CaveParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair" ):
                return visitor.visitPair(self)
            else:
                return visitor.visitChildren(self)




    def pair(self):

        localctx = CaveParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.x()
            self.state = 31
            self.match(CaveParser.T__1)
            self.state = 32
            self.y()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class XContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(CaveParser.NumberContext,0)


        def getRuleIndex(self):
            return CaveParser.RULE_x

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterX" ):
                listener.enterX(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitX" ):
                listener.exitX(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitX" ):
                return visitor.visitX(self)
            else:
                return visitor.visitChildren(self)




    def x(self):

        localctx = CaveParser.XContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_x)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class YContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(CaveParser.NumberContext,0)


        def getRuleIndex(self):
            return CaveParser.RULE_y

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterY" ):
                listener.enterY(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitY" ):
                listener.exitY(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitY" ):
                return visitor.visitY(self)
            else:
                return visitor.visitChildren(self)




    def y(self):

        localctx = CaveParser.YContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_y)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CaveParser.INT, 0)

        def getRuleIndex(self):
            return CaveParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = CaveParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(CaveParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





