import sys
import ply.lex as lex
import lexer
import parser

if __name__ == '__main__':
    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        file = open(filename, "r")
    except:
        print(f'Cannot open { filename } file')
        sys.exit(0)

    parser = parser.parser
    text = file.read()
    parser.parse(text, lexer=lexer.lexer)
