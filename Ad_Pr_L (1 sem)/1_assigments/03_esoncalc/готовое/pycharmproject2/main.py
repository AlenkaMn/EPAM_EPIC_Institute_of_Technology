import math
from antlr4 import FileStream, CommonTokenStream
from EsonLexer import EsonLexer
from EsonParser import EsonParser
from EsonVisitor import EsonVisitor
import datetime
import json
import sys


def parse_time(time):
    return datetime.datetime.strptime(
        time,
        '%H:%M:%S.%f' if '.' in time[:15] else '%H:%M:%S')


def parse_date(date):
    return datetime.datetime.fromisoformat(date)


def parse_datetime(dt):
    d, t = dt.split('T')
    d = parse_date(d)
    t = parse_time(t)
    return datetime.datetime.combine(d.date(), t.time())


def format_date(time):
    return time.strftime('%Y-%m-%d')


def format_time(date):
    return date.strftime('%H:%M:%S.%f')


def format_datetime(dt):
    return dt.strftime('%Y-%m-%dT%H:%M:%S.%f')


class Visitor(EsonVisitor):
    def visitStart(self, ctx: EsonParser.ItemContext):
        return self.visitObject(ctx.object_())

    def visitObject(self, ctx: EsonParser.ObjectContext):
        result = {}
        for pair_1 in ctx.pair():
            pair = self.visitPair(pair_1)
            if pair:
                i, j = pair
                if i:
                    result[i] = j
        return result

    def visitDict(self, ctx: EsonParser.DictContext):
        dic = {}
        for i in ctx.pair():
            pair_result = self.visit(i)
            if pair_result:
                i, j = pair_result
                if i!=None and j!=None:
                    dic[i] = j
        return dic

    def visitPair(self, ctx: EsonParser.PairContext):
        key_ctx = ctx.key()
        value_ctx = ctx.value()

        if key_ctx is not None and value_ctx is not None:
            key = self.visitKey(key_ctx)
            value = self.visitValue(value_ctx)
            if value == 'null':
                return key, None
            return key, value
        else:
            return None

    def visitKey(self, ctx: EsonParser.KeyContext):
        if ctx.WORD():
            name = ctx.WORD().getText()
            if name[0]==name[-1]=='"':
                name = name[1:-1]
            return name
        elif ctx.FOR_DOUBLE_QUOTES():
            return str(ctx.FOR_DOUBLE_QUOTES().getText()[1:-1]).encode().decode('unicode_escape')

    def visitValue(self, ctx: EsonParser.ValueContext):
        if ctx.NUMBER():
            result = self.parseNumber(ctx.NUMBER().getText())
            if not isinstance(result, float):
                return int(result)
            return float(result)
        elif ctx.NULL():
            return None
        elif ctx.FOR_SINGLE_QUOTES():
            return str(ctx.FOR_SINGLE_QUOTES().getText()[1:-1]).encode().decode('unicode_escape')
        elif ctx.FOR_DOUBLE_QUOTES():
            return str(ctx.FOR_DOUBLE_QUOTES().getText()[1:-1]).encode().decode('unicode_escape')
        elif ctx.WORD():
            return ctx.WORD().getText()
        elif ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.array():
            return self.visitArray(ctx.array())
        elif ctx.TIME():
            time_get = parse_time(ctx.TIME().getText())
            return format_time(time_get)
        elif ctx.DATE():
            date_get = parse_date(ctx.DATE().getText())
            return format_date(date_get)
        elif ctx.DATETIME():
            datetime_get = parse_datetime(ctx.DATETIME().getText())
            return format_datetime(datetime_get)
        elif ctx.BOOL():
            if ctx.BOOL().getText() == "true":
                return True
            else:
                return False
        elif ctx.dict_():
            return self.visit(ctx.dict_())

        else:
            return None

    def visitExpr(self, ctx: EsonParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.term())
        else:
            l = self.visit(ctx.expr())
            r = self.visit(ctx.term())
            # сумма
            if ctx.getChild(1).getText() == '+':
                return l + r
            # разность
            else:
                return l - r

    def visitTerm(self, ctx: EsonParser.TermContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.factor())
        else:
            l = self.visit(ctx.term())
            r = self.visit(ctx.factor())
            # умножить
            if ctx.getChild(1).getText() == '*':
                return l * r
            # поделить
            else:  # '/'
                return l / r

    def visitFactor(self, ctx: EsonParser.FactorContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.primary())
        else:
            return -self.visit(ctx.factor())
        
    def parseNumber(self, number_str):
        return (
            int(number_str, 16) if number_str.startswith("0x") or number_str.startswith("-0x") or number_str.startswith(
                "+0x")
            else int(number_str, 8) if (number_str.startswith("0") or number_str.startswith(
                "+0") or number_str.startswith("-0")) and "." not in number_str and "e" not in number_str
            else int(number_str) if "." not in number_str and "e" not in number_str
            else float(number_str)
        )
        
    def visitPrimary(self, ctx: EsonParser.PrimaryContext):
        if ctx.NUMBER():
            result = self.parseNumber(ctx.NUMBER().getText())
            if not isinstance(result, float):
                return int(result)
            return float(result)
        elif ctx.SIN():
            expr_result = self.visitExpr(ctx.expr())
            return math.sin(expr_result)
        elif ctx.COS():
            expr_result = self.visitExpr(ctx.expr())
            return math.cos(expr_result)
        else:
            return self.visit(ctx.expr())
    
    def visitArray(self, ctx: EsonParser.ArrayContext):
        return [self.visitValue(value_ctx) for value_ctx in ctx.value()]
    
    
in_stream = FileStream('input.eson')
lexer = EsonLexer(in_stream)
stream = CommonTokenStream(lexer)
parser = EsonParser(stream)
tree = parser.item()
visitor = Visitor()
result = visitor.visit(tree)
json.dump(result, sys.stdout, indent='  ', sort_keys=True)
