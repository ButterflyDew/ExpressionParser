# 语法分析模块
import ply.yacc as yacc
from .lexicalParser import tokens
from .modifyLetterVal import letters
from graphviz import Digraph
import os
import shutil
synerr = 0

'''
语法树节点定义：
type 类型
expression 子表达式字符串
value 值
children 子节点
'''
class Node:
    def __init__(self, type, expression, value, children=None):
        self.type = type
        self.value = value
        self.strVal = expression
        if children:
            self.children = children
        else:
            self.children = [ ]

# 二元运算符处理
def p_binary_operators(p):
    '''expression : expression PLUS term
                  | expression MINUS term
       term       : factor MULTIPLY term
                  | factor DIVIDE term
       factor     : base POWER factor'''
    if p[2] == '+':
        p[0] = Node('expression', p[1].strVal + '+' + p[3].strVal, p[1].value + p[3].value, [p[1], Node('PLUS', '+', '+'), p[3]])
        # p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = Node('expression', p[1].strVal + '-' + p[3].strVal, p[1].value - p[3].value, [p[1], Node('MINUS', '-', '-'), p[3]])
        # p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = Node('term', p[1].strVal + '*' + p[3].strVal, p[1].value * p[3].value, [p[1], Node('MULTIPLY', '*', '*'), p[3]])
        # p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = Node('term', p[1].strVal + '/' + p[3].strVal, p[1].value / p[3].value, [p[1], Node('DIVIDE', '/', '/'), p[3]])
        # p[0] = p[1] / p[3]
    elif p[2] == '^':
        p[0] = Node('factor', p[1].strVal + '^' + p[3].strVal, p[1].value ** p[3].value, [p[1], Node('POWER', '^', '^'), p[3]])
        # p[0] = p[1] ** p[3]


# def p_pushdown(p):
#     '''expression : term
#        term       : factor
#        factor     : base
#        base       : identifier
#                   | DIGIT
#                   | real'''
#     p[0] = p[1]

def p_expression_term(p):
    'expression : term'
    p[0] = Node('expression', p[1].strVal, p[1].value, [p[1]])

def p_term_factor(p):
    'term : factor'
    p[0] = Node('term', p[1].strVal, p[1].value, [p[1]])

def p_factor_base(p):
    'factor : base'
    p[0] = Node('factor', p[1].strVal, p[1].value, [p[1]])

def p_base_identifier(p):
    'base : identifier'
    p[0] = Node('base', p[1].strVal, p[1].value, [p[1]])

def p_base_DIGIT(p):
    'base : DIGIT'
    p[0] = Node('base', str(p[1]), p[1], [Node('DIGIT', str(p[1]), p[1])])

def p_base_real(p):
    'base : real'
    p[0] = Node('base', p[1].strVal, p[1].value, [p[1]])

# 括号处理
def p_base_expression(p):
    'base : LPAREN expression RPAREN'
    p[0] = Node('base', '(' + p[2].strVal + ')', p[2].value, [Node('LPAREN', '(', '('), p[2], Node('RPAREN', ')', ')')])

# 标识符处理
def p_indentifier(p):
    '''identifier : LETTER
                  | DIGIT LETTER'''
    if len(p) == 2:
        p[0] = Node('identifier', p[1], letters.getMap(p[1]), [Node('LETTER', p[1], p[1])])
        # p[0] = letters.getMap(p[1])
    else:
        p[0] = Node('identifier', str(p[1]) + p[2], p[1] * letters.getMap(p[2]), [Node('DIGIT', str(p[1]), p[1]), Node('LETTER', p[2], letters.getMap(p[2]))])
        # p[0] = p[1] * letters.getMap(p[2])

# 实数处理
def p_real_digit(p):
    'real : DIGIT DOT DIGIT'
    real = str(p[1]) + '.' + str(p[3])
    p[0] = Node('real', real, float(real), [Node('DIGIT', str(p[1]), p[1]), Node('Dot', '.', '.'), Node('DIGIT', str(p[3]), p[3])])
    # p[0] = float(real)

# 语法分析错误
def p_error(p):
    print('Syntax error')
    global synerr
    synerr = 1

parser = yacc.yacc()


class syntacticParser:
    def __init__(self) -> None:
        # 创建一个 Digraph 对象
        self.dot = Digraph()
        self.cnt = 0
        global synerr
        synerr = 0
        pass
    
    def issynerr(self):
        global synerr
        return synerr

    def parse(self, expression):
        ret = parser.parse(expression)
        return ret
    
    def write_text(self, text):
        with open('OutFile/Syntax_tree.txt', 'a') as file:
            file.write(text + '\n')

    # 遍历语法树
    def dfs(self, node, dep):
        # if type(node.value)==float:
        #     tval = "{:.3f}".format(node.value)
        # else:
        #     tval = node.value
        # info = node.type + ":" + str(tval)

        info = node.type + ":" + node.strVal
        text = "--" * dep + info
        self.write_text(text)
        self.cnt += 1
        now = str(self.cnt)
        self.dot.node(now,info)
        if node.children:
            for i in node.children:
                chi = self.dfs(i,dep+1)
                self.dot.edge(now,chi)
        return now
        #self.write_text(text)

    def getRoot(self, expression):
        root = self.parse(expression=expression)
        return root

    def genePic(self, expression):
        if os.path.exists('OutFile/Syntax_tree.txt'):
            os.remove('OutFile/Syntax_tree.txt')
        
        self.dfs(self.getRoot(expression), 1)
        self.dot.render("syntax_tree.gv", format="png")

        src_file = "syntax_tree.gv.png"
        dest_file = "OutFile/syntax_tree.gv.png"
        shutil.copy(src_file, dest_file)

    def getValue(self, expression):
        root = self.parse(expression=expression)
        return root.value
