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

    # @addToClass(AST.Node)
    # def printTree(self, indent=0):
    #     self.printTree()

    @addToClass(AST.If)
    def printTree(self, indent=0):
        print(generateIndent(indent) + "If")
        if isinstance(self.condition, str):
            print(generateIndent(indent+1) + self.condition)
        else:   
            self.condition.printTree(indent + 1)
        if isinstance(self.instruction, list):
            for inst in self.instruction:
                inst.printTree(indent+1)
        else:   
            self.instruction.printTree(indent + 1)

        if(self.else_instruction):
            self.else_instruction.printTree(indent+1)

    @addToClass(AST.Block)
    def printTree(self, indent=0):
        self.instructions.printTree(indent)

    @addToClass(AST.While)
    def printTree(self, indent=0):
        print(generateIndent(indent) + "WHILE")
        self.condition.printTree(indent+1)
        self.instruction.printTree(indent+1)

    @addToClass(AST.For)
    def printTree(self, indent=0):
        print(generateIndent(indent) + "FOR")
        self.id.printTree(indent+1)
        self.range.printTree(indent+1)
        self.instruction.printTree(indent+1)

    @addToClass(AST.Range)
    def printTree(self, indent=0):
        print(generateIndent(indent) + "RANGE")
        if isinstance(self.start, str):
            print(generateIndent(indent+1) + self.start)
        else:   
            self.start.printTree(indent + 1)
        if isinstance(self.end, str):
            print(generateIndent(indent+1) + self.end)
        else:   
            self.end.printTree(indent + 1)
    
    @addToClass(AST.Break)
    def printTree(self, indent=0):
        print(generateIndent(indent) + "BREAK")

    @addToClass(AST.Continue)
    def printTree(self, indent=0):
        print(generateIndent(indent) + "CONTINUE")

    @addToClass(AST.Return)
    def printTree(self, indent=0):
        print(generateIndent(indent) + "RETURN")

    @addToClass(AST.Print)
    def printTree(self, indent=0):
        print(generateIndent(indent) + "PRINT")
        self.arguments.printTree(indent+1)

    @addToClass(AST.BinOp)
    def printTree(self, indent=0):
        print(generateIndent(indent) + self.op)
        if isinstance(self.left, str):
            print(generateIndent(indent+1) + self.left)
        else:   
            self.left.printTree(indent + 1)
        
        if isinstance(self.right, str):
            print(generateIndent(indent+1) + self.right)
        else:   
            self.right.printTree(indent + 1)

    @addToClass(AST.Uminus)
    def printTree(self, indent=0):
        print(generateIndent(indent) + "UMINUS")
        if isinstance(self.expression, str):
            print(generateIndent(indent+1) + self.expression)
        else:   
            self.expression.printTree(indent + 1)

    @addToClass(AST.Transpose)
    def printTree(self, indent = 0):
        print(generateIndent(indent)+"Transpose")
        if isinstance(self.expression, str):
            print(generateIndent(indent+1) + self.expression)
        else:   
            self.expression.printTree(indent + 1)

    @addToClass(AST.InstructionsOp)
    def printTree(self, indent=0):
        # for instruction in self.instructions:
        self.instructions.printTree(indent)

    @addToClass(AST.Instructions)
    def printTree(self, indent=0):
        for instruction in self.instructions:
            instruction.printTree(indent)

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
        if(isinstance(self.element, str)):
            print(generateIndent(indent+1) + self.element)   
        else: 
            self.element.printTree(indent=indent + 1)
        if self.sequence:
            self.sequence.printTree(indent=indent + 1)
        else:
            print(generateIndent(indent+1) + "EmptySeq")

    @addToClass(AST.Ints)
    def printTree(self, indent=0):
        print(generateIndent(indent) + "Ints")

        self.element.printTree(indent=indent + 1)
        if self.ints:
            self.ints.printTree(indent=indent + 1)
        else:
            print(generateIndent(indent+1) + "EmptyInts")

    @addToClass(AST.Assign)
    def printTree(self, indent=0):
        print(generateIndent(indent) + self.op)
        self.variable.printTree(indent=indent + 1)
        if isinstance(self.expression, str):
            print(generateIndent(indent+1) + self.expression)
        else:   
            self.expression.printTree(indent + 1)

    @addToClass(AST.ArrayAssign)
    def printTree(self, indent=0):
        print(generateIndent(indent) + self.op)
        self.array_values.printTree()
        self.expression.printTree(  )

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
