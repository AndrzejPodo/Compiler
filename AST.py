class Node(object):
    pass

class InstructionsOp(Node):
    def __init__(self, instructions=None):
        self.instructions = instructions

class Instructions(Node):
    def __init__(self, instruction):
        self.instructions = [instruction]

    def add(self, instruction):
        self.instructions.append(instruction)

class Ints(Node):
    def __init__(self, element, ints = None):
        self.ints = ints
        self.element = element

class Array(Node):
    def __init__(self, sequence=[]):
        self.sequence = sequence

class Num(Node):
    def __init__(self, value):
        self.value = float(value)

class Variable(Node):
    def __init__(self, name):
        self.name = name

class Transpose(Node):
    def __init__(self, expression):
        self.expression = expression

class Uminus(Node):
    def __init__(self, expression):
        self.expression = expression

class BinOp(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class ArrayValues(Node):
    def __init__(self, ints):
        self.ints = ints

class ArrayOp(Node):
    def __init__(self, operation, argument):
        self.operation = operation
        self.argument = argument

class Block(Node):
    def __init__(self, instructions):
        self.instructions = instructions

class If(Node):
    def __init__(self, condition, instruction, else_instuction=None):
        self.condition = condition
        self.instruction = instruction
        self.else_instuction = else_instuction

class Assign(Node):
    def __init__(self, op, variable, expression):
        self.op = op
        self.variable = variable
        self.expression = expression

class ArrayAssign(Node):
    def __init__(self, op, variable, array_indexes, expression):
        self.op = op
        self.variable = variable
        self.array_indexes = array_indexes
        self.expression = expression

class Sequence(Node):
    def __init__(self, element, sequence = None):
        self.sequence = sequence
        self.element = element

class Print(Node):
    def __init__(self, arguments):
        self.arguments = arguments

class While(Node):
    def __init__(self, condition, instruction):
        self.condition = condition
        self.instruction = instruction

class Range(Node):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class For(Node):
    def __init__(self, variable, range, instruction):
        self.id = variable
        self.range = range
        self.instruction = instruction

class Break(Node):
    def __init__(self):
        pass

class Continue(Node):
    def __init__(self):
        pass

class Return(Node):
    def __init__(self, arguments=None):
        self.arguments = arguments

class Error(Node):
    def __init__(self):
        pass