import os
import pickle

import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('Resources/background.png')

#import image mode to list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

#print((len(imgModeList)))

# Load encoding file
print('Loading encode file ...')
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
print(studentIds)
print('Encode file complete ...')
while True:
    success, img = cap.read()


while True:
    success, img = cap.read()

    imgBackground[162:162+480, 55:55+640] = img
    imgBackground[44:44+633, 808:808+414] = imgModeList[0]

    cv2.imshow("Face Attendance", img)
    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)