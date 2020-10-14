import ply.lex as lex

literals = "+-*/=<>()[]{}:',;"

tokens = (
    'ID',        # id
    'ZEROS',     # zeros
    'ONES',      # ones
    'INTNUM',    # integer number
    'FLOAT',     # floating point number
    'STRING',    # string
    'EYE',       # eye
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
    'EQ'         # ==
)

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
