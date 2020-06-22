from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Users
from datetime import datetime


def index(request):
    
    return render(request,'users/index.html')


def register(request):
    response = ''
    response = Users.objects.registration_validation(request.POST)

    if response ["status"]:
        request.session['user_id'] = response['user_id']
        return redirect('/wishlist/dashboard', messages)
    else:
        for error in response['errors']:
            messages.error(request, error)
        return redirect ('/')
   

    
def login(request):
    response = ''
    response = Users.objects.User_login(request.POST)

    if response["status"]:
        request.session['user_id'] = response['user_id']
        return redirect('/wishlist/dashboard', messages)
    else:
        for error in response['errors']:
            messages.error(request, error)
            return redirect ('/')
    return redirect('/wishlist/dashboard')

def logout(request):
    request.session.clear()
    return redirect('/')


