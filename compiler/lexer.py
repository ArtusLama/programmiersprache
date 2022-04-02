
import sys
from token import Token, TokenType
#from compiler.token import TokenType

class Lexer:

    def __init__(self, input):
        
        self.code = input + "\n"
        
        self.curChar = ""
        self.curPos = -1
        self.nextChar()


    def error(self, message):
        sys.exit("\n[LEXING ERROR]\n-> " + message)

    def skipComment(self):
        if self.curChar == "#":
            while self.curChar != "\n":
                self.nextChar()
    
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
        self.skipComment()

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





        elif self.curChar == "=":
            if self.peek() == "=":
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.EQEQ)
            else:
                token = Token(self.curChar, TokenType.EQ)

        elif self.curChar == ">":
            if self.peek() == "=":
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.GREATEREQUAL)
            else:
                token = Token(self.curChar, TokenType.GREATER)

        elif self.curChar == "<":
            if self.peek() == "=":
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.LESSEQUAL)
            else:
                token = Token(self.curChar, TokenType.LESS)

        elif self.curChar == "!":
            if self.peek() == "=":
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.NOTEQ)
            else:
                self.error(f"Expected '!=', got '!{self.peek()}'")


        elif self.curChar == '\"':
 
            self.nextChar()
            startPos = self.curPos

            while self.curChar != '\"':
                if self.curChar == '\r' or self.curChar == '\n' or self.curChar == '\t' or self.curChar == '\\' or self.curChar == '%':
                    self.error("Illegal character in string.")
                self.nextChar()

            tokenText = self.code[startPos : self.curPos]
            token = Token(tokenText, TokenType.STRING)



        else:
            self.error(f"Unknown token '{self.curChar}'")

        self.nextChar()
        return token