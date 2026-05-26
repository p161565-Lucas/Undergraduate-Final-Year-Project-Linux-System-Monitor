import sys
from PyQt5 import QtWidgets
# from UI.login.login import login_
from UI.login.loginForm import login_window
# from UI.login.login2Form import login2_window
# from UI.CPU.execute import Ui_CPU

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    login = login_window()
    # login2 = login_window()
    # CPU = Ui_CPU()
    # CPU.setupUi(CPU)
    login.show()
    # login2.show()
    sys.exit(app.exec_())
