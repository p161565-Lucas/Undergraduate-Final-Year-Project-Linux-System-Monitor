import paramiko
import re
# from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets, QtCore
from UI.interface.untitled import Ui_Form

class MainWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.update_timer = QtCore.QTimer()  # 设置定时器
        self.update_timer.start(2000)  # 开启20ms定时器
        self.init_solt()

    def init_solt(self):
        """
        初始化槽函数
        :return:
        """
        self.update_timer.timeout.connect(self.Data_Acquisition)  # 延迟30ms

    def connect_linux(self):
        """
        连接虚拟机配置
        :return:
        """
        # 设置虚拟机的IP地址、用户名和脚本路径
        self.script_path = '/home/abc/top_script.sh'  # 脚本在虚拟机里面的路径
        self.hostname = '192.168.206.128'  # 虚拟机ip
        self.username = 'abc'  # 虚拟机用户名
        # 创建SSH客户端
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 连接到虚拟机
        self.client.connect(self.hostname, username=self.username, password="abc", port=22)

    def Data_Acquisition(self):
        """
        运行shell脚本，处理结果
        :return:
        """
        self.connect_linux()
        # 执行shell脚本
        stdin, stdout, stderr = self.client.exec_command(f'bash {self.script_path}')
        self.output = stdout.read().decode('utf-8', errors='ignore')
        print(self.output)

        # 使用正则表达式提取CPU空闲时间百分比
        self.cpu_idle_percentage = re.search(r',\s*([\d.]+)\sid,', self.output)
        if self.cpu_idle_percentage:
            idle_percentage = self.cpu_idle_percentage.group(1)
            print("CPU利用率:", round(100 - float(idle_percentage), 2))
            cpu = "CPU利用率： {:.2f}%".format(100 - float(idle_percentage))
            self.label.setText(cpu)  # 将获取到的CPU利用率设置为label的文本
        else:
            print("未找到CPU利用率")

        # 关闭连接
        self.client.close()

        # 按行分割数据
        rows = self.output.splitlines()

        # 创建一个空的二维列表
        result = []

        # 遍历每一行数据
        for row in rows:
            # 按空格分割每一行数据
            elements = row.split()
            # 将分割后的元素添加到二维列表中
            result.append(elements)

        # 任务总数
        task = "总任务数：" + result[1][1]
        self.label_2.setText(task)

        # 内存使用率
        mem = round(float(result[3][5]) / float(result[3][3]) * 100, 2)
        mem = "内存占用率：" + str(mem) + '%'
        self.label_3.setText(mem)

        # 找出线程数据
        data = result[7:]  # 第8行开始是线程数据

        for row in data:
            row.pop(7)  # 第三个值无效
        # print(data[1][0])
        # 添加线程数据
        self.tableWidget.setRowCount(0)
        for i in range(len(data)):
            row_count = self.tableWidget.rowCount()  # 返回当前行数(尾部)
            self.tableWidget.insertRow(row_count)  # 尾部插入一行
            for j in range(0, len(data[i])):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(data[i][j])))
