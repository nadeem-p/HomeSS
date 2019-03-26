from django.shortcuts import render
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
db = firebase.database()
# Create your views here.
def home(request):

    idToken  = request.session['uid']
    user = authentication.get_account_info(idToken)
    userid = user['users'][0]['localId']
    data = db.child("users").child(userid).child("CurrentDetails").get()
    return render(request, 'dashboard.html', data)

def profile(request):
    # need to add context dictionary for user data
    
    return render(request, 'profile.html', )