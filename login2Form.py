import sys

import pymssql
# import psycopg2
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore
# from PyQt5.uic.properties import QtCore

from UI.login import login2
from UI.login import login
from UI.login import loginForm
from UI.login.login2 import Ui_MainWindow
from UI.CPU.execute import CPU

class login2window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(login2window, self).__init__()
        # self.lineEdit2 = None
        self.ui = Ui_MainWindow()
        self.setupUi(self)  # 创建窗体对象
        # self.show()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(5, 5)
        self.shadow.setBlurRadius(15)
        self.shadow.setColor(QtCore.Qt.blue)
        # self.ui.textBrowser.setGraphicsEffect(self.shadow)
        self.init()


    def init(self):
        self.pushButton_3.clicked.connect(self.register_button)  # 连接槽
        self.pushButton_4.clicked.connect(self.return_button)

    def register_button(self):
        if self.lineEdit.text() == "":
            QMessageBox.warning(self, '警告', '账号不能为空，请输入！')
        if self.lineEdit_2.text() == "":
            QMessageBox.warning(self, '警告', '密码不能为空，请输入！')
        if self.lineEdit_3.text() == "":
            QMessageBox.information(self, '警告', '请确认密码！')
            return None
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        confirm = self.lineEdit_3.text()
        admin_list = []
        password_list = []
        conn = pymssql.connect(server="127.0.0.1", database='rsn', user='sa', password='123')
        cur = conn.cursor()
        cur.execute("select * from users")
        # 从数据库游标（cursor）中获取查询结果的所有行
        rows = cur.fetchall()
        print(rows)
        for row in rows:
            if row[0] == username:
                QMessageBox.information(self, '错误', '用户名已存在!请重新注册')
                return None
            if self.lineEdit_3.text() != self.lineEdit_2.text():
                QMessageBox.information(self, '错误', '两次密码不一致!')
                return None
            if self.lineEdit.text() == self.lineEdit_2.text():
                QMessageBox.information(self, '错误','账号和密码不能相同，请重新输入!')
                return None
        try:
            cur.execute(f"insert into users(accounts,passswords) values('{username}','{password}')")
            conn.commit()
            QMessageBox.information(self, '错误', '注册成功!')
            self.close()
        except Exception as e:
            print(e)
            QMessageBox.warning(self, '错误', '注册失败!请重新注册')
            conn.rollback()
            conn.close()

    def return_button(self):
            self.close()

if __name__ == '__main__':   #用于当前窗体测试
    app = QApplication(sys.argv)   #创建GUI应用程序
    MainWindow = QMainWindow()     #创建窗体
    ui = login2.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())