from django.shortcuts import render, redirect
from django.contrib import auth
from dashboard import views as d_views
import pyrebase
from django.contrib import messages

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
db = firebase.database()
storage = firebase.storage()

def signIn(request):
    return render(request, 'loginReg/signIn.html')

def postsignIn(request):

    email = request.POST.get('email')
    pwd = request.POST.get('password')

    try:
        user = authentication.sign_in_with_email_and_password(email, pwd)
    except:
        msg = 'Invalid credentials!'
        return render(request, 'loginReg/signIn.html', {"msg":msg})
    
    session_id = user['idToken']
    request.session['uid'] = str(session_id)


    return redirect('Dash-home')

def postsignup(request):

    name = request.POST.get('name')
    email = request.POST.get('email')
    pwd = request.POST.get('password')
    contact = request.POST.get('contact')
    user = authentication.create_user_with_email_and_password(email, pwd)
    uid = user["localId"]
    print(uid)
    data = {
        "Name": name,
        "Contact": contact
    }
    if request.method == 'POST' and request.FILES['profimage']:
        profimage = request.FILES['profimage']
        storage.child("users").child(uid).child(str(name.lower())+'.jpg').put(profimage)
    db.child("users").child(uid).child("details").set(data)
    messages.success(request, 'Registration Successful!')

    return render(request, 'loginReg/signIn.html')

def logout(request):
    auth.logout(request)
    return render(request, 'loginReg/signIn.html')