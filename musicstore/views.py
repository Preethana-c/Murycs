from django.shortcuts import render,redirect
from django import forms
from django.http import HttpResponse
from .forms import ListViewForm
from django.http import HttpRequest
from .forms import NewUserForm
from django.contrib.auth import login, logout, authenticate #add this

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
import http.client
import json

# Create your views here.

def home_view(request):
    print("Home view")
    return render(request,"home.html")


def index_view(request):

    if 'Artist' in request.POST:
        Artist=request.POST['Artist']
    else:
        Artist='Billie eilish'

    form = ListViewForm()
    form.name = Artist
    res_dict=form.connect_genius()
    hits = res_dict['response']['hits']

    songlist = []
    for  i in range(len(hits)):
        data = {
            'header_image_url' : hits[i]['result']['header_image_url'],
            'full_title' : hits[i]['result']['full_title'],
            'artist_name' : hits[i]['result']['artist_names'],
            'release_date' : hits[i]['result']['release_date_for_display'],
            'path' : hits[i]['result']['path'],
            'url':hits[i]['result']['url'],
        }
        songlist.append(data)

    #print(songlist)
    context={'songlist':songlist,'Artist':Artist}
    return render(request,"Index.html",context)

def register_request(request):
    print("In register_request with request method " + request.method)
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            print("valid form")
            user = form.save()
            login(request, user)
            print("Registration successful." )
            messages.success(request, "Registration successful." )
            return redirect("index")
        else:
            print("form is not valid")
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
    print("Login request")
    print(request.method)
    if request.method == "POST":
        print("In side post")
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print("form valid")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                print(username)
                return redirect("index")
            else:
                print("invalid user")
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
            print("invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
    print("logout request from user")
    print(request.user)
    #logout(request, request.user)
    return redirect("home.html")


