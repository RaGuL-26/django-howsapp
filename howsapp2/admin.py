from django.contrib import admin

# Register your models here.
from .models import RoomMessage,Rooms

admin.site.register(Rooms)
admin.site.register(RoomMessage)