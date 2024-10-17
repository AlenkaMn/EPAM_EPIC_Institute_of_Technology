# Generated from Tokenize.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,1,7,6,-1,2,0,7,0,1,0,1,0,1,0,1,0,0,0,1,1,1,1,0,1,2,0,9,10,32,
        32,6,0,1,1,0,0,0,1,3,1,0,0,0,3,4,7,0,0,0,4,5,1,0,0,0,5,6,6,0,0,0,
        6,2,1,0,0,0,1,0,1,6,0,0
    ]

class Tokenize(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SPACE = 1

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "SPACE" ]

    ruleNames = [ "SPACE" ]

    grammarFileName = "Tokenize.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


