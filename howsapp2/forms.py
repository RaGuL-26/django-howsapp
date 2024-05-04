from django import forms

from .models import Rooms

class Createroom(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = ['name_of_room','slug']
