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

def p_val(p):
    """ value : STRING
              | num """

def p_val_array(p):
    """ values : value
               | value ',' values"""

def p_rows(p): #TODO
    """ rows : '[' values ']'
             | '[' values ']' ',' rows """

def p_array(p): #TODO
    """ array : '[' ']'
              | '[' rows ']'"""

def p_array_val(p):
    """ array_val : '[' INTNUM ',' INTNUM ']' 
                  | '[' INTNUM ']' """

def p_expression(p):
    """ expression : num
                   | ID """

def p_expression_transpose(p):
    """ expression : ID TRANSPOSE """

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
                   | expression DOTDIV expression"""


def p_expression_rel(p):
    """ expression_rel : expression '>' expression
                       | expression '<' expression
                       | expression GE expression
                       | expression LE expression
                       | expression EQ expression
                       | expression NOTEQ expression"""

def p_array_operations(p):
    """ array_op : ZEROS '(' INTNUM ')' 
                  | ONES '(' INTNUM ')'
                  | EYE '(' INTNUM ')' """

def p_block(p):
    """ block : '{' instructions '}' """

def p_if(p):
    """ if : IF '(' assignment ')' instruction %prec IF
           | IF '(' assignment ')' instruction ELSE instruction """

def p_assign(p):
    """ assign : ID '=' assignment ';'
               | ID ADDASSIGN assignment ';'
               | ID SUBASSIGN assignment ';'
               | ID MULASSIGN assignment ';'
               | ID DIVASSIGN assignment ';' """

def p_assign_array(p):
    """ assign_array : ID array_val '=' assignment ';'
                     | ID array_val ADDASSIGN assignment ';'
                     | ID array_val SUBASSIGN assignment ';'
                     | ID array_val MULASSIGN assignment ';'
                     | ID array_val DIVASSIGN assignment ';' """

def p_assignment(p):
    """ assignment : expression
                   | array
                   | expression_rel
                   | STRING 
                   | array_op """

def p_sequence(p):
    """ sequence : assignment
                 | assignment ',' sequence"""

def p_print(p):
    """ print : PRINT sequence ';' """

def p_while(p):
    """ while : WHILE '(' assignment ')' instruction """

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
               | RETURN assignment ';' """

parser = yacc.yacc()
