# Generated from Eson.g4 by ANTLR 4.13.1
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
        4,1,26,85,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,5,2,26,8,2,10,2,12,
        2,29,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,3,5,51,8,5,1,6,1,6,1,6,1,6,5,6,57,8,6,10,
        6,12,6,60,9,6,3,6,62,8,6,1,6,3,6,65,8,6,1,6,1,6,1,7,1,7,1,7,1,7,
        5,7,73,8,7,10,7,12,7,76,9,7,3,7,78,8,7,1,7,3,7,81,8,7,1,7,1,7,1,
        7,0,0,8,0,2,4,6,8,10,12,14,0,1,2,0,15,15,17,17,94,0,16,1,0,0,0,2,
        19,1,0,0,0,4,21,1,0,0,0,6,32,1,0,0,0,8,36,1,0,0,0,10,50,1,0,0,0,
        12,52,1,0,0,0,14,68,1,0,0,0,16,17,3,2,1,0,17,18,5,0,0,1,18,1,1,0,
        0,0,19,20,3,4,2,0,20,3,1,0,0,0,21,22,5,1,0,0,22,27,3,6,3,0,23,24,
        5,2,0,0,24,26,3,6,3,0,25,23,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,
        27,28,1,0,0,0,28,30,1,0,0,0,29,27,1,0,0,0,30,31,5,3,0,0,31,5,1,0,
        0,0,32,33,3,8,4,0,33,34,5,4,0,0,34,35,3,10,5,0,35,7,1,0,0,0,36,37,
        7,0,0,0,37,9,1,0,0,0,38,51,5,17,0,0,39,51,3,12,6,0,40,51,3,14,7,
        0,41,51,5,9,0,0,42,51,5,10,0,0,43,51,5,12,0,0,44,51,5,13,0,0,45,
        51,5,14,0,0,46,51,5,15,0,0,47,51,5,16,0,0,48,51,5,18,0,0,49,51,5,
        19,0,0,50,38,1,0,0,0,50,39,1,0,0,0,50,40,1,0,0,0,50,41,1,0,0,0,50,
        42,1,0,0,0,50,43,1,0,0,0,50,44,1,0,0,0,50,45,1,0,0,0,50,46,1,0,0,
        0,50,47,1,0,0,0,50,48,1,0,0,0,50,49,1,0,0,0,51,11,1,0,0,0,52,61,
        5,5,0,0,53,58,3,10,5,0,54,55,5,2,0,0,55,57,3,10,5,0,56,54,1,0,0,
        0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,62,1,0,0,0,60,58,
        1,0,0,0,61,53,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,65,5,2,0,0,
        64,63,1,0,0,0,64,65,1,0,0,0,65,66,1,0,0,0,66,67,5,6,0,0,67,13,1,
        0,0,0,68,77,5,1,0,0,69,74,3,6,3,0,70,71,5,2,0,0,71,73,3,6,3,0,72,
        70,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,78,1,0,0,
        0,76,74,1,0,0,0,77,69,1,0,0,0,77,78,1,0,0,0,78,80,1,0,0,0,79,81,
        5,2,0,0,80,79,1,0,0,0,80,81,1,0,0,0,81,82,1,0,0,0,82,83,5,3,0,0,
        83,15,1,0,0,0,8,27,50,58,61,64,74,77,80
    ]

class EsonParser ( Parser ):

    grammarFileName = "Eson.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "','", "'}'", "'='", "'['", "']'", 
                     "<INVALID>", "<INVALID>", "'null'", "<INVALID>", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "SPACE", "COMMENT", 
                      "NULL", "BOOL", "DOT", "DATE", "DATETIME", "TIME", 
                      "FOR_DOUBLE_QUOTES", "FOR_SINGLE_QUOTES", "WORD", 
                      "NUMBER", "INTEGER", "OCTAL_NUMBER", "INT", "EXPONENT", 
                      "FLOAT", "HEX", "DIGIT", "HEX_DIGIT" ]

    RULE_start = 0
    RULE_item = 1
    RULE_object = 2
    RULE_pair = 3
    RULE_key = 4
    RULE_value = 5
    RULE_array = 6
    RULE_dict = 7

    ruleNames =  [ "start", "item", "object", "pair", "key", "value", "array", 
                   "dict" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    SPACE=7
    COMMENT=8
    NULL=9
    BOOL=10
    DOT=11
    DATE=12
    DATETIME=13
    TIME=14
    FOR_DOUBLE_QUOTES=15
    FOR_SINGLE_QUOTES=16
    WORD=17
    NUMBER=18
    INTEGER=19
    OCTAL_NUMBER=20
    INT=21
    EXPONENT=22
    FLOAT=23
    HEX=24
    DIGIT=25
    HEX_DIGIT=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def item(self):
            return self.getTypedRuleContext(EsonParser.ItemContext,0)


        def EOF(self):
            return self.getToken(EsonParser.EOF, 0)

        def getRuleIndex(self):
            return EsonParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = EsonParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.item()
            self.state = 17
            self.match(EsonParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def object_(self):
            return self.getTypedRuleContext(EsonParser.ObjectContext,0)


        def getRuleIndex(self):
            return EsonParser.RULE_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem" ):
                listener.enterItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem" ):
                listener.exitItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem" ):
                return visitor.visitItem(self)
            else:
                return visitor.visitChildren(self)




    def item(self):

        localctx = EsonParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.object_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EsonParser.PairContext)
            else:
                return self.getTypedRuleContext(EsonParser.PairContext,i)


        def getRuleIndex(self):
            return EsonParser.RULE_object

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject" ):
                listener.enterObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject" ):
                listener.exitObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject" ):
                return visitor.visitObject(self)
            else:
                return visitor.visitChildren(self)




    def object_(self):

        localctx = EsonParser.ObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_object)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(EsonParser.T__0)
            self.state = 22
            self.pair()
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 23
                self.match(EsonParser.T__1)
                self.state = 24
                self.pair()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
            self.match(EsonParser.T__2)
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

        def key(self):
            return self.getTypedRuleContext(EsonParser.KeyContext,0)


        def value(self):
            return self.getTypedRuleContext(EsonParser.ValueContext,0)


        def getRuleIndex(self):
            return EsonParser.RULE_pair

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

        localctx = EsonParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.key()
            self.state = 33
            self.match(EsonParser.T__3)
            self.state = 34
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(EsonParser.WORD, 0)

        def FOR_DOUBLE_QUOTES(self):
            return self.getToken(EsonParser.FOR_DOUBLE_QUOTES, 0)

        def getRuleIndex(self):
            return EsonParser.RULE_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey" ):
                listener.enterKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey" ):
                listener.exitKey(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKey" ):
                return visitor.visitKey(self)
            else:
                return visitor.visitChildren(self)




    def key(self):

        localctx = EsonParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_key)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            _la = self._input.LA(1)
            if not(_la==15 or _la==17):
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


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(EsonParser.WORD, 0)

        def array(self):
            return self.getTypedRuleContext(EsonParser.ArrayContext,0)


        def dict_(self):
            return self.getTypedRuleContext(EsonParser.DictContext,0)


        def NULL(self):
            return self.getToken(EsonParser.NULL, 0)

        def BOOL(self):
            return self.getToken(EsonParser.BOOL, 0)

        def DATE(self):
            return self.getToken(EsonParser.DATE, 0)

        def DATETIME(self):
            return self.getToken(EsonParser.DATETIME, 0)

        def TIME(self):
            return self.getToken(EsonParser.TIME, 0)

        def FOR_DOUBLE_QUOTES(self):
            return self.getToken(EsonParser.FOR_DOUBLE_QUOTES, 0)

        def FOR_SINGLE_QUOTES(self):
            return self.getToken(EsonParser.FOR_SINGLE_QUOTES, 0)

        def NUMBER(self):
            return self.getToken(EsonParser.NUMBER, 0)

        def INTEGER(self):
            return self.getToken(EsonParser.INTEGER, 0)

        def getRuleIndex(self):
            return EsonParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = EsonParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_value)
        try:
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(EsonParser.WORD)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.array()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.dict_()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 41
                self.match(EsonParser.NULL)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 42
                self.match(EsonParser.BOOL)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 6)
                self.state = 43
                self.match(EsonParser.DATE)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 7)
                self.state = 44
                self.match(EsonParser.DATETIME)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 8)
                self.state = 45
                self.match(EsonParser.TIME)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 9)
                self.state = 46
                self.match(EsonParser.FOR_DOUBLE_QUOTES)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 10)
                self.state = 47
                self.match(EsonParser.FOR_SINGLE_QUOTES)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 11)
                self.state = 48
                self.match(EsonParser.NUMBER)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 12)
                self.state = 49
                self.match(EsonParser.INTEGER)
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


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EsonParser.ValueContext)
            else:
                return self.getTypedRuleContext(EsonParser.ValueContext,i)


        def getRuleIndex(self):
            return EsonParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = EsonParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(EsonParser.T__4)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1046050) != 0):
                self.state = 53
                self.value()
                self.state = 58
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 54
                        self.match(EsonParser.T__1)
                        self.state = 55
                        self.value() 
                    self.state = 60
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)



            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 63
                self.match(EsonParser.T__1)


            self.state = 66
            self.match(EsonParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DictContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EsonParser.PairContext)
            else:
                return self.getTypedRuleContext(EsonParser.PairContext,i)


        def getRuleIndex(self):
            return EsonParser.RULE_dict

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDict" ):
                listener.enterDict(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDict" ):
                listener.exitDict(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDict" ):
                return visitor.visitDict(self)
            else:
                return visitor.visitChildren(self)




    def dict_(self):

        localctx = EsonParser.DictContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_dict)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(EsonParser.T__0)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15 or _la==17:
                self.state = 69
                self.pair()
                self.state = 74
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 70
                        self.match(EsonParser.T__1)
                        self.state = 71
                        self.pair() 
                    self.state = 76
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)



            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 79
                self.match(EsonParser.T__1)


            self.state = 82
            self.match(EsonParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





