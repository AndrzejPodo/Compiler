import scanner
import ply.yacc as yacc
import lexer as scanner
import AST

tokens = scanner.tokens

precedence = (
   ("nonassoc", 'IF'),
   ("nonassoc", 'ELSE'),
   ("nonassoc", '<', '>', 'EQ', 'NOTEQ', 'GE', 'LE'),
   ("left", '+', '-'),
   ("left", 'DOTADD', 'DOTSUB'),
   ("left", '*', '/'),
   ("left", 'DOTMUL', 'DOTDIV'),
   ("left", 'TRANSPOSE'),
   ("right", 'UMINUS')
)

def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")

def p_program(p):
    """program : instructions_opt"""
    p[0] = p[1]

def p_instructions_opt_1(p):
    """instructions_opt : instructions """
    p[0] = AST.InstructionsOp(p[1])

def p_instructions_opt_2(p):
    """instructions_opt : """
    p[0] = AST.InstructionsOp()

def p_instructions_1(p):
    """instructions : instructions instruction """
    p[0] = p[1]
    p[0].add(p[2])

def p_instructions_2(p):
    """instructions : instruction """
    p[0] = AST.Instructions(p[1])

def p_instruction(p):
    """ instruction :  if
                    |  for
                    |  while
                    |  break
                    |  continue
                    |  print
                    |  block
                    |  return 
                    |  assign 
                    |  assign_array
                    """
    p[0] = p[1]

def p_num(p):
    """ num : INTNUM
            | FLOAT """
    p[0] = AST.Num(p[1])

def p_int_seq(p):
    """ ints : INTNUM
             | INTNUM ',' ints"""
    if(len(p) == 2):
        p[0] = AST.Ints(AST.Num(p[1]))
    else:
        p[0] = AST.Ints(AST.Num(p[1]), p[3])

# array is empty or contains any sequence (this is how it work in python)
def p_array(p):
    """ array : '[' ']'
              | '[' sequence ']' """
    if(len(p) == 3):
        p[0] = AST.Array()
    else:
        p[0] = AST.Array(p[2])

# array can have more than two dimensions so [int] and [int,int] wont be enough
def p_array_val(p):
    """ array_val : ID '[' ints ']' """
    p[0] = AST.ArrayValues(p[3])

def p_expression(p):
    """ expression : num
                   | ID
                   | STRING 
                   | array 
                   | '(' expression ')'"""
    if (len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = p[2]

# if we don't care about type during parsing than here we also should have expression TRANSPOSE
def p_expression_transpose(p):
    """ expression : expression TRANSPOSE """
    p[0] = AST.Transpose(p[1])

def p_expression_uminus(p):
    """ expression : '-' expression %prec UMINUS """
    p[0] = AST.Uminus(p[2])

def p_expression_bin_op(p):
    """ expression : expression '+' expression 
                   | expression '-' expression
                   | expression '*' expression
                   | expression '/' expression
                   | expression DOTADD expression
                   | expression DOTSUB expression
                   | expression DOTMUL expression
                   | expression DOTDIV expression
                   | expression '>' expression
                   | expression '<' expression
                   | expression GE expression
                   | expression LE expression
                   | expression EQ expression
                   | expression NOTEQ expression"""
    p[0] = AST.BinOp(p[2], p[1], p[3])

def p_array_operations(p):
    """ expression : ZEROS '(' INTNUM ')' 
                   | ONES '(' INTNUM ')'
                   | EYE '(' INTNUM ')' """
    p[0] = AST.ArrayOp(p[1], AST.Num(p[3]))

def p_block(p):
    """ block : '{' instructions '}' """
    p[0] =  AST.Block(p[2])

def p_if(p):
    """ if : IF '(' expression ')' instruction %prec IF
           | IF '(' expression ')' instruction ELSE instruction"""
    if(len(p) == 6):
        p[0] = AST.If(p[3], [p[5]])
    else:
        p[0] = AST.If(p[3], p[5], p[7])

def p_assign(p):
    """ assign : ID '=' expression ';'
               | ID ADDASSIGN expression ';'
               | ID SUBASSIGN expression ';'
               | ID MULASSIGN expression ';'
               | ID DIVASSIGN expression ';' """
    p[0] = AST.Assign(p[2], AST.Variable(p[1]), p[3])

def p_assign_array(p):
    """ assign_array : array_val '=' expression ';'
                     | array_val ADDASSIGN expression ';'
                     | array_val SUBASSIGN expression ';'
                     | array_val MULASSIGN expression ';'
                     | array_val DIVASSIGN expression ';' """
    p[0] = AST.ArrayAssign(p[1], p[2], p[3])

def p_sequence(p):
    """ sequence : expression
                 | expression ',' sequence"""
    if(len(p) == 2):
        p[0] = AST.Sequence(p[1])
    else:
        p[0] = AST.Sequence(p[1], p[3])

def p_print(p):
    """ print : PRINT sequence ';' """
    p[0] = AST.Print(p[2])

def p_while(p):
    """ while : WHILE '(' expression ')' instruction"""
    p[0] = AST.While(p[3], p[5])

def p_range(p):
    """ range : expression ':' expression """
    p[0] = AST.Range(p[1], p[3])

def p_for(p):
    """ for : FOR ID '=' range instruction """
    p[0] = AST.For(AST.Variable(p[2]), p[4], p[5])

def p_break(p):
    """ break : BREAK ';' """
    p[0] = AST.Break()

def p_continue(p):
    """ continue : CONTINUE ';' """
    p[0] = AST.Continue()

def p_return(p):
    """ return : RETURN ';' 
               | RETURN expression ';' """
    if(len(p) == 3):
        p[0] = AST.Return()
    else:
        p[0] = AST.Return(p[2])

parser = yacc.yacc()
