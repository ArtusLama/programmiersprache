import sys
from token import TokenType

from lexer import Lexer





def compile_file(path: str):
    print("start compiling")
    with open(path) as file:
        for line in file:

            lexer = Lexer(line)
            #lexer = Lexer("int main<str argv> {")

            token = lexer.getToken()
            while token.kind != TokenType.EOF:
                if token.kind != TokenType.NEWLINE:
                    print(token.kind)
                token = lexer.getToken()

            # while lexer.peek() != "\0":
            #     lexer.nextChar()
            





if __name__ == "__main__":
    compile_file(sys.argv[1]) # python compile.py hallo.q