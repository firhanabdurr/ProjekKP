import os
import pickle
import cvzone
import cv2
import face_recognition
import numpy as np

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

    if not success:
        print("Error: Unable to read a frame from the webcam.")
        break  # Break the loop if reading fails

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    # print("Image dimensions:", img.shape)

    faceCurframe = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurframe)

    imgBackground[162:162 + 480, 55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[0]

    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurframe):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.compare_faces(encodeListKnown, encodeFace)
        # print("matches", matches)
        # print("faceDis", faceDis)

        matchIndex = np.argmin(faceDis)
        # print("Match Index", matchIndex)

        if matches[matchIndex]:
            # print("Known face detected")
            # print(studentIds[matchIndex])
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            bbox = 55 + x1, 162 + y1, x2-x1, y2 - y1
            imgBackground = cvzone.cornerRect(imgBackground,bbox,rt=0)

    cv2.imshow("Face Attendance", img)
    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)