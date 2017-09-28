# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sat May 20 11:43:10 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from user import Ui_UserInfo
from trainner import tranning
import cv2
import numpy as np
import sqlite3
from profile import getProfile
import datetime


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

class Ui_MainWindow(object):
    def recog(self):
        faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        cam=cv2.VideoCapture(0)
        rec=cv2.createLBPHFaceRecognizer()
        rec.load("recognizer\\trainnindData.yml")
        font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_PLAIN,2,.5,1,1,1)
        temp=0
        while(True):
            ret,img=cam.read()
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=faceDetect.detectMultiScale(gray,1.3,5)
            for(x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                id,conf=rec.predict(gray[y:y+h,x:x+w])
                profile=getProfile(id)
                if(profile!=None):
                    cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[1]),(x,y-10),font,(255,0,0))
                    now=datetime.datetime.now()
                    now=now.strftime("%Y-%m-%d %H:%M:%S")
                    if(temp==0):
                        start=now
                        temp=1
                    self.user_history.setText("Name: "+str(profile[1])+"\nAge: "+str(profile[2])+"\nGender: "+str(profile[3])+"\nCriminal Record: "+str(profile[4])+"\nStart: "+str(start)+"\nLast: "+str(now))
            cv2.imshow("Face Recognition",img)
            if(cv2.waitKey(1)==ord('q')):
                break
        cam.release()
        cv2.destroyAllWindows()
        
    def train(self):
        tranning()
        msg=QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Warning)
        msg.setWindowTitle("Success")
        msg.setText("Tranning Successful")
        msg.setStandardButtons(QtGui.QMessageBox.Ok)
        msg.exec_() 
        
    def user(self):
        self.form=QtGui.QDialog()
        self.ui=Ui_UserInfo()
        self.ui.setupUi(self.form)
        self.form.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(678, 452)
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.user_history = QtGui.QTextBrowser(self.centralwidget)
        self.user_history.setGeometry(QtCore.QRect(380, 80, 256, 341))
        self.user_history.setObjectName(_fromUtf8("user_history"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 10, 281, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 60, 111, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.data_btn = QtGui.QPushButton(self.centralwidget)
        self.data_btn.setGeometry(QtCore.QRect(130, 150, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.data_btn.setFont(font)
        self.data_btn.setObjectName(_fromUtf8("data_btn"))
        ########Create Data Set Connection#######
        self.data_btn.clicked.connect(self.user)
        ########End Data Set Connector##########
        self.train_btn = QtGui.QPushButton(self.centralwidget)
        self.train_btn.setGeometry(QtCore.QRect(130, 200, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.train_btn.setFont(font)
        self.train_btn.setObjectName(_fromUtf8("train_btn"))
        self.train_btn.clicked.connect(self.train)#ujjjjj
        self.recog_btn = QtGui.QPushButton(self.centralwidget)
        self.recog_btn.setGeometry(QtCore.QRect(130, 252, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.recog_btn.setFont(font)
        self.recog_btn.setObjectName(_fromUtf8("recog_btn"))
        self.recog_btn.clicked.connect(self.recog)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 430, 201, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Face Recognizer", None))
        self.label.setText(_translate("MainWindow", "Face Recognition", None))
        self.label_2.setText(_translate("MainWindow", "History of Visitor", None))
        self.data_btn.setText(_translate("MainWindow", "Create Dataset", None))
        self.train_btn.setText(_translate("MainWindow", "Trainning", None))
        self.recog_btn.setText(_translate("MainWindow", "Recognition", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">©Copyright 2017, Md. Raton Alli</span></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

