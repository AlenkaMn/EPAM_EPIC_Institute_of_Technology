from antlr4 import InputStream
import Tokenize

f = open('input.txt')
for line in f.readlines():
    in_stream = InputStream(line.strip())
    lexer = Tokenize.Tokenize(in_stream)
    print('---')
    for token in lexer.getAllTokens():
        print(token.text)