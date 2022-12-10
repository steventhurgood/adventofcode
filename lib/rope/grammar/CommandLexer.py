# Generated from Command.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,35,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,4,4,25,8,4,11,4,12,4,26,
        1,5,4,5,30,8,5,11,5,12,5,31,1,6,1,6,0,0,7,1,1,3,2,5,3,7,4,9,5,11,
        6,13,7,1,0,3,1,0,48,57,2,0,9,9,32,32,2,0,10,10,13,13,36,0,1,1,0,
        0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,
        0,13,1,0,0,0,1,15,1,0,0,0,3,17,1,0,0,0,5,19,1,0,0,0,7,21,1,0,0,0,
        9,24,1,0,0,0,11,29,1,0,0,0,13,33,1,0,0,0,15,16,5,85,0,0,16,2,1,0,
        0,0,17,18,5,68,0,0,18,4,1,0,0,0,19,20,5,76,0,0,20,6,1,0,0,0,21,22,
        5,82,0,0,22,8,1,0,0,0,23,25,7,0,0,0,24,23,1,0,0,0,25,26,1,0,0,0,
        26,24,1,0,0,0,26,27,1,0,0,0,27,10,1,0,0,0,28,30,7,1,0,0,29,28,1,
        0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,12,1,0,0,0,33,
        34,7,2,0,0,34,14,1,0,0,0,3,0,26,31,0
    ]

class CommandLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    INT = 5
    WHITESPACE = 6
    NEWLINE = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'U'", "'D'", "'L'", "'R'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "WHITESPACE", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "INT", "WHITESPACE", "NEWLINE" ]

    grammarFileName = "Command.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


