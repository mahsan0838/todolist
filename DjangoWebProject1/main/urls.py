
           ################# MAIN ###################



from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

urlpatterns = [
   # path('admin/', admin.site.urls),
    path("<int:id>", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
    
    
    ]
