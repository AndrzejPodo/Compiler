from __future__ import print_function
import AST


def addToClass(cls):

    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator


def generateIndent(i):
    if i > 0:
        return "  ".join(['|' for _i in range(i)]) + "  "
    else:
        return ""


class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self, indent=0):
        self.printTree()

    @addToClass(AST.InstructionsOp)
    def printTree(self, indent=0):
        self.instructions.printTree()

    @addToClass(AST.Instructions)
    def printTree(self, indent=0):
        for instruction in self.instructions:
            instruction.printTree()

    @addToClass(AST.Num)
    def printTree(self, indent=0):
        print(generateIndent(indent) + str(self.value))

    @addToClass(AST.Variable)
    def printTree(self, indent=0):
        print(generateIndent(indent) + self.name)

    @addToClass(AST.Array)
    def printTree(self, indent=0):
        print(generateIndent(indent) + "Arr")
        self.sequence.printTree(indent=indent+1)

    @addToClass(AST.Sequence)
    def printTree(self, indent=0):
        print(generateIndent(indent) + "Seq")
        self.element.printTree(indent=indent + 1)
        if self.sequence:
            self.sequence.printTree(indent=indent + 1)
        else:
            print(generateIndent(indent+1) + "EmptySeq")

    @addToClass(AST.Ints)
    def printTree(self, indent=0):
        print(generateIndent(indent) + "Ints")
        self.element.printTree(indent=indent + 1)
        if self.sequence:
            self.sequence.printTree(indent=indent + 1)
        else:
            print(generateIndent(indent+1) + "EmptyInts")

    @addToClass(AST.Assign)
    def printTree(self, indent=0):
        print(generateIndent(indent) + self.op)
        self.variable.printTree(indent=indent + 1)
        self.expression.printTree(indent=indent + 1)

    @addToClass(AST.ArrayAssign)
    def printTree(self, indent=0):
        print()

    @addToClass(AST.ArrayOp)
    def printTree(self, indent=0):
        print(generateIndent(indent) + self.operation)
        self.argument.printTree()

    @addToClass(AST.ArrayValues)
    def printTree(self, indent=0):
        print(generateIndent(indent) + "ArrVal")
        self.ints.printTree()

    @addToClass(AST.Error)
    def printTree(self, indent=0):
        pass
        # fill in the body

    # define printTree for other classes
    # ...
