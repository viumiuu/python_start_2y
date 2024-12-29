# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(591, 552)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.video = QVideoWidget(self.centralwidget)
        self.video.setGeometry(QtCore.QRect(320, 170, 231, 221))
        self.video.setObjectName("video")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.video)
        self.verticalLayout.setObjectName("verticalLayout")
        self.calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar.setGeometry(QtCore.QRect(10, 10, 291, 251))
        self.calendar.setGridVisible(True)
        self.calendar.setNavigationBarVisible(False)
        self.calendar.setDateEditEnabled(True)
        self.calendar.setObjectName("calendar")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(320, 30, 151, 41))
        self.start.setObjectName("start")
        self.autostart = QtWidgets.QCheckBox(self.centralwidget)
        self.autostart.setGeometry(QtCore.QRect(330, 120, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.autostart.setFont(font)
        self.autostart.setObjectName("autostart")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(320, 80, 151, 41))
        self.stop.setObjectName("stop")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.autostart.setText(_translate("MainWindow", "Автостарт"))
        self.stop.setText(_translate("MainWindow", "Stop"))
from PyQt5.QtMultimediaWidgets import QVideoWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())