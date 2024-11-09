from django import forms
from .models import *

class Tasksform(forms.ModelForm):
    class Meta:
        model = User
        fields = ("fullname","username","email","phone_number")
        
        
class Taksform(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("name","image")
        
class Takform(forms.ModelForm):
    class Meta:
        model = Talant
        fields = ['title','image','description','video','user','location','category']



class Taform(forms.ModelForm):
    class Meta:
        model = Aplication
        fields = ['user','talant','price','message','duraction','status']
