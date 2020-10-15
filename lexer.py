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
)

tokens = list(tokens) + list(reserved.values())

t_ignore_COMMENT = r'\#.*' # rule for discarding comments

t_ignore = ' \t\n' # we want to ingore tabs, new lines and spaces

t_INTNUM = r'\d+' # integer number is just digit one or more times ex. 1, 00012 

t_FLOAT = r'(\d+\.\d*)|(\.\d+)' # float number is digit one or more times, dot and digit one ore more time ex. 000231.23

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

lexer = lex.lex()

data_1 = '''
A = zeros(5); # create 5x5 matrix filled with zeros
B = ones(7);  # create 7x7 matrix filled with ones
I = eye(10);  # create 10x10 matrix filled with ones on diagonal and zeros elsewhere
D1 = A.+B' ;  # add element-wise A with transpose of B
D2 -= A.-B' ; # substract element-wise A with transpose of B
D3 *= A.*B' ; # multiply element-wise A with transpose of B
D4 /= A./B' ; # divide element-wise A with transpose of B
'''

data_2 = '''
A = zeros(5);  # create 5x5 matrix filled with zeros
B = ones(7);   # create 7x7 matrix filled with ones
I = eye(10);   # create 10x10 matrix filled with ones on diagonal and zeros elsewhere
D1 = A.+B' ; # add element-wise A with transpose of B
D2 -= A.-B' ; # substract element-wise A with transpose of B
D3 *= A.*B' ; # multiply element-wise A with transpose of B
D4 /= A./B' ; # divide element-wise A with transpose of B

E1 = [ [ 1, 2, 3],
       [ 4, 5, 6],
       [ 7, 8, 9] ];

res1 = 60.500;
res2 = 60.;
res3 = .500;
res4 = 60.52E2;
str = "Hello world";

if (m==n) { 
    if (m >= n) 
        print res;
}
'''

lexer.input(data_2)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break   
    print(f'({tok.lineno}): {tok.type}({tok.value})')

