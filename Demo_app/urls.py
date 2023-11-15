from django.urls import path 
from .views import home
from . import views
app_name = 'Demo_app'

urlpatterns = [
    path('home/',views.home,name ='home'),
    path('',views.landingpage,name ='landingpage'),
    path('roadmap/',views.roadmap,name ='roadmap'),
]
