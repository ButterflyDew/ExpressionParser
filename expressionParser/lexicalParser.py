# 词法分析模块
import ply.lex as lex

# token列表
tokens = (
    'DIGIT',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'POWER',
    'LPAREN',
    'RPAREN',
    'DOT',
    'LETTER'
)

# token对应的正则表达式
t_PLUS       = r'\+'
t_MINUS      = r'-'
t_MULTIPLY   = r'\*'
t_DIVIDE     = r'/'
t_POWER      = r'\^'
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_DOT        = r'\.'
t_LETTER     = r'([a-z]|[A-Z])+'

def t_DIGIT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# 出现不合法字符
errlist = []
def t_error(t):
    if t.value[0] != ' ':
        print("Illegal character '%s'" % t.value[0])
        errlist.append(t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()


class lexicalParser:
    def __init__(self) -> None:
        pass
    
    def parser(self, expression):
        global errlist
        errlist = []
        lexer.input(expression)
        ret = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            ret.append(tok)
        
        return ret,errlist


if __name__ == '__main__':
    lex = lexicalParser()
    
    print(lex.parser("(x+2)^2/y"))