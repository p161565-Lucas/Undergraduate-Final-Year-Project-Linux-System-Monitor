import sys

import pymssql
# import psycopg2
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore
# from PyQt5.uic.properties import QtCore

from UI.login import login
from UI.login import login2
from UI.login.login2Form import login2window
from UI.login.login2 import Ui_MainWindow
from UI.login.login import Ui_MainWindow
from UI.CPU.execute import CPU


user_now = ''

class login_window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(login_window, self).__init__()
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

# class login2_window(QtWidgets.QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super(login2_window, self).__init__()
#         self.ui = Ui_MainWindow()
#         self.setupUi(self)
#     def Open(self):
#         self.show()
        # account = self.ui.lineEdit.text()
        # password = self.ui.lineEdit_2.text()
        # account_list = []
        # password_list = []
        # conn = psycopg2.connect(database='rsn', user='sa', password='123', host='192.168.182.1',port=1433)
        # cur = conn.cursor()
        # cur.execute("select * from users")
        # rows = cur.fetchall()
        # for row in rows:
        #     account_list.append(row[0])
        #     password_list.append(row[1])
        #     print(account_list,password_list)
        # conn.commit()
        # conn.close()
        # for i in range(len(account_list)):
        #     if account == account_list[i] and password == password_list[i]:
        #     self.ui = Ui_MainWindow
        #     self.close()
        # else:
        #     print("Wrong username or password")
        # self.admin = "20201507"
        # self.Password = "000"
        # self.admin = self.lineEdit.text()
        # self.password = self.lineEdit_2.text()
        # admin_list = []
        # password_list = []

    def init(self):
        self.pushButton.clicked.connect(self.login_button)  # 连接槽
        self.pushButton_3.clicked.connect(self.register_button) # 连接槽

    def login_button(self):
        if self.lineEdit.text() == "":
            QMessageBox.warning(self, '警告', '账号不能为空，请输入！')
        if self.lineEdit_2.text() == "":
            QMessageBox.warning(self, '警告', '密码不能为空，请输入！')
            return None
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        conn = pymssql.connect(server="127.0.0.1", database='rsn', user='sa', password='123')
        cur = conn.cursor()
        cur.execute("select * from users")
        rows = cur.fetchall()
        print(rows)
        #conn.commit()
        conn.close()

        for row in rows:
            if row[0] == username and row[1] == password:
                self.mw = CPU()
                self.mw.show()

                # 2关闭本窗口
                self.close()
                break
        else:
            QMessageBox.critical(self, '错误', '用户名或密码错误！')
            self.lineEdit_2.clear()
            return None


    def register_button(self):
        self.ui = login2window()
        self.ui.show()


        # if self.lineEdit.text() == "":
        #     QMessageBox.warning(self, '警告', '账号不能为空，请输入！')
        # if self.lineEdit_2.text() == "":
        #     QMessageBox.warning(self, '警告', '密码不能为空，请输入！')
        #     return None
        # username = self.lineEdit.text()
        # password = self.lineEdit_2.text()
        # admin_list = []
        # password_list = []
        # conn = pymssql.connect(server="127.0.0.1", database='rsn', user='sa', password='123')
        # cur = conn.cursor()
        #
        # try:
        #     cur.execute(f"insert into users(accounts,passswords) values('{username}','{password}')")
        #     conn.commit()
        #     QMessageBox.information(self, '错误', '注册成功!')
        # except Exception as e:
        #     print(e)
        #     QMessageBox.warning(self, '错误', '注册失败!')
        #     conn.rollback()
        #
        # conn.close()

if __name__ == '__main__':   #用于当前窗体测试
    app = QApplication(sys.argv)   #创建GUI应用程序
    MainWindow = QMainWindow()     #创建窗体
    ui = login.Ui_MainWindow()
    # ui2 = login2.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
