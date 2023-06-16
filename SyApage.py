from PyQt5.QtWidgets import * 
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.Qt import *
from expressionParser.SyA import SyA
import shutil

# Synerr 窗口
class SyAError(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("错误")
        self.setModal(True)
        
        # 设置窗口内容
        self.label = QLabel("Syntax error,请输入正确的表达式", self)
        
        # 添加确定按钮
        self.button = QPushButton("确定", self)
        self.button.clicked.connect(self.accept)
        
        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

# 未进行词法分析错误窗口
class ErrorDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("错误")
        self.setModal(True)
        
        # 设置窗口内容
        self.label = QLabel("还未进行词法分析", self)
        
        # 添加确定按钮
        self.button = QPushButton("确定", self)
        self.button.clicked.connect(self.accept)
        
        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

# 语法分析界面类
class SyntaxAnalysis(QWidget):
    def __init__(self, p):    
        super().__init__()
        self.initUI()
        self.par = p
        self.path = self.par.page2.path


    def initUI(self):
        self.iscof = 0
        title_label = QLabel("语法分析")
        font = title_label.font()
        font.setBold(True)
        font_size = font.pointSize()+10
        font.setPointSize(font_size)
        title_label.setFont(font)

        conf_btn = QPushButton("开始进行语法分析")
        conf_btn.clicked.connect(self.sta_btn)

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)

        self.vbox = QVBoxLayout()

        self.vbox.addWidget(title_label)
        self.vbox.addWidget(conf_btn)
        self.vbox.addWidget(self.view)

        self.setLayout(self.vbox)
        self.show()

    # 点击按钮事件
    def sta_btn(self):
        if self.par.page2.iscof == False:
            #show_error_dialog()
            error_dialog = ErrorDialog()
            error_dialog.exec_()
        else:
            path = self.par.page2.path
            SyAma = SyA(path)
            if SyAma.geterr() == 1:
                synerr = SyAError()
                synerr.exec_()
                return
            self.iscof = 1
            pixmap = QPixmap("syntax_tree.gv.png")
            pixmap = pixmap.scaled(800,750,Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)
            self.scene.addPixmap(pixmap)
            #print("OK")



