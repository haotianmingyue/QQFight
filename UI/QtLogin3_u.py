# 开发者 haotian
# 开发时间: 2021/7/2 11:03
from PyQt5.QtWidgets import QApplication, QMainWindow

import QtLogin3

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainWindow=QMainWindow()
    # 实例化
    ui=QtLogin3.Ui_MainWindow()

    # 想主窗口添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())