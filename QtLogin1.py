# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtLogin1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(QtWidgets.QMainWindow):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(736, 456)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 40, 151, 81))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 41, 51))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 190, 72, 15))
        self.label_3.setMinimumSize(QtCore.QSize(0, 15))
        self.label_3.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(120, 240, 91, 19))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(220, 240, 91, 19))
        self.checkBox_2.setObjectName("checkBox_2")
        self.login = QtWidgets.QPushButton(Dialog)
        self.login.setGeometry(QtCore.QRect(120, 280, 151, 41))
        self.login.setObjectName("login")
        self.username = QtWidgets.QTextEdit(Dialog)
        self.username.setGeometry(QtCore.QRect(123, 126, 221, 31))
        self.username.setObjectName("username")
        self.password = QtWidgets.QTextEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(123, 186, 221, 31))
        self.password.setObjectName("password")
        self.exit = QtWidgets.QToolButton(Dialog)
        self.exit.setGeometry(QtCore.QRect(300, 280, 151, 41))
        self.exit.setObjectName("exit")

        self.retranslateUi(Dialog)
        self.login.clicked.connect(self.login_click)
        def login_click():
            print(self.username.toPlainText())

        self.exit.clicked.connect(self.exit.click)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "登录"))
        self.label_2.setText(_translate("Dialog", "用户"))
        self.label_3.setText(_translate("Dialog", "密码"))
        self.checkBox.setText(_translate("Dialog", "记住密码"))
        self.checkBox_2.setText(_translate("Dialog", "记住qq"))
        self.login.setText(_translate("Dialog", "登录"))
        self.exit.setText(_translate("Dialog", "取消"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Dialog()
    window.show()
    sys.exit(app.exec_())
