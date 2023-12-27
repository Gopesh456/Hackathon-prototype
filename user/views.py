from django.shortcuts import render , redirect
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def loginPage(req):

    if req.user.is_authenticated:
        return redirect('/questions')
    if req.method == 'POST':
        username = req.POST['user-name']
        password = req.POST['password']
        try:
            user = User.objects.get(username = username)
            # print('username exists')
        except:
            print(req,'Username does not exist')
        user = authenticate(req, username = username, password = password)

        if user is not None:
            login(req, user)
            return redirect('/questions')
        else:
            messages.error(req,"Username or Password is Incorrect")
    return render(req,'user/index.html')


def logoutUser(req):
    logout(req)
    return redirect('/login/')