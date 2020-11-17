import ply.lex as lex

literals = "+-*/=<>()[]{}:',;"

reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'for' : 'FOR',
    'while' : 'WHILE',
    'break' : 'BREAK',
    'continue' : 'CONTINUE',
    'return' : 'RETURN',
    'eye' : 'EYE',
    'zeros' : 'ZEROS',
    'ones' : 'ONES',
    'print' : 'PRINT'
}

tokens = (
    'ID',        # id
    'INTNUM',    # integer number
    'FLOAT',     # floating point number
    'STRING',    # string
    'DOTADD',    # .+ 
    'DOTSUB',    # .- 
    'DOTMUL',    # .* 
    'DOTDIV',    # ./ 
    'ADDASSIGN', # += 
    'SUBASSIGN', # -= 
    'MULASSIGN', # *= 
    'DIVASSIGN', # /= 
    'GE',        # >= 
    'LE',        # <= 
    'NOTEQ',     # != 
    'EQ',        # == 
    'TRANSPOSE',
    'UMINUS'

)

tokens = list(tokens) + list(reserved.values())

t_ignore_COMMENT = r'\#.*' # rule for discarding comments

t_ignore = ' \t\n' # we want to ingore tabs, new lines and spaces

t_FLOAT = r'((\d+\.\d*)|(\.\d+))(E-?\d+)?' # float number is digit one or more times, dot and digit one ore more time ex. 000231.23 

t_INTNUM = r'\d+' # integer number is just digit one or more times ex. 1, 00012 

t_STRING = r'"([^"\\]|(\\")|(\\))*"' # strings in form "charcacters" it is possible to escape " in string like "its a \"cat\""
# first character as undersore or letter, rest of characters as letters underscores or digits
# example: A, _A _A__, A_9

#specs for dot operations and assign operations
t_DOTADD = r'\.\+'
t_DOTSUB = r'\.-'
t_DOTMUL = r'\.\*'
t_DOTDIV = r'\./'
t_ADDASSIGN = r'\+='
t_SUBASSIGN = r'-='
t_MULASSIGN = r'\*='
t_DIVASSIGN = r'/='
t_GE = r'>='
t_LE = r'<='
t_NOTEQ = r'\!='
t_EQ = r'=='
t_TRANSPOSE = r'\''

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*' 
    t.type = reserved.get(t.value, 'ID')
    return t

def t_newline(t):
    r';'
    t.lexer.lineno += len(t.value) # len(t.value) because for example ';;;;' means four new lines
    t.value = ';'
    t.type = ';'
    return t

 # Error handling rule
def t_error(t):
    print(f'Illegal character {t.value[0]} at line {t.lineno}' )
    t.lexer.skip(1)

lexer = lex.lex()
