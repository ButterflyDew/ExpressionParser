from PyQt5.QtWidgets import * 
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.Qt import *

#首页
class mainpage(QWidget):
    def __init__(self):    
        super().__init__()
        self.initUI()

    def initUI(self):
        self.iscof = 0
        title_label = QLabel("首页")
        font = title_label.font()
        font.setBold(True)
        font_size = font.pointSize()+15
        font.setPointSize(font_size)
        title_label.setFont(font)
        title_label.setAlignment(Qt.AlignCenter) 

        author_label = QLabel("作者：万宇恒，杨宇轩")
        font2 = author_label.font()
        font2.setBold(True)
        font2_size = font2.pointSize()+7
        font2.setPointSize(font2_size)
        author_label.setFont(font2)
        author_label.setAlignment(Qt.AlignCenter) 

        intro_label = QLabel("      本应用实现了一个表达式求值的⽂法，此⽂法是⽤于描述⼀个包含加减乘除乘幂运算、括号和标识符、整数、实数的表达式的语法规则。该表达式的运算符按照优先级排序，其中乘幂运算符的优先级最⾼，加减运算符的优先级最低。此外，加减运算符是左结合，⽽乘除乘幂运算符是右结合。该⽂法可以被⽤于进⾏表达式的词法分析、语法分析和语义分析，以计算表达式中各部分的值并输出整个表达式的值。这个⽂法可能会被应⽤于编写计算器或其他类似的⼯具，也可以作为编程语⾔中表达式的语法规则。\n\n    为了使用本应用，你需要在词法分析界面导入写有表达式的 .txt 文件，其内容为一个可带未知数的表达式，例如 (x+2)^2/y（表达式的具体规则见文档）。")
        intro_label.setWordWrap(True)
        
        font3 = intro_label.font()
        font3.setBold(True)
        font3_size = font3.pointSize()+5
        font3.setPointSize(font3_size)
        intro_label.setFont(font3)

        lab = QLabel()
        lab.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(title_label)
        self.vbox.addWidget(author_label)
        self.vbox.addWidget(intro_label)
        self.vbox.addWidget(lab)
        self.setLayout(self.vbox)
        self.show()
