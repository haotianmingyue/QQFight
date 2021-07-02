# 开发者 haotian
# 开发时间: 2021/7/1 21:45
import sys
from PyQt5.QtWidgets import QApplication,QWidget
if __name__ == '__main__':
    # 创建QApplication
    app=QApplication(sys.argv)
    # 创建一个窗口
    w=QWidget()
    # 设置尺寸
    w.resize(400,400)
    # 移动窗口
    w.move(300,300)
    # 设置窗口标题
    w.setWindowTitle('first pyqt5')
    # 显示窗口
    w.show()
    # 进入程序主循环，并通过exit函数确保循环安全结束
    sys.exit(app.exec())