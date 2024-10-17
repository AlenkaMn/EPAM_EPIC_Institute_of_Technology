from antlr4 import FileStream, CommonTokenStream
from EsonLexer import EsonLexer
from EsonParser import EsonParser
from EsonVisitor import EsonVisitor
import datetime
import json
import sys
from datetime import datetime
import datetime


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
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%f")


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
        if ctx:
            key = self.visitKey(ctx.key()) if ctx.key() else None
            value = self.visitValue(ctx.value()) if ctx.value() else None

            if value == 'null':
                return (key, None) if key else None
            return (key, value) if key else None
        return None


    def visitKey(self, ctx: EsonParser.KeyContext):
        if ctx.WORD():
            name = ctx.WORD().getText()
            if name[0]==name[-1]=='"':
                name = name[1:-1]
            return name
        elif ctx.FOR_DOUBLE_QUOTES():
            return str(ctx.FOR_DOUBLE_QUOTES().getText()[1:-1]).encode().decode('unicode_escape')

    def parseNumber(self, number_str):
        return (
            int(number_str, 16) if number_str.startswith("0x") or number_str.startswith("-0x") or number_str.startswith(
                "+0x")
            else int(number_str, 8) if (number_str.startswith("0") or number_str.startswith(
                "+0") or number_str.startswith("-0")) and "." not in number_str and "e" not in number_str
            else int(number_str) if "." not in number_str and "e" not in number_str
            else float(number_str)
        )

    def visitValue(self, ctx: EsonParser.ValueContext):
        if ctx.NULL():
            return None
        elif ctx.FOR_SINGLE_QUOTES():
            return str(ctx.FOR_SINGLE_QUOTES().getText()[1:-1]).encode().decode('unicode_escape')
        elif ctx.FOR_DOUBLE_QUOTES():
            return str(ctx.FOR_DOUBLE_QUOTES().getText()[1:-1]).encode().decode('unicode_escape')
        elif ctx.WORD():
            return ctx.WORD().getText()
        elif ctx.DATE():
            date_get = parse_date(ctx.DATE().getText())
            return format_date(date_get)
        elif ctx.DATETIME():
            datetime_get = parse_datetime(ctx.DATETIME().getText())
            return format_datetime(datetime_get)
        elif ctx.TIME():
            time_get = parse_time(ctx.TIME().getText())
            return format_time(time_get)
        elif ctx.NUMBER():
            return self.parseNumber(ctx.NUMBER().getText())
        elif ctx.INTEGER():
            return int(ctx.INTEGER().getText())
        elif ctx.dict_():
            return self.visit(ctx.dict_())
        elif ctx.array():
            return self.visitArray(ctx.array())
        elif ctx.BOOL():
            if ctx.BOOL().getText() == "true":
                return True
            else:
                return False
        else:
            return None

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
