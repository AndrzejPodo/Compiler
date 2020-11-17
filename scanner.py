import sys
import ply.lex as lex
import lexer

if __name__ == '__main__':
    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        file = open(filename, "r")
    except:
        print(f'Cannot open { filename } file')
        sys.exit(0)

    text = file.read()
    lexer = lexer.lexer
    lexer.input(text)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(f'{tok.lineno}:{tok.type}({tok.value})')
