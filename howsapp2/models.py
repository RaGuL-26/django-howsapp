from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Rooms(models.Model):
    name_of_room = models.CharField(max_length=50)
    slug = models.SlugField(max_length=40)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name_of_room
    
class RoomMessage(models.Model):
    content = models.TextField()
    Author = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Rooms,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Author.username
    
    
    