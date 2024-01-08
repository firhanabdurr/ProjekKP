import cv2
import os
import face_recognition
import  pickle

#import face images
folderPath = 'Images'
modePathList = os.listdir(folderPath)
imgList = []
for path in modePathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
print(len(imgList))