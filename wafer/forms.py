from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from wafer.models import WaferUser

# forms defined here handles user inputs

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = WaferUser
        fields = ('username', 'email', 'profile_pic')