# Generated from Eson.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .EsonParser import EsonParser
else:
    from EsonParser import EsonParser

# This class defines a complete generic visitor for a parse tree produced by EsonParser.

class EsonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EsonParser#start.
    def visitStart(self, ctx:EsonParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsonParser#item.
    def visitItem(self, ctx:EsonParser.ItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsonParser#object.
    def visitObject(self, ctx:EsonParser.ObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsonParser#pair.
    def visitPair(self, ctx:EsonParser.PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsonParser#key.
    def visitKey(self, ctx:EsonParser.KeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsonParser#value.
    def visitValue(self, ctx:EsonParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsonParser#array.
    def visitArray(self, ctx:EsonParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsonParser#dict.
    def visitDict(self, ctx:EsonParser.DictContext):
        return self.visitChildren(ctx)



del EsonParser