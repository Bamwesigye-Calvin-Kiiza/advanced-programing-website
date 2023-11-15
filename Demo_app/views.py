from django.shortcuts import render,redirect

# Create your views here.

def home (request):
    return render(request,'Demo_app/home.html',{})

def landingpage (request):
    return render(request,'Demo_app/landingpage.html',{})

def roadmap(request):
    return render(request,'Demo_app/roadmap.html',{})