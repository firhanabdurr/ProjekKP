import os
import pickle
import numpy as np
import cv2
import face_recognition
import cvzone
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db
# from firebase_admin import storage
# from datetime import datetime

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

    faceCurframe = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurframe)

    imgBackground[162:162 + 480, 55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[0]

    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurframe):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print("matches",matches)

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            # coordinates bounding box doesn't appear
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            # Print coordinates
            print(f"Bounding Box Coordinates: y1={y1}, x2={x2}, y2={y2}, x1={x1}")
            bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
            imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0, colorR=(0, 255, 0), t=2)  # Draw bounding box

    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)
