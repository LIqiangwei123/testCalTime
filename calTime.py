# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calTime.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(61, 24, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 551, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 130, 581, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.filepath = QtWidgets.QTextEdit(self.centralwidget)
        self.filepath.setGeometry(QtCore.QRect(30, 250, 721, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.filepath.setFont(font)
        self.filepath.setObjectName("filepath")
        self.cal = QtWidgets.QPushButton(self.centralwidget)
        self.cal.setGeometry(QtCore.QRect(30, 390, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.cal.setFont(font)
        self.cal.setObjectName("cal")
        self.getTime1 = QtWidgets.QTextEdit(self.centralwidget)
        self.getTime1.setGeometry(QtCore.QRect(450, 320, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.getTime1.setFont(font)
        self.getTime1.setObjectName("getTime1")
        self.getTime2 = QtWidgets.QTextEdit(self.centralwidget)
        self.getTime2.setGeometry(QtCore.QRect(450, 420, 311, 87))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.getTime2.setFont(font)
        self.getTime2.setObjectName("getTime2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 335, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 430, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menucalculateTime = QtWidgets.QMenu(self.menubar)
        self.menucalculateTime.setObjectName("menucalculateTime")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menucalculateTime.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "计算时间并导出excel"))
        self.label_2.setText(_translate("MainWindow", "支持的音频格式有：mp3, m4a, wav"))
        self.label_3.setText(_translate("MainWindow", "支持的视频格式有：mp4, mov, avi"))
        self.filepath.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">请输入音频所在文件夹的绝对路径，如：D:\\《朝花夕拾》\\\\</span></p></body></html>"))
        self.cal.setText(_translate("MainWindow", "计算时间"))
        self.getTime1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt;\">0</span></p></body></html>"))
        self.getTime2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt;\">0:00:00</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "总时间（秒）"))
        self.label_5.setText(_translate("MainWindow", "总时间（换算后）"))
        self.menucalculateTime.setTitle(_translate("MainWindow", "calculateTime\\"))

