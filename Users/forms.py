from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1',
                  'password2', 'first_name', 'last_name', ]


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['profile_pic', ]


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['reason','context','evidence']

