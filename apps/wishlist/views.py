from django.shortcuts import render, HttpResponse, redirect
from ..wishlist.models import Users
from django.contrib import messages 
from .models import Item
from datetime import datetime

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    if 'user_id' in request.session:
        context = {
        'user': Users.objects.get(id = request.session['user_id']), 
        'items' : Item.objects.filter(other = request.session['user_id']),
        'other_items' : Item.objects.exclude(other = request.session['user_id']),
    }
    return render(request,'wishlist/dashboard.html', context) 

def create(request, item_id):
    if 'user_id' not in request.session:
        return redirect('/')
    Item.objects.createOther(request.session['user_id'], item_id)
    return redirect('/wishlist/dashboard')

def removeItem(request, item_id):
    if 'user_id' not in request.session:
        return redirect('/')
    Item.objects.removeItem(request.session['user_id'], item_id)
    return redirect('/wishlist/dashboard')

def delete(request, item_id):
    if 'user_id' not in request.session:
        return redirect('/')
    Item.objects.deleteItem(request.session['user_id'], item_id)
    return redirect('/wishlist/dashboard')

def show_item(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request,'wishlist/createItem.html')

def createItem(request):
    if 'user_id' not in request.session:
        return redirect('/')
    print('createitem views')
    response = Item.objects.createItem(request.POST, request.session['user_id'])
    if response['status']:
        return redirect('/wishlist/dashboard', messages)
    else:
        for error in response['errors']:
            messages.error(request,error)
    return redirect('/wishlist/show_item')
def results(request, item_id):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'items': Item.objects.get(id = item_id)
    }
    return render(request,'wishlist/results.html', context)




