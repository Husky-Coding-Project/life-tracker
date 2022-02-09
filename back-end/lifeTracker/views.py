from django.shortcuts import render
import pyrebase

config = {
    "apiKey": "AIzaSyAH04XvLgIE7r3KCho7rUU9dzGep2j9zkM",
    "authDomain": "lifetracker-3ae8c.firebaseapp.com",
    "projectId": "lifetracker-3ae8c",
    "storageBucket": "lifetracker-3ae8c.appspot.com",
    "messagingSenderId": "58044515519",
    "appId": "1:58044515519:web:a912b3668ce5b05b63720a",
    "measurementId": "G-Y8FTLG1LEX"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

def signIn(request):
    return render(request, "signIn.html")