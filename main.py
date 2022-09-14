import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import calTime
from functools import partial
from calculate_time import cal_time


def click_success(ui):
    # 获取路径
    path = ui.filepath.toPlainText()

    # 计算
    all_time, converted_all_time = cal_time(path)


    # 设置窗口值
    ui.getTime1.setText(str(all_time))
    ui.getTime2.setText(str(converted_all_time))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = calTime.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # 添加按钮行为 click_success函数
    ui.cal.clicked.connect(partial(click_success, ui))

    sys.exit(app.exec_())
