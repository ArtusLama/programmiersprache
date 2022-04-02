
import sys
from token import TokenType
from lexer import *
class Parser:

    def __init__(self, lexer, emitter):
        self.lexer = lexer
        self.emitter = emitter

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
        
        elif self.checkToken(TokenType.VAR_NAME):
            print("VARIABLE")

            self.nextToken()
            if self.checkToken(TokenType.EQ):
                print("SET VARIABLE")
                self.nextToken()


        self.newLine()
                        
    
    def newLine(self):
        #print("NEW LINE")

        self.match(TokenType.NEWLINE)
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()


    def program(self):
        print("PRGRAM")
        #self.emitter.headerLine("#include <stdio.h>")
        #self.emitter.headerLine("int main(void){")

        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()

        while not self.checkToken(TokenType.EOF):
            self.statement()

        #self.emitter.emitLine("return 0;")
        #self.emitter.emitLine("}")
            

    
    
    


