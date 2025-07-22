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
import streamlit as st
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate({
    "type": st.secrets.firebase.type,
    "project_id": st.secrets.firebase.project_id,
    "private_key_id": st.secrets.firebase.private_key_id,
    "private_key": st.secrets.firebase.private_key,
    "client_email": st.secrets.firebase.client_email,
    "client_id": st.secrets.firebase.client_id,
    "auth_uri": st.secrets.firebase.auth_uri,
    "token_uri": st.secrets.firebase.token_uri,
    "auth_provider_x509_cert_url": st.secrets.firebase.auth_provider_x509_cert_url,
    "client_x509_cert_url": st.secrets.firebase.client_x509_cert_url,
    "universe_domain": st.secrets.firebase.universe_domain,
})

firebase_admin.initialize_app(cred)

