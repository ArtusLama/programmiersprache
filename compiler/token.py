

import enum

class Token:

    def __init__(self, tokenText, tokenKind):
        self.text = tokenText
        self.kind = tokenKind


class TokenType(enum.Enum):

        EOF = -1
        NEWLINE = 0

        INT = 1
        FLOAT = 2
        VAR_NAME = 3
        STRING = 4

        VAR_TYPE_INT = [10, "int"]
        VAR_TYPE_FLOAT = [11, "float"]
        VAR_TYPE_STRING = [12, "str"]
        
        FUNC_NAME = 13


        BRACKET_OPEN = 51
        BRACKET_CLOSE = 52

        #keywords
        PRINT = [101, "print"]
        IF = [102, "if"]
        ELIF = [103, "elif"]
        RETURN = [104, "return"]
        ELSE = 105


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
        


