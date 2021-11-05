from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class CreateUserTRForm(ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Trainer
        fields = ['user','name','surname' ,'email', 'password',
                  'specialist', 'gender', ]