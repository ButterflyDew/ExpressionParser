from PyQt5.QtWidgets import * 
import pandas as pd
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.Qt import *
from expressionParser.SeA import SeA
import shutil
import os
# 未进行语法分析窗口
class ErrorDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("错误")
        self.setModal(True)
        
        # 设置窗口内容
        self.label = QLabel("还未进行语法分析", self)
        
        # 添加确定按钮
        self.button = QPushButton("确定", self)
        self.button.clicked.connect(self.accept)
        
        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

# 输入未知数窗口
class InputDialog(QDialog):
    def __init__(self, varlist, valuelist, expression):
        super().__init__()
        self.setWindowTitle("请输入表达式未知参数的值")
        self.setModal(True)
        layout = QVBoxLayout()

        exp = QLabel("表达式为："+expression)
        self.lab = QLabel("请输入变量的值：")
        layout.addWidget(exp)
        layout.addWidget(self.lab)

        self.k = len(varlist)

        self.values = []
        for i in range(self.k):
            label = QLabel(varlist[i]+"=")
            line_edit = QLineEdit()
            self.values.append(line_edit)
            hb = QHBoxLayout()
            hb.addWidget(label)
            hb.addWidget(line_edit)

            layout.addLayout(hb)

        submit_button = QPushButton("确认")
        submit_button.clicked.connect(lambda: self.submit_values(valuelist))
        layout.addWidget(submit_button)

        self.setLayout(layout)

    def submit_values(self,valuelist):
        values = [line_edit.text() for line_edit in self.values]
        flg = 0
        print(values)
        for i in values:
            #print(i)
            try:
                ivalue = float(i)
            except ValueError:
                self.lab.setText("存在不为实数的输入，请重新输入：")
                return
            
        for i in values:
            valuelist.append(float(i))
            
        #print("Submitted values:", values)
        self.accept()

# 获取表达式
def getex(path):
    ex = ''
    with open(path, 'r') as f:
        ex = f.read()
        f.close()
    return ex

# 语义分析界面类
class SemanticAnalysis(QWidget):
    def __init__(self, p):    
        super().__init__()
        self.initUI()
        self.par = p
        #self.path = self.par.page2.path

    def initUI(self):
        title_label = QLabel("语义分析")
        font = title_label.font()
        font.setBold(True)
        font_size = font.pointSize() + 10
        font.setPointSize(font_size)
        title_label.setFont(font)

        conf_btn = QPushButton("开始进行语义分析")
        conf_btn.clicked.connect(self.sta_btn)

        self.exp_lab = QLabel("表达式为：")
        self.exp_res_lab = QLabel()
            
        self.token_lab = QLabel("Token列表为：")
        self.gird = QTableWidget()
        self.gird.setColumnCount(3)
        self.gird.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        header = self.gird.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch) 
        self.vbox = QVBoxLayout()

        self.vbox.addWidget(title_label)
        self.vbox.addWidget(conf_btn)
        self.vbox.addWidget(self.exp_lab)
        self.vbox.addWidget(self.exp_res_lab)
        self.vbox.addWidget(self.token_lab)
        self.vbox.addWidget(self.gird)

        self.setLayout(self.vbox)
        self.show()

    # 确认按钮事件
    def sta_btn(self):
        if self.par.page3.iscof == False:
            #show_error_dialog()
            error_dialog = ErrorDialog()
            error_dialog.exec_()
        else:
            #print("OK")
            path = self.par.page2.path
            #print(path)
            SeAma = SeA(path)
            varlist = SeAma.getvar()
            #varlist = ['x','y','z']
            valuelist = []
            ex = getex(path=path)
            if len(varlist) != 0:
                input_dialog = InputDialog(varlist, valuelist, ex)
                input_dialog.exec_()
                print(valuelist)

            SeAma.inputvalue(valuelist)
            
            token = SeAma.gettoken()
            res = SeAma.getres()

            self.exp_lab.setText("表达式为："+ex)

            sval = ex + "=" + str(res)
            if len(varlist)>0:
                sval = sval + ",其中"
                sval += ', '.join([s+'='+str(x) for s,x in zip(varlist, valuelist)]) + '.'
            else:
                sval +='.'

            self.exp_res_lab.setText(sval)
            
            # self.token_lab.setParent(None)
            # self.vbox.addWidget(self.token_lab)
            self.gird.setRowCount((len(token)+2)//3)

            r,c = 0,0
            lisx = []
            for x in token:
                #print(x)
                sx = "("+ str(x.type) + ", " + str(x.value) + ", " + str(x.lineno) + ", " + str(x.lexpos) + ")"
                #print("sx:"+sx)
                lisx.append(sx)
                table_item = QTableWidgetItem(sx)
                #print(str(r)+","+str(c))
                self.gird.setItem(r, c, table_item)
                if c==2:
                    r=r+1
                    c=0
                else:
                    c=c+1

            df = pd.DataFrame(lisx, columns=["token"])
            df.to_excel('OutFile/SyntacticParser.xlsx', index=False)
            # self.gird.setParent(None)
            # self.vbox.addWidget(self.gird)
            #print(token)
            #print("res:"+str(SeAma.getres()))
            # 获取当前工作目录
            current_dir = os.getcwd()

            src_file = "expressionParser/parser.out"
            dest_file = "OutFile/parser.out"

            #构建源文件和目标文件的完整路径
            src_path = os.path.join(current_dir, src_file)
            dest_path = os.path.join(current_dir, dest_file)

            shutil.move(src_path, dest_path)

