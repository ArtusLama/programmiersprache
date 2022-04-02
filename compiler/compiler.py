#!/usr/bin/env python3
import sys
from token import TokenType

from Parser import *
from emitter import Emitter
from lexer import *





def compile_file(path: str):
    print("start compiling")


    with open(path) as file:
        code = file.read()

    lexer = Lexer(code)
    emitter = Emitter("out.c")
    parser = Parser(lexer, emitter)

    parser.program()
    #emitter.writeFile()
    print("FINISCH!!!")
            





if __name__ == "__main__":
    compile_file(sys.argv[1]) # python compile.py hallo.q
