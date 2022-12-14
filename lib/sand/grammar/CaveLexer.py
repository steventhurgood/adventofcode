# Generated from Cave.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,5,30,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,
        0,1,1,1,1,1,2,1,2,1,3,3,3,20,8,3,1,3,4,3,23,8,3,11,3,12,3,24,1,4,
        1,4,1,4,1,4,0,0,5,1,1,3,2,5,3,7,4,9,5,1,0,1,1,0,48,57,31,0,1,1,0,
        0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,1,11,1,0,0,0,
        3,14,1,0,0,0,5,16,1,0,0,0,7,19,1,0,0,0,9,26,1,0,0,0,11,12,5,45,0,
        0,12,13,5,62,0,0,13,2,1,0,0,0,14,15,5,44,0,0,15,4,1,0,0,0,16,17,
        5,10,0,0,17,6,1,0,0,0,18,20,5,45,0,0,19,18,1,0,0,0,19,20,1,0,0,0,
        20,22,1,0,0,0,21,23,7,0,0,0,22,21,1,0,0,0,23,24,1,0,0,0,24,22,1,
        0,0,0,24,25,1,0,0,0,25,8,1,0,0,0,26,27,5,32,0,0,27,28,1,0,0,0,28,
        29,6,4,0,0,29,10,1,0,0,0,3,0,19,24,1,6,0,0
    ]

class CaveLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    NL = 3
    INT = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'->'", "','", "'\\n'", "' '" ]

    symbolicNames = [ "<INVALID>",
            "NL", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "NL", "INT", "WS" ]

    grammarFileName = "Cave.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


