from tree import Tree

class SyntaxItem(Tree):

    def get_location(self):
        try:
            return self.location
        except AttributeError:
            return 'unknown'

class Program(SyntaxItem):
    def __init__(self, declarations):
        self.declarations = declarations
    
    def get_parts(self):
        return self.declarations

class VariableDecl(SyntaxItem):
    def __init__(self, type, name):
        self.type, self.name = type, name
    
    def get_parts(self):
        return self.type, self.name

class FunctionDecl(SyntaxItem):
    def __init__(self, type, name, args, body):
        self.type, self.name, self.args, self.body = type, name, args, body
    
    def get_parts(self):
        return self.type, self.name, self.args, self.body

class Builtin(SyntaxItem):
    def __init__(self, type, name, args):
        self.type, self.name, self.args = type, name, args
    
    def get_parts(self):
        return self.type, self.name, self.args

class ArgDecl(SyntaxItem):
    def __init__(self, type, name):
        self.type, self.name = type, name
    
    def get_parts(self):
        return self.type, self.name

class Block(SyntaxItem):
    def __init__(self, statements):
        self.statements = statements
    
    def get_parts(self):
        return self.statements

class Statement(SyntaxItem):
    def __init__(self, expression):
        self.expression = expression
    
    def get_parts(self):
        return [self.expression]

class IfStatement(SyntaxItem):
    def __init__(self, expression, block):
        self.expression = expression
        self.block = block
    
    def get_parts(self):
        return [self.expression, self.block]

class WhileStatement(SyntaxItem):
    def __init__(self, expression, block):
        self.expression = expression
        self.block = block
    
    def get_parts(self):
        return [self.expression, self.block]

class ReturnStatement(SyntaxItem):
    def __init__(self, expression):
        self.expression = expression
    
    def get_parts(self):
        return [self.expression]

class Expression(SyntaxItem):
    pass

class BinaryOperation(Expression):
    def __init__(self, parts):
        self.parts = parts
    
    def get_parts(self):
        return self.parts

class FunctionCall(Expression):
    def __init__(self, name, args):
        self.name, self.args = name, args
    
    def get_parts(self):
        return self.name, self.args

class Name(Expression):
    def __init__(self, name):
        if isinstance(name, VariableDecl):
            self.declaration = name
            name = name.name
        self.name = name
    
    def get_parts(self):
        return [self.name]

class Numeral(Expression):
    def __init__(self, value):
        self.value = int(value)
    
    def get_parts(self):
        return [self.value]

class Type(SyntaxItem):
    def __init__(self, name):
        self.name = name
    
    def get_parts(self):
        return (self.name,)

void_type = Type('void')
int_type = Type('int')
bool_type = Type('bool')

known_types = { 'void': void_type, 'int': int_type, 'bool': bool_type }

out_builtin = Builtin(void_type, '__out__', [ArgDecl(int_type, 'value'), ArgDecl(int_type, 'port')])

known_builtins = {
    '__out__': out_builtin
}
