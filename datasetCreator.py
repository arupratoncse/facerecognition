import cv2
import sqlite3
import numpy as np
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)

def insertOrUpdate(Id,Name,Age,Gender,Cr):
    con=sqlite3.connect("Face.db")
    sql="SELECT * FROM people WHERE id="+str(Id)
    data=con.execute(sql)
    isExitData=0
    for row in data:
        isExitData=1
    if(isExitData==1):
        sql="UPDATE people SET name="+str(Name)+",age="+str(Age)+",gender="+str(Gender)+",ciminalRecord="+str(Cr)+" WHERE id="+str(Id)
    else:
        sql="INSERT INTO people(id,name,age,gender,ciminalRecord) Values("+str(Id)+","+str(Name)+","+str(Age)+","+str(Gender)+","+str(Cr)+")"
    con.execute(sql)
    con.commit()
    con.close()


def createDataSet(id,name,age,gender,cr):
    name='"'+str(name)+'"'
    gender='"'+str(gender)+'"'
    cr='"'+str(cr)+'"'
    insertOrUpdate(id,name,age,gender,cr)
    sampleNum=0
    while(True):
        ret,img=cam.read()
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces:
            sampleNum=sampleNum+1
            cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
            cv2.waitKey(50)
        cv2.imshow("Face Detection",img)
        cv2.waitKey(1)
        if(sampleNum>20):
            #cam.release()
            cv2.destroyAllWindows()
            break
