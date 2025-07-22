import pyrebase
import firebase_admin
from firebase_admin import credentials, firestore
import streamlit as st

# Pyrebase config (public)
firebase_config = {
    "apiKey": "AIzaSyDFUhDzELGpZcZRCnK_pYAh7J4z5rgrGRU",
    "authDomain": "sports-2f624.firebaseapp.com",
    "databaseURL": "https://sports-2f624.firebaseio.com",
    "projectId": "sports-2f624",
    "storageBucket": "sports-2f624.appspot.com",
    "messagingSenderId": "427346095578",
    "appId": "1:427346095578:web:8bb4e91405b733b292a4e3"
}
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

# Firebase Admin (for Firestore)
service_account_info = st.secrets["firebase"]  # matches [firebase] in TOML
cred = credentials.Certificate(dict(service_account_info))
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        "projectId": service_account_info["project_id"]
    })
db = firestore.client()
