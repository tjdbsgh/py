import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("secret.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://bssm-2c27e-default-rtdb.firebaseio.com/'
})

# Import database module.
from firebase_admin import db

# Get a database reference to our posts
ref = db.reference()
ref.update({"hi":1234})
ref = db.reference('1')
print(ref.get())