from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login,logout
from django.shortcuts import render, get_object_or_404
from . import models
from django.http import JsonResponse
from .models import Rooms, RoomMessage
from .forms import Createroom
from django.contrib.admin.views.decorators import staff_member_required



# Create your views here.
def home_page(request):
    return render(request,'index.html')

#sign-up page rendering

def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'SuccessFully Registered')
            return redirect('home_page')
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form': form})

def signin_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            login(request,form.get_user())
            messages.success(request,'LoggedIn Successfully')
            return redirect('home_page')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

def logout_page(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request,'LoggedOut SuccessFully')
    return redirect('home_page')

def rooms(request):
    rooms_list = Rooms.objects.all()
    return render(request, "success.html", {"rooms_list": rooms_list})

def room(request, slug):
    room = Rooms.objects.get(slug = slug)
    messages = RoomMessage.objects.filter(room=room)
    return render(request, "slugs.html", {"room": room, "slug": slug, "messages": messages})

def create_room(request):
    if request.method == 'POST':
        form = Createroom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = Createroom()
    return render(request, 'addgroup.html',{'form':form})


@staff_member_required
def room_delete(request,id):
    room = get_object_or_404(Rooms, id=id)
    if request.method == 'POST':
        room.delete()
        return redirect('viewpostpage')  # Redirect to the room list page after deletion
    return render(request, 'room_confirm_delete.html', {'room': room})



        


