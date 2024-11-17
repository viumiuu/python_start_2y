# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(332, 398)
        font = QtGui.QFont()
        font.setPointSize(13)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_generete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_generete.setGeometry(QtCore.QRect(110, 240, 80, 22))
        self.btn_generete.setStyleSheet("background-color: #af0cf5;\n"
"border: 2px solid black")
        self.btn_generete.setObjectName("btn_generete")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(60, 90, 195, 25))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(60, 140, 169, 23))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.result.setFont(font)
        self.result.setObjectName("result")
        self.cb_numbers = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_numbers.setGeometry(QtCore.QRect(60, 180, 159, 20))
        self.cb_numbers.setObjectName("cb_numbers")
        self.cb_alphabet = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_alphabet.setGeometry(QtCore.QRect(60, 200, 171, 20))
        self.cb_alphabet.setObjectName("cb_alphabet")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 332, 24))
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
        self.btn_generete.setText(_translate("MainWindow", "Згенерувати"))
        self.title.setText(_translate("MainWindow", "Генератор паролів"))
        self.result.setText(_translate("MainWindow", "Тут буде результат"))
        self.cb_numbers.setText(_translate("MainWindow", "Використовувати число"))
        self.cb_alphabet.setText(_translate("MainWindow", "Використовувати алфавіт"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())