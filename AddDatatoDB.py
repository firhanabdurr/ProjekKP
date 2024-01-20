import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://faceattendancerealtime-a0586-default-rtdb.firebaseio.com/'
})

ref = db.reference('Students')

data = {
    "963852":
        {
            "name": "Elon Musk",
            "class": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2024-01-20 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)