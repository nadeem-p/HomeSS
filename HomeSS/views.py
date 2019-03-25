from django.shortcuts import render
from django.contrib import auth
import pyrebase

config = {
    'apiKey': "AIzaSyAWjK69Bjgu89j4T1L-UnFc7f5XZUgzxxE",
    'authDomain': "homess.firebaseapp.com",
    'databaseURL': "https://homess.firebaseio.com",
    'projectId': "homess",
    'storageBucket': "homess.appspot.com",
    'messagingSenderId': "623277496566"
}

firebase = pyrebase.initialize_app(config)
authentication = firebase.auth()

def signIn(request):
    return render(request, 'signIn.html')

def postsignIn(request):

    email = request.POST.get('email')
    pwd = request.POST.get('password')
    try:
        user = authentication.sign_in_with_email_and_password(email, pwd)
    except:
        msg = 'Invalid credentials!'
        return render(request, 'signIn.html', {"msg":msg})
    
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, 'welcome.html', {"email":email})

def postsignup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    pwd = request.POST.get('password')
    contact = request.POST.get('contact')

def logout(request):
    auth.logout(request)
    return render(request, 'signIn.html')