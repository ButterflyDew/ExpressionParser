from PyQt5.QtWidgets import * 
import pandas as pd
import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.Qt import *
from FileUploadWidget import FileUploadWidget
from expressionParser.lexicalParser import lexicalParser

class LexicalAnalysis(QWidget):
    def __init__(self):    
        super().__init__()
        self.initUI()

    def initUI(self):
        self.iscof = 0
        self.path = "nop"

        title_label = QLabel("词法分析")
        font = title_label.font()
        font.setBold(True)
        font_size = font.pointSize() + 10
        font.setPointSize(font_size)
        title_label.setFont(font)
        #title_label.setAlignment(Qt.AlignCenter) 


        self.FUW = FileUploadWidget()
        conf_btn = QPushButton("确认")
        conf_btn.clicked.connect(self.confirm)
        hb1 = QHBoxLayout()
        hb1.addWidget(self.FUW)
        hb1.addWidget(conf_btn)

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["type", "value","lexpos"]) 

        self.table_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        header = self.table_widget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch) 

        self.vbox = QVBoxLayout()

        self.vbox.addWidget(title_label)
        self.vbox.addLayout(hb1)
        self.vbox.addWidget(self.table_widget)

        self.setLayout(self.vbox)
        self.show()

    def confirm(self):
        self.path = self.FUW.path
        #print(self.path)
        s = ''
        with open(self.path, 'r') as f:
            s = f.read()
            f.close()
        LA = lexicalParser()
        self.data = []
        lextok= LA.parser(s)
        for x in lextok:
            self.data.append((x.type,x.value,x.lexpos))
        print(self.data)
        folder_path = 'OutFile'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        df = pd.DataFrame(self.data, columns=["type", "value","lexpos"])
        df.to_excel('OutFile/LexicalParser.xlsx', index=False)

        self.table_widget.setRowCount(len(self.data))
        for row, (ty,va,lex) in enumerate(self.data):
            ty_widget = QTableWidgetItem(ty)
            va_widget = QTableWidgetItem(str(va))
            #li_widget = QTableWidgetItem(str(li))
            lex_widget = QTableWidgetItem(str(lex))
            
            self.table_widget.setItem(row, 0, ty_widget)
            self.table_widget.setItem(row, 1, va_widget)
            #self.table_widget.setItem(row, 2, li_widget)
            self.table_widget.setItem(row, 2, lex_widget)

        self.iscof = 1
        #print(self.path)
