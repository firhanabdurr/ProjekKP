import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://faceattendancerealtime-a0586-default-rtdb.firebaseio.com/'
})

ref = db.reference('Students')

data = {
    "146":
        {
            "name": "Agni Khoirunnisa",
            "class": "6",
            "total_attendance": 1,
            "last_attendance_time": "2024-01-20 00:54:34"
        },
    "147":
        {
            "name": "Atysha Fitria",
            "class": "6",
            "total_attendance": 1,
            "last_attendance_time": "2024-01-20 00:54:34"
        },
    "148":
        {
            "name": "Fauzan Indra Nuh ",
            "class": "6",
            "total_attendance": 1,
            "last_attendance_time": "2024-01-20 00:54:34"
        },
    "149":
        {
            "name": "Hopipah Zahrani",
            "class": "6",
            "total_attendance": 1,
            "last_attendance_time": "2024-01-20 00:54:34"
        },
    "150":
        {
            "name": "Keyra Sekar Febriyani",
            "class": "6",
            "total_attendance": 1,
            "last_attendance_time": "2024-01-20 00:54:34"
        },
    "151":
        {
            "name": "M Azka Pratama",
            "class": "6",
            "total_attendance": 1,
            "last_attendance_time": "2024-01-20 00:54:34"
        },
    "152":
        {
            "name": "Nazla Aini",
            "class": "6",
            "total_attendance": 1,
            "last_attendance_time": "2024-01-20 00:54:34"
        },
    "153":
        {
            "name": "Nasrulloh Rival Petran",
            "class": "6",
            "total_attendance": 1,
            "last_attendance_time": "2024-01-20 00:54:34"
        },
    "154":
        {
            "name": "Safa Dwi Febriani",
            "class": "6",
            "total_attendance": 1,
            "last_attendance_time": "2024-01-20 00:54:34"
        },
    "155":
        {
            "name": "Shakila Indriyani",
            "class": "6",
            "total_attendance": 1,
            "last_attendance_time": "2024-01-20 00:54:34"
        },
    "156":
        {
            "name": "Yusuf Ahmad Fauzi",
            "class": "6",
            "total_attendance": 1,
            "last_attendance_time": "2024-01-20 00:54:34"
        },
    "157":
        {
            "name": "Safitri Sabilillah R",
            "class": "6",
            "total_attendance": 1,
            "last_attendance_time": "2024-01-20 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)