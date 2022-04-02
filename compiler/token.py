

from lib2to3.pgen2.token import INDENT, STRING


class Token:

    def __init__(self, tokenText, tokenKind):

        self.text = tokenText
        self.kind = tokenKind


class TokenType(enum.Enum):

        EOF = -1
        NEWLINE = 0

        NUMBER = 1
        INDENT = 2
        STRING = 3

        #keywords
        PRINT = 101

        #operators
        EQ = 201
        PLUS = 202
        MINUS = 203
        MULTIPLY = 204
        DIVISION = 205
