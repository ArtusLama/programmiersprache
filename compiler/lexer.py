
from keyword import iskeyword
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

        elif self.curChar == "{":
            token = Token(self.curChar, TokenType.BRACKET_OPEN)
        elif self.curChar == "}":
            token = Token(self.curChar, TokenType.BRACKET_CLOSE)
        
        


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
            elif self.peek() == ">":
                lastChar = self.curChar
                self.nextChar()
                token = Token(lastChar + self.curChar, TokenType.ELSE)
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

            
        elif self.curChar.isdigit():
            
            startPos = self.curPos
            isFloat = False

            self.nextChar()
            while self.curChar.isdigit() or self.curChar == ".":
                if self.curChar == ".":
                    if not isFloat: isFloat = True
                    else: self.error("Second '.' in number")
                self.nextChar()

                

            tokenText = self.code[startPos : self.curPos]
            
            #token = isFloat if Token(tokenText, TokenType.FLOAT) else Token(tokenText, TokenType.INT)
            if isFloat:
                token = Token(tokenText, TokenType.FLOAT)
            else:
                token = Token(tokenText, TokenType.INT)


        elif self.curChar.isalpha():
            startPos = self.curPos
            while self.curChar.isalpha():
                self.nextChar()

            tokenText = self.code[startPos : self.curPos]

            isKeyword = False
            for kind in TokenType:
                if type(kind.value) != int:
                    if kind.value[1] == tokenText:
                        token = Token(tokenText, kind)
                        isKeyword = True
                        break
            
            if not isKeyword:
                token = Token(tokenText, TokenType.VAR_NAME)

        else:
            self.error(f"Unknown token '{self.curChar}'")
        
        self.nextChar()
        return token