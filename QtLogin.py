# gui.py
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'encrypt.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#
# Writen By Mr. REDHAT From HUST

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

import AES


class UiMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(UiMainWindow, self).__init__(parent)

        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.setStyleSheet("#MainWindow{background-color: pink}")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.setFont(font)
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("central_widget")

        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setGeometry(QtCore.QRect(20, 90, 111, 31))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.central_widget)
        self.label_2.setGeometry(QtCore.QRect(23, 170, 101, 31))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.central_widget)
        self.label_3.setGeometry(QtCore.QRect(20, 270, 111, 31))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.central_widget)
        self.label_4.setGeometry(QtCore.QRect(20, 390, 111, 31))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.input_text = QtWidgets.QPlainTextEdit(self.central_widget)
        self.input_text.setGeometry(QtCore.QRect(130, 60, 500, 111))
        self.input_text.setObjectName("input_text")
        self.key_text = QtWidgets.QPlainTextEdit(self.central_widget)
        self.key_text.setGeometry(QtCore.QRect(130, 175, 500, 31))
        self.key_text.setObjectName("key_text")
        self.encrypted_text = QtWidgets.QPlainTextEdit(self.central_widget)
        self.encrypted_text.setGeometry(QtCore.QRect(130, 220, 500, 111))
        self.encrypted_text.setObjectName("encrypted_text")
        self.decrypted_text = QtWidgets.QPlainTextEdit(self.central_widget)
        self.decrypted_text.setGeometry(QtCore.QRect(130, 350, 500, 111))
        self.decrypted_text.setObjectName("decrypted_text")

        self.push_button_1 = QtWidgets.QPushButton(self.central_widget)
        self.push_button_1.setGeometry(QtCore.QRect(660, 175, 81, 31))
        self.push_button_1.setFont(font)
        self.push_button_1.setObjectName("pushButton_1")
        self.push_button_2 = QtWidgets.QPushButton(self.central_widget)
        self.push_button_2.setGeometry(QtCore.QRect(660, 262, 81, 31))
        self.push_button_2.setFont(font)
        self.push_button_2.setObjectName("pushButton_2")
        self.push_button_3 = QtWidgets.QPushButton(self.central_widget)
        self.push_button_3.setGeometry(QtCore.QRect(660, 390, 81, 31))
        self.push_button_3.setFont(font)
        self.push_button_3.setObjectName("pushButton_3")

        self.setCentralWidget(self.central_widget)
        self.menu_bar = QtWidgets.QMenuBar(self)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menu_bar.setObjectName("menu_bar")
        self.setMenuBar(self.menu_bar)
        self.status_bar = QtWidgets.QStatusBar(self)
        self.status_bar.setObjectName("status_bar")
        self.setStatusBar(self.status_bar)

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "input:"))
        self.label_2.setText(_translate("MainWindow", "key:"))
        self.label_3.setText(_translate("MainWindow", "encrypted:"))
        self.label_4.setText(_translate("MainWindow", "decrypted:"))
        self.push_button_1.setText(_translate("MainWindow", "encrypt"))
        self.push_button_2.setText(_translate("MainWindow", "decrypt"))
        self.push_button_3.setText(_translate("MainWindow", "quit"))
        self.push_button_1.clicked.connect(self.on_push_button_1_clicked)
        self.push_button_2.clicked.connect(self.on_push_button_2_clicked)
        self.push_button_3.clicked.connect(self.on_push_button_3_clicked)

    def on_push_button_1_clicked(self):
        if str(self.input_text.toPlainText()) and len(str(self.key_text.toPlainText())) == 16:
            key = AES.PrpCrypt(str(self.key_text.toPlainText()))  # 初始化密钥
            e = key.encrypt(str(self.input_text.toPlainText()))  # 加密
            self.encrypted_text.setPlainText(bytes.decode(e))  # 字节码e转utf-8
            print('encrypted!')
        elif len(str(self.key_text.toPlainText())) == 16:
            QtWidgets.QMessageBox.warning(self, "Warning!", 'Please input your text to encrypt!')
        elif str(self.key_text.toPlainText()) and str(self.input_text.toPlainText()):
            QtWidgets.QMessageBox.warning(self, "Warning!", 'The key must be 16bits!')
        elif str(self.input_text.toPlainText()):
            QtWidgets.QMessageBox.warning(self, "Warning!", 'Please enter your key!')
        else:
            QtWidgets.QMessageBox.warning(self, "Warning!", 'Please check the input_text and the key!')

    def on_push_button_2_clicked(self):
        if len(str(self.encrypted_text.toPlainText())) % 32 == 0 and len(str(self.key_text.toPlainText())) == 16:
            key = AES.PrpCrypt(str(self.key_text.toPlainText()))
            try:
                d = key.decrypt(str(self.encrypted_text.toPlainText()))  # 解码
            except Exception as e:
                print(e)
                QtWidgets.QMessageBox.warning(self, "Warning!", 'Appcrash happened! Please check the encrypted and key')
                # try语句转为异常处理防止程序崩溃
            else:
                self.decrypted_text.setPlainText(d)
        else:
            QtWidgets.QMessageBox.warning(self, "Warning!", 'Incorrect key or encrypted text!')

    def on_push_button_3_clicked(self):
        sys.exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UiMainWindow()
    window.show()
    sys.exit(app.exec_())
