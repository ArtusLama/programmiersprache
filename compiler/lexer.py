
import sys
from token import Token, TokenType


class Lexer:

    def __init__(self, input):
        
        self.code = input + "\n"
        
        self.curChar = ""
        self.curPos = -1
        self.nextChar()


    def error(self, message):
        sys.exit("\n[LEXING ERROR]\n-> " + message)


    
    def nextChar(self):
        self.curPos += 1
        if self.curPos >= len(self.code):
            self.curChar = "\0"
        else:
            self.curChar = self.code[self.curPos]

        


    def peek(self):
        if self.curPos + 1 >= len(self.code):
            return "\0"
        return self.code[self.curPos + 1]


    def skipWhitespace(self):
        while self.curChar == " " or self.curChar == "\t" or self.curChar == "\r":
            self.nextChar()

    
    def getToken(self):
        self.skipWhitespace()
        
        token = None

        # MATH OPERATORS
        if self.curChar == "+":
            token = Token(self.curChar, TokenType.PLUS)
        elif self.curChar == "-":
            token = Token(self.curChar, TokenType.MINUS)
        elif self.curChar == "*":
            token = Token(self.curChar, TokenType.MULTIPLY)
        elif self.curChar == "/":
            token = Token(self.curChar, TokenType.DIVISION)

        
        
        elif self.curChar == "\n":
            token = Token(self.curChar, TokenType.NEWLINE)
        elif self.curChar == "\0":
            token = Token("", TokenType.EOF)




        else:
            self.error(f"Unknown token '{self.curChar}'")

        self.nextChar()
        return token