import sys
from token import TokenType

from Parser import *
from lexer import *





def compile_file(path: str):
    print("start compiling")


    with open(path) as file:
        code = file.read()

    lexer = Lexer(code)
    parser = Parser(lexer)

    parser.program()
    print("FINISCH!!!")
            





if __name__ == "__main__":
    compile_file(sys.argv[1]) # python compile.py hallo.q