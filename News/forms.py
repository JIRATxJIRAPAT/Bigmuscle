from django import forms
from django.forms import ModelForm
from News.models import *


class CreateNewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title','context','ps','pic1','pic2','pic3','pic4' ]