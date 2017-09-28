import os
import cv2
import numpy as np
from PIL import Image

def tranning():
    recognizer=cv2.createLBPHFaceRecognizer()
    path='dataSet'
    Ids,faces=getImageWithId(path)
    recognizer.train(faces,np.array(Ids))
    recognizer.save('recognizer/trainnindData.yml')
    cv2.destroyAllWindows()

def getImageWithId(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    IDs=[]
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L')
        faceNp=np.array(faceImg,'uint8')
        ID=int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        IDs.append(ID)
        cv2.imshow("Training",faceNp)
        cv2.waitKey(10)
    return IDs, faces




