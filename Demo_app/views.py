from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,DeleteView,UpdateView,FormView
from django.views.generic.list import ListView
from .models import *
from django.urls import reverse_lazy
# Create your views here.

def home (request):
    return render(request,'Demo_app/home.html',{})

def landingpage (request):
    return render(request,'Demo_app/landingpage.html',{})

def roadmap(request):
    return render(request,'Demo_app/roadmap.html',{})

class AddComment(CreateView):
    model = Comment
    fields = ('title', 'message')
    template_name = 'Demo_app/addcomment.html'
    success_url = reverse_lazy('Demo_app:home')

class commentview(ListView):
    model = Comment
    template_name = 'Demo_app/comments.html'
    context_object_name = 'comment_list'
    
    