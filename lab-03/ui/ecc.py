# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\ecc.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(892, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tieuDe = QtWidgets.QLabel(self.centralwidget)
        self.tieuDe.setGeometry(QtCore.QRect(170, 20, 298, 58))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.tieuDe.setFont(font)
        self.tieuDe.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.tieuDe.setObjectName("tieuDe")
        self.information = QtWidgets.QLabel(self.centralwidget)
        self.information.setGeometry(QtCore.QRect(40, 120, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.information.setFont(font)
        self.information.setObjectName("information")
        self.signature = QtWidgets.QLabel(self.centralwidget)
        self.signature.setGeometry(QtCore.QRect(40, 240, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.signature.setFont(font)
        self.signature.setObjectName("signature")
        self.bt_generate = QtWidgets.QPushButton(self.centralwidget)
        self.bt_generate.setGeometry(QtCore.QRect(580, 60, 131, 32))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.bt_generate.setFont(font)
        self.bt_generate.setObjectName("bt_generate")
        self.bt_sign = QtWidgets.QPushButton(self.centralwidget)
        self.bt_sign.setGeometry(QtCore.QRect(220, 370, 113, 32))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.bt_sign.setFont(font)
        self.bt_sign.setObjectName("bt_sign")
        self.bt_verify = QtWidgets.QPushButton(self.centralwidget)
        self.bt_verify.setGeometry(QtCore.QRect(520, 370, 113, 32))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.bt_verify.setFont(font)
        self.bt_verify.setObjectName("bt_verify")
        self.txt_information = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_information.setGeometry(QtCore.QRect(170, 110, 541, 78))
        self.txt_information.setObjectName("txt_information")
        self.txt_signature = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_signature.setGeometry(QtCore.QRect(170, 220, 541, 78))
        self.txt_signature.setObjectName("txt_signature")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 892, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tieuDe.setText(_translate("MainWindow", "ECC CIPHER"))
        self.information.setText(_translate("MainWindow", "Information"))
        self.signature.setText(_translate("MainWindow", "Signature"))
        self.bt_generate.setText(_translate("MainWindow", "Generate Keys"))
        self.bt_sign.setText(_translate("MainWindow", "Sign"))
        self.bt_verify.setText(_translate("MainWindow", "Verify"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
