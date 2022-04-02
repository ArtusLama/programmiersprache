



import enum
from lib2to3.pgen2.token import GREATEREQUAL, LESSEQUAL


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
        PLUS = 201
        MINUS = 202
        MULTIPLY = 203
        DIVISION = 204

        EQ = 205             # =
        EQEQ = 206           # ==
        NOTEQ = 207          # !=
        LESS = 208           # <
        LESSEQUAL = 209      # <=
        GREATER = 210        # >
        GREATEREQUAL = 211   # >=
        


