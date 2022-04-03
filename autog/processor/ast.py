from random import randint
from importlib import import_module

class Ast():

    def __init__(self, spelling=None):
        self.spelling = spelling

    def get(self):
        return None

class StringLiteral(Ast):
    
    def get(self):
        return self.spelling

class IntegerLiteral(Ast):
    
    def get(self):
        return int(self.spelling)

class FloatLiteral(Ast):
    
    def get(self):
        return float(self.spelling)

class InExpression(Ast):
    
    def __init__(self, comma_separated_expressions):
        super().__init__()
        self.expressions = comma_separated_expressions

    def get(self):
        vals = []
        for expr in self.expressions:
            vals.append(expr.get())

        return vals[randint(0, len(vals) - 1)]

class RangeExpression(Ast):
    
    def __init__(self, start, end):
        super().__init__()
        self.start = start
        self.end = end

    def get(self):
        return randint(self.start.get(), self.end.get())

class ListExpression(Ast):
    
    def __init__(self, lower, upper, expr):
        super().__init__()
        self.lower = lower
        self.upper = upper
        self.expr = expr

    def get(self):
        size = randint(self.lower.get(), self.upper.get())
        val = [0] * size
        for i in range(size):
            val[i] = self.expr.get()

        return val

class VarargExpression(ListExpression):
    pass

class DictExpression(Ast):
    
    def __init__(self, elems):
        super().__init__()
        self.elems = elems

    def get(self):
        d = {}
        for elem in self.elems:
            d[elem[0].get()] = elem[1].get()
        
        return d

class SetExpression(Ast):
    
    def __init__(self, vals):
        super().__init__()
        self.vals = vals

    def get(self):
        d = set()
        for val in self.vals:
            d.add(val.get())
        
        return d

class ObjectExpression(Ast):
    
    def __init__(self, classpath, params):
        super().__init__()
        self.classpath = classpath
        self.params = params

    def get(self):
        path_parts = self.classpath.get().split('.')
        path = '.'.join(path_parts[0:len(path_parts) - 1])
        class_name = path_parts[-1]

        mod = __name__
        if path:
            mod = import_module(path)

        klass = getattr(mod, class_name)
        
        params = []
        for p in self.params:
            params.append(p.get())

        return klass(*params)
