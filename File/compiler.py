from enum import Enum, auto

class TokenType(Enum):
    IDENTIFIER = auto()
    KEYWORD = auto()
    SYMBOL = auto()
    NUMBER = auto()
    STRING = auto()
    OPERATOR = auto()
    EOF = auto()

class Token:
    def __init__(self, type: TokenType, value: str, line: int, column: int):
        self.type = type
        self.value = value
        self.line = line
        self.column = column

class Lexer:
    def __init__(self, source_code: str):
        self.source_code = source_code
        self.tokens = []
        self.current_char = ''
        self.pos = -1
        self.line = 1
        self.column = 0
        self.advance()

    def advance(self):
        self.pos += 1
        self.column += 1
        if self.pos < len(self.source_code):
            self.current_char = self.source_code[self.pos]
        else:
            self.current_char = None

    def tokenize(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.handle_whitespace()
            elif self.current_char.isalpha() or self.current_char == '_':
                self.tokens.append(self.make_identifier_or_keyword())
            elif self.current_char.isdigit():
                self.tokens.append(self.make_number())
            elif self.current_char == '"':
                self.tokens.append(self.make_string())
            elif self.current_char in '+-*/=<>!.':
                self.tokens.append(self.make_operator_or_symbol())
            elif self.current_char in '(){}[],;':
                self.tokens.append(Token(TokenType.SYMBOL, self.current_char, self.line, self.column))
                self.advance()
            else:
                raise Exception(f'Unexpected character {self.current_char} at line {self.line}, column {self.column}')
        self.tokens.append(Token(TokenType.EOF, '', self.line, self.column))
        return self.tokens

    def handle_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            if self.current_char == '\n':
                self.line += 1
                self.column = 0
            self.advance()

    def make_identifier_or_keyword(self):
        start_pos = self.pos
        start_col = self.column
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            self.advance()
        value = self.source_code[start_pos:self.pos]
        token_type = TokenType.KEYWORD if value in {'function', 'class', 'enum', 'interface', 'if', 'else', 'for', 'while', 'return'} else TokenType.IDENTIFIER
        return Token(token_type, value, self.line, start_col)

    def make_number(self):
        start_pos = self.pos
        start_col = self.column
        while self.current_char is not None and self.current_char.isdigit():
            self.advance()
        value = self.source_code[start_pos:self.pos]
        return Token(TokenType.NUMBER, value, self.line, start_col)

    def make_string(self):
        start_pos = self.pos
        start_col = self.column
        self.advance()
        while self.current_char is not None and self.current_char != '"':
            self.advance()
        if self.current_char is None:
            raise Exception(f'Unterminated string at line {self.line}, column {start_col}')
        self.advance()
        value = self.source_code[start_pos+1:self.pos-1]
        return Token(TokenType.STRING, value, self.line, start_col)

    def make_operator_or_symbol(self):
        start_pos = self.pos
        start_col = self.column
        op = self.current_char
        self.advance()
        if self.current_char in {'=', '>'}:
            op += self.current_char
            self.advance()
        return Token(TokenType.OPERATOR if op in '+-*/=<>!' else TokenType.SYMBOL, op, self.line, start_col)
class Node:
    pass

class Program(Node):
    def __init__(self, body):
        self.body = body

class FunctionDeclaration(Node):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

class FunctionCall(Node):
    def __init__(self, name, args):
        self.name = name
        self.args = args

class ClassDeclaration(Node):
    def __init__(self, name, body):
        self.name = name
        self.body = body

class InterfaceDeclaration(Node):
    def __init__(self, name, body):
        self.name = name
        self.body = body

class EnumDeclaration(Node):
    def __init__(self, name, members):
        self.name = name
        self.members = members

class Block(Node):
    def __init__(self, statements):
        self.statements = statements

class VariableDeclaration(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Assignment(Node):
    def __init__(self, target, value):
        self.target = target
        self.value = value

class IfStatement(Node):
    def __init__(self, condition, body, else_body):
        self.condition = condition
        self.body = body
        self.else_body = else_body

class WhileLoop(Node):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class ForLoop(Node):
    def __init__(self, init, condition, increment, body):
        self.init = init
        self.condition = condition
        self.increment = increment
        self.body = body

class ReturnStatement(Node):
    def __init__(self, value):
        self.value = value

class Expression(Node):
    pass

class BinaryOperation(Expression):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

class Literal(Expression):
    def __init__(self, value):
        self.value = value

class Identifier(Expression):
    def __init__(self, name):
        self.name = name

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos]

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]

    def parse(self):
        statements = []
        while self.current_token.type != TokenType.EOF:
            if self.current_token.type == TokenType.KEYWORD:
                if self.current_token.value == 'function':
                    statements.append(self.parse_function_declaration())
                elif self.current_token.value == 'class':
                    statements.append(self.parse_class_declaration())
                elif self.current_token.value == 'interface':
                    statements.append(self.parse_interface_declaration())
                elif self.current_token.value == 'enum':
                    statements.append(self.parse_enum_declaration())
                else:
                    raise Exception(f'Unexpected keyword {self.current_token.value}')
            else:
                statements.append(self.parse_statement())
        return Program(statements)

    def parse_function_declaration(self):
        self.advance()  # 'function'
        name = self.current_token.value
        self.advance()  # function name
        self.advance()  # '('
        params = self.parse_parameters()
        self.advance()  # ')'
        body = self.parse_block()
        return FunctionDeclaration(name, params, body)

    def parse_class_declaration(self):
        self.advance()  # 'class'
        name = self.current_token.value
        self.advance()  # class name
        body = self.parse_block()
        return ClassDeclaration(name, body)

    def parse_interface_declaration(self):
        self.advance()  # 'interface'
        name = self.current_token.value
        self.advance()  # interface name
        body = self.parse_block()
        return InterfaceDeclaration(name, body)

    def parse_enum_declaration(self):
        self.advance()  # 'enum'
        name = self.current_token.value
        self.advance()  # enum name
        self.advance()  # '{'
        members = []
        while self.current_token.type != TokenType.SYMBOL or self.current_token.value != '}':
            members.append(self.current_token.value)
            self.advance()
            if self.current_token.type == TokenType.SYMBOL and self.current_token.value == ',':
                self.advance()
        self.advance()  # '}'
        return EnumDeclaration(name, members)

    def parse_parameters(self):
        params = []
        while self.current_token.type != TokenType.SYMBOL or self.current_token.value != ')':
            params.append(self.current_token.value)
            self.advance()
            if self.current_token.type == TokenType.SYMBOL and self.current_token.value == ',':
                self.advance()
        return params

    def parse_block(self):
        self.advance()  # '{'
        statements = []
        while self.current_token.type != TokenType.SYMBOL or self.current_token.value != '}':
            if self.current_token.type == TokenType.SYMBOL and self.current_token.value == ';':
                self.advance()
                continue
            statements.append(self.parse_statement())
        self.advance()  # '}'
        return Block(statements)

    def parse_statement(self):
        if self.current_token.type == TokenType.IDENTIFIER:
            identifier = self.current_token.value
            self.advance()
            if self.current_token.type == TokenType.SYMBOL and self.current_token.value == '=':
                self.advance()  # '='
                value = self.parse_expression()
                if self.current_token.type == TokenType.SYMBOL and self.current_token.value == ';':
                    self.advance()  # ';'
                return Assignment(identifier, value)
            elif self.current_token.type == TokenType.SYMBOL and self.current_token.value == '(':
                self.advance()  # '('
                args = self.parse_arguments()
                self.advance()  # ')'
                if self.current_token.type == TokenType.SYMBOL and self.current_token.value == ';':
                    self.advance()  # ';'
                return FunctionCall(identifier, args)
        elif self.current_token.type == TokenType.KEYWORD:
            if self.current_token.value == 'if':
                return self.parse_if_statement()
            elif self.current_token.value == 'while':
                return self.parse_while_loop()
            elif self.current_token.value == 'for':
                return self.parse_for_loop()
            elif self.current_token.value == 'return':
                return self.parse_return_statement()
        raise Exception(f'Unexpected statement {self.current_token.value}')

    def parse_if_statement(self):
        self.advance()  # 'if'
        condition = self.parse_expression()
        body = self.parse_block()
        else_body = None
        if self.current_token.type == TokenType.KEYWORD and self.current_token.value == 'else':
            self.advance()  # 'else'
            else_body = self.parse_block()
        return IfStatement(condition, body, else_body)

    def parse_while_loop(self):
        self.advance()  # 'while'
        condition = self.parse_expression()
        body = self.parse_block()
        return WhileLoop(condition, body)

    def parse_for_loop(self):
        self.advance()  # 'for'
        init = self.parse_statement()
        condition = self.parse_expression()
        self.advance()  # ';'
        increment = self.parse_statement()
        body = self.parse_block()
        return ForLoop(init, condition, increment, body)

    def parse_return_statement(self):
        self.advance()  # 'return'
        value = self.parse_expression()
        if self.current_token.type == TokenType.SYMBOL and self.current_token.value == ';':
            self.advance()  # ';'
        return ReturnStatement(value)

    def parse_expression(self):
        left = self.parse_term()
        while self.current_token.type == TokenType.OPERATOR and self.current_token.value in {'+', '-'}:
            operator = self.current_token.value
            self.advance()
            right = self.parse_term()
            left = BinaryOperation(left, operator, right)
        return left

    def parse_term(self):
        left = self.parse_factor()
        while self.current_token.type == TokenType.OPERATOR and self.current_token.value in {'*', '/'}:
            operator = self.current_token.value
            self.advance()
            right = self.parse_factor()
            left = BinaryOperation(left, operator, right)
        return left

    def parse_factor(self):
        if self.current_token.type == TokenType.NUMBER:
            value = self.current_token.value
            self.advance()
            return Literal(value)
        elif self.current_token.type == TokenType.IDENTIFIER:
            name = self.current_token.value
            self.advance()
            return Identifier(name)
        elif self.current_token.type == TokenType.SYMBOL and self.current_token.value == '(':
            self.advance()
            expr = self.parse_expression()
            self.advance()  # ')'
            return expr
        raise Exception(f'Unexpected factor {self.current_token.value}')
    
    def parse_arguments(self):
        args = []
        while self.current_token.type != TokenType.SYMBOL or self.current_token.value != ')':
            args.append(self.parse_expression())
            if self.current_token.type == TokenType.SYMBOL and self.current_token.value == ',':
                self.advance()
        return args


class CodeGenerator:
    def __init__(self):
        self.output = []

    def generate(self, node):
        if isinstance(node, Program):
            for statement in node.body:
                self.generate(statement)
        elif isinstance(node, FunctionDeclaration):
            self.output.append(f'def {node.name}({", ".join(node.params)}):')
            self.generate(node.body)
        elif isinstance(node, ClassDeclaration):
            self.output.append(f'class {node.name}:')
            self.generate(node.body)
        elif isinstance(node, InterfaceDeclaration):
            # Interfaces werden in Python nicht direkt unterstützt, könnten aber durch Kommentare dargestellt werden
            self.output.append(f'# Interface {node.name}')
            self.generate(node.body)
        elif isinstance(node, EnumDeclaration):
            self.output.append(f'class {node.name}(Enum):')
            for member in node.members:
                self.output.append(f'    {member} = auto()')
        elif isinstance(node, Block):
            for statement in node.body:
                self.output.append('    ' + self.generate_statement(statement))
        elif isinstance(node, Assignment):
            self.output.append(f'{node.target} = {self.generate_expression(node.value)}')
        elif isinstance(node, IfStatement):
            self.output.append(f'if {self.generate_expression(node.condition)}:')
            self.generate(node.body)
            if node.else_body:
                self.output.append('else:')
                self.generate(node.else_body)
        elif isinstance(node, WhileLoop):
            self.output.append(f'while {self.generate_expression(node.condition)}:')
            self.generate(node.body)
        elif isinstance(node, ForLoop):
            self.output.append(f'for {node.init.target} in range({self.generate_expression(node.init.value)}, {self.generate_expression(node.condition)}, {self.generate_expression(node.increment.value)}):')
            self.generate(node.body)
        elif isinstance(node, ReturnStatement):
            self.output.append(f'return {self.generate_expression(node.value)}')
        elif isinstance(node, FunctionCall):
            args = ", ".join([self.generate_expression(arg) for arg in node.args])
            self.output.append(f'{node.name}({args})')

    def generate_statement(self, statement):
        if isinstance(statement, Assignment):
            return f'{statement.target} = {self.generate_expression(statement.value)}'
        elif isinstance(statement, IfStatement):
            return f'if {self.generate_expression(statement.condition)}:\n    {self.generate_block(statement.body)}'
        elif isinstance(statement, WhileLoop):
            return f'while {self.generate_expression(statement.condition)}:\n    {self.generate_block(statement.body)}'
        elif isinstance(statement, ForLoop):
            return f'for {statement.init.target} in range({self.generate_expression(statement.init.value)}, {self.generate_expression(statement.condition)}, {self.generate_expression(statement.increment.value)}):\n    {self.generate_block(statement.body)}'
        elif isinstance(statement, ReturnStatement):
            return f'return {self.generate_expression(statement.value)}'
        elif isinstance(statement, FunctionCall):
            args = ", ".join([self.generate_expression(arg) for arg in statement.args])
            return f'{statement.name}({args})'
        raise Exception(f'Unexpected statement {statement}')

    def generate_expression(self, expression):
        if isinstance(expression, BinaryOperation):
            return f'{self.generate_expression(expression.left)} {expression.operator} {self.generate_expression(expression.right)}'
        elif isinstance(expression, Literal):
            return expression.value
        elif isinstance(expression, Identifier):
            return expression.name
        raise Exception(f'Unexpected expression {expression}')

def main():
    source_code = """
    function add(x, y) {
        return x + y;
    }

    class Point {
        function __init__(self, x, y) {
            this.x = x;
            this.y = y;
        }
    }

    enum Color {
        RED, GREEN, BLUE
    }
    """
    
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    codegen = CodeGenerator()
    codegen.generate(ast)
    
    generated_code = '\n'.join(codegen.output)
    print(generated_code)  # Ausgabe des generierten Python-Codes
    
    exec(generated_code)

if __name__ == '__main__':
    main()
