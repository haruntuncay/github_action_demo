import importlib
import pyflakes.api as pa
import pyflakes.reporter
import enum

DEBUG = False

class Error(enum.Enum):
    INDENT_EXPECTED = 'expected an indented block'
    UNEXPECTED_INDENT = 'unexpected indent'
    INVALID_SYNTAX = 'invalid syntax'
    NAME_ERROR = 'undefined name'
    CANT_ASSIGN = 'cannot assign to literal'
    INDENT_NOT_MATCH = 'unindent does not match any outer indentation level'

class MReporter(pyflakes.reporter.Reporter):

    def __init__(self):
        super().__init__(self, self)
        self.output = []

    def write(self, txt):
        self.output.append(txt)

def get_error_type(msg):
    if len(msg) == 0:
        return Error.INVALID_SYNTAX
    
    for err in list(Error):
        if msg.lower().find(err.value) > -1:
            return err

    return Error.INVALID_SYNTAX

def def_statement(lines, lineno, index):
    if index < 0 or index == len(lines):
        return True

    first_word = lines[index].split(' ')[0]

    if index - 1 >= 0 and lines[index-1].split(' ')[0] in ['from', 'import']:
        return True
    
    return first_word == 'def'

def delete_above(lines, lineno, stop_condition=def_statement):
    start = lineno - 1
    end = start

    while not stop_condition(lines, lineno, end):
        end -= 1

    while start >= 0 and end <= start:
        lines.pop(start)
        start -= 1

def delete_below(lines, lineno, stop_condition=def_statement):
    start = lineno
    end = start
    while not stop_condition(lines, lineno, end):
        end += 1

    while end > start:
        lines.pop(start)
        end -= 1

def get_source(input):
    while True:
        try:
            modname = input.split('.')[0]
            return importlib.import_module(modname)
        except Exception as e:
            if DEBUG:
                print('Error Type is', type(e), '\n')

            lines = None
            with open(input, 'r') as file:
                lines = file.readlines()

            if len(lines) == 0:
                if DEBUG:
                    print('NO LINES WERE LEFT')
                break

            reporter = MReporter()
            pa.checkPath(input, reporter)
            if DEBUG:
                print(reporter.output)

            parts = reporter.output[0].split(':')
            lineno = int(parts[1])
            msg = parts[-1]

            if DEBUG:
                print('error in line ', lineno, msg)

            if get_error_type(msg) == Error.INDENT_EXPECTED:
                # above function has empty body
                if lines[lineno-1].startswith('def'):
                    delete_above(lines, lineno-1)
                else:
                    delete_below(lines, lineno)
                    delete_above(lines, lineno)
            else:
                delete_below(lines, lineno)
                delete_above(lines, lineno)

            modified_input = 'modified_input.py'
            with open(modified_input, 'w') as file:
                file.writelines(lines)
            
            input = modified_input
