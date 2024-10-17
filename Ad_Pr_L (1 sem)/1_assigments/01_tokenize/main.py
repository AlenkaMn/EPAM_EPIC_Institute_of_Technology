from antlr4 import InputStream
import Tokenize
print("hui")
f = open('input.txt')
for line in f.readlines():
    in_stream = InputStream(line.strip())
    lexer = Tokenize.Tokenize(in_stream)
    print('---')6ЦЙ3цуы
    for token in lexer.getAllTokens():
        print(token.text)