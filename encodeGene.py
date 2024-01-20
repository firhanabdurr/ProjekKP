import cv2
import os
import face_recognition
import  pickle
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from  firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://faceattendancerealtime-a0586-default-rtdb.firebaseio.com/',
    'storageBucket': 'faceattendancerealtime-a0586.appspot.com'
})

#import face images
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

print(path)
print(os.path.splitext(path)[0])
print(studentIds)
print(len(imgList))

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList
# def findEncodings(imagesList):
#     encodeList = []
#     for img in imagesList:
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         face_encodings = face_recognition.face_encodings(img)
#
#         # Check if any face was found in the image
#         if len(face_encodings) > 0:
#             encode = face_encodings[0]
#             encodeList.append(encode)
#         else:
#             print("No face found in one or more images.")
#
#     return encodeList

encodListKnown = findEncodings(imgList)


print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
# print(encodeListKnown)
print("Encoding Ended ...")
#
file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")

