# Generated from Eson.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .EsonParser import EsonParser
else:
    from EsonParser import EsonParser

# This class defines a complete listener for a parse tree produced by EsonParser.
class EsonListener(ParseTreeListener):

    # Enter a parse tree produced by EsonParser#start.
    def enterStart(self, ctx:EsonParser.StartContext):
        pass

    # Exit a parse tree produced by EsonParser#start.
    def exitStart(self, ctx:EsonParser.StartContext):
        pass


    # Enter a parse tree produced by EsonParser#item.
    def enterItem(self, ctx:EsonParser.ItemContext):
        pass

    # Exit a parse tree produced by EsonParser#item.
    def exitItem(self, ctx:EsonParser.ItemContext):
        pass


    # Enter a parse tree produced by EsonParser#object.
    def enterObject(self, ctx:EsonParser.ObjectContext):
        pass

    # Exit a parse tree produced by EsonParser#object.
    def exitObject(self, ctx:EsonParser.ObjectContext):
        pass


    # Enter a parse tree produced by EsonParser#pair.
    def enterPair(self, ctx:EsonParser.PairContext):
        pass

    # Exit a parse tree produced by EsonParser#pair.
    def exitPair(self, ctx:EsonParser.PairContext):
        pass


    # Enter a parse tree produced by EsonParser#key.
    def enterKey(self, ctx:EsonParser.KeyContext):
        pass

    # Exit a parse tree produced by EsonParser#key.
    def exitKey(self, ctx:EsonParser.KeyContext):
        pass


    # Enter a parse tree produced by EsonParser#value.
    def enterValue(self, ctx:EsonParser.ValueContext):
        pass

    # Exit a parse tree produced by EsonParser#value.
    def exitValue(self, ctx:EsonParser.ValueContext):
        pass


    # Enter a parse tree produced by EsonParser#array.
    def enterArray(self, ctx:EsonParser.ArrayContext):
        pass

    # Exit a parse tree produced by EsonParser#array.
    def exitArray(self, ctx:EsonParser.ArrayContext):
        pass


    # Enter a parse tree produced by EsonParser#dict.
    def enterDict(self, ctx:EsonParser.DictContext):
        pass

    # Exit a parse tree produced by EsonParser#dict.
    def exitDict(self, ctx:EsonParser.DictContext):
        pass



del EsonParser