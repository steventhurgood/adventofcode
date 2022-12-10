# Generated from CPU.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,5,33,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,
        0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,2,3,2,23,8,2,1,2,4,2,26,8,2,11,2,
        12,2,27,1,3,1,3,1,4,1,4,0,0,5,1,1,3,2,5,3,7,4,9,5,1,0,1,1,0,48,57,
        34,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,1,
        11,1,0,0,0,3,16,1,0,0,0,5,22,1,0,0,0,7,29,1,0,0,0,9,31,1,0,0,0,11,
        12,5,110,0,0,12,13,5,111,0,0,13,14,5,111,0,0,14,15,5,112,0,0,15,
        2,1,0,0,0,16,17,5,97,0,0,17,18,5,100,0,0,18,19,5,100,0,0,19,20,5,
        120,0,0,20,4,1,0,0,0,21,23,5,45,0,0,22,21,1,0,0,0,22,23,1,0,0,0,
        23,25,1,0,0,0,24,26,7,0,0,0,25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,
        0,0,0,27,28,1,0,0,0,28,6,1,0,0,0,29,30,5,10,0,0,30,8,1,0,0,0,31,
        32,5,32,0,0,32,10,1,0,0,0,3,0,22,27,0
    ]

class CPULexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    INT = 3
    NL = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'noop'", "'addx'", "'\\n'", "' '" ]

    symbolicNames = [ "<INVALID>",
            "INT", "NL", "WS" ]

    ruleNames = [ "T__0", "T__1", "INT", "NL", "WS" ]

    grammarFileName = "CPU.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


