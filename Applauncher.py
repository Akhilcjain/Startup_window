# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Applauncher.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Applauncher(object):
    def arduino_click(self):
    	os.system("arduino")
    def music_click(self):
    	os.system("arduino")
    def pycharm_click(self):
    	os.system("pycharm")
    def qt_click(self):
    	os.system("/usr/lib/x86_64-linux-gnu/qt5/bin/designer")
    def videos_click(self):
    	os.system("cd Videos")
    def eclipse_click(self):
    	os.system("arduino")
    def setupUi(self, Applauncher):
        Applauncher.setObjectName(_fromUtf8("Applauncher"))
        Applauncher.resize(184, 361)
        Applauncher.setStyleSheet(_fromUtf8("QFrame#frame{\n"
"border: 3px solid #ffffff;\n"
"background-color: rgb(60,60,60);\n"
"}\n"
"QDialog{\n"
"background-color: rgb(60,60,60);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(87,87,87);\n"
"border-radius:5px;\n"
"color:#ffffff;\n"
"background-image: URL(\"arduino.jpeg\");\n"
"text-align:right;\n"
"padding-right:10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 85, 0);\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(103,103,103);\n"
"}\n"
"QLabel{\n"
"color:#ffffff;\n"
"}"))
        self.frame = QtGui.QFrame(Applauncher)
        self.frame.setGeometry(QtCore.QRect(10, 20, 161, 331))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.arduino_btn = QtGui.QPushButton(self.frame)
        self.arduino_btn.setGeometry(QtCore.QRect(20, 20, 131, 41))
        self.arduino_btn.setObjectName(_fromUtf8("arduino_btn"))
        self.arduino_btn.clicked.connect(self.arduino_click)
        self.music_btn = QtGui.QPushButton(self.frame)
        self.music_btn.setGeometry(QtCore.QRect(20, 170, 131, 41))
        self.music_btn.setObjectName(_fromUtf8("music_btn"))
        self.music_btn.clicked.connect(self.music_click)
        self.pycharm_btn = QtGui.QPushButton(self.frame)
        self.pycharm_btn.setGeometry(QtCore.QRect(20, 120, 131, 41))
        self.pycharm_btn.setObjectName(_fromUtf8("pycharm_btn"))
        self.pycharm_btn.clicked.connect(self.pycharm_click)
        self.eclipse_btn = QtGui.QPushButton(self.frame)
        self.eclipse_btn.setGeometry(QtCore.QRect(20, 70, 131, 41))
        self.eclipse_btn.setObjectName(_fromUtf8("eclipse_btn"))
        self.eclipse_btn.clicked.connect(self.eclipse_click)
        self.videos_btn = QtGui.QPushButton(self.frame)
        self.videos_btn.setGeometry(QtCore.QRect(20, 270, 131, 41))
        self.videos_btn.setObjectName(_fromUtf8("videos_btn"))
        self.videos_btn.clicked.connect(self.videos_click)
        self.qt_btn = QtGui.QPushButton(self.frame)
        self.qt_btn.setGeometry(QtCore.QRect(20, 220, 131, 41))
        self.qt_btn.setObjectName(_fromUtf8("qt_btn"))
        self.qt_btn.clicked.connect(self.qt_click)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 20, 31, 31))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/Arduino/arduino.jpeg")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 25, 31, 31))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/Arduino/arduino_edited.jpg")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 75, 31, 31))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/Eclipse/eclipse_editted.jpeg")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 175, 31, 31))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8(":/Music/music2_uneditted.jpg")))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(40, 125, 31, 31))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8(":/Pycharm/pycharm_editted.jpg")))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(40, 225, 31, 31))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8(":/QTDesigner/pyqt2_edited.png")))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(40, 275, 31, 31))
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setPixmap(QtGui.QPixmap(_fromUtf8(":/Videos/videos_edited.jpg")))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.retranslateUi(Applauncher)
        QtCore.QMetaObject.connectSlotsByName(Applauncher)

    def retranslateUi(self, Applauncher):
        Applauncher.setWindowTitle(_translate("Applauncher", "Applauncher", None))
        self.arduino_btn.setText(_translate("Applauncher", "Arduino", None))
        self.music_btn.setText(_translate("Applauncher", "Music", None))
        self.pycharm_btn.setText(_translate("Applauncher", "PyCharm", None))
        self.eclipse_btn.setText(_translate("Applauncher", "Eclipse", None))
        self.videos_btn.setText(_translate("Applauncher", "Videos", None))
        self.qt_btn.setText(_translate("Applauncher", "QT", None))

import images

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Applauncher = QtGui.QDialog()
    ui = Ui_Applauncher()
    ui.setupUi(Applauncher)
    Applauncher.show()
    sys.exit(app.exec_())

