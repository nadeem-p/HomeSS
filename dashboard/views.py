from django.shortcuts import render
import pyrebase
from django.contrib import auth

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


def home(request):

    idToken  = request.session['uid']
    user = authentication.get_account_info(idToken)
    userid = user['users'][0]['localId']
    print(userid)
    try:
        data = db.child("users").child(userid).child("CurrentReading").get()
        print(dict(data.val()))
        data = dict(data.val())
        data['status'] = 1
    except:
        data = {
            "status" : 0
        }
    print(request.get_full_path)
    return render(request, 'dashboard/dashboard.html', data)

def profile(request):
    idToken  = request.session['uid']
    user = authentication.get_account_info(idToken)
    userid = user['users'][0]['localId']
    print(user['users'])
    details_dict = db.child("users").child(userid).child("details").get()
    details_dict = dict(details_dict.val())
    name = details_dict['Name']
    storage.child("users").child(userid).child(name.lower()+'.jpg').download('../../static/dashboard/img/imgs/'+name+'.jpg')
    # need to add context dictionary for user data
    return render(request, 'dashboard/profile.html', {'name': name})

def uploadPics(request):
    idToken  = request.session['uid']
    user = authentication.get_account_info(idToken)
    userid = user['users'][0]['localId']
    if request.method == 'POST' and request.FILES['facialimgvid']:
        storage = firebase.storage()
        videoFile = request.FILES['facialimgvid']
        name = request.POST.get('personName')
        print(videoFile)
        db.child("users").child(userid).child("Known faces").set(name)
        storage.child(userid).child("videos").child(name+".mp4").put(videoFile)
        #do video slicing and get pictures.

        

    return render(request, 'dashboard/dashboard.html')

def logout(request):

    auth.logout(request)
    return render(request, 'signIn.html')