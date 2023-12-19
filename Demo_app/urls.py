from django.urls import path 
from .views import home
from . import views
from .views import AddComment,commentview
app_name = 'Demo_app'

urlpatterns = [
    path('home/',views.home,name ='home'),
    path('',views.landingpage,name ='landingpage'),
    path('roadmap/',views.roadmap,name ='roadmap'),
    path('addcomment/',AddComment.as_view(),name='addcomment'),
    path('comments/',commentview.as_view(),name='comment'),
]
