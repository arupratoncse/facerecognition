# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userinfo.ui'
#
# Created: Sun May 21 11:56:37 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import cv2
import sqlite3
import numpy as np
from datasetCreator import createDataSet
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


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

class Ui_UserInfo(object):
    def createData(self):
        self.id=self.id_line.text()
        self.name=self.name_line.text()
        self.age=self.age_line.text()
        self.gender=self.gender_line.text()
        self.cr=self.cr_line.text()
        createDataSet(self.id,self.name,self.age,self.gender,self.cr)
        
        #UserInfo.accept()
        
    def setupUi(self, UserInfo):
        UserInfo.setObjectName(_fromUtf8("UserInfo"))
        UserInfo.resize(308, 233)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../GUI/Face Recognition SqLite/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UserInfo.setWindowIcon(icon)
        self.label = QtGui.QLabel(UserInfo)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(71, 30, 20, 20))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setFrameShadow(QtGui.QFrame.Plain)
        self.label.setLineWidth(1)
        self.label.setMidLineWidth(0)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.id_line = QtGui.QLineEdit(UserInfo)
        self.id_line.setGeometry(QtCore.QRect(100, 30, 113, 20))
        self.id_line.setObjectName(_fromUtf8("id_line"))
        self.label_2 = QtGui.QLabel(UserInfo)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(19, 60, 71, 20))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtGui.QFrame.Plain)
        self.label_2.setLineWidth(1)
        self.label_2.setMidLineWidth(0)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(UserInfo)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(29, 90, 61, 20))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_3.setFrameShadow(QtGui.QFrame.Plain)
        self.label_3.setLineWidth(1)
        self.label_3.setMidLineWidth(0)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(UserInfo)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(29, 120, 61, 21))
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_4.setFrameShadow(QtGui.QFrame.Plain)
        self.label_4.setLineWidth(1)
        self.label_4.setMidLineWidth(0)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(UserInfo)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(9, 150, 81, 21))
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_5.setFrameShadow(QtGui.QFrame.Plain)
        self.label_5.setLineWidth(1)
        self.label_5.setMidLineWidth(0)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.name_line = QtGui.QLineEdit(UserInfo)
        self.name_line.setGeometry(QtCore.QRect(100, 60, 113, 20))
        self.name_line.setObjectName(_fromUtf8("name_line"))
        self.age_line = QtGui.QLineEdit(UserInfo)
        self.age_line.setGeometry(QtCore.QRect(100, 90, 113, 20))
        self.age_line.setObjectName(_fromUtf8("age_line"))
        self.gender_line = QtGui.QLineEdit(UserInfo)
        self.gender_line.setGeometry(QtCore.QRect(100, 120, 113, 20))
        self.gender_line.setObjectName(_fromUtf8("gender_line"))
        self.cr_line = QtGui.QLineEdit(UserInfo)
        self.cr_line.setGeometry(QtCore.QRect(100, 150, 113, 20))
        self.cr_line.setObjectName(_fromUtf8("cr_line"))
        self.ok_btn = QtGui.QPushButton(UserInfo)
        self.ok_btn.setGeometry(QtCore.QRect(100, 190, 71, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ok_btn.setFont(font)
        self.ok_btn.setObjectName(_fromUtf8("ok_btn"))
        self.ok_btn.clicked.connect(self.createData)##click
        self.cencel_btn = QtGui.QPushButton(UserInfo)
        self.cencel_btn.setGeometry(QtCore.QRect(180, 190, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cencel_btn.setFont(font)
        self.cencel_btn.setObjectName(_fromUtf8("cencel_btn"))

        self.retranslateUi(UserInfo)
        QtCore.QObject.connect(self.cencel_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), UserInfo.close)
        QtCore.QMetaObject.connectSlotsByName(UserInfo)

    def retranslateUi(self, UserInfo):
        UserInfo.setWindowTitle(_translate("UserInfo", "User Information", None))
        self.label.setText(_translate("UserInfo", "ID", None))
        self.label_2.setText(_translate("UserInfo", "Name", None))
        self.label_3.setText(_translate("UserInfo", "Age", None))
        self.label_4.setText(_translate("UserInfo", "Gender", None))
        self.label_5.setText(_translate("UserInfo", "Criminal Record", None))
        self.ok_btn.setText(_translate("UserInfo", "Ok", None))
        self.cencel_btn.setText(_translate("UserInfo", "Cancel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    UserInfo = QtGui.QDialog()
    ui = Ui_UserInfo()
    ui.setupUi(UserInfo)
    UserInfo.show()
    sys.exit(app.exec_())

