
import sys
from token import TokenType
from lexer import *
class Parser:

    def __init__(self, lexer):
        self.lexer = lexer

        self.curToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()

    def checkToken(self, kind):
        return kind == self.curToken.kind


    def checkPeek(self, kind):
        return kind == self.peekToken.kind


    def match(self, kind):
        if not self.checkToken:
            self.error(f"Expected '{kind.name}', got '{self.curToken.kind.name}'")
        self.nextToken()


    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()

    def error(self, message):
        sys.exit("\n[Error]\n-> " + message)
    
    def statement(self):



        if self.checkToken(TokenType.PRINT):
            print("PRINT STATEMENT")

            self.nextToken()
            if self.checkToken(TokenType.LESS):
                self.nextToken()
                if self.checkToken(TokenType.STRING) or self.checkToken(TokenType.VAR_NAME):
                    self.nextToken()
                    if self.checkToken(TokenType.GREATER):
                        
                        print("correct print")
                        self.nextToken()
        
        elif self.checkToken(TokenType.IF):
            print("IF STATEMENT")

            self.nextToken()
            self.nextToken()
            self.comparison() 

            self.match(TokenType.BRACKET_OPEN)
            self.newLine()

            while not self.checkToken(TokenType.BRACKET_CLOSE):
                self.statement()

            self.match(TokenType.BRACKET_CLOSE)


        self.newLine()
                        
    
    def newLine(self):
        #print("NEW LINE")

        self.match(TokenType.NEWLINE)
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()


    def program(self):
        print("PRGRAM")

        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()

        while not self.checkToken(TokenType.EOF):
            self.statement()
            

    def isComparisonOperator(self):
            return self.checkToken(TokenType.GREATER) or self.checkToken(TokenType.GREATEREQUAL) or self.checkToken(TokenType.LESS) or self.checkToken(TokenType.LESSEQUAL) or self.checkToken(TokenType.EQEQ) or self.checkToken(TokenType.NOTEQ)

    def expression(self):
        print("EXPRESSION")

        self.term()
        while self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
            self.nextToken()
            self.term()

    def term(self):
        print("TERM")

        self.unary()
        while self.checkToken(TokenType.MULTIPLY) or self.checkToken(TokenType.DIVISION):
            self.nextToken()
            self.unary()

    def unary(self):
        print("UNARY")

        if self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
            self.nextToken()        
        self.primary()


    def primary(self):
        print(f"PRIMARY ({self.curToken.text})")

        if self.checkToken(TokenType.INT): 
            self.nextToken()
        elif self.checkToken(TokenType.FLOAT):
            self.nextToken()
        else:

            self.error(f"Unexpected token at {self.curToken.text}")



    def comparison(self):
        print("COMPARISON")
        self.expression()

        if self.isComparisonOperator():
            self.nextToken()
            self.expression()
        else:
            self.error(f"Expected comparison operator at: {self.curToken.text}")

        while self.isComparisonOperator():
            self.nextToken()
            self.expression()
    
    


