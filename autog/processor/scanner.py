from .token import *

EOT = '\0'

class Scanner():
    
    def __init__(self, data):
        if type(data) != str:
            data = str(data)

        self.data = data
        self.index = 0
        self.ch = data[self.index]

    def consume(self, ch=None):
        if not ch or ch == self.ch:
            self.index += 1
        elif ch != self.ch:
            raise RuntimeError('unexpected char received')

        if self.index < len(self.data):
            self.ch = self.data[self.index]
        else:
            self.ch = EOT

    def next(self):
        if self.index == len(self.data):
            return EOT
        return self.data[self.index + 1]
    
    
    def prev(self):
        return self.data[self.index - 1]

    @staticmethod
    def iswhitespace(ch):
        return ch in [' ', '\n', '\r', '\t']
    
    @staticmethod
    def isletter(ch):
        return (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')
    
    @staticmethod
    def isdigit(ch):
        return ch >= '0' and ch <= '9'
    
    def scan_whitespace(self):
        while Scanner.iswhitespace(self.ch):
            self.consume()
    
    def scan(self):
        if Scanner.iswhitespace(self.ch):
            self.scan_whitespace()
        
        token_type = None
        spelling = []

        if Scanner.isletter(self.ch):
            while Scanner.isletter(self.ch):
                spelling.append(self.ch)
                self.consume()
            token_type = Type.IDENTIFIER
        elif Scanner.isdigit(self.ch) or self.ch == '+' or self.ch == '-':
            dot_seen = False
            sign_seen = False

            if (self.ch == '+' or self.ch == '-'):
                if sign_seen:
                    raise RuntimeError('Only one sign character is allowed')
                    
                sign_seen = True
                # sign is in incorrect position
                if len(spelling) > 0:
                    raise RuntimeError('Sign can only appear at the head of a number')
                spelling.append(self.ch)
                self.consume()

            while Scanner.isdigit(self.ch) or self.ch == '.':
                if self.ch == '.':
                    if dot_seen:
                        raise RuntimeError('syntax error, two dots (.) was seen')
                    dot_seen == True
                    self.consume()
                    continue
    
                spelling.append(self.ch)
                self.consume()
            token_type = Type.INTEGER
            if dot_seen:
                token_type = Type.FLOAT
        elif self.ch == '\'':
            self.consume()
            while True:
                if self.ch == '\'' and self.prev() != '\\':
                    self.consume()
                    break
                spelling.append(self.ch)
                self.consume()
            token_type = Type.STRING
        elif self.ch == ',':
            self.consume()
            spelling.append(',')
            token_type = Type.COMMA
        elif self.ch == ':':
            self.consume()
            spelling.append(':')
            token_type = Type.COLON
        elif self.ch == ';':
            self.consume()
            spelling.append(';')
            token_type = Type.SEMICOLON
        elif self.ch == '(':
            self.consume()
            spelling.append('(')
            token_type = Type.LPARAN
        elif self.ch == ')':
            self.consume()
            spelling.append(')')
            token_type = Type.RPARAN
        elif self.ch == '{':
            self.consume()
            spelling.append('{')
            token_type = Type.LCURLY
        elif self.ch == '}':
            self.consume()
            spelling.append('}')
            token_type = Type.RCURLY
        elif self.ch == '[':
            self.consume()
            spelling.append('[')
            token_type = Type.LSQUARE
        elif self.ch == ']':
            self.consume()
            spelling.append(']')
            token_type = Type.RSQUARE
        elif self.ch == '=':
            self.consume()
            spelling.append('=')
            token_type = Type.EQUAL
        elif self.ch == EOT:
            self.consume()
            token_type = Type.EOT

        token = Token(token_type, ''.join(spelling))
        return token
