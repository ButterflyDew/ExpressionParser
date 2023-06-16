from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel, QFileDialog, QLineEdit
# 选择文件布局框
class FileUploadWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        
        self.file_path_label = QLineEdit(self)
        self.layout.addWidget(self.file_path_label)
        self.path = "-"
        self.upload_button = QPushButton('选择文件', self)
        self.upload_button.clicked.connect(self.open_file_dialog)
        self.layout.addWidget(self.upload_button)
    # 获取路径
    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, '选择文件')
        self.path = file_path
        if file_path:
            self.file_path_label.setText(file_path)
            self.read_file(file_path)
    # 读取文件
    def read_file(self, file_path):
        with open(file_path, 'r') as file:
            file_content = file.read()
            #print(file_content)
            return file_content
        return -1

#app = QApplication([])
#window = FileUploadWidget()
#window.show()
#app.exec()
