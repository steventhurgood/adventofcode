# Generated from Monkey.g4 by ANTLR 4.11.1
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
        4,1,15,100,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,3,0,33,8,0,4,0,35,8,0,11,0,12,0,36,1,0,3,0,40,
        8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,4,
        1,4,1,4,1,4,1,5,1,5,3,5,62,8,5,4,5,64,8,5,11,5,12,5,65,1,6,1,6,1,
        6,1,6,1,7,1,7,1,7,1,7,3,7,76,8,7,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,
        11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,
        14,1,14,1,14,0,0,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,0,
        92,0,34,1,0,0,0,2,41,1,0,0,0,4,48,1,0,0,0,6,53,1,0,0,0,8,55,1,0,
        0,0,10,63,1,0,0,0,12,67,1,0,0,0,14,75,1,0,0,0,16,77,1,0,0,0,18,79,
        1,0,0,0,20,82,1,0,0,0,22,84,1,0,0,0,24,87,1,0,0,0,26,91,1,0,0,0,
        28,95,1,0,0,0,30,32,3,2,1,0,31,33,5,14,0,0,32,31,1,0,0,0,32,33,1,
        0,0,0,33,35,1,0,0,0,34,30,1,0,0,0,35,36,1,0,0,0,36,34,1,0,0,0,36,
        37,1,0,0,0,37,39,1,0,0,0,38,40,5,0,0,1,39,38,1,0,0,0,39,40,1,0,0,
        0,40,1,1,0,0,0,41,42,3,4,2,0,42,43,3,8,4,0,43,44,3,12,6,0,44,45,
        3,24,12,0,45,46,3,26,13,0,46,47,3,28,14,0,47,3,1,0,0,0,48,49,5,1,
        0,0,49,50,3,6,3,0,50,51,5,2,0,0,51,52,5,14,0,0,52,5,1,0,0,0,53,54,
        5,13,0,0,54,7,1,0,0,0,55,56,5,11,0,0,56,57,3,10,5,0,57,58,5,14,0,
        0,58,9,1,0,0,0,59,61,3,6,3,0,60,62,5,12,0,0,61,60,1,0,0,0,61,62,
        1,0,0,0,62,64,1,0,0,0,63,59,1,0,0,0,64,65,1,0,0,0,65,63,1,0,0,0,
        65,66,1,0,0,0,66,11,1,0,0,0,67,68,5,3,0,0,68,69,3,14,7,0,69,70,5,
        14,0,0,70,13,1,0,0,0,71,76,3,16,8,0,72,76,3,18,9,0,73,76,3,20,10,
        0,74,76,3,22,11,0,75,71,1,0,0,0,75,72,1,0,0,0,75,73,1,0,0,0,75,74,
        1,0,0,0,76,15,1,0,0,0,77,78,5,4,0,0,78,17,1,0,0,0,79,80,5,5,0,0,
        80,81,3,6,3,0,81,19,1,0,0,0,82,83,5,6,0,0,83,21,1,0,0,0,84,85,5,
        7,0,0,85,86,3,6,3,0,86,23,1,0,0,0,87,88,5,8,0,0,88,89,3,6,3,0,89,
        90,5,14,0,0,90,25,1,0,0,0,91,92,5,9,0,0,92,93,3,6,3,0,93,94,5,14,
        0,0,94,27,1,0,0,0,95,96,5,10,0,0,96,97,3,6,3,0,97,98,5,14,0,0,98,
        29,1,0,0,0,6,32,36,39,61,65,75
    ]

class MonkeyParser ( Parser ):

    grammarFileName = "Monkey.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Monkey '", "':'", "'  Operation: new = old '", 
                     "'* old'", "'* '", "'+ old'", "'+ '", "'  Test: divisible by '", 
                     "'    If true: throw to monkey '", "'    If false: throw to monkey '", 
                     "'  Starting items: '", "', '", "<INVALID>", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ITEMS_PREFIX", 
                      "COMMA", "INT", "NL", "LINE" ]

    RULE_monkeys = 0
    RULE_monkey = 1
    RULE_identifier = 2
    RULE_number = 3
    RULE_items = 4
    RULE_itemlist = 5
    RULE_operation = 6
    RULE_expr = 7
    RULE_mul_old_expr = 8
    RULE_mul_num_expr = 9
    RULE_sum_old_expr = 10
    RULE_sum_num_expr = 11
    RULE_test = 12
    RULE_iftrue = 13
    RULE_iffalse = 14

    ruleNames =  [ "monkeys", "monkey", "identifier", "number", "items", 
                   "itemlist", "operation", "expr", "mul_old_expr", "mul_num_expr", 
                   "sum_old_expr", "sum_num_expr", "test", "iftrue", "iffalse" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    ITEMS_PREFIX=11
    COMMA=12
    INT=13
    NL=14
    LINE=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class MonkeysContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def monkey(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MonkeyParser.MonkeyContext)
            else:
                return self.getTypedRuleContext(MonkeyParser.MonkeyContext,i)


        def EOF(self):
            return self.getToken(MonkeyParser.EOF, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(MonkeyParser.NL)
            else:
                return self.getToken(MonkeyParser.NL, i)

        def getRuleIndex(self):
            return MonkeyParser.RULE_monkeys

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMonkeys" ):
                listener.enterMonkeys(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMonkeys" ):
                listener.exitMonkeys(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMonkeys" ):
                return visitor.visitMonkeys(self)
            else:
                return visitor.visitChildren(self)




    def monkeys(self):

        localctx = MonkeyParser.MonkeysContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_monkeys)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.monkey()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==14:
                    self.state = 31
                    self.match(MonkeyParser.NL)


                self.state = 36 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 38
                self.match(MonkeyParser.EOF)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MonkeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(MonkeyParser.IdentifierContext,0)


        def items(self):
            return self.getTypedRuleContext(MonkeyParser.ItemsContext,0)


        def operation(self):
            return self.getTypedRuleContext(MonkeyParser.OperationContext,0)


        def test(self):
            return self.getTypedRuleContext(MonkeyParser.TestContext,0)


        def iftrue(self):
            return self.getTypedRuleContext(MonkeyParser.IftrueContext,0)


        def iffalse(self):
            return self.getTypedRuleContext(MonkeyParser.IffalseContext,0)


        def getRuleIndex(self):
            return MonkeyParser.RULE_monkey

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMonkey" ):
                listener.enterMonkey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMonkey" ):
                listener.exitMonkey(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMonkey" ):
                return visitor.visitMonkey(self)
            else:
                return visitor.visitChildren(self)




    def monkey(self):

        localctx = MonkeyParser.MonkeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_monkey)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.identifier()
            self.state = 42
            self.items()
            self.state = 43
            self.operation()
            self.state = 44
            self.test()
            self.state = 45
            self.iftrue()
            self.state = 46
            self.iffalse()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(MonkeyParser.NumberContext,0)


        def NL(self):
            return self.getToken(MonkeyParser.NL, 0)

        def getRuleIndex(self):
            return MonkeyParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = MonkeyParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(MonkeyParser.T__0)
            self.state = 49
            self.number()
            self.state = 50
            self.match(MonkeyParser.T__1)
            self.state = 51
            self.match(MonkeyParser.NL)
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
            return self.getToken(MonkeyParser.INT, 0)

        def getRuleIndex(self):
            return MonkeyParser.RULE_number

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

        localctx = MonkeyParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(MonkeyParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ITEMS_PREFIX(self):
            return self.getToken(MonkeyParser.ITEMS_PREFIX, 0)

        def itemlist(self):
            return self.getTypedRuleContext(MonkeyParser.ItemlistContext,0)


        def NL(self):
            return self.getToken(MonkeyParser.NL, 0)

        def getRuleIndex(self):
            return MonkeyParser.RULE_items

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItems" ):
                listener.enterItems(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItems" ):
                listener.exitItems(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItems" ):
                return visitor.visitItems(self)
            else:
                return visitor.visitChildren(self)




    def items(self):

        localctx = MonkeyParser.ItemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_items)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(MonkeyParser.ITEMS_PREFIX)
            self.state = 56
            self.itemlist()
            self.state = 57
            self.match(MonkeyParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MonkeyParser.NumberContext)
            else:
                return self.getTypedRuleContext(MonkeyParser.NumberContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MonkeyParser.COMMA)
            else:
                return self.getToken(MonkeyParser.COMMA, i)

        def getRuleIndex(self):
            return MonkeyParser.RULE_itemlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItemlist" ):
                listener.enterItemlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItemlist" ):
                listener.exitItemlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItemlist" ):
                return visitor.visitItemlist(self)
            else:
                return visitor.visitChildren(self)




    def itemlist(self):

        localctx = MonkeyParser.ItemlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_itemlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 59
                self.number()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 60
                    self.match(MonkeyParser.COMMA)


                self.state = 65 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==13):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MonkeyParser.ExprContext,0)


        def NL(self):
            return self.getToken(MonkeyParser.NL, 0)

        def getRuleIndex(self):
            return MonkeyParser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperation" ):
                return visitor.visitOperation(self)
            else:
                return visitor.visitChildren(self)




    def operation(self):

        localctx = MonkeyParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_operation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(MonkeyParser.T__2)
            self.state = 68
            self.expr()
            self.state = 69
            self.match(MonkeyParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mul_old_expr(self):
            return self.getTypedRuleContext(MonkeyParser.Mul_old_exprContext,0)


        def mul_num_expr(self):
            return self.getTypedRuleContext(MonkeyParser.Mul_num_exprContext,0)


        def sum_old_expr(self):
            return self.getTypedRuleContext(MonkeyParser.Sum_old_exprContext,0)


        def sum_num_expr(self):
            return self.getTypedRuleContext(MonkeyParser.Sum_num_exprContext,0)


        def getRuleIndex(self):
            return MonkeyParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MonkeyParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expr)
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.mul_old_expr()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.mul_num_expr()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.sum_old_expr()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 74
                self.sum_num_expr()
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


    class Mul_old_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyParser.RULE_mul_old_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul_old_expr" ):
                listener.enterMul_old_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul_old_expr" ):
                listener.exitMul_old_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_old_expr" ):
                return visitor.visitMul_old_expr(self)
            else:
                return visitor.visitChildren(self)




    def mul_old_expr(self):

        localctx = MonkeyParser.Mul_old_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_mul_old_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(MonkeyParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mul_num_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(MonkeyParser.NumberContext,0)


        def getRuleIndex(self):
            return MonkeyParser.RULE_mul_num_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul_num_expr" ):
                listener.enterMul_num_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul_num_expr" ):
                listener.exitMul_num_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_num_expr" ):
                return visitor.visitMul_num_expr(self)
            else:
                return visitor.visitChildren(self)




    def mul_num_expr(self):

        localctx = MonkeyParser.Mul_num_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_mul_num_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(MonkeyParser.T__4)
            self.state = 80
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sum_old_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MonkeyParser.RULE_sum_old_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSum_old_expr" ):
                listener.enterSum_old_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSum_old_expr" ):
                listener.exitSum_old_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSum_old_expr" ):
                return visitor.visitSum_old_expr(self)
            else:
                return visitor.visitChildren(self)




    def sum_old_expr(self):

        localctx = MonkeyParser.Sum_old_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_sum_old_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(MonkeyParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sum_num_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(MonkeyParser.NumberContext,0)


        def getRuleIndex(self):
            return MonkeyParser.RULE_sum_num_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSum_num_expr" ):
                listener.enterSum_num_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSum_num_expr" ):
                listener.exitSum_num_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSum_num_expr" ):
                return visitor.visitSum_num_expr(self)
            else:
                return visitor.visitChildren(self)




    def sum_num_expr(self):

        localctx = MonkeyParser.Sum_num_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_sum_num_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(MonkeyParser.T__6)
            self.state = 85
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(MonkeyParser.NumberContext,0)


        def NL(self):
            return self.getToken(MonkeyParser.NL, 0)

        def getRuleIndex(self):
            return MonkeyParser.RULE_test

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTest" ):
                listener.enterTest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTest" ):
                listener.exitTest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTest" ):
                return visitor.visitTest(self)
            else:
                return visitor.visitChildren(self)




    def test(self):

        localctx = MonkeyParser.TestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_test)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(MonkeyParser.T__7)
            self.state = 88
            self.number()
            self.state = 89
            self.match(MonkeyParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IftrueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(MonkeyParser.NumberContext,0)


        def NL(self):
            return self.getToken(MonkeyParser.NL, 0)

        def getRuleIndex(self):
            return MonkeyParser.RULE_iftrue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIftrue" ):
                listener.enterIftrue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIftrue" ):
                listener.exitIftrue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIftrue" ):
                return visitor.visitIftrue(self)
            else:
                return visitor.visitChildren(self)




    def iftrue(self):

        localctx = MonkeyParser.IftrueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_iftrue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(MonkeyParser.T__8)
            self.state = 92
            self.number()
            self.state = 93
            self.match(MonkeyParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IffalseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(MonkeyParser.NumberContext,0)


        def NL(self):
            return self.getToken(MonkeyParser.NL, 0)

        def getRuleIndex(self):
            return MonkeyParser.RULE_iffalse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIffalse" ):
                listener.enterIffalse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIffalse" ):
                listener.exitIffalse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIffalse" ):
                return visitor.visitIffalse(self)
            else:
                return visitor.visitChildren(self)




    def iffalse(self):

        localctx = MonkeyParser.IffalseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_iffalse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(MonkeyParser.T__9)
            self.state = 96
            self.number()
            self.state = 97
            self.match(MonkeyParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





