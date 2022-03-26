from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    first_name = forms.Field()
    last_name = forms.Field()
    email = forms.EmailField()
    mobile_number = forms.CharField()
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'mobile_number', 'password1', 'password2']