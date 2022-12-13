# Generated from Compare.g4 by ANTLR 4.11.1
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
        4,1,6,45,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        1,0,4,0,16,8,0,11,0,12,0,17,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,
        1,4,3,4,30,8,4,1,4,3,4,33,8,4,1,5,1,5,1,6,1,6,1,6,5,6,40,8,6,10,
        6,12,6,43,9,6,1,6,0,0,7,0,2,4,6,8,10,12,0,0,41,0,15,1,0,0,0,2,19,
        1,0,0,0,4,22,1,0,0,0,6,24,1,0,0,0,8,32,1,0,0,0,10,34,1,0,0,0,12,
        36,1,0,0,0,14,16,3,2,1,0,15,14,1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,
        0,17,18,1,0,0,0,18,1,1,0,0,0,19,20,3,4,2,0,20,21,3,6,3,0,21,3,1,
        0,0,0,22,23,3,8,4,0,23,5,1,0,0,0,24,25,3,8,4,0,25,7,1,0,0,0,26,33,
        3,10,5,0,27,29,5,1,0,0,28,30,3,12,6,0,29,28,1,0,0,0,29,30,1,0,0,
        0,30,31,1,0,0,0,31,33,5,2,0,0,32,26,1,0,0,0,32,27,1,0,0,0,33,9,1,
        0,0,0,34,35,5,4,0,0,35,11,1,0,0,0,36,41,3,8,4,0,37,38,5,3,0,0,38,
        40,3,8,4,0,39,37,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,
        0,42,13,1,0,0,0,43,41,1,0,0,0,4,17,29,32,41
    ]

class CompareParser ( Parser ):

    grammarFileName = "Compare.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "COMMA", "INT", 
                      "WS", "END" ]

    RULE_pairs = 0
    RULE_pair = 1
    RULE_left = 2
    RULE_right = 3
    RULE_list_or_int = 4
    RULE_number = 5
    RULE_list = 6

    ruleNames =  [ "pairs", "pair", "left", "right", "list_or_int", "number", 
                   "list" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    COMMA=3
    INT=4
    WS=5
    END=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PairsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompareParser.PairContext)
            else:
                return self.getTypedRuleContext(CompareParser.PairContext,i)


        def getRuleIndex(self):
            return CompareParser.RULE_pairs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPairs" ):
                listener.enterPairs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPairs" ):
                listener.exitPairs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPairs" ):
                return visitor.visitPairs(self)
            else:
                return visitor.visitChildren(self)




    def pairs(self):

        localctx = CompareParser.PairsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_pairs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.pair()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==4):
                    break

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

        def left(self):
            return self.getTypedRuleContext(CompareParser.LeftContext,0)


        def right(self):
            return self.getTypedRuleContext(CompareParser.RightContext,0)


        def getRuleIndex(self):
            return CompareParser.RULE_pair

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

        localctx = CompareParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.left()
            self.state = 20
            self.right()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LeftContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_or_int(self):
            return self.getTypedRuleContext(CompareParser.List_or_intContext,0)


        def getRuleIndex(self):
            return CompareParser.RULE_left

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeft" ):
                listener.enterLeft(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeft" ):
                listener.exitLeft(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeft" ):
                return visitor.visitLeft(self)
            else:
                return visitor.visitChildren(self)




    def left(self):

        localctx = CompareParser.LeftContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_left)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.list_or_int()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RightContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_or_int(self):
            return self.getTypedRuleContext(CompareParser.List_or_intContext,0)


        def getRuleIndex(self):
            return CompareParser.RULE_right

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRight" ):
                listener.enterRight(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRight" ):
                listener.exitRight(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRight" ):
                return visitor.visitRight(self)
            else:
                return visitor.visitChildren(self)




    def right(self):

        localctx = CompareParser.RightContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_right)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.list_or_int()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_or_intContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(CompareParser.NumberContext,0)


        def list_(self):
            return self.getTypedRuleContext(CompareParser.ListContext,0)


        def getRuleIndex(self):
            return CompareParser.RULE_list_or_int

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_or_int" ):
                listener.enterList_or_int(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_or_int" ):
                listener.exitList_or_int(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_or_int" ):
                return visitor.visitList_or_int(self)
            else:
                return visitor.visitChildren(self)




    def list_or_int(self):

        localctx = CompareParser.List_or_intContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_list_or_int)
        self._la = 0 # Token type
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.number()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(CompareParser.T__0)
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1 or _la==4:
                    self.state = 28
                    self.list_()


                self.state = 31
                self.match(CompareParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

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
            return self.getToken(CompareParser.INT, 0)

        def getRuleIndex(self):
            return CompareParser.RULE_number

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

        localctx = CompareParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(CompareParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_or_int(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompareParser.List_or_intContext)
            else:
                return self.getTypedRuleContext(CompareParser.List_or_intContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CompareParser.COMMA)
            else:
                return self.getToken(CompareParser.COMMA, i)

        def getRuleIndex(self):
            return CompareParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = CompareParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.list_or_int()
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 37
                self.match(CompareParser.COMMA)
                self.state = 38
                self.list_or_int()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





