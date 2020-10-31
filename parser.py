import scanner
import ply.yacc as yacc
import lexer as scanner

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

def p_instructions_opt_1(p):
    """instructions_opt : instructions """

def p_instructions_opt_2(p):
    """instructions_opt : """

def p_instructions_1(p):
    """instructions : instructions instruction """

def p_instructions_2(p):
    """instructions : instruction """

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

def p_num(p):
    """ num : INTNUM
            | FLOAT """

def p_int_seq(p):
    """ ints : INTNUM
             | INTNUM ',' ints"""

# array is empty or contains any sequence (this is how it work in python)
def p_array(p):
    """ array : '[' ']'
              | '[' sequence ']' """

# array can have more than two dimensions so [int] and [int,int] wont be enough
def p_array_val(p):
    """ array_val : '[' ints ']' 
    """

def p_expression(p):
    """ expression : num
                   | ID
                   | STRING 
                   | array 
                   | '(' expression ')'"""

# if we don't care about type during parsing than here we also should have expression TRANSPOSE
def p_expression_transpose(p):
    """ expression : expression TRANSPOSE """

def p_expression_uminus(p):
    """ expression : '-' expression %prec UMINUS """

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

def p_array_val_expression(p):
    """expression : ID array_val """

def p_array_operations(p):
    """ expression : ZEROS '(' INTNUM ')' 
                   | ONES '(' INTNUM ')'
                   | EYE '(' INTNUM ')' """

def p_block(p):
    """ block : '{' instructions '}' """

def p_if(p):
    """ if : IF '(' expression ')' instruction %prec IF
           | IF '(' expression ')' instruction ELSE instruction"""

def p_assign(p):
    """ assign : ID '=' expression ';'
               | ID ADDASSIGN expression ';'
               | ID SUBASSIGN expression ';'
               | ID MULASSIGN expression ';'
               | ID DIVASSIGN expression ';' """

def p_assign_array(p):
    """ assign_array : ID array_val '=' expression ';'
                     | ID array_val ADDASSIGN expression ';'
                     | ID array_val SUBASSIGN expression ';'
                     | ID array_val MULASSIGN expression ';'
                     | ID array_val DIVASSIGN expression ';' """
def p_sequence(p):
    """ sequence : expression
                 | expression ',' sequence"""

def p_print(p):
    """ print : PRINT sequence ';' """

def p_while(p):
    """ while : WHILE '(' expression ')' instruction"""

def p_range(p):
    """ range : expression ':' expression """

def p_for(p):
    """ for : FOR ID '=' range instruction """

def p_break(p):
    """ break : BREAK ';' """

def p_continue(p):
    """ continue : CONTINUE ';' """

def p_return(p):
    """ return : RETURN ';' 
               | RETURN expression ';' """

parser = yacc.yacc()
