from PyQt5.QtWidgets import * 
import sys
from PyQt5.QtCore import  *
from PyQt5.QtGui import  *
from PyQt5.QtSql import *
from PyQt5.Qt import *
from mainpage import mainpage
from LApage import LexicalAnalysis
from SyApage import SyntaxAnalysis
from SeApage import SemanticAnalysis

# 主程序
class WindowClass(QWidget):
    def __init__(self,parent=None):
        super(WindowClass, self).__init__(parent)
        self.Window_Title="实习文法设计"
        self.setWindowTitle(self.Window_Title)
        self.resize(1000,600)

        logo = QLabel()
        pixmap = QPixmap('logo.png') 
        logos = 285
        logo.setFixedSize(logos,logos)
        pixmap = pixmap.scaled(logos,logos,Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)
        logo.setPixmap(pixmap)
        

        btn1 = QPushButton("首页")
        btn1.clicked.connect(self.tranmp)
        btn1.setFixedSize(300, 45)

        btn2 = QPushButton("词法分析")
        btn2.clicked.connect(self.tranLA)
        btn2.setFixedSize(300, 45)

        btn3 = QPushButton("语法分析")
        btn3.clicked.connect(self.tranSya)
        btn3.setFixedSize(300, 45)

        btn4 = QPushButton("语意分析")
        btn4.clicked.connect(self.tranSea)
        btn4.setFixedSize(300, 45)

        btn5 = QPushButton("退出")
        btn5.clicked.connect(self.quit_application)
        btn5.setFixedSize(300, 45)

        leftv = QVBoxLayout()

        leftv.addWidget(logo)
        leftv.addWidget(btn1)
        leftv.addWidget(btn2)
        leftv.addWidget(btn3)
        leftv.addWidget(btn4)
        leftv.addWidget(btn5)

        rr,cc = 800,600
        self.rigv = QVBoxLayout()
        self.page1 = mainpage()
        self.page1.setFixedSize(rr,cc)
        self.page2 = LexicalAnalysis()
        self.page2.setFixedSize(rr,cc)
        self.page3 = SyntaxAnalysis(self)
        self.page3.setFixedSize(rr,cc)
        self.page4 = SemanticAnalysis(self)
        self.page4.setFixedSize(rr,cc)
        self.rigv.addWidget(self.page1)

        self.page2.setVisible(False)
        self.page3.setVisible(False)
        self.page4.setVisible(False)

        self.mainwindow = QHBoxLayout()
        self.mainwindow.addLayout(leftv)
        self.mainwindow.addLayout(self.rigv)

        self.setLayout(self.mainwindow)
        self.show()
    def delwget(self):
        for i in range(self.rigv.count()):
            item = self.rigv.itemAt(i)
            wget = item.widget()
            self.rigv.removeWidget(wget)
            wget.setVisible(False)

    def tranmp(self):
        self.delwget()
        self.page1.setVisible(True)
        self.rigv.addWidget(self.page1)

    def tranLA(self):
        self.delwget()
        self.page2.setVisible(True)
        self.rigv.addWidget(self.page2)

    def tranSya(self):
        self.delwget()
        self.page3.setVisible(True)
        self.rigv.addWidget(self.page3)

    def tranSea(self):
        self.delwget()
        self.page4.setVisible(True)
        self.rigv.addWidget(self.page4)

    def quit_application(self):
        QCoreApplication.instance().quit()


if __name__=="__main__":
    app=QApplication(sys.argv)
    win=WindowClass()
    win.show()
    sys.exit(app.exec_())