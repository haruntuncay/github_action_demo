from .scanner import Scanner
from .token import *
from .ast import *

class Parser():

    def __init__(self, data):
        self.scanner = Scanner(data)
        self.token = self.scanner.scan()

    def consume(self, token_type=None):
        if token_type == None or self.token.type == token_type:
            self.token = self.scanner.scan()
        elif self.token.type != token_type:
            raise RuntimeError('token doesnt match')

    def parseInteger(self):
        token = self.token
        self.consume(Type.INTEGER)
        return IntegerLiteral(token.spelling)

    def parseString(self):
        token = self.token
        self.consume(Type.STRING)
        return StringLiteral(token.spelling)

    def parse(self):
        t = self.token.type

        if t == Type.EOT:
            return

        if t == Type.STRING:
            return self.parseString()
        elif t == Type.INTEGER:
            return self.parseInteger()
        elif t == Type.FLOAT:
            ast = FloatLiteral(self.token.spelling)
            self.consume()
            return ast
        elif t == Type.IN:
            self.consume()
            self.consume(Type.LPARAN)
            expressions = [self.parse()]
            while self.token.type == Type.COMMA:
                self.consume()
                expressions.append(self.parse())
            self.consume(Type.RPARAN)
            return InExpression(expressions)
        elif t == Type.RANGE:
            self.consume()
            self.consume(Type.LPARAN)
            start = self.parseInteger()
            self.consume(Type.COMMA)
            end = self.parseInteger()
            self.consume(Type.RPARAN)
            return RangeExpression(start, end)
        elif t == Type.VARARG or t == Type.LIST:
            self.consume()
            self.consume(Type.LPARAN)
            lower = self.parseInteger()
            self.consume(Type.SEMICOLON)
            upper = self.parseInteger()
            self.consume(Type.SEMICOLON)
            expr = self.parse()
            self.consume(Type.RPARAN)    

            if t == Type.VARARG:        
                return VarargExpression(lower, upper, expr)
            return ListExpression(lower, upper, expr)
        elif t == Type.DICT:
            self.consume()
            self.consume(Type.LPARAN)
            key = self.parseString()
            self.consume(Type.EQUAL)
            val = self.parse()

            elems = [(key, val)]
            while self.token.type == Type.COMMA:
                self.consume()
                key = self.parseString()
                self.consume(Type.EQUAL)
                val = self.parse()
                elems.append((key, val))
            
            self.consume(Type.RPARAN)

            return DictExpression(elems)
        elif t == Type.SET:
            self.consume()
            self.consume(Type.LPARAN)
            val = self.parse()
            vals = [val]
            while self.token.type == Type.COMMA:
                self.consume()
                vals.append(self.parse())
            self.consume(Type.RPARAN)
            return SetExpression(vals)
        elif t == Type.OBJECT:
            self.consume()
            self.consume(Type.LPARAN)
            classpath = self.parseString()
            if self.token.type == Type.COMMA:
                self.consume()
                self.consume(Type.LPARAN)
                params = [self.parse()]
                while self.token.type == Type.COMMA:
                    self.consume()
                    params.append(self.parse())
                self.consume(Type.RPARAN)
            self.consume(Type.RPARAN)
            return ObjectExpression(classpath, params)



