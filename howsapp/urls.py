"""
URL configuration for howsapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from howsapp2 import views as secondviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',secondviews.home_page,name='home_page'),
    path('signup',secondviews.signup_page,name='signup_page'),
    path('signin',secondviews.signin_page,name='signin_page'),
    path('logoutpage',secondviews.logout_page,name='logout_page'),
    path('addgroup/',secondviews.create_room,name='createroom'),
    path('viewpostpage',secondviews.rooms,name='viewpostpage'),
    path('chat/<slug:slug>/',secondviews.room,name='using_slug'),
    path('deletepost/<int:id>',secondviews.room_delete,name='delete_room'),
]

