from enum import IntEnum, auto

class Type(IntEnum):
    IDENTIFIER = auto()
    # LITERALS
    INTEGER = auto()
    STRING = auto()
    FLOAT = auto()
    BOOLEAN = auto()
    # RESERVED WORDS
    IN = auto()
    RANGE = auto()
    LIST = auto()
    VARARG = auto()
    DICT = auto()
    SET = auto()
    OBJECT = auto()
    # PUNCTUATIONS
    LPARAN = auto()
    RPARAN = auto()
    LCURLY = auto()
    RCURLY = auto()
    LSQUARE = auto()
    RSQUARE = auto()
    COMMA = auto()
    COLON = auto()
    SEMICOLON = auto()
    EQUAL = auto()
    PLUS = auto()
    MINUS = auto()
    EOT = auto()
    ERROR = auto()

RESERVED_KEYWORD_START = Type.IN.value
RESERVED_KEYWORD_END = Type.OBJECT.value

token_spellings = ['#', 'id', 'integer', 'string', 'float', 'boolean',
                    'in', 'range', 'list', 'vararg', 'dict', 'set', 'object',
                    '(', ')', '{', '}', '[', ']', ',', ':', ';', '=', '+', '-', '\0', 'ERROR']
    

class Token():

    def __init__(self, type, spelling):
        self.type = type
        self.spelling = spelling

        # check for reserved words
        if type == Type.IDENTIFIER:
            reserved_spelling_found = False
            
            for i in range(RESERVED_KEYWORD_START, RESERVED_KEYWORD_END + 1):
                if self.spelling == token_spellings[i]:
                    self.type = Type(i)
                    reserved_spelling_found = True

            if not reserved_spelling_found:
                self.type = Type.STRING




       
       
